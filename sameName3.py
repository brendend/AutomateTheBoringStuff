def spam():
    global eggs
    eggs = 'spam' # this is global

def bacon():
    eggs = 'bacon' # this is a local variable

def ham():
    print(eggs) # this is the global

eggs = 42 #this is global
spam()
print(eggs)
