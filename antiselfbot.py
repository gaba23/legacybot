import discord
from discord.ext import commands
from datetime import datetime, timedelta

class Antiselfbot(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        criou = member.created_at + timedelta(days=10)
        
        print(criou)
        print(datetime.today())
        
        if datetime.today() < criou:
            await member.create_dm()
            embed=discord.Embed(
                title="📝Motivo: Sua conta tem menos de 10 dias ", 
                description="Desculpe mas para ser um cliente você precisa de pelo menos 10 dias de vida!", 
                color=0x8e0101
            )
            embed.set_author(name="🚫| Você foi expulso do servidor!")
            embed.add_field(
                name="👤 Expulso por:", 
                value="Automaticamente", 
                inline=True
            )
            embed.add_field(
                name="💬 Observação:", 
                value="O Filtro de contas fakes está ativo neste servidor.", 
                inline=True
            )
            await member.send(embed=embed)
            await member.kick()

def setup(bot):
    bot.add_cog(Antiselfbot(bot))