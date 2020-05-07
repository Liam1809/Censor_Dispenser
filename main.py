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

