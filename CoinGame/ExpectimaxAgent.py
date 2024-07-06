from board import Board
from agent import Agent

class ExpectimaxAgent(Agent):
    def __init__(self, player=1, depth=1):
        super().__init__(player)
        
    def next_action(self, obs):
        return self.expectimax(obs)
    
    def heuristic_utility(self, board):
        return 0
    
    def expectimax(self, board):
        possible_actions = board.get_possible_actions()
        action = possible_actions[0]
        return action