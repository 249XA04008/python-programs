Word=str(input("Enter a string: "))
count=0
for i in Word:
    if i in "aeiouAEIOU":
        count+=1
print(f"The number of vowels in the string is: {count}")