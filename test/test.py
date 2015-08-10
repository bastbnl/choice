import choice

def c():
  print("Delete confirmed")

# Get a yes or no response (default is no)
confirm = choice.Binary('Are you sure you want to delete?', False).ask()
if confirm:
    c()

# Input an arbitrary value, check for correctness
howmany = choice.Input('How many pies?', int).ask()
print("You ordered {0} pies".format(howmany))

# Choose from a set of options
entree = choice.Menu(['steak', 'potatoes', 'eggplant']).ask()
print("You choice {0}".format(entree))


posts = ['post {0}'.format(num) for num in range(15)]

resp = choice.Menu(posts, ['edit', 'delete', 'publish'], ['newpost', 'exit']).ask()
print(resp)

resp = choice.Input('Enter an integer', int).ask()
resp = choice.Input('Enter a string with "a" in it', choice.validate(lambda s: "a" in s)).ask()

resp = choice.Binary('Yes or no?', True).ask()
resp = choice.Binary('yes or No?', False).ask()
resp = choice.Binary('yes or no?').ask()
