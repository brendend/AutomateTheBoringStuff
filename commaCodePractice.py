spam = ['dogs', 'cats', 'birds', 'monkeys']
def sentence(x):
    if len(x) == 1:
        return x[0] + ', '
    return (', '.join(x[:-1])+ ' and ' + x[-1])

print(sentence(spam))