# Give the class a name
class PersonalAssistant:
  # Add an __init__ function here
  def __init__(self, todos,birthdays):

    self.todos = todos
    self.birthdays = birthdays
   #Add function to add to do 
  def add_todo(self,new_item):
    self.todos.append(new_item)

   #Add function to remove todo item
  def remove_todo(self,todo_item):
    if todo_item in self.todos:
    # Get the todo_item index in list
      index = self.todos.index(todo_item)
    # pop the index for todo_item in todos list
      self.todos.pop(index)
      return f'{todo_item} was removed'
    else:
      print("Todo is not in list!")

  def get_todo(self):
    return self.todos

  def get_birthdays(self):
    return self.birthdays

  def get_birthday(self,name):
    if name in self.birthdays:
      return f"{name}'s birthday is on {self.birthdays[name]}."
    else:
      return "Can't find a birthad for this person..."

  def add_birthday(self, name, date):
    if name in self.birthdays:
      return f"You already have a birthday for {name}"
    else:
      self.birthdays[name] = date
      return f"{name}'s birthday has been added"

  # Complete the get_contact function code
  def get_contact(self, name):
      if name in self.contacts:
         return  self.contacts[name]
      else:
        return "No contact with that name!"
  def remove_birthday(self, name):
      if name in self.birthdays:
          self.birthdays.pop(name)
          return f"{name}'s birthday has been removed."
      else:
          return "Sorry, there is no recorded birthday for that person."
# Code to test output of the class
#assistant = PersonalAssistant()
#assistant.add_todo('Pick up groceries')
#assistant.remove_todo('Pick up groceries')
# Change name to one from your contacts
#print(assistant.get_contact("Chelsea"))
#print(assistant.get_todo())
#print(assistant.get_birthday("Luz"))