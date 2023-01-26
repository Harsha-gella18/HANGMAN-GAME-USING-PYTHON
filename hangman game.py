import random
print(''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    ''')
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
word_list=["apple","banana","orange","mango","pineapple","grape","strawberry","watermelon","kiwi","peach","lion","tiger","bear","elephant","giraffe","wolf","hippopotamus","raccoon","kangaroo","penguin"]
chosen_word=random.choice(word_list)
str=[]
word_length=len(chosen_word)
lives=6
for i in range(word_length):
    str+="_"
end_game=False
while not end_game: 
    guess=input("enter the letter").lower()
    for i in range(word_length):
        letter=chosen_word[i]
        if letter==guess:
            str[i]=letter
    if guess not in chosen_word:
       print("it is not in the choose word")
       lives-=1
       if lives==0:
          end_game=True
          print("you Loose")
       print(stages[lives])
    print(f"{' '.join(str)}")
    if "_" not in str:
        end_game=True
        print("you win")
