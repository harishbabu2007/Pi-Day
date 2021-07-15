from pi_day_module import PiDay


user_choice = int(input("Enter 1 for pi value and 2 for relation between e and pi : "))

while(1):
  if user_choice == 1:
    p = int(input("Enter a number of decimal places : "))
    p = PiDay(p)
    p.get_pi()
    break

  elif user_choice == 2:
    p = PiDay(15)
    p.get_relation_e()
    break

  else:
    print("please enter a proper value")