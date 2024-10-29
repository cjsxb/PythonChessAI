import chess
import chess.variant
import random

class ChessBotInterface:

    @staticmethod
    def getBoardObject(variant):
        # Return Chess board type depending on game mode.
        if variant == "chess960":
            return chess.Board(chess960=True)

        possibleBoards = {
            "standard": chess.Board,
            "crazyhouse": chess.variant.CrazyhouseBoard,
            "antichess": chess.variant.AntichessBoard,
            "atomic": chess.variant.AtomicBoard,
            "horde": chess.variant.HordeBoard,
            "kingOfTheHill": chess.variant.KingOfTheHillBoard,
            "racingKings": chess.variant.RacingKingsBoard,
            "threeCheck": chess.variant.ThreeCheckBoard
        }

        return possibleBoards[variant]()


class SalmonSpaghetti(ChessBotInterface):

    def getBestMove(self, gameState, variant):
        board = self.getBoardObject(variant)

        # This is going to update our imaginary board with current chess moves played
        for move in gameState.move_list:
            board.push_uci(move)

        moves = list(board.legal_moves)

        # Check if any move results in checkmate
        checkmateMove = self.checkcheckMate(moves, board, 1)
        if checkmateMove:
            return checkmateMove

        moveToPlay = ""

        # Loop through all moves available to engine
        for move in moves:
            if self.checkIfMated(move, board):
                moves.remove(move)
                continue
            # If any move is a capture, play that move
            if board.is_capture(move):
                # Check if square is defended
                if self.defended(move, board, 1):
                    continue
                moveToPlay = move
            # Or a check
            elif board.gives_check(move):
                if self.defended(move, board, 1):
                    continue
                moveToPlay = move
                break

        # If unsure what to do, play random move from list
        if moveToPlay != "":
            return moveToPlay.uci()
        else:
            if not moves:
                return random.choice(list(board.legal_moves)).uci()
            else:
                return random.choice(moves).uci()

    # Calculate if game can be won by AI
    def checkcheckMate(self, moves, board, depth):
        newboard = chess.Board(board.fen())
        for move in moves:
            # Create a copy of the board and push the move
            newboard.push(move)

            # Check if the opponent is in checkmate
            if newboard.is_checkmate():
                print(f"Checkmate will occur after {move.uci()}")
                newboard.pop()  # Undo the move
                return move.uci()

            # Undo the move after checking
            newboard.pop()
        return False

    # Check if piece available to taking is defended
    def defended(self, move, board, depth):

        newboard = chess.Board(board.fen())
        toSquare = move.to_square
        newboard.push(move)

        # Check if the piece on the new square is defended
        defended = False

        # Check all legal moves for the opponent
        for opponent_move in newboard.legal_moves:
            if opponent_move.to_square == toSquare:
                defended = True
                break

        return defended

    # Make sure we are not getting checkmated, avoid moves that lead to that
    def checkIfMated(self, move, board):

        newboard = chess.Board(board.fen())
        newboard.push(move)

        for opponentMove in newboard.legal_moves:
            newboard.push(opponentMove)
            # Check if we are in checkmate
            if newboard.is_checkmate():
                print(f"Checkmate will occur after {move.uci()}")
                return True
            newboard.pop()
        return False

    # Check if our pieces are hanging
    def checkIfHangingFuture(self, move, board):

        newboard = chess.Board(board.fen())
        toSquare = move.to_square

        for opponentMove in newboard.legal_moves:
            newboard.push(opponentMove)
            if opponentMove.to_square == toSquare:
                print(f"They can take our piece after {move.uci()}")
                return True
            newboard.pop()

        return False
