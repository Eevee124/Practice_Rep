import random

class Coinflips:
    def __init__(self):
        self.__guesses = []
        self.__prev_game = []

    def play(self, guess):
        if not (guess == "heads" or guess == "tails"): raise Warning("invalid  guess")

        res = random.choice(["tails", "heads"])

        self.__guesses.append(guess)
        self.__prev_game.append(res)

        return res
    
    def winner(self):
        correct = []

        for i in range(len(self.__guesses)):
            if self.__guesses[i] == self.__prev_game[i]: correct.append(True)

        print(sum(correct))

        return sum(correct) > (len(self.__guesses) // 2)

    def __str__(self):
        return " ".join(self.__prev_game)

t = Coinflips()
try:
    t.play("arms")
except Warning:
    print("invalid choice")
# Your play results may be different from this example due to randomness
print(t.play("heads"))
print(t.play("tails"))
print(t.play("heads"))
print(t)
print(t.winner())