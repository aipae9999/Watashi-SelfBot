import discord
from discord.ext import commands


# This bit allows you to more easily unban members via ID or name#discrim
# Taken mostly from R. Danny
# https://github.com/Rapptz/RoboDanny/blob/rewrite/cogs/mod.py#L83-L94
class BannedMember(commands.Converter):
    async def convert(self, ctx, arg):
        bans = await ctx.guild.bans()

        try:
            member_id = int(arg)
            user = discord.utils.find(lambda u: u.user.id == member_id, bans)
        except ValueError:
            user = discord.utils.find(lambda u: str(u.user) == arg, bans)

        if user is None:
            return None

        return user


class Mod:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['k'])
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        """ Kick a member from the server """
        await ctx.guild.kick(member, reason=reason)
        await ctx.send(f'Member `{member}` kicked.\n'
                       f'Reason: `{reason}`.')

    @commands.command(aliases=['kb'])
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        """ Ban a member from the server """
        await ctx.guild.ban(member, reason=reason, delete_message_days=0)
        await ctx.send(f'Member `{member}` banned.\n'
                       f'Reason: `{reason}`.')

    @commands.command(aliases=['ub'])
    async def unban(self, ctx, member: BannedMember, *, reason=None):
        """ Unban a member from the server
        Since you can't highlight them anymore use their name#discrim or ID """
        await ctx.guild.unban(member.user, reason=reason)
        await ctx.send(f'Member `{member.user}` unbanned.\n'
                       f'Reason: `{reason}`.')


def setup(bot):
    bot.add_cog(Mod(bot))
