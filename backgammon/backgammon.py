#hatalar 81626
# y in self.board.points düşündüğüm şeyi temsil etmiyor☑️
# bütün pieceler birbirinin klonu. tuhaf sonuçlara yol açar(birinin statüsü diğerlerini de etkiler)☑️
# directionı kullanmayı unutmuşum. bunu kullanmak potential positions bloğunu yarı yarıya kısaltabilir☑️
# hatalar 81726
# 1. <= len(...)  →  < len(...)☑️
# 2. target2 geçersizken target0 ve target1 neden hâlâ çalışmalı?☑️

#81826
#is cell movable metodu eklenmeli ve bu hesaplamalar potential movestan çıkartılmalı☑️
#display board garip davranmaya başladıı☑️

#81926
#capture piece ekleı☑️
# 82026
# Oyuncu iki kez oynayablir. ilk hamleden sonra potential move güncellenmelidir ve oyuncu tekrar seçim yapmalıdır.zarlar çift gelirse oyuncu dörte kere seçim yapmalıdır.
# capturer_pos boş kalınca index out of range hatası veriyor ☑️

#81926
#çift gelirse zarları silmemelisin? ☑️ 

#9826
#vurulan taşları hapse at ☑️

import random

class Game:
   def __init__(self):
       self.board = Board()
       self.dice = Dice()
       self.player1 = Player("Player 1", "w")
       self.player2 = Player("Player 2", "b")
       self.player = self.player1
       self.piece = Piece(color=None)
       self.nextturn = None
       self.running = False
       self.memory = [self.dice.value["dice1"],self.dice.value["dice2"]]
       self.moves_left = 4 if self.memory[0] == self.memory[1] else 2

   def switch_player(self):
        if self.player == self.player1:
            self.player = self.player2
        else:
            self.player = self.player1

        print(f"\n{self.player.name}'s turn ({self.player.color})")      

   def choose_action(self):
       action = print("> stats\n > new game"),
       return action
 
   def display_dices(self):
       return print(f'Dices: {game.dice.value.get("dice1")}, {game.dice.value.get("dice2")}')

   def is_cell_open(self,cellnr):
        isvalid = True
        cell = self.board.points[cellnr]
        if len(cell) > 1:
         if cell[0].color != self.player.color: 
             isvalid = False
        return isvalid

   def selected_position(self):
        decision  = int(input("please select a cell to play from >"))
        return decision  
   
   def potential_positions(self,decision):
       potential_moves =  {"dice1":[],"dice2":[]}
       all_potential_moves = {"dice1":[],"dice2":[]}
       union = [potential_moves,all_potential_moves]
       x = self.board.points[decision]
       x1 = self.board.points
       if len(x) > 0 and self.player.color == x[0].color: 
        if "dice1" in self.dice.value:
         target0 = decision + x[0].direction*self.dice.value["dice1"]
         target0_valid = 0 <= target0 < len(self.board.points)
         if target0_valid:
            if self.is_cell_open(target0):    
                            potential_moves["dice1"].append(target0)         
        if "dice2" in self.dice.value:
         target1 = decision + x[0].direction*self.dice.value["dice2"]
         target1_valid = 0 <= target1 < len(self.board.points)
         if target1_valid:
            if self.is_cell_open(target1):    
                        potential_moves["dice2"].append(target1)         
        # target2 = decision + x[0].direction*(dice.value[0] + dice.value[1])     
        # target2_valid = 0 <= target2 < len(self.board.points) 
        # target0_open = target0_valid and self.is_cell_open(target0)
        # target1_open = target1_valid and self.is_cell_open(target1)   
        for a in x1:   
            if len(a) > 0 and a[0].color == self.player.color:
                if "dice1" in self.dice.value:
                 all_target0 = x1.index(a) + x[0].direction*self.dice.value["dice1"] 
                 all_target0_valid = 0 <=  all_target0 < len(self.board.points)
                 if all_target0_valid:
                    if self.is_cell_open(all_target0):    
                                    all_potential_moves["dice1"].append(all_target0)                 
                if "dice2" in self.dice.value:         
                 all_target1 = x1.index(a) + x[0].direction*self.dice.value["dice2"]
                 all_target1_valid = 0 <=  all_target1 < len(self.board.points)
                 if all_target1_valid:
                    if self.is_cell_open(all_target1):    
                                all_potential_moves["dice2"].append(all_target1)                 
                # all_target2 = x1.index(a) + x[0].direction*(dice.value[0] + dice.value[1])
                # all_target2_valid = 0 <=  all_target2 < len(self.board.points)
                # all_target0_open = all_target0_valid and self.is_cell_open(all_target0)
                # all_target1_open = all_target1_valid and self.is_cell_open(all_target1)                                     
                # if all_target2_valid :
                #     if self.is_cell_open(all_target2):  
                #         if all_target0_open or all_target1_open:
                #             all_potential_moves.append(all_target2)                                                           
        # if target2_valid and target2 in all_potential_moves:
        #      if self.is_cell_open(target2):  
        #         if target0_open or target1_open:
        #              potential_moves.append(target2) 
        # print(f'Dices: {self.dice.value.get("dice1")}, {self.dice.value.get("dice2")}')
                                                                                                                       
       return union

   def moveisvalid(self, move,potential_moves):
        ismovevalid = False
        if move in potential_moves["dice1"] or move in potential_moves["dice2"]:
            ismovevalid = True
        return ismovevalid

   
   def makemove(self, move):
        old_pos = self.board.points[decision]
        piece = old_pos[0]
        self.capture_piece(decision,move)           
        old_pos.remove(piece)
        new_pos =self.board.points[move]
        new_pos.append(piece)
        print(f"piece moved to {move}")       

   def updatedicevalues(self, move, potential_moves):  
       potential_moves = potential_moves[0]
       dice_values = self.memory
       if dice_values[0] != dice_values[1]:
            if move in potential_moves["dice1"]:
                del self.dice.value["dice1"]
            elif move in potential_moves["dice2"]:
                del self.dice.value["dice2"] 
       elif dice_values[0] == dice_values[1]:
                if game.moves_left < 3:
                    if move in potential_moves["dice1"]:
                        del self.dice.value["dice1"]
                    elif move in potential_moves["dice2"]:
                        del self.dice.value["dice2"]                  

   def select_move(self, potential_moves,decision):
        potential_moves = potential_moves[0]
        print("Possible moves: >", potential_moves)
        move = int(input("Select where you want to move: "))

        if move in potential_moves["dice1"] or move in potential_moves["dice2"]:
            old_pos = self.board.points[decision]
            piece = old_pos[0]

            # if self.dice.value["dice1"] == self.dice.value["dice2"]:
            #     print("you have two extra moves with this pair")          

            return move

        print("Invalid move")
        return None

   def capture_piece(self, decision, move):
       capturer_pos = self.board.points[decision]
       captured_pos = self.board.points[move]
       prison = self.board.prison
       if len(capturer_pos) > 0:
        capturer = capturer_pos[0]
        if len(captured_pos) > 0:       
            captured = captured_pos[0]
            if capturer.color != captured.color:
                captured.iscaptured = True
                captured_pos.remove(captured)
            else:
                pass
            return captured.iscaptured

   def start_game(self):
    self.board.points[0].extend(Piece("w") for _ in range(2))
    self.board.points[5].extend(Piece("b") for _ in range(1))
    self.board.points[7].extend(Piece("b") for _ in range(3))
    self.board.points[11].extend(Piece("w") for _ in range(5))
    self.board.points[12].extend(Piece("b") for _ in range(5))
    self.board.points[16].extend(Piece("w") for _ in range(3))
    self.board.points[18].extend(Piece("w") for _ in range(5))
    self.board.points[23].extend(Piece("b") for _ in range(2))

class Player:
    def __init__(self,name,color):
         self.name = name 
         self.color = color
         self.score = 0
         self.win  = 0
         self.lose = 0
         self.matches_played = 0
         self.win_total = 0
         self.lose_total = 0
         self.player_info = {}

    # def create_player(self):
    #     self.name = input(f"name >")          
    #     with open("players.txt", "w") as file:
    #         file.write(
    #            "name:" + " " + player.name+ ",\n" +
    #            "L:" + " " + str(player.lose) + ",\n" +
    #            "W:" + " " + str(player.win)
    #         )    
    #     print(f"new player {self.name} has been created")        
class Piece:
   def __init__(self,color):
       self.color = color 
       self.iscaptured = False
       self.isscored = False
       self.direction = 1 if color == "w" else -1
    
   def __repr__(self):
       return f"{self.color}"
       
class Dice:
    def __init__(self):
        self.value = {}
        self.roll_dices()

    def roll(self):
        return random.randint(1, 6)

    def roll_dices(self):
        self.value = {
            "dice1": self.roll(),
            "dice2": self.roll()
        }
       
class Board:
   def __init__(self):
       self.size = 24
       self.points = [[] for _ in range(self.size)]
       self.prison = []
   def place_piece(self, piece, position):
       self.points[position].append(piece)
       piece.position = position
       return self.points
       
   def count_piece(self, position):
       return len(self.points[position])

   def color_of_cell(self,point):     
             return set(self.points[point])
   def display(self):
      display_board = []       
      for point in self.points:
            counts = {}
            for item in point:
             if item.color in counts:
                    counts[item.color] += 1
             else:
                    counts[item.color] = 1
            display_board.append(counts)
      return display_board             
board = Board()
game = Game()
game.start_game()
# with open("player.txt","r") as file:
#     content =file.read()
#     if content == "":
#         print("no player record found. creating new player...")
#         new_player = player.create_player()
#     else:
#         print(f"welcome {player.name}")
#player1 = game.player.create_player()
while True:
    print(f"\nTurn: {game.player.name} ({game.player.color})")
    
    while game.moves_left > 0:
        print(game.board.display())
        game.display_dices()
        decision = game.selected_position()
        positions = game.potential_positions(decision)
        move = game.select_move(positions, decision)

        if game.moveisvalid(move,positions[0]):
          game.makemove(move)
          game.updatedicevalues(move, positions)
          game.moves_left -= 1

        print(game.moves_left)

    if game.moves_left == 0:
        game.switch_player()
        game.memory.clear()  
        game.dice.roll_dices()
        game.memory.append(game.dice.value["dice1"])
        game.memory.append(game.dice.value["dice2"])
        game.moves_left = 4 if game.memory[0] == game.memory[1] else 2


    

    


