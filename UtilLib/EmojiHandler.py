from disnake import Emoji, Guild


def get_emoji(emojis: [], emoji_id: str) -> object:
    """
    Gets the specified emoji should the bot have said emoji.


    :param emojis: Guild.fetch_emojis() OR Bot.emojis
    :param emoji_id: The emoji to use, use \:EMOJI_NAME: to get id
    :return:
    """
    for emoji in emojis:
        print(f"{emoji_id} | <:{emoji.name}:{emoji.id}>")
        if emoji_id.lstrip(f'\\') == f"<:{emoji.name}:{emoji.id}>":
            return emoji
