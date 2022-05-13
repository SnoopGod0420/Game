def wild_fight():
  pokename = 
  print("A wild", pokename ,"has appeared!")
  time.sleep(1)
  print("What will you do", Username +"!")
  fight_choice = input("Fight(F), Run(R), Catch(C)")
  if fight_choice == 'F':
    fight()              #functions will be made for F,C and R
  elif fight_choice == 'R':
    home()
  elif fight_choice == 'C':
    catch()
  
    