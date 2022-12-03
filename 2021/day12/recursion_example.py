def recurse(i):
    print(i)
    if i == 0:
        return
    recurse(i-1)
    return

def hello(name):
    print("Hello {}".format(name))

def square(x):
    """ A function to square the variable x. """
    return x*x

def main():
    hello("Becca") 
    hello("Sarah")
    hello("Waffles")
    print(square(5))
    recurse(10)


if __name__ == '__main__':
    main()
