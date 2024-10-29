import berserk
import os
from Game import Game
from SalmonSpaghetti import SalmonSpaghetti

# API Token, DO NOT SHARE
token = os.getenv("API_TOKEN")
session = berserk.TokenSession("lip_R8E6dNuIQbhk5Gg71NXY")
client = berserk.Client(session=session)

# When first making bot account on Lichess, must upgrade new account to BOT with
# client.account.upgrade_to_bot

print("Starting SalmonSpaghetti")

bot = SalmonSpaghetti()

while True:
    try:
        # Forever loop through Lichess API stream, play calculate and send moves
        for event in client.bots.stream_incoming_events():
            # Accept every challenge for now
            if event['type'] == 'challenge':
                challengeData = event['challenge']
                print("Accepting Challenge from {}".format(challengeData['challenger']['name']))
                client.bots.accept_challenge(challengeData['id'])
            elif event['type'] == 'gameStart':
                # When a game is starting, this code will always run
                gameData = event['game']
                game = Game(client, gameData['id'], bot)
                print("Starting Game")
                game.start()
    except RuntimeError:
        print("Something went wrong...")

