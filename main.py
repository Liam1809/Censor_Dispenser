# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

punctuation = [",", "!", "?", ".", "%", "/", "(", ")"]

def censor_one(email, censored_sen):
  length = censored_sen
  censor_len = ""
  for element in length:
    censor_len += "*"
  email = email.replace(censored_sen, censor_len)
  return email

# print(censor_one(email_one, "learning algorithms"))

proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself", "Helena"]

def censor_two(email, censored_list):
  # sort list based on its length in descending order
  for i in range(len(censored_list)):
    for j in range(i+1, len(censored_list)):
      if len(censored_list[i]) < len(censored_list[j]):
        temp = censored_list[i]
        censored_list[i] = censored_list[j]
        censored_list[j] = temp
  count = 0
  #take the largest element in length
  length = censored_list[0]
  censor_len = ""
  for element in length:
      censor_len += "*"
  while(count < len(censored_list)):
    email = email.replace(censored_list[i], censor_len)
    count += 1
  return email

# print(censor_two(email_two, proprietary_terms))

negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressed", "concerning", "horrible", "horribly", "questionable"]
print(email_three)

def censor_three(email, censored_list):
     text = email.split()
     return text
     for word in text:
         for element in word:
             print(element)

censor_three(email_three, negative_words)