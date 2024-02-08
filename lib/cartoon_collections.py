def roll_call_dwarves(dwarves):
    for i, dwarf in enumerate(dwarves, 1):
        print(f"{i}. {dwarf}")

def summon_captain_planet(planeteer_calls):
    return [call.capitalize() + '!' for call in planeteer_calls]

def long_planeteer_calls(calls):
    for call in calls:
        if len(call) > 4:
            return True
    return False

def find_the_cheese(snacks):
    cheeses = ["cheddar", "gouda", "camembert"]
    for item in snacks:
        if item in cheeses:
            return item
    return None

