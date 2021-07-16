from pi_day_module import PiDay


user_choice = int(input("Enter 1 for pi value and 2 for relation between e and pi, 3 for value of pi at a decimal place \n: "))

while(1):
  if user_choice == 1:
    p = int(input("Enter a number of decimal places : "))
    p = PiDay(p)
    p.get_pi()
    break

  elif user_choice == 2:
    p = PiDay(1000)

    # geting the value of pi and e
    p.get_pi()
    print("\n")
    p.compute_e()
    p.get_relation_e()

    break

  elif user_choice == 3:
    p = int(input("Enter a number of decimal places : "))
    p = PiDay(p)
    p.value_at_place_pi()
    break

  else:
    print("please enter a proper value")
    break