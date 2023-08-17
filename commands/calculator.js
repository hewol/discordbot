const { EmbedBuilder, SlashCommandBuilder } = require("discord.js");

module.exports = {
  data: new SlashCommandBuilder()
    .setName("calc")
    .setDescription("Calculate the given expression")
    .addStringOption((option) =>
      option
        .setName("Expression")
        .setDescription("Enter the Expression in the format 26*3 and 345/5")
        .setRequired(true)
    ),
  async execute(interaction) {
    const option_cmd = interaction.options.getString("Expression");
    const expression = option_cmd.content.split(" ")[1];

    let result;

    try {
      result = eval(expression);

      if (expression === "0/0") {
        message
          .reply(
            "Imagine that you have zero cookies and you split them evenly among zero friends. How many cookies does each person get? See? It doesn't make sense. And Cookie Monster is sad that there are no cookies, and you are sad that you have no friends."
          )
          .catch((err) => {
            console.log(err);
          }); // Handle 0/0
      } else if (isNaN(result)) {
        message.reply("Not Approved").catch((err) => {
          console.log(err);
        }); // Handle division by zero
      } else {
        message.reply(`Answer: ${result}`).catch((err) => {
          console.log(err);
        });
      }
    } catch (error) {
      message.reply(
        "Please enter a valid expression like `$calc 3*23` or `$calc 34+35`"
      ); // Handle other errors
    }
  },
};
