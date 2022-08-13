import os
import json
import discord
import datetime
from discord.ext import commands

class Info():
    def __init__(self):
        self.info_fn = "info.json" # fn = filename
        self.datetime_format = "%d/%m/%Y %H:%M"

        if os.path.exists(self.info_fn):
            self.info = json.loads(self.info_fn)
        else:
            self.info = {
                "emojis": {
                    "jigsaw": ":jigsaw:",
                    "brain": ":brain:",
                    "speech": ":speech_balloon:",
                    "heart": ":heart:",
                    "cross": ":x:"
                },
                "puzzles": {
                    "role_name": "weekly puzzles",
                    "channel_id": 892032997220573204,
                    "release_datetime": "08/08/2022 12:00",
                    "week_num": -1,
                    "img_urls": [],
                    "speed_bonus": -1,
                    "submission_link": ""
                },
                "sb": {
                    "role_name": "weekly games",
                    "channel_id": 1001742058601590824,
                    "release_datetime": "08/08/2022 12:00",
                    "week_num": -1,
                    "img_url": "",
                    "submission_link": ""
                },
                "ciyk": {
                    "role_name": "weekly games",
                    "channel_id": 1001742058601590824,
                    "discuss_id": 1001742642427744326,
                    "release_datetime": "08/08/2022 12:00",
                    "week_num": -1,
                    "img_url": "",
                    "submission_link": ""
                }
            }
        
        self.puzz_datetime = self.str_to_datetime(self.info["puzzles"]["release_datetime"])
        self.sb_datetime = self.str_to_datetime(self.info["sb"]["release_datetime"])
        self.ciyk_datetime = self.str_to_datetime(self.info["ciyk"]["release_datetime"])

        self.day_names = {
            0: "Monday",
            1: "Tuesday",
            2: "Wednesday",
            3: "Thursday",
            4: "Friday",
            5: "Saturday",
            6: "Sunday"
        }

    # expects the %d/%m/%Y %H:%M format
    def str_to_datetime(self, string: str) -> datetime.datetime:
        date, time = string.split()

        day, month, year = date.split("/")
        hour, minute = time.split(":")

        return datetime.datetime(int(year), int(month), int(day), int(hour), int(minute))

    def get_puzz_text(self, ctx: commands.context.Context) -> str:
        emojis = self.info["emojis"]
        puzz_info = self.info["puzzles"]
        role_name = puzz_info["role_name"]
        puzz_tag = f"@/{discord.utils.get(ctx.guild.roles, name=role_name)}\n"
        line1 = f'{emojis["jigsaw"]} **WEEKLY PUZZLES: WEEK {puzz_info["week_num"]}** {emojis["jigsaw"]}\n'
        line2 = f'**SPEED BONUS:** {puzz_info["speed_bonus"]} MINUTES\n'
        line3 = f'*Hints will be unlimited after {puzz_info["speed_bonus"]} minutes is up AND after the top 3 solvers have finished!*\n\n'
        line4 = f'**Submit your answers here:** {puzz_info["submission_link"]}\n'
        line5 = "You can submit as many times as you want!\n"
        line6 = "Your highest score will be kept."

        return puzz_tag + line1 + line2 + line3 + line4 + line5 + line6

    def get_sb_text(self, ctx: commands.context.Context) -> str:
        emojis = self.info["emojis"]
        sb_info = self.info["sb"]
        role_name = sb_info["role_name"]
        sb_tag = f"@/{discord.utils.get(ctx.guild.roles, name=role_name)}\n"
        line1 = f'{emojis["brain"]} **SECOND BEST: WEEK {sb_info["week_num"]}** {emojis["brain"]}\n\n'
        line2 = f"Try your best to guess what the second most popular answer will be!\n\n"
        line3 = f'**Submit your answers here:** {sb_info["submission_link"]}\n\n'

        return sb_tag + line1 + line2 + line3 + sb_info["img_url"]
    
    def get_ciyk_text(self, ctx: commands.context.Context) -> str:
        emojis = self.info["emojis"]
        ciyk_info = self.info["ciyk"]
        role_name = ciyk_info["role_name"]
        ciyk_tag = f"@/{discord.utils.get(ctx.guild.roles, name=role_name)}\n\n"
        line1 = f'{emojis["speech"]} **COMMENT IF YOU KNOW: WEEK {ciyk_info["week_num"]}** {emojis["speech"]}\n'
        line2 = f'If you think you know the pattern, comment an answer that follows it in <#{ciyk_info["discuss_id"]}>\n'
        line3 = f'We\'ll react with a {emojis["heart"]} if you\'re right and a {emojis["cross"]} if you\'re wrong!\n\n'

        return ciyk_tag + line1 + line2 + line3 + ciyk_info["img_url"]

    # this method exists as just an easy way to change the data in one method call in setpuzzles/setsb/setciyk    
    def change_data(self, puzz_name: str, new_data: dict[str]):
        self.info[puzz_name]["week_num"] = new_data["week_num"]
        self.info[puzz_name]["submission_link"] = new_data["submission_link"]

        if "puzzles" == puzz_name:
            self.info[puzz_name]["img_urls"] = new_data["img_urls"]
            self.info[puzz_name]["speed_bonus"] = new_data["speed_bonus"]
        else:
            self.info[puzz_name]["img_url"] = new_data["img_url"]

        # write the new info to the json file so that it is not lost if the bot shuts down
        with open(self.info_fn, "w") as info:
            new_json = json.dumps(self.info, indent=4)

            info.write(new_json)