import os

import hikari
import lightbulb

from dotenv import load_dotenv

load_dotenv()
bot = lightbulb.BotApp(token=os.getenv("TOKEN"), prefix="!",
                       intents=hikari.Intents.ALL_UNPRIVILEGED | hikari.Intents.MESSAGE_CONTENT)


@bot.listen(hikari.StartedEvent)
async def on_ready(event: hikari.StartedEvent):
    print(f"Logged in as {str(bot.get_me())}!")
    bot.load_extensions_from("./commands", must_exist=True)

bot.run()
