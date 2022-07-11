

def TreasureIsland():
  print("After fairing the harsh seas for 6 months, your crew comes across an uncharted island\nYou're tasked with with leading the shore party in search of supplies.\nAs you clear the beach and begin hacking through the thick brush of the jungle,\nyou come across a stone path that appears ancient.\n")
  choice_1 = (input("Upon following the path for some time, you've arrived at a crossroads\nWhich way will you go, left or right?"))

  if choice_1[0].upper() == "R":
    print("You and your mates are barraged by arrows from an unknown location. The only place you'll be sailing is the river Styx")
  elif choice_1[0].upper() == "L":
    print("After passing several obelisk structures and rock carvings the canyon begins to wrap around you.\nA narrow doorway into a dark cave revals itself around a bend of the rockface.\nThe ancient ruins seem to stretch into the depths.\nThe only options are to proceed or climb out.")
    choice_2 = input("Forward through the cave or up?")
    if choice_2[0].upper() == "F" or choice_2 == 'cave':
      print('''
        <>=======() 
        (/\___   /|\\          ()==========<>_
              \_/ | \\        //|\   ______/ \)
                \_|  \\      // | \_/
                  \|\/|\_   //  /\/
                  (oo)\ \_//  /
                  //_/\_\/ /  |
                @@/  |=\  \  |
                      \_=\_ \ |
                        \==\ \|\_ snd
                    __(\===\(  )\
                    (((~) __(_/   |
                        (((~) \  /
                        ______/ /
                        '------'
        ''')
      print("There are several torches just within the entrance,\nafter lighting one you discover a large lizard creature.\nYou are dragon barbecue.")
    elif choice_2[0].upper() == 'U' or choice_2 == 'cliff':
      print("upon scaling the cliff you discover a big ol pile of cash.")

TreasureIsland()