# using the wikipedia package by importing it.
import wikipedia

# user input
answer = input('which page would you like to see?: ')
# try the code
try:
    #  this is going to go into the imported wikipedia at page and take the user input - matching the input and provideing the content
    selected = wikipedia.page(answer)

# this will print the matched page title and the matched page content
    print(selected.title)
    print(selected.content)
    # this will catch if the page id does not match a page
except wikipedia.exceptions.PageError:
    print("does not exist. Please try another page")
    # this will catch any other failures and print an easily read message
except:
    print('Something went wrong. Please try again later')    
