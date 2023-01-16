# pomenohenn
Think you got a good voacbulary? Try pomenohenn!

Apparently, we can ![very easily read words when only the first and last letter are in place](https://www.mrc-cbu.cam.ac.uk/people/matt.davis/cmabridge/).

Well, unlike the original Cambridge research, this activity is contextless. You're not able to infer a word based on it's surrounding words, akin to the handicap an NLP engine gets when you don't train it with sentential connotations.

If you're up to it, then simply run the python file.

`git clone https://github.com/pikulet/pomenohenn`

`pip3 install -r requirements.txt`

`python3 main.py`

I find it a pretty great way to spend a minute or two, and you can let me know your score :)

![image](https://user-images.githubusercontent.com/24848927/139468509-0f16c68e-6049-4285-b198-26855ced382d.png)

# Improvements

Some quick improvements i can think of
- Include a difficulty level, corresponding to the minimum word length you'll get
- Include more words! I'm current using the word list from Eric Price @ MIT, and it contains mostly common / short words. A lot of the words got filtered away because I wanted to keep the words relatively challenging
- Configuring the maximum number of retries
- Timer! A quickway to challenge yourself in one minute. Would be a great way to compete with friends too

