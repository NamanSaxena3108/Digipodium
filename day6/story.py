story=''
while True:
    line=input('>>>')
    if not line:
        print("The End.")
        break
    story+=line+'\n'
print(f"Your Story \n{story}")