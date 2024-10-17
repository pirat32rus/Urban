calls = 0

def coind_calls():
    global calls
    calls += 1
    
def string_info(string):
    coind_calls()
    return len(string), string.upper(), string.lower()
    
def is_contains(string, list_to_search):
    coind_calls()
    return string.lower() in (item.lower() for item in list_to_search)

print(string_info('Capybara'))

print(string_info('Armageddon'))

print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN

print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches

print(calls)