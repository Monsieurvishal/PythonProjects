
# @author Neel Patel
# @file PasswordGenerator.py

import random
import string
    
invalidcharacters= set(string.punctuation)

size = int(input("Please enter the length for the password (greater than 4:) "))
password_chars = string.ascii_letters.upper()+string.ascii_letters.lower()+ string.digits + string.punctuation
generated_pass = ""
count=1
while count==1:
    generated_pass=''
    for i in range(size):
        generated_pass += random.choice(password_chars)
        
        
    if (any(x.isupper() for x in generated_pass)):
        if (any(x.islower() for x in generated_pass)):
            if (any(x.isdigit() for x in generated_pass)):
                if any(char in invalidcharacters for char in generated_pass):
                    count=0
    
    
print("Random password: " + generated_pass)   
