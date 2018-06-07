import asyncio
import discordbot




bot = discordbot.DiscordBot()

@bot.command(pass_context=True)
async def addGame(ctx):

    #Revise if the message sent has addtional characters than just the command
    if len(ctx.message.content) > 9:
        # Adds the message for further modifications
        writable = ctx.message.content[10:]

        try:
            file = open('games.txt', 'a')
            numValue = file.write(writable + '\n')
            file.close()
            await bot.send_message(ctx.message.channel,
                                   'Thank you, game has been added to the list. I will start looking for discounts just for you <3')
        except Exception as e:
            await bot.send_message(ctx.message.channel, 'Something went wrong, try again later')
            print(e)

    else:
        await bot.send_message(ctx.message.channel, 'I need a game to look for some hot discounts for you, man.')


@bot.command(pass_context = True)
async def showList(ctx):
    finalMessage = ''
    file = open('games.txt', 'r')

    counter = 1
    for nextGame in file:
        finalMessage += '{}.- {} \n'.format(str(counter), nextGame)
        counter += 1

    file.close()

    if len(finalMessage) > 0:
        await bot.send_message(ctx.message.channel, finalMessage)
    else:
        await bot.send_message(ctx.message.channel, 'There are no games in the list')


@bot.command(pass_context = True)
async def removeGame(ctx):
    gameToRemove = ctx.message.content[13:] + "\n"
    listBackup = []
    file = open('games.txt', 'r')

    for game in file:
        listBackup.append(game)

    file.close()


    while gameToRemove in listBackup:
        listBackup.remove(gameToRemove)
    print(listBackup)

    file = open('games.txt', 'w')
    for game in listBackup:
        file.write('{} \n'.format(game))

    file.close()

    await bot.send_message(ctx.message.channel, 'It worked! your game has been burned to the death :D')

#Execute bot.py
bot.run()