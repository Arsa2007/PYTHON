import random

def get_choices():
  player = input("Enter a choice (rock, paper, scissors)") 
  ddict=['scissors','paper','rock']
  computer = random.choices(ddict)
  dict={"PlAYERCHOICE":player,"COMPUTERCHOICE":computer}
  return dict
  
  



def check(play,comp):
  if play == comp :
    return "It's a tie"
    
  elif play == "rock" :
     if comp == "scissors" :  
       return "rock wins" 
  elif play == "rock" : 
     if comp == "paper" :  
        return "paper wins"
  elif play == "rock" :
     if comp == "rock" :  
       return "TIE"
       
  elif play == "scissors" :
     if comp == "paper" : 
       return "scissors wins"
  elif play == "scissors"  :
     if comp == "rock" :
       return "rock wins"
  elif play == "scissors" :
      if comp == "scissors" :
        return "TIE"
        
  elif play == "paper" :
      if comp == "scissors" :
        return "scissors wins"     
  elif play == "paper" :
     if comp == "rock" :
      return "rock wins"
  elif play == "paper" :
   if comp == "paper" :
    return "TIE"
  else:
    return "invalid"

def play_game():
 GAME = get_choices()
 GAME1 = check(GAME["PlAYERCHOICE"],GAME["COMPUTERCHOICE"][0])
 print(GAME1)
  


a = play_game() 
print(a)


      

        