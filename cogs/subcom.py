import discord
from discord.ext import commands
import asyncio

class Tasks(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.tasks = {}

        '''
        Ideal format is going to be:
        {
            1: {
                    "Task Name": "Testing 1 2 3",
                    "Owner": None,
                    "Due Date": None
                },
            2: {
                    "Task Name": "Testing 4 5 6",
                    "Owner": "turtle#6635",
                    "Due Date": None
                }
        }
        '''

        @commands.commmand()
        async def tasks(self, ctx: commands.context.Context):
            user_roles = ctx.author.roles
            allowed_user = ("Executive" in [role.name for role in user_roles]) #or "Subcommittee" in user_roles)

            if allowed_user:
                embed_msg = discord.Embed(title="Active Tasks", color=discord.Color.greyple())
                
                # Pull tasks from storage
                # self.tasks = idk open memory and get stuff
                
                # Extract tasks
                temp_number = [num for num in self.tasks]
                temp_names = [self.tasks[x]["Task Name"] for x in temp_number]
                temp_owners = [self.tasks[x]["Owner"] for x in temp_number]
                temp_due_dates = [self.tasks[x]["Due Date"] for x in temp_number]
                embed_msg.add_field(name="Task Name", value="".join(temp_names), inline=True)
                embed_msg.add_field(name="Owner", value="".join(temp_owners), inline=True)
                embed_msg.add_field(name="Due Date", value="".join(temp_due_dates), inline=True)

                return embed_msg
        
        @commands.command()
        async def add_task(self, ctx: commands.context.Context, *args):
            user_roles = ctx.author.roles
            allowed_user = ("Executive" in [role.name for role in user_roles]) #or "Subcommittee" in user_roles)

            if allowed_user:
                return 1
            
            return 0
        
        @commands.command()
        async def assign_task(self, ctx: commands.context.Context, *args):
            user_roles = ctx.author.roles
            allowed_user = ("Executive" in [role.name for role in user_roles]) #or "Subcommittee" in user_roles)

            if allowed_user:
                # If no argument, assign to author
                return 1
            return 0
        
        @commands.command()
        async def remove_task(self, ctx: commands.context.Context, n: int):
            user_roles = ctx.author.roles
            allowed_user = ("Executive" in [role.name for role in user_roles]) #or "Subcommittee" in user_roles)

            if allowed_user:
                # Check that n is a valid key in self.tasks
                return 1
            # Reminder to log exited task into #archived-tasks w/ owner
            # and date of completion
            return 0