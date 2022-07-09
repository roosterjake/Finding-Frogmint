print('''
   o-o
  (   )  
  /`-'\ 
 :'}#{':
} \! !/ {  
`-'   `-'
                 |.|
                 |.|
                |\./|
                |\./|
.               |\./|               .
 \^.\          |\\.//|          /.^/
  \--.|\       |\\.//|       /|.--/
    \--.| \    |\\.//|    / |.--/
     \---.|\    |\./|    /|.---/
        \--.|\  |\./|  /|.--/
           \ .\  |.|  /. /
 _ -_^_^_^_-  \ \\ // /  -_^_^_^_- _
   - -/_/_/- ^ ^  |  ^ ^ -\_\_\- -
''')
print("Welcome to Finding Frogmint.")
print("Your mission is to find the Frogmint.") 





choice1 = input("Would you like to look up or down? ").lower()

if choice1 == "up":
  choice2 = input("You are on the right track, keep searching!!! \n Would you like to play music or go to work? ").lower()
  if choice2 == "play music":
    choice3 = input("Your senses are strong, you are very close to Frogmint. \n Do you prefer enlightenment or negativity? ").lower()
    if "enlightenment":
      print("You found Frogmint! Enjoy!")
  else: 
    print("Maybe Frogmint is not for you at this time.")
  
else:
  print("Please consider looking up next time!")
  
