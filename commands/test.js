const { EmbedBuilder, SlashCommandBuilder } = require("discord.js");

module.exports = {
  data: new SlashCommandBuilder()
    .setName("test")
    .setDescription("Test slash comamnds"),
  async execute(interaction) {
    const embed = new EmbedBuilder()
      .setColor("#315D6E")
      .setTitle("Test embed!")
      .setDescription("Description");
    interaction.reply({ embeds: [embed] }).catch((err) => {
      console.log(err);
    });
  },
};
