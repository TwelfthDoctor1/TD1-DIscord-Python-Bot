"""
TD1 Python Bot Servicing Pipeline

Check Version Numbers and update accordingly.
"""
from UtilLib.LoggerService import BaseLoggerService
from VersionControl import __version__
import urllib.request
import urllib.error


class ServicingPipelineHandler(BaseLoggerService):
    pass


# URL Containing Version of Bot via GitHub [RAW]
SERVICING_PIPELINE_URL = "https://raw.githubusercontent.com/TwelfthDoctor1/TD1-Discord-Python-Bot/main/VersionControl.py"

# urllib Handling
PIPELINE_REQUEST = urllib.request.Request(url=SERVICING_PIPELINE_URL, method="GET")

PIPELINE_SERVICE = ServicingPipelineHandler()


def get_github_version():
    """
    Gets the GitHub Version String based on the VersionControl.py in the TD1 Python Bot GitHub
    :return:
    """
    try:
        with urllib.request.urlopen(PIPELINE_REQUEST) as response:
            # Get Raw Content from URL and decode bytes with UTF-8
            html = response.read().decode("utf-8")
            vc_list_data = html.split()
            for x in vc_list_data:
                if x == "__version__":

                    # Get First Word of Version Text
                    x_pos = vc_list_data.index(x)

                    # Remove Starting "
                    git_state_ver = vc_list_data[x_pos + 2].partition('"')[2]

                    x_pos += 3

                    # Get Next Words of Version Text
                    while vc_list_data[x_pos].find("\"") == -1:
                        git_state_ver = git_state_ver + " " + vc_list_data[x_pos]

                        x_pos += 1

                    # Get Last Word of Version Text (ends with ")
                    # Remove Ending "
                    git_state_ver = git_state_ver + " " + vc_list_data[x_pos].partition('"')[0]

                    return git_state_ver

    except urllib.error.URLError as e:
        PIPELINE_SERVICE.error(
            f"[FAILURE IN GETTING VERSION IN GITHUB] Either the associated URL is invalid or that the data is not raw "
            f"or may be caused by other issues."
            f"\nPerhaps Check your internet connection?"
        )

        if hasattr(e, "code") and hasattr(e, "reason"):
            # HTTP Error Code + Reason
            PIPELINE_SERVICE.error(f"HTTP ERROR CODE {e.code} | {e.reason}")

        elif hasattr(e, "reason"):
            # HTTP Error Reason
            PIPELINE_SERVICE.error(f"FAILURE REASON | {e.reason}")

        else:
            # Exception Error Dump
            PIPELINE_SERVICE.error(f"RAW FAILURE REASON | {e}")

        return None


def check_current_version():
    NEED_UPDATE = False
    git_version = get_github_version()

    if git_version is None:
        PIPELINE_SERVICE.warn(f"Failed to acquire version stored in GitHub. Assume latest version as {__version__}."
                              f"\nUse Manual Update instead to update the code files.", to_console=False)
        return

    curr_vers = __version__.split()
    git_vers = git_version.split()

    if curr_vers[-1] == git_vers[-1]:
        PIPELINE_SERVICE.info(f"Current Version of code matches that of GitHub | {__version__}", to_console=False)

    else:
        # Individually Check Numbering based on the Semantic Versioning (or TD1 Context: Major, Minor, Micro Versioning)
        vers_1 = curr_vers[-1].split(".")
        vers_2 = git_vers[-1].split(".")

        # Major Versioning Check
        if int(vers_1[0]) == int(vers_2[0]):
            PIPELINE_SERVICE.debug(
                f"Version Specific Check [Major]: Current {vers_1[0]} | Git {vers_2[0]} - Same Major Version",
                to_console=False
            )

        elif int(vers_1[0]) < int(vers_2[0]):
            PIPELINE_SERVICE.debug(
                f"Version Specific Check [Major]: Current {vers_1[0]} | Git {vers_2[0]} - Git is Higher, Need to Update",
                to_console=False
            )
            NEED_UPDATE = True

        else:
            PIPELINE_SERVICE.debug(
                f"Version Specific Check [Major]: Current {vers_1[0]} | Git {vers_2[0]} - Current is Higher, "
                f"Likely on Beta or Dev",
                to_console=False
            )

        # Minor Versioning Check
        if int(vers_1[1]) == int(vers_2[1]) and NEED_UPDATE is False:
            PIPELINE_SERVICE.debug(
                f"Version Specific Check [Minor]: Current {vers_1[1]} | Git {vers_2[1]} - Same Minor Version",
                to_console=False
            )

        elif int(vers_1[1]) < int(vers_2[1]) and NEED_UPDATE is False:
            PIPELINE_SERVICE.debug(
                f"Version Specific Check [Minor]: Current {vers_1[1]} | Git {vers_2[1]} - Git is Higher, Need to Update",
                to_console=False
            )
            NEED_UPDATE = True

        elif int(vers_1[1]) > int(vers_2[1]) and NEED_UPDATE is False:
            PIPELINE_SERVICE.debug(
                f"Version Specific Check [Minor]: Current {vers_1[1]} | Git {vers_2[1]} - Current is Higher, "
                f"Likely on Beta or Dev",
                to_console=False
            )

        # Micro Versioning Check
        if int(vers_1[2]) == int(vers_2[2]) and NEED_UPDATE is False:
            PIPELINE_SERVICE.debug(
                f"Version Specific Check [Micro]: Current {vers_1[2]} | Git {vers_2[2]} - Same Micro Version",
                to_console=False
            )

        elif int(vers_1[2]) < int(vers_2[2]) and NEED_UPDATE is False:
            PIPELINE_SERVICE.debug(
                f"Version Specific Check [Micro]: Current {vers_1[2]} | Git {vers_2[2]} - Git is Higher, "
                f"Need to Update",
                to_console=False
            )
            NEED_UPDATE = True

        elif int(vers_1[2]) > int(vers_2[2]) and NEED_UPDATE is False:
            PIPELINE_SERVICE.debug(
                f"Version Specific Check [Micro]: Current {vers_1[2]} | Git {vers_2[2]} - Current is Higher, "
                f"Likely on Beta or Dev",
                to_console=False
            )

    # Final Verdict Response
    if NEED_UPDATE is True:
        PIPELINE_SERVICE.info(
            f"[Current Version: {__version__} | GitHub Version: {git_version}]"
            f"\nThere is an update available to the program. You can update it through GitHub or "
            f"by locally cloning to your repository."
        )
    else:
        PIPELINE_SERVICE.info(
            f"[Current Version: {__version__} | GitHub Version: {git_version}]"
            f"\nCurrent version of code is up-to-date."
        )

