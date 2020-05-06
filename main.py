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

