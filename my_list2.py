#!/usr/bin/env python
# coding: utf-8

# In[1]:


my_list = []
my_list.append("apples")
print(my_list)
my_list.append("pears")
print(my_list)
my_list.remove("apples")
print(my_list)


# In[2]:


my_name = input("What is your name?")
if my_name == "Asliddin":
    print(f"Hello admin!")
else:
    print(f"Hello {my_name}")
  


# In[3]:


my_name = input("What is your name?")
if my_name == "Asliddin":
    print(f"Hello admin!")
else:
    print(f"Hello {my_name}")


# In[ ]:


my_name = input("What is your name?")
if my_name == "Asliddin":
    print(f"Hello admin!")
else:
    print(f"Hello {my_name}")


# In[6]:


current_users = ["Asliddin", "Jalol", "Johongir", "Sherzod", "Muxammadjon"]
new_users = ["Noila", "Jalol", "Durdona", "Johongir", "Marjona"]

for username in new_users:
    if username in current_users:
        print("Username unavailable.")
    else:
        print("Username available.")


# In[9]:


import random
secretNumber = random.randint(20, 40)
print('I am thinking of a number between 20 and 40.')

for guessesTaken in range(1, 7):
    print('Take a guess.')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break   

if guess == secretNumber:
    print('Good job! You guessed my number in ' + str(guessesTaken) + 'guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber))


# In[ ]:




