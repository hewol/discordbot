// main.js

const { Client } = require("discord.js");
const client = new Client({ intents: 33281 });
require('dotenv').config();

// Event: Bot is ready
client.once("ready", () => {
  console.log(`Logged in as ${client.user.tag}!`);
});

// Event: !ceata, !open
client.on("messageCreate", (message) => {
  if (message.content === "!ceata") {
    message.reply("ok");
  }

  if (message.content == "!open") {
    message.reply("ok");
  }
});

// Login as the bot
client.login(process.env.BOT_TOKEN);
