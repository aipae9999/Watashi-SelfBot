import discord
import pyfiglet
from discord.ext import commands


class Figlet:
    def __init__(self, bot):
        self.bot = bot
        self.cmd = bot.get_command

    @commands.command(aliases=['ascii', 'fig', 'asc'])
    async def figlet(self, ctx, *, message: str):
        """Cool FigletFont Text"""
        await ctx.message.delete()
        try:
            await ctx.send(f'```http\n{pyfiglet.figlet_format(message)}```')
        except discord.HTTPException:
            await ctx.invoke(self.cmd('error'), err='Message too large!')

    @commands.command(aliases=['asciislant', 'figslant', 'ascslant'])
    async def figletslant(self, ctx, *, message: str):
        """Cool FigletSlant Text"""
        await ctx.message.delete()
        f = pyfiglet.Figlet(font='slant')
        try:
            await ctx.send(f'```http\n{f.renderText(message)}```')
        except discord.HTTPException:
            await ctx.invoke(self.cmd('error'), err='Message too large!')

    @commands.command(aliases=['asciibulbhead', 'figbulbhead', 'ascbulbhead'])
    async def figletbulbhead(self, ctx, *, message: str):
        """Cool FigletBulbLook Text"""
        await ctx.message.delete()
        f = pyfiglet.Figlet(font='bulbhead')
        try:
            await ctx.send(f'```http\n{f.renderText(message)}```')
        except discord.HTTPException:
            await ctx.invoke(self.cmd('error'), err='Message too large!')

    @commands.command(aliases=['ascii3d', 'fig3d', 'asc3d'])
    async def figlet3d(self, ctx, *, message: str):
        """Cool Figlet3D Text"""
        await ctx.message.delete()
        f = pyfiglet.Figlet(font='larry3d')
        try:
            await ctx.send(f'```http\n{f.renderText(message)}```')
        except discord.HTTPException:
            await ctx.invoke(self.cmd('error'), err='Message too large!')

    @commands.command(aliases=['asciirectangle', 'figrectangle', 'ascrectangle'])
    async def figletrectangle(self, ctx, *, message: str):
        """Cool FigletRegtangular Text"""
        await ctx.message.delete()
        f = pyfiglet.Figlet(font='rectangles')
        try:
            await ctx.send(f'```http\n{f.renderText(message)}```')
        except discord.HTTPException:
            await ctx.invoke(self.cmd('error'), err='Message too large!')

    @commands.command(aliases=['asciiscript', 'figscript', 'ascscript'])
    async def figletscript(self, ctx, *, message: str):
        """Cool FigletNeatWriting Text"""
        await ctx.message.delete()
        f = pyfiglet.Figlet(font='slscript')
        try:
            await ctx.send(f'```http\n{f.renderText(message)}```')
        except discord.HTTPException:
            await ctx.invoke(self.cmd('error'), err='Message too large!')


def setup(bot):
    bot.add_cog(Figlet(bot))
