from agent import Agent
import numpy as np
from board import Board

class MiniMaxAgent(Agent):
    def __init__(self, player=1, MaxDepth=1):
        super().__init__(player)
        self.Maxdepth = MaxDepth

    def eval_disparity(board):
        row_lengths = [len(row) for row in board]
        return -(max(row_lengths) - min(row_lengths))
    
    def eval_max_coins_in_row(board):
        return max(len(row) for row in board)
    
    def eval_QuantityOfCoins(board):
        return sum(len(row) for row in board)
    
    def eval_possible_moves(board):
        return len(board.get_possible_actions())
    
    def eval_max_coins_in_row(board):
        max_coins = max(len(row) for row in board)
        return -max_coins

    def next_action(self, obs):
        _, best_action= self.minimax(obs, 0 , self.player, float('-inf'), float('inf')) # inicializamos la beta en infinito y el alpha en -infinito
        return best_action
    
    def heuristic_utility(self, board):
         # Contar monedas restantes
        return eval_disparity(board) + eval_max_coins_in_row  # Menos monedas restantes es mejor
    
    def minimax(self, board, depth, MaxPlayer, alpha, beta):
        if board.is_end(self.player)[0] or depth == self.Maxdepth:
            return self.heuristic_utility(board), None  # Devolver None para la acción en el caso base
    
        actions = board.get_possible_actions()

        if self.player == MaxPlayer:  # Maximizar la utilidad
            best_value = float('-inf')
            best_action = None
            for action in actions:
                board_copy = board.clone()
                board_copy.play(action)
                value, _ = self.minimax(board_copy, depth + 1,3 -self.player, alpha, beta)  # Le damos el turno al otro jugador
                if value > best_value:
                    best_value = value
                    best_action = action
                alpha = max(alpha, best_value)
                if beta <= alpha:
                    break  # Cortar la rama si beta es menor o igual a alpha
            return best_value, best_action  # Devolver tanto el valor como la acción

        else:  # Minimizar la utilidad
            best_value = float('inf')
            best_action = None
            for action in actions:
                board_copy = board.clone()
                board_copy.play(action)
                value, _ = self.minimax(board_copy, depth + 1,3 -self.player, alpha, beta) # Le damos el turno al otro jugador
                if value < best_value:
                    best_value = value
                    best_action = action
                beta = min(beta, best_value)
                if beta <= alpha:
                    break  # Cortar la rama si beta es menor o igual a alpha
            return best_value, best_action