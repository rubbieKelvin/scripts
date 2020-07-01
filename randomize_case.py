from sys import argv          # for reading command line argument
from random import choice     # randomization


def randomize(string):
    """returns randomly generated cases per charactar"""
    return "".join(
        [
            choice(
                [char.upper(), char.lower()]
            ) for char in string
        ]
    )

# this block reads sys.argv then randomize the input
if __name__ == "__main__" and len(argv) > 1:
    args = argv[1:]
    for arg in args:
        print(f"string \"{arg}\":", randomize(arg))


# this block runs when there's no passed argument
# it just ask the user for inputs instead and then randomize
if __name__ == "__main__" and len(argv) <= 1:
    while True:
        try:
            text = input("enter a text to randomize: ")
        except (KeyboardInterrupt, EOFError) as e:
            break
        if text:
            print("randomized cased string:", randomize(text))
        else:
            break