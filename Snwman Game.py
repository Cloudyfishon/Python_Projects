#get a wordlist from the Internet
import urllib.request
def readwebsit(url):
  file = urllib.request.urlopen(url)
  word_list = file.read()
  word_list = str(word_list, encoding='utf-8')
  return  word_list

url = "https://www.mit.edu/~ecprice/wordlist.10000"
word_list = readwebsit(url)
word_list= list(word_list.split('\n'))
#print(word_list)



#check if the input is valid
def valid(answer):
  alphabetic = answer.isalpha()
  global valida
  if len(answer) == 1:
      length = True
      
  else:
      length = False
  
  if alphabetic == True and length == True:
      
      valida = True
      return True
  else:
      valida = False
      return False
  
#check if the guessing is repeat
def repeat(answer):
  #used_ = used.curselection
  #if answer in used.get():
  global repeata
  repeata = False
  #for i in used.curselection():
  for i in range(0,position):
      if answer == used.get(i):
          repeata = True
          return True
  

#check if the answer is correct
def match(answer):
  matched = False
  global times
  times = 0
  for o in range(0,num_letter):
      if answer == word[o]:
          global empty_answer
          empty_answer[o] = answer
          matched = True
          times +=1
  if matched == True:
      return True
  return times

#the end of the game
def game_over():
  new_game = True
  window_game.destroy()
  global over_text
  if chance == 0:
      correct_answer = ' '.join(word)
      over_text = "Game over! It's {}\n Do you want to play again?".format(correct_answer.upper())
  elif empty_answer == word:
      correct_answer = ' '.join(word)
      over_text = "{} Congratulation! You win!\n Do you want to play again?".format(correct_answer.upper())
  over = tk.messagebox.askyesno(" ",over_text)
  if over:
      start()
  else:
      window.destroy()
   
      
    
          

#make a GUI
import tkinter as tk

window = tk.Tk()
window.title('Snowman game')
window.geometry('400x200')

var = tk.StringVar()
l = tk.Label(window, textvariable = var, font = ('Arial',12), width = 30, height = 2)
l.pack()
var.set('Welcome to snowman')



def start():
  global window_game
  window_game = tk.Toplevel(window)
  window_game.geometry('600x400')
  window_game.title('Snowman')
  new_game = True
  
  #print select a random word
  def select():
      global chance
      if chance == 6:
          selection = tk.Label(window_game, text = 'selecting a random word...', font = ('Arial',15) , anchor = 'center')
          selection.pack()
      
             
  def matching():
      #find out the correct answer
      var2 = tk.StringVar()
      correct_answer = tk.Label(window_game,textvariable = var2, font = ('Arial',15), width = 40, height = 2).place(x=5,y=220)
      var2.set(' ')
      answer = guessing_answer.get()
      if match(answer) == True:
          state = "Correct! {} is in the word {} times.".format(answer,times)
          var2.set(state)
          answer = guessing_answer.get()
          
      else:
          var2.set("Incorrect guessing")
          global chance
          chance = chance - 1
          
  def enter():
      #if the answer is valid
      global answer
      answer = guessing_answer.get()
      if valid(answer) == False:
          tk.messagebox.showerror("WRONG","Invalid value...Please enter again.")
          

      elif repeat(answer) == True:
          repeat_text = "You have already guess: {} Try again...".format(answer)
          tk.messagebox.showerror("WRONG",repeat_text)
      
      #if the answer is correct
      if valida == True and repeata == False:
          global position
          position +=1
          used.insert(position,answer)
          matching()
          var1.set(empty_answer)
          if chance == 0 or empty_answer == word:
              game_over()
              
          re_chance = "You have {} incorrect guesses remaining.".format(chance)
          var3.set(re_chance)
      
        

 
              
  if new_game == True:   
  #choose a random word
      import random
      global word
      word = list(word_list[random.randrange(0,len(word_list))])
  
      #find out how many letters does this word have
      global num_letter
      num_letter = int(len(word))
      global empty_answer
      empty_answer = list("_"*num_letter)
      global used
      used = tk.Listbox(window_game)
      used.insert(1," ")
      #used.pack()
      global position
      position = 1
      global chance
      chance = 6
      select()
      new_game =False
  
  if chance != 0 and empty_answer != word:
      
      #print the empty word
      var1 = tk.StringVar()
      emp_answer = tk.Label(window_game, textvariable = var1, font = ('Arial',15), width = 2*num_letter, height = 2 , anchor = 'center')
      emp_answer.pack()
      var1.set(empty_answer)
      var3 = tk.StringVar()
      remain_chance = tk.Label(window_game, textvariable = var3, font = ('Arial',15), width = 45,height = 2).place(x = 5, y = 70)
      re_chance = "You have {} incorrect guesses remaining.".format(chance)
      var3.set(re_chance)
      
      #ask user to input their answer
      l2 = tk.Label(window_game, text = "Please enter a letter to guess: ", font = ('Arial',15), width = 30, height = 2).place(x=5,y=120)
      guessing = tk.StringVar()
      guessing_answer = tk.Entry(window_game, textvariable = guessing)
      guessing_answer.place(x=260,y=120)
      b1 = tk.Button(window_game, text = 'Confirm', width = 10, height = 2, command = enter)
      b1.place(x=300,y=160)
 
          
      #answer = guessing_answer.get()
     # position +=1
     # used.insert(position,answer)
      
      
      
      

  
      
b = tk.Button(window, text = 'START', width = 15, height = 2, bg = 'yellow', command = start)
b.pack()

play = False
#game()

  

  
window.mainloop()
      

