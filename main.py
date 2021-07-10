import json
#imports PersonalAssistant.py file
from PersonalAssistant import PersonalAssistant

#ADD CODE: open JSON file and pass data to PersonalAssistant class
with open("todo.json", 'r')as todos, open("birthdays.json", "r") as birthdays:
  todo_list = json.load(todos)
  birthday_list = json.load(birthdays)

  assistant = PersonalAssistant(todo_list,birthday_list)
done = False

while not done:
  user_command = input(
    "\n\nHow can I help you? \n 1: Add a to-do\n 2: Remove a to-do\n 3: Get to-do list\n 4: Get Birthday \n 5: Add Birthday\n 6: Remove Birthday\n Select a number or type 'Exit to quit: ")

  if user_command == "1":
    user_input = input("Item to add to to-do list: ")
    assistant.add_todo(user_input)
  elif user_command == "2":
    user_input = input("Item to remove from to-do list: ")
    assistant.remove_todo(user_input)
  elif user_command == "3":
    print("Your to-do list")
    print(assistant.get_todo())
  elif user_command == "4":
    print('\nYour birthday contacts: \n')
    for name in assistant.get_birthdays():
      print(name)
    user_input = input("\nEnter a name: ")
    print(f"\n{assistant.get_birthday(user_input)}")
  elif user_command == "5":
    print('Add a birthday: \n')
    name = input('Name of the person: ')
    birthday = input('Their birthday (ex:08/08/2012): ')
    print(f"\n{assistant.add_birthday(name, birthday)}")
  elif user_command == "6":
    print('Your birthday contacts: \n')
    for name in assistant.get_birthdays():
      print(name)
    user_input = input('\nWhich birhtday do you want to remove? ')

    print(f"\n{assistant.remove_birthday(user_input)}")
  elif user_command.lower() =='exit':
    done = True
    print("\nGoodby, see you soon!")
else:
  print('\nNot a valid command.')
#ADD CODE: write data to JSON file
with open("todo.json", "w") as write_file, open("birthdays.json", "w") as write_birthdays:
  json.dump(assistant.get_todo(),write_file)
  json.dump(assistant.get_birthdays(),write_birthdays)