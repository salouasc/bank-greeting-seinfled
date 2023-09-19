word = input("Greeting: ")
if word.lower().replace(" ","").startswith("hello"):
    print("$0")
elif word.lower().startswith("h") and not word.lower()==("hello"):
    print("$20")
else:
    print("$100")