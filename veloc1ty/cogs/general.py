from . import (
    Cog ,
    Bot ,
    Context ,
    Button ,
    View
)
from time import monotonic , time
from disnake.ext.commands import  command , bot_has_permissions , slash_command
from disnake import Color , Embed , ButtonStyle
from disnake import ApplicationCommandInteraction as SlashContext
from datetime import timedelta

class General_CMDS(Cog):
    '''
    Basic Bot Related Commands 
    '''
    
    @command(
        name = 'ping',
        aliases = ['latency'] ,
        description = 'Bot\'s websocket Latency in ms'
    )
    @bot_has_permissions(send_messages=True , embed_links = True , read_message_history=True)
    async def ping_command( self , ctx : Context ):
        '''
        Bot Latency
        '''
        e = monotonic()
        msg = await ctx.reply(
            embed = Embed(
                title = f'{ctx.bot.my_emojis["wave2"]}\u200bPing !',
                color = Color.blue()
            ).add_field(name='Bot Latency',value='```yaml\nCalc ms\n```').add_field(name='Script Latency',value='```yaml\nCalc ms\n```')
        )
        await msg.edit(
            embed = Embed(
                title = f"{ctx.bot.my_emojis['wave2']} Pong !" ,
                color = Color.blue()
            ).add_field(name='Bot Latency',value=f'```yaml\n{round(ctx.bot.latency*1000)}ms\n```').add_field(name='Script Latency',value=f'```yaml\n{round((monotonic()-e)*1000)}ms\n```')
        )

    @command(
        name = 'botinfo',
        aliases=['about' , 'stats'] ,
        description= 'Some basic info and stats about the Bot'
    )
    @bot_has_permissions(send_messages=True , embed_links = True , read_message_history=True)
    async def send_bot_info(self , ctx : Context):
        '''
        Developer info , stats and support for the bot
        '''
        embed = Embed(
            color = Color.purple() ,
            description=F'''
**{ctx.bot.user.name.upper()}** is a bot made by [{str(ctx.bot.bot_owner)}](https://discord.com/users/{str(ctx.bot.bot_owner.id)}) ;
Use `{(await ctx.bot.get_prefix_from_database(ctx.bot , ctx.message))[2]}help` for info about bot commands 

**Bot Stats**
```yaml
Uptime : {timedelta(seconds=int(time() - ctx.bot.boot_time))}
Servers : {len(ctx.bot.guilds)}
Cached Users : {len(ctx.bot.users)}
```
**MADE WITH** 
[`python 3.9`](https://www.python.org/downloads/release/python-390/) , [`disnake`](https://pypi.org/project/disnake)
'''
        ).set_thumbnail(url=(ctx.bot.user.avatar or ctx.bot.user.default_avatar).url).set_footer(text=f'Requested by {ctx.author}', icon_url=(ctx.author.avatar or ctx.author.default_avatar).url)
        embed.set_author(name=ctx.bot.user.name.upper(), icon_url=(ctx.bot.user.avatar or ctx.bot.user.default_avatar).url)
        embed.set_image(url=ctx.bot.banner)
        view = View()
        buttons = [
            Button(style=ButtonStyle.url , label='Invite Bot',url=ctx.bot.invite_url , emoji='🔗') ,
            Button(style=ButtonStyle.url , label='Vote', url=f'https://top.gg/bot/{ctx.bot.user.id}/vote', emoji='💙') ,
            Button(style=ButtonStyle.url , label='Support', url=f'https://discord.gg/{ctx.bot.server_invite}', emoji='👀')
        ]
        for button in buttons:
            view.add_item(button)
        
        await ctx.reply(embed=embed , view=view)

    @slash_command(
        name='ping' ,
        description='Bot\'s Latency'
    )
    async def send_ping(self , ctx  : SlashContext ):
        '''
        The bot's websocket Latency,
        '''

        e = monotonic()
        await ctx.response.send_message(
            ephemeral=True ,
            embed = Embed(
                title = f'{ctx.bot.my_emojis["wave2"]}\u200bPing !',
                color = Color.blue()
            ).add_field(name='Bot Latency',value='```yaml\nCalc ms\n```').add_field(name='Script Latency',value='```yaml\nCalc ms\n```')
        )
        await ctx.edit_original_message(
            embed = Embed(
                title = f"{ctx.bot.my_emojis['wave2']}\u200b Pong !" ,
                color = Color.blue()
            ).add_field(name='Bot Latency',value=f'```yaml\n{round(ctx.bot.latency*1000)}ms\n```').add_field(name='Script Latency',value=f'```yaml\n{round((monotonic()-e)*1000)}ms\n```')
        )

       
   
    
def setup(bot : Bot):
    bot.add_cog(General_CMDS(bot))