#Crete a class Symbol with two attributes color and icon
class Symbol:
    def __init__(self,color,icon)->str:
        self.color = color
        self.icon = icon

#crete a class Card which inherits from class symbol

class Card(Symbol):
    def __init__(self,color,icon,value)->str:
        super().__init__(color,icon)
        self.value = value

   
    def __str__(self): #function to create on card
        return f"{self.color},{self.icon},{self.value}"

card = Card('red',"♥","3") 
print(card)
            




        