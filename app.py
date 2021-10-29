import random
import requests


class App:
    def __init__(self, dictionary, max_tries):
        print("welcome! /s to skip and /q to quit")
        self.phenn = Pomenohenn(dictionary)
        self.max_tries = max_tries
        self.score = Score()

    def run(self):
        while not self.run_question():
            pass

    def run_question(self):
        self.score.add_total()
        qn = self.phenn.get_question()
        print("**", qn, "**:")

        for i in range(self.max_tries):
            answer = input()
            if answer == "/s":
                break
            elif answer == "/q":
                self.score.tabulate()
                return True
            elif self.phenn.check_answer(answer):
                self.score.add_correct()
                return False

        print("failed... **", self.phenn.get_answer(), "**")
        return False


class Score:
    def __init__(self):
        self.total = 0
        self.correct = 0

    def add_total(self):
        self.total += 1

    def add_correct(self):
        self.correct += 1
        if self.correct % 5 == 0:
            self.tabulate()

    def tabulate(self):
        print("total questions:", self.total, "correct:", self.correct)


class Pomenohenn:
    def __init__(self, dictionary):
        self.all_words = self.parse_dictionary(dictionary)
        self.current_word = None

    def get_question(self):
        word_len = 0
        while word_len < 6:
            self.current_word = random.choice(self.all_words)
            word_len = len(self.current_word)

        return self.phenn()

    def phenn(self):
        to_move = list(self.current_word[1:-1])
        random.shuffle(to_move)

        return self.current_word[0] + "".join(to_move) + self.current_word[-1]

    def check_answer(self, ans):
        return ans == self.current_word

    def get_answer(self):
        return self.current_word

    def parse_dictionary(self, dictionary):
        resp = requests.get(dictionary)
        return resp.content.decode().splitlines()
