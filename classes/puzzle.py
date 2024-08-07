import discord


class BasePuzzle:
    def __init__(self, channel: int, time: str, week: int, images: list, display_name: str):
        self.release_channel = channel
        self.release_time = time
        self.week = week
        self.image_urls = images
        self.display_name = display_name


class DiscussionPuzzle(BasePuzzle):
    def __init__(self, role_name: str, release_channel: int, discussion_channel: int, release_time: str, week: int, image_urls: list, display_name: str):
        self.type = "discussion"
        super().__init__(release_channel, release_time, week, image_urls, display_name)
        self.role_name = role_name
        self.discussion_channel = discussion_channel

    def get_tag(self, guild: discord.Guild, mention: bool):
        if mention:
            tag = f"{discord.utils.get(guild.roles, name=self.role_name).mention}\n\n"
        else:
            tag = f"{discord.utils.get(guild.roles, name=self.role_name)}\n\n"

        return tag

    def get_text(self, guild: discord.Guild, mention: bool):
        lines = [
            self.get_tag(guild, mention),
            f"**COMMENT IF YOU KNOW: WEEK {self.week}**\n\n",
            f"If you think you know the pattern, comment an answer that follows it in <#{self.discussion_channel}>\n",
            f"We'll react with a :heart: if you're right and a :x: if you're wrong!\n\n"
        ]
        return " ".join(lines)


class ChillPuzzle(BasePuzzle):
    def __init__(self, role_name: str, release_channel: int, release_time: str, week: int, image_urls: list, display_name: str, *, interactive_link: str = ""):
        self.type = "chill"
        super().__init__(release_channel, release_time, week, image_urls, display_name)
        self.role_name = role_name
        self.interactive_link = interactive_link

    def get_tag(self, guild: discord.Guild, mention: bool):
        if mention:
            tag = f"{discord.utils.get(guild.roles, name=self.role_name).mention}\n\n"
        else:
            tag = f"{discord.utils.get(guild.roles, name=self.role_name)}\n\n"

        return tag

    def get_text(self, guild: discord.Guild, mention: bool):
        lines = [
            self.get_tag(guild, mention),
            f"**{self.display_name}: WEEK {self.week}**"
        ]

        if self.interactive_link:
            lines.append(f"\n\nInteractive version: {self.interactive_link}")

        return " ".join(lines)


class WeeklyPuzzle(BasePuzzle):
    def __init__(self, role_name: str, release_channel: int, release_time: str, week: int, image_urls: list, display_name: str, submission_link: str, *, interactive_link: str = ""):
        self.type = "weekly"
        super().__init__(release_channel, release_time, week, image_urls, display_name)
        self.role_name = role_name
        self.submission_link = submission_link
        self.interactive_link = interactive_link

    def get_tag(self, guild: discord.Guild, mention: bool):
        if mention:
            tag = f"{discord.utils.get(guild.roles, name=self.role_name).mention}\n\n"
        else:
            tag = f"{discord.utils.get(guild.roles, name=self.role_name)}\n\n"

        return tag

    def get_text(self, guild: discord.Guild, mention: bool):
        lines = [
            self.get_tag(guild, mention),
            f"**WEEKLY PUZZLE COMPETITION: WEEK {self.week}**\n",
            f"**\\- {self.display_name} -**\n\n",
            "_Hints will be unlimited after the top 3 solvers have finished!_\n\n",
            f"Submit your answers here: {self.submission_link}\n\n",
            "_You can submit as many times as you want!_\n",
            "_Your highest score will be kept._"
        ]

        if self.interactive_link:
            lines.append(f"\n\nInteractive version: {self.interactive_link}")

        return " ".join(lines)


class JFFPuzzle(BasePuzzle):
    def __init__(self, release_channel: int, release_time: str, week: int, image_urls: list, display_name: str, submission_link: str, *, interactive_link: str = ""):
        self.type = "jff"
        super().__init__(release_channel, release_time, week, image_urls, display_name)
        self.submission_link = submission_link
        self.interactive_link = interactive_link

    def get_text(self, guild: discord.Guild, mention: bool):
        lines = [
            f"**JUST-FOR-FUN: WEEK {self.week}**\n",
            f"**\\- {self.display_name} -**\n\n"
        ]
        return " ".join(lines)