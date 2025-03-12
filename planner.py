# Empty list to build directory of gamers
gamers = []

# Checks validity of gamer entries before adding them to the gamer list
def add_gamer(gamer, gamers_list):
    if gamer.get("name") and gamer.get("availability"):
        gamers_list.append(gamer)
    else:
        print("Missing name or availability data.")

# Example of a single gamers availability stored as a dictionary
kimberly = {
    "name": "Kimberly Warner",
    "availability": ["Monday", "Tuesday", "Friday"]
}

# Adding multiple sample gamers for testing
add_gamer(kimberly, gamers)
add_gamer({'name':'Thomas Nelson','availability': ["Tuesday", "Thursday", "Saturday"]}, gamers)
add_gamer({'name':'Joyce Sellers','availability': ["Monday", "Wednesday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'Michelle Reyes','availability': ["Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Stephen Adams','availability': ["Thursday", "Saturday"]}, gamers)
add_gamer({'name': 'Joanne Lynn', 'availability': ["Monday", "Thursday"]}, gamers)
add_gamer({'name':'Latasha Bryan','availability': ["Monday", "Sunday"]}, gamers)
add_gamer({'name':'Crystal Brewer','availability': ["Thursday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'James Barnes Jr.','availability': ["Tuesday", "Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Michel Trujillo','availability': ["Monday", "Tuesday", "Wednesday"]}, gamers)

# For creating blank frequency tables on demand
def build_daily_frequency_table():
    return {
        "Monday": 0,
        "Tuesday": 0,
        "Wednesday": 0,
        "Thursday": 0,
        "Friday": 0,
        "Saturday": 0,
        "Sunday": 0
    }

# Creating blank frequency table and storing to bed edited by later functions
count_availability = build_daily_frequency_table()

# Determines number of people available on each weekday and stores this in provided frequency table
def calculate_availability(gamers_list, available_frequency):
    for element in gamers_list:
        availability = element.get("availability")
        for day in availability:
            available_frequency[day] += 1

# Calculates available weekday frequency on provided test data and prints for debugging
calculate_availability(gamers, count_availability)
print(count_availability)

# Returns the date with highest frequency. If two dates are tied, returns earliest in the week.
def find_best_night(availability_table):
    highest_count = 0
    highest_count_day = ""
    for day in availability_table:
        count = availability_table[day]
        if count > highest_count:
            highest_count = count
            highest_count_day = day
    return highest_count_day

# Checks for and prints the night with the highest availability in our test data
game_night = find_best_night(count_availability)
print(game_night)

# Provides a list of individual names who are available on the highest availability weekday
def available_on_night(gamers_list, day):
    available_gamers = []
    for element in gamers_list:
        name = element.get("name")
        availability = element.get("availability")
        if day in availability:
            available_gamers.append(name)
    return available_gamers

# Generates list of test data individuals available on the test data highest availability weekday
# Prints the list of names for debugging
attending_game_night = available_on_night(gamers, game_night)
print(attending_game_night)

# Email template for notifying attendees of the planned day and game being played
form_email = "Hello {name}! Just wanted to let you know that we have planned {day_of_week} night to play {game}."

# Applies provided list of attendees to the formatting of the email templte and prints for each of them
def send_email(gamers_who_can_attend, day, game):
    for attendee in gamers_who_can_attend:
        print(form_email.format(name=attendee, day_of_week=day, game=game))

# Creates notification email for test data attendees
send_email(attending_game_night, game_night, "Abruptly Goblins!")

# Blank list to build directory of those unable to attend the highest availability frequency weekday
unable_to_attend_best_night = []

# Adds those not able to attend the highest availability frequency weekday to a list
for element in gamers:
    if not game_night in element.get("availability"):
        unable_to_attend_best_night.append(element)

# Creates new blank frequency table
second_night_availability = build_daily_frequency_table()

# Generates second preference by re-determining highest availability frequency only on those unable to attend the most frequent weekday
calculate_availability(unable_to_attend_best_night, second_night_availability)
second_night = find_best_night(second_night_availability)

# Creates second preference list and email notification from provided test data
available_second_game_night = available_on_night(gamers, second_night)
send_email(available_second_game_night, second_night, "Abruptly Goblins!")