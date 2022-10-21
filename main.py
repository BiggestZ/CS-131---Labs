def form():
  """The form function that collects info from users"""
  # Get street number
  name = get_name()
  streetNum = get_street_num()
  town = get_town()
  state = get_state()
  country = get_count()
  age = get_age()
  phone = get_phoneNum()
  email = get_email()
  # Collect more pieces of information by writing more functions

  # Then, print out all our collected info in a form
  print("=====================")
  print("We've collected the following information:")
  print("- Name:", name)
  print("- Town:", town)
  print("- State:", state)
  print("- Country:", country)
  print("- Street Number:", streetNum)
  print("- Age:", age)
  print("- Phone Number:", phone)
  print("- Email:", email)
  # add more
  print("=====================")


def get_street_num():
  """ EXAMPLE: Gets the user's street number.
  Repeats until a valid street number is given.
  Output:
  - streetNum: an integer representing the user's street number
  """
  streetNum = input("Enter the street number of your address: ")

  # Check to see if it's empty!
  if streetNum == "":
    print("SORRY! You forgot to input your street number!\n")
    return get_street_num()
  # Check to see if it's a number!
  elif streetNum.isdigit() == False:
    print("SORRY! Your street number should be a positive number\n")
    return get_street_num()
  else:
    return streetNum

def get_age():
  """ Gets the user's age
  Repeats until a valid age is given
  """
  age = input("Enter your age: ")
  # WRITE MORE CODE HERE
  if(age == ""):
    print("Please enter a number!")
    return get_age();
  elif (int(age) > 120 or int(age) < 0):
    print("Please enter a valid age!")
    return get_age();
  else:
    return age

# TODO: WRITE MORE FUNCTIONS THAT CHECK INPUT!

def get_phoneNum():
  phoneNum = input("Please Enter Your Phone Number(No Dashes Ex:2123321290): ")

  if (phoneNum == ""):
    print("Please enter a number!")
    return get_phoneNum()
  elif (len(phoneNum) != 10):
    print("Please enter a real phone number(Ex:2123321290)!")
    return get_phoneNum()
  elif (phoneNum.isdigit() == False):
    print("Please enter positive numbers(No letters or negative numbers): ")
    return get_phoneNum()
  else:
    p1 = phoneNum[0:3]
    p2 = phoneNum[3:6]
    p3 = phoneNum[6:]
    finNum = "(" + p1 + ") " + p2 + "-" + p3
    return finNum

def get_email():
  email = input("Please Enter Your Email: ")

  if ("@" not in email or "." not in email or len(email) < 5):
    return get_email()
  else:
    return email.lower()

def get_name():
  name = input("Please Enter Your Full Name: ")
  s_name = name.split(" ")
  for i in s_name:
    if(not i.isalpha() and "-" not in i):
      return get_name()
    elif (len(i) < 2):
      return get_name()
  else:
    return name


def get_town():
  town = input("Please Enter the town you are from: ")
  s_town = town.split(" ")
  for i in s_town:
    if (not i.isalpha()):
      return get_state()
    elif (len(i) < 2):
      return get_state()
    else:
      return town

def get_state():
  state = input("Please Enter the state you are from ( write N/A if International): ")
  st_town = state.split(" ")
  for g in st_town:
    if (not g.isalpha()):
      return get_state()
    elif (len(g) < 2):
      return get_state()
    else:
      return state

def get_count():
  country = input("Please Enter the country you are from: ")
  s_country = country.split(" ")
  for z in s_country:
    if (not z.isalpha()):
      return get_count()
    elif (len(z) < 2):
      return get_count()
    else:
      return country
# Runs the primary program
form()

"""
Would your program work for the visitors in Part III? If not, why not? What assumptions did you make about the personal information of the visitors? What assumptions did you make about how this information would be entered?:


My Program would not work for the part 3 visitors. For the First Visitor, My program would 
fail at the phone number. I programmed the form to only take numbers that are a length of 10 numbers, 
the length of an American Phone Number without dashes. For the 2nd visitor, I did not consider if the 
user were to intentionally leave the boxes blank, or provide a website as input.
						 								
___________________________________________________________

How would you change your program so that it wouldn’t fail? What are the advantages and disadvantages of doing this? You do not have to actually make the changes, only describe what you would do.
	
I would have to change the phone number so that it can take more or less than 10 numbers. 
This can make my code less effective at validating the information by giving the user more control 
over their input. For the 2nd visitor, I would have to create a seperate field where people can enter 
other forms of data (website links, social media, etc) as well as make it so fields can be left 
intentionally blank.

___________________________________________________________ 								
Why might programmers care about these things? How might you approach these problems differently in the future? 


A programmer cares about these things because not accounting for these factors makes our code 
less accessible and therefore ineffective. 
There is no point in creating a form that people cannot use. I will use this lab as a lesson to 
consider when my constraints may be excessive or exclusive to particular groups.		
"""
