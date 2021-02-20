


def color_text(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)
  
text = 'Hello, World'
colored_text = color_text(255, 0, 0, text)


class game_da_velha():  
  def __init__(self):
    self.table=[["","",""],["","",""],["","",""]]
    self.turn="x"

  def who_win(self,table):
    if(table[0][0]==table[1][1] and table[1][1]==table[2][2]):
      return table[0][0]
    elif(table[2][0]==table[1][1] and table[1][1]==table[0][2]):
      return table[2][0]
    else:
      line=[] #horizontal
      line2=[] #vertical
      dist_i = len(table)
      dist_j=len(table[0])
      
      for i in range(dist_i):
        for j in range(dist_j):
          #print(table[i][j],"...AQUI")
          line.append(table[i][j])
          line2.append(table[j][i])
        if(line[0]==line[1] and line[1]== line[2]):
          return line[0]
        elif(line2[0]==line2[1] and line2[1]== line2[2]):
          return line2[0]
        line=[]
        line2=[]
      return "" 


  def new_game(self):
    self.table=[["","",""],["","",""],["","",""]]
    self.turn="x"

  def show_table(self, table):    
    print("\n  1|2|3 ")
    dist=len(table[0])
    for i in range(dist):
      print(i + 1, table[i][0] , "|" , table[i][1], "|" , table[i][2])      
      if(i<dist-1):
        print("--------")

    print("\n")
      


  def move(self,piece,a,b):
    if(self.table[a][b]!=""):        
        print(color_text(255, 0, 0,"Casa ocupada!"),"\n")
        return 0
    if(self.turn==piece):      
      if(self.turn == "x"):
        self.turn="o"
      else:
        self.turn="x"
      
    else:
      print(color_text(255, 0, 0,"Agora é a vez do: "), color_text(255, 255, 0,self.turn),"\n")
      return 0
    
    self.table[a][b]=piece
    win = self.who_win(self.table)
    if(win != ""):
      
      print(color_text(255, 0, 0, "O '"), color_text(0, 255, 0, win), color_text(255, 0, 0, "' venceu o jogo!"))
      self.show_table(self.table)
      self.new_game()      
      
    self.show_table(self.table)



print("  1|2|3 ")
print("1  | | ")
print("--------")
print("2  | | ")
print("--------")
print("3  | | \n")
game = game_da_velha()
while True:
  #print(game.table)
  while game.who_win(game.table)!="x" or game.who_win(game.table)!="o":    
    entrada = input(color_text(230, 230, 230,"Coloque a peça e a posicao, exemplo 'x12',  : "))
    """print(entrada[0]!="x")
    print(entrada[0]!=["o"])
    print(int(entrada[1]) < 1)
    print(int(entrada[1]) > 3) 
    print(int(entrada[2]) < 1)
    print(int(entrada[2]) > 3)"""
    while((entrada[0]!="x" and entrada[0]!="o") or (int(entrada[1]) < 1)  and int(entrada[1]) > 3 or int(entrada[2]) < 1 and int(entrada[2]) > 3):
      print("\n por favor digite um valor válido, 'x' ou 'o'")  
      entrada = input("Coloque a peça e a posicao, exemplo 'x12',  : ")
      print("\n")
    game.move(entrada[0],int(entrada[1])-1,int(entrada[2])-1)






  


