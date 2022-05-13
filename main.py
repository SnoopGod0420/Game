def wild_fight():
  print("A wild", pokename ,"has appeared!")
  time.sleep(1)
  print("What will you do", Username +"!")
  fight_choice = input("Fight(F), Run(R), Catch(C)")
  if fight_choice == 'F':
    fight()
  elif fight_choice == 'R':
    home()
  else fight_choice == 'C':
    catch()
    
    