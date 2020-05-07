# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

# list of punctuation
punctuation = [",", "!", "?", ".", "%", "/", "(", ")"]

def censor_one(email, censored_sen):
  # censor
  censor_len = ""
  for element in censored_sen:
      if element == " ":
          censor_len += " "
      else:
          censor_len += "*"
  email = email.replace(censored_sen, censor_len)
  return email

# print(censor_one(email_one, "learning algorithm"))

# list of proprietary_terms
proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself", "Helena"]

def censor_two(email, censored_list):
   # sort list based on its length in descending order
  for i in range(len(censored_list)):
     for j in range(i+1, len(censored_list)):
       if len(censored_list[i]) < len(censored_list[j]):
         temp = censored_list[i]
         censored_list[i] = censored_list[j]
         censored_list[j] = temp
  # censor
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

# list of negative words
negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressing", "concerning", "horrible", "Horribly", "questionable"]

def censor_three(email, censored_list, negative_words):
    text = []
    # append to text
    email = censor_two(email, censored_list)
    for words in email.split():
        text.append(words)
    # censor
    count = 0
    for i in range(len(text)):
        for element in negative_words:
          if element in text[i]:
             count += 1
             if count > 2:
                word_clean = text[i]
                for sign in punctuation:
                    word_clean = word_clean.strip(sign)
                censor_len  = ""
                for element in word_clean:
                    censor_len += "*"
                text[i] = text[i].replace(word_clean, censor_len)
    # organise text
    count1 = 0
    for i in range(len(text)):
            if "," in text[i] and i < 3:
                text[i] += "\n\n"
            if "," in text[i] and i == len(text) -1 - 3:
                text[i] += "\n\n"
            if "." in text[i]:
                count1 += 1
                if count1 == 3:
                    text[i] += "\n\n"
                elif count1 == 6:
                    text[i] += "\n\n"
                elif count1 == 8:
                    text[i] += "\n\n"
                elif count1 == 10:
                    text[i] += "\n\n"
    return " ".join(text)

# print(censor_three(email_three, proprietary_terms, negative_words))
    
def censor_four(email,censored_all):
    text = []
    # append to text
    for words in email.split():
        text.append(words)
    # censor
    for i in range(len(text)):
        for element in censored_all:
            if element in text[i]:
                # censor the target word
                word_target = text[i]
                censor_len = ""
                for element in word_target:
                    censor_len += "*"
                for sign in punctuation:
                    word_target = word_target.strip(sign)
                text[i] = text[i].replace(word_target, censor_len)
                # censor the target word before
                word_target_before = text[i - 1]
                censor_len_before = ""
                for element in word_target_before:
                    censor_len_before += "*"
                for sign in punctuation:
                    word_target_before = word_target_before.strip(sign)
                text[i - 1] = text[i - 1].replace(word_target_before, censor_len_before)
            # censor the target word after
                word_target_after = text[i + 1]
                censor_len_after = ""
                for element in word_target_after:
                    censor_len_after += "*"
                for sign in punctuation:
                    word_target_after = word_target_after.strip(sign)
                text[i + 1] = text[i +1].replace(word_target_after, censor_len_after)
    # organise text
    count = 0
    for i in range(len(text)):
            if "!" in text[i] and count == 0:
                text[i] += "\n\n"
            if "." in text[i]:
                count += 1
                if count == 5:
                    text[i] += "\n\n"
                elif count == 7:
                    text[i] += "\n\n"
                elif count == 10:
                    text[i] += "\n\n"
                elif count == 15:
                    text[i] += "\n\n"
    return " ".join(text)
    
# print(censor_four(email_four,(proprietary_terms + negative_words)))                   
            

