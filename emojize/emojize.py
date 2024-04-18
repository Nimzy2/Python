import emoji

user_input = input("Enter your emoji: ") 

emojize = emoji.emojize(user_input, language='alias')

print("output:",emojize)