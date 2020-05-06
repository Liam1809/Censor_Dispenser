# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

punctuation = [",", "!", "?", ".", "%", "/", "(", ")"]

def censor_one(email, censored_sen):
  censor_len = ""
  for element in censored_sen:
      if element == " ":
          censor_len += " "
      else:
          censor_len += "*"
  email = email.replace(censored_sen, censor_len)
  return email

# print(censor_one(email_one, "learning algorithm"))

proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself", "Helena"]

def censor_two(email, censored_list):
      
  for words in censored_list:
          censor_len = ""
          for letter in words:
              if letter == " ":
                  censor_len += " "
              else:
                  censor_len += "*" 
          email = email.replace(words, censor_len)
  return email

# print(censor_two(email_two, proprietary_terms))

negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressing", "concerning", "horrible", "horribly", "questionable"]

def censor_three(email, censored_list, negative_words):
    text = []
    email = censor_two(email, censored_list)
    for words in email.split():
        text.append(words)
    for i in range(len(text)):
        count = 0
        if text[i] in negative_words:
                word_clean = text[i]
                censor_len  = ""
                for element in word_clean:
                    censor_len += "*"
                for sign in punctuation:
                    word_clean = word_clean.strip(sign)
                text[i] = text[i].replace(word_clean, censor_len)
    return " ".join(text)
    
    
# print(censor_three(email_three, proprietary_terms, negative_words))
    
# def censor_four(email)