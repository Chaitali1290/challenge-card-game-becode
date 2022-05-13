#creating a class board
class Board: 
    def __init__(self,player,turn_count:int,active_cards,history_cards):
        self.player=player
        self.turn_count=turn_count
        self.active_cards=active_cards
        self.history_cards=history_cards

    def start_game(self):
        
