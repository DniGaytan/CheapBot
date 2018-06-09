import json
import asyncio
import discordbot

bot = discordbot.DiscordBot()

@bot.command(pass_context=True)
async def addGame(ctx):

    #Revise if the message sent has addtional characters than just the command
    if len(ctx.message.content) > 9:
        gameTitle = ctx.message.content[10:]

        newGame = {
            "game": gameTitle,
            "discount_price": "unknown",
            "discount_store": "unknown",
            "deal_link": "unknown",
            "platform": "unknown"
        }

        try:
            jsonFile = open('games.json', 'r')
            jsonDict = json.load(jsonFile)
            jsonFile.close()

            jsonDict['games'].append(newGame)

            jsonFile = open('games.json', 'w')
            jsonFile.write(json.dumps(jsonDict))
            jsonFile.close()

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
    jsonFile = open("games.json", 'r')
    jsonDict = json.load(jsonFile)
    jsonFile.close()

    counter = 1
    for game in jsonDict['games']:
        finalMessage += "{}.- {} \n".format(counter, game['game'])
        counter += 1


    if len(finalMessage) > 0:
        await bot.send_message(ctx.message.channel, finalMessage)
    else:
        await bot.send_message(ctx.message.channel, 'There are no games in the list')


@bot.command(pass_context = True)
async def removeGame(ctx):
    gameToRemove = ctx.message.content[13:]
    jsonFile = open('games.json', 'r')
    jsonDict = json.load(jsonFile)
    jsonFile.close()

    for game in jsonDict['games']:
        if game['game'] == gameToRemove:
            jsonDict['games'].remove(game)
            try:
                jsonFile = open('games.json', 'w')
                jsonFile.write(json.dumps(jsonDict))
                await bot.send_message(ctx.message.channel, 'It worked! your game has been burned to the death :D')
            except Exception as e:
                print(e)
                await bot.send_message(ctx.message.channel,
                                       'Something went wrong, telling my boss about the current mistake. Try again later')
            finally:
                jsonFile.close()







#Execute bot.py
bot.run()