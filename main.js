// index.js

const { Client } = require('discord.js');
const client = new Client();
require('dotenv').config();

// Event: Bot is ready
client.once('ready', () => {
  console.log(`Logged in as ${client.user.tag}!`);
});

// Event: !ceata
client.on('message', (message) => {
  if (message.content === '!ceata') {
    message.reply('ok');
  }
});

// Event: !open
client.on('message', (message) => {
    if (message.content === '!open') {
      message.reply('ok');
    }
  });

// Login as the bot
client.login('process.env.BOT_TOKEN');
