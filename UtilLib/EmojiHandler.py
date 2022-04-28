from disnake import Emoji, Guild


async def get_emoji(guild: Guild, emoji_id: str) -> object:
    for emoji in await guild.fetch_emojis():
        print(f"{emoji_id} | <:{emoji.name}:{emoji.id}>")
        if emoji_id.lstrip(f'\\') == f"<:{emoji.name}:{emoji.id}>":
            return emoji
