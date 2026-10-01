while True:
#    Твое имя и сколько тебе лет
  print("Как тебя зовут?")
  name = str(input("Введите имя:"))
  print("Привет,", name)

  print("А сколько тебе лет?")
  age = input("Введите ваш возраст:")
  if not age.isdigit():
    print("Возраст должен быть числом. Попробуем снова.\n")
    continue
  age = int(age)

  print(f"Значит ты {name} и тебе {age}?")
  question1 = str(input("(Да или Нет) Твой ответ   "))
  if question1.lower() in ("да", "yes"):
    print("Все я запомнил как тебя зовут")
    break
  elif question1.lower() in ("нет", "no"):
    print("Ах ты врун")
    print("Тогда")
  else:
    print("Что ты написал?")