import discord
import urbandictionary as ud
from discord.ext import commands


class UrbanDictionary:
    def __init__(self, bot):
        self.bot = bot

    @commands.group(invoke_without_command=True, aliases=['ud', 'urbandict'])
    async def urban(self, ctx, *, query: str):
        """ Check UrbanDictionary for the meaning of a word """
        await ctx.message.delete()
        try:
            resultlst = await self.bot.loop.run_in_executor(None, ud.define, query)
            item = resultlst[0]
        except:
            return

        em = discord.Embed(color=0x00ffff)
        em.set_author(name="\U0001f4d6 Urban Dictionary")
        em.add_field(name="Word", value=item.word, inline=False)
        em.add_field(name="Definition", value=item.definition, inline=False)
        em.add_field(name="Example(s)", value=item.example, inline=False)
        await ctx.send(embed=em)

    @urban.command(aliases=['-s'])
    async def search(self, ctx, *, query: str):
        """Search A Specific Word In The Urban Dict"""

        # TODO:
        # Re-evaluate this command
        # Reason: very spammy and not necessarily intuitive for the user
        await ctx.message.delete()
        resultlst = await self.bot.loop.run_in_executor(None, ud.define, query)

        msg = str()
        for number, option in enumerate(resultlst[:4]):
            msg += "{0}. {1}\n".format(number + 1, option.word)
        em = discord.Embed(title="Results", description=msg,
                           color=0x00ffff)
        em.set_footer(text="Type 'exit' to leave the menu.")
        menumsg = await ctx.send(embed=em)

        def check(m):
            return m.author == ctx.message.author and m.channel == ctx.message.channel and m.content.isdigit()
        response = await self.bot.wait_for('message', check=check)

        try:
            if response.content.lower() == 'exit':
                await response.delete()
                await menumsg.delete()
                return
            else:
                await response.delete()
                await menumsg.delete()
                item = resultlst[int(response.content) - 1]
        except IndexError:
            return

        em = discord.Embed(color=0x00ffff)
        em.set_author(name="\U0001f4d6 Urban Dictionary")
        em.add_field(name="Word", value=item.word)
        em.add_field(name="Definition", value=item.definition)
        em.add_field(name="Example(s)", value=item.example)
        await ctx.send(embed=em)

    @urban.command(aliases=['-r'])
    async def random(self, ctx):
        """Search A Random Word In The Urban Dict"""
        await ctx.message.delete()
        item = await self.bot.loop.run_in_executor(None, ud.random)

        em = discord.Embed(color=0x00ffff)
        em.set_author(name="\U0001f4d6 Urban Dictionary")
        em.add_field(name="Word", value=item[0].word)
        em.add_field(name="Definition", value=item[0].definition)
        em.add_field(name="Example(s)", value=item[0].example)
        await ctx.send(embed=em)


def setup(bot):
    bot.add_cog(UrbanDictionary(bot))
