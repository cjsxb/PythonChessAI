import threading

from GameInfo import GameState, ChatLine, GameFull


class Game(threading.Thread):
    def __init__(self, client, game_id, bot, **kwargs):
        super().__init__(**kwargs)
        self.game_id = game_id
        self.bot = bot
        self.client = client
        self.bot_id = client.account.get()['id']

        self.stream = client.bots.stream_game_state(game_id)

        #  Get all game data from lichess API (GameFull object)
        self.full_state = GameFull(next(self.stream))
        self.playing_as = "white" if self.full_state.white_id == self.bot_id else "black"
        self.variant = self.full_state.variant
        self.initial_fen = self.full_state.initial_fen

        gameState = self.full_state.gameState
        if self.bots_turn(gameState):
            self.handle_move(gameState)

    def run(self):
        while True:
            for event in self.stream:
                if event['type'] == 'gameState':
                    gameState = GameState(event)
                    if gameState.is_finished:
                        return
                    self.handle_move(gameState)
                elif event['type'] == 'chatLine':
                    chatline = ChatLine(event)
                    response = self.bot.getResponseToMessage(chatline)
                    if response:
                        self.client.bots.post_message(self.game_id, response)

    def handle_move(self, gameState):
        if not self.bots_turn(gameState):
            return
        bestMove = self.bot.getBestMove(gameState, self.variant)
        self.client.bots.make_move(self.game_id, bestMove)

    def bots_turn(self, gameState):
        parity = 0 if self.playing_as == "white" else 1
        return gameState.num_moves % 2 == parity
