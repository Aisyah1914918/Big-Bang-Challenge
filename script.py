import json

output = []

# Iterate through numbers 1 to 100
for x in range(1, 101):
    
    if x % 3 == 0 and x % 5 == 0:
        # If divisible by both 3 and 5, display BIGBANG after that to the output list
        output.append("BIGBANG")
    
    elif x % 3 == 0:
        #If divisible by 3, display BIG after that to the output list
        output.append("BIG") 
    
    elif x % 5 == 0:
        #If divisible by 5, display BANG after that to the output list 
        output.append("BANG")
    
    else: 
        #If not divisible by 3 or 5, display the number tested as a string to the output list
        output.append(str(x))

#display the list to a JSON file 
with open('output.json', 'w') as file:
    json.dump(output, file)