import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='?', intents=intents)


@bot.command(help="Dit bonjour",
             description="Permet de vérifier le status du bot")
async def bonjour(ctx):
  await ctx.send(f"Bonjour {ctx.author} !")


@bot.command()
async def pile(ctx):
  await ctx.send("pong")


@bot.command(help="Morpion", description="Permet de jouer au morpion")
async def morpion(ctx):
  board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
  win_cases = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7],
               [2, 5, 8], [0, 4, 8], [2, 4, 6]]

  player1 = ":x:"
  player2 = ":o:"
  current_player = player1

  def display_board():
    display = ""
    for row in board:
      for i in range(3):
        if row[i] == 0:
          display += ":white_large_square:"
        else:
          display = display + str(row[i]) 
      display += "\n"
    return display

  def position_r(p):
    return (p - 1) // 3  # lignes

  def position_c(p):
    return (p - 1) % 3

  def check_win():
    for case in win_cases:
      if board[case[0] // 3][case[0] % 3] == board[case[1] // 3][
          case[1] % 3] == board[case[2] // 3][case[2] % 3] != 0:
        return True
    return False

  def check_draw():
    return all(cell != 0 for row in board for cell in row)

  async def place(player):

    def check(message):
      return message.author == ctx.author and message.content.isdigit(
      ) and int(message.content) in range(1, 10)

    while True:
      await ctx.send(f"Au tour de {player}, entrez une position (1-9) :")
      try:
        message = await bot.wait_for('message', check=check, timeout=60.0)
        position = int(message.content)
        r = position_r(position)
        c = position_c(position)

        if board[r][c] == 0:
          board[r][c] = player
          break
        else:
          await ctx.send("Case déjà prise, veuillez choisir une autre.")
      except Exception:
        await ctx.send(
            "Entrée invalide ou temps écoulé. Veuillez entrer un nombre entre 1 et 9."
        )

  async def play():
    nonlocal current_player
    while True:
      await ctx.send(f"Plateau actuel :\n{display_board()}")
      await place(current_player)
      if check_win():
        await ctx.send(
            f"Le joueur {current_player} a gagné !\n{display_board()}")
        break
      if check_draw():
        await ctx.send(f"Égalité !\n{display_board()}")
        break
      current_player = player2 if current_player == player1 else player1

  await play()


token = os.environ['TOKEN_BOT_DISCORD']
bot.run(token)
