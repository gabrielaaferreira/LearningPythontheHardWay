name = 'Zed A. Shaw'
age = 35
height = 74 #inches
weight = 180 #pounds
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

inches_to_centimeters = height*2.54
pounds_to_kg = weight/2.2046

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"That is {inches_to_centimeters} centimeters")
print(f"He's {weight} pounds heavy")
print(f"That is {pounds_to_kg} kilograms")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

total = age+ height + weight
print(f"If I add {age}, {height}, and {weight} I get a {total}.")

