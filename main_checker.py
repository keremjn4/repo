import random

class Game:
   def __init__(self):
       self.board = Board()
       self.dice = Dice()
       self.player = Player(name=None,color=None)
       self.piece = Piece(color=None)
       self.running = False

#    def potential_moves(self):
#         points = self.board.points    
#         if dice.value[0] != dice.value[1]:
#          potential_positions = {
#              index: (index +dice.value[0],index + dice.value[1],index + dice.value[0] + dice.value[1])
#                for index, point in enumerate(points)
#                                  if len(point) > 0
#                                  if point[0].color == board.color_of_cell(index+dice.value[0])
#                                  }
#         else:
#           potential_positions = {index: (index +dice.value[0]*4,(index +dice.value[0],index +dice.value[0]*2),(index +dice.value[0])) for index, point in enumerate(points) if len(point) > 0}
#         return potential_positions,f"dice: {(dice.value[0],dice.value[1])}"

   def selected_position(self):
       decision = int(input("please select a cell for your next move"))
       return decision
   
   def potential_positions(self,decision):
       potential_moves = []
       x = self.board.points[decision]
       if self.player.color == "w":  
            y = self.board.points[decision+dice.value[0]]
            z = self.board.points[decision+dice.value[1]]
            p = self.board.points[decision+dice.value[0] + dice.value[1]]                   
            if len(x) > 0 and y in self.board.points and self.player.color == x[0].color:
                    if len(y) == 0:    
                            potential_moves.append(decision+dice.value[0])      
                    elif len(y) > 0 and x[0].color == y[0].color:
                        potential_moves.append(decision+dice.value[0])

                    elif len(y) > 0 and x[0].color != y[0].color:
                        if len(y) ==1:
                            potential_moves.append(decision+dice.value[0])
                
            if len(x) > 0 and z in self.board.points:
                    if len(z) == 0:    
                        potential_moves.append(decision+dice.value[1])      
                    elif len(z) > 0 and x[0].color == z[0].color:
                        potential_moves.append(decision+dice.value[1])
                    elif len(z) > 0 and x[0].color != z[0].color:
                        if len(z) ==1:
                            potential_moves.append(decision+dice.value[1])

            if len(x) > 0 and p in self.board.points:
                   if len(p) <= 1 or x[0].color == p[0].color:
                        if len(y) > 1 and x[0].color != y[0].color:
                            if len(z) <= 1:
                                potential_moves.append(decision+dice.value[1] +dice.value[0]) 
                        elif len(z) > 1 and x[0].color != z[0].color:
                            if len(y) <= 1:
                                potential_moves.append(decision+dice.value[1] +dice.value[0])  
                        else:  potential_moves.append(decision+dice.value[1] +dice.value[0])
                                                            
       if self.player.color == "b":
            k = self.board.points[decision-dice.value[0] - dice.value[1]]
            t = self.board.points[decision-dice.value[0]]
            s = self.board.points[decision-dice.value[1]]
            if len(x) > 0 and t in self.board.points and decision-dice.value[0] > 0:
                    if len(t) == 0:    
                            potential_moves.append(decision-dice.value[0])      
                    elif len(t) > 0 and x[0].color == t[0].color:
                        potential_moves.append(decision-dice.value[0])
                    elif len(t) > 0 and x[0].color != t[0].color:
                        if len(t) ==1:
                            potential_moves.append(decision-dice.value[0])
                
            if len(x) > 0 and s in self.board.points and decision-dice.value[1] > 0:
                    if len(s) == 0:    
                        potential_moves.append(decision-dice.value[1])      
                    elif len(s) > 0 and x[0].color == s[0].color:
                        potential_moves.append(decision-dice.value[1])
                    elif len(s) > 0 and x[0].color != s[0].color:
                        if len(s) ==1:
                            potential_moves.append(decision-dice.value[1])

            if len(x) > 0 and k in self.board.points:
                   if len(k) <= 1 or x[0].color == k[0].color:
                        if len(t) > 1 and x[0].color != t[0].color:
                            if len(s) <= 1:
                                potential_moves.append(decision-dice.value[1]-dice.value[0]) 
                        elif len(s) > 1 and x[0].color != s[0].color:
                            if len(t) <= 1:
                                potential_moves.append(decision-dice.value[1]-dice.value[0])  
                        else:  potential_moves.append(decision-dice.value[1]-dice.value[0])                            
        
       return potential_moves, f"dice: {(dice.value[0],dice.value[1])}"

   def start_game(self):
       w = self.piece = Piece(color="w")
       b = self.piece = Piece(color="b")
       board = self.board.points
       board[0].extend([w]*2)
       board[5].extend([b]*5)
       board[7].extend([b]*3)
       board[11].extend([w]*5)
       board[12].extend([b]*5)
       board[16].extend([w]*3)
       board[18].extend([w]*5)
       board[23].extend([b]*2)

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

    def create_player(self):
        self.name = input(f"name >")      
        self.color = input(f"color >")    
        self.player_info["name": self.name, "color": self.color, "score": self.score, "win": self.win]
               
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
      self.value = (random.randint(1,6),random.randint(1,6))
      
class Board:
   def __init__(self):
       self.size = 24
       self.points = [[] for _ in range(self.size)]
     
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
             if item in counts:
                    counts[item] += 1
             else:
                    counts[item] = 1
            display_board.append(counts)
      return display_board             
board = Board()
dice = Dice()
game = Game()
player = Player("kerem","b")
game.player = player
game.start_game()
player1 = game.player.create_player()
print(game.board.points)
print(game.board.display())
print(game.potential_positions(23))
print(game.board.color_of_cell(5))
print(game.board.count_piece(5))
print(game.player.color)


  
  



