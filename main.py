import app

dictionary = "https://www.mit.edu/~ecprice/wordlist.10000"
max_tries = 3

if __name__ == "__main__":
    engine = app.App(dictionary, max_tries)
    engine.run()
