from agent import Agent
import numpy as np
from board import Board

class MiniMaxAgent(Agent):
    def __init__(self, player=1, MaxDepth=1):
        super().__init__(player)
        self.Maxdepth = MaxDepth
        
    def next_action(self, obs):
        _, best_action= self.minimax(obs, 0 , self.player)
        return best_action
    
    def heuristic_utility(self, board):
        total_coins = np.sum(board.grid == 1)  # Contar monedas restantes
        return -total_coins  # Menos monedas restantes es mejor
    
    def minimax(self, board, depth, MaxPlayer):
        if board.is_end(self.player)[0] or depth == self.Maxdepth:
            return self.heuristic_utility(board), None  # Devolver None para la acción en el caso base
    
        actions = board.get_possible_actions()

        if self.player == MaxPlayer:  # Maximizar la utilidad
            best_value = float('-inf')
            best_action = None
            for action in actions:
                board_copy = board.clone()
                board_copy.play(action)
                value, _ = self.minimax(board_copy, depth + 1,3 -self.player)  # Le damos el turno al otro jugador
                if value > best_value:
                    best_value = value
                    best_action = action
            return best_value, best_action  # Devolver tanto el valor como la acción

        else:  # Minimizar la utilidad
            best_value = float('inf')
            best_action = None
            for action in actions:
                board_copy = board.clone()
                board_copy.play(action)
                value, _ = self.minimax(board_copy, depth + 1,3 -self.player) # Le damos el turno al otro jugador
                if value < best_value:
                    best_value = value
                    best_action = action
            return best_value, best_action