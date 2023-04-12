# The Authors are Bethany Berlage, Olivia Busk, and Rosemary Hoffman

name_dict = {
    "Busk": "Olivia",
    "Berlage": "Bethany",
    "Hoffman": "Rosemary",
    "Paradisio": "Vinnie",
    "Nixon": "Emily",
    "Anspach": "Grace",
    "Bong": "Saerin",
    "Eafon": "Breanna",
    "O'Roark": "Katherine",
    "Stephenson": "Sarah",
    "Dockery": "Krista",
    "Faye Gallaway": "Gabrielle"
}

freq_dict = {}
for first_name in name_dict.values():
    if first_name in freq_dict:
        freq_dict[first_name] += 1
    else:
        freq_dict[first_name] = 1

print(freq_dict)

