// main.js

const { Client } = require("discord.js");
const client = new Client({ intents: 33281 });
require('dotenv').config();

const statusList = [
  { type: 'PLAYING', name: 'GitHub' },
  { type: 'PLAYING', name: 'Nothing' },
  { type: 'STREAMING', name: 'Nothing' },
  { type: 'PLAYING', name: 'aerOS' },
  { type: 'PLAYING', name: 'Terminal' }
];

client.on('ready', () => {
  console.log('Bot is online');

  setInterval(() => {
    const randomStatus = statusList[Math.floor(Math.random() * statusList.length)];
    client.user.setPresence({
      activity: { name: randomStatus.name },
      status: 'online',
      type: randomStatus.type
    })
      .then(console.log)
      .catch(console.error);
  }, 30 * 60 * 1000); // 30 minutes interval
}); 

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

// Event: Reply "Hello!" if pinged
client.on("messageCreate", (message) => {
  if (message.content === "<@1141365284968607758>") {
    message.reply("Hello!");
  }
});

// Login as the bot
client.login(process.env.BOT_TOKEN);
