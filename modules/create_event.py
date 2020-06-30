from ics import Calendar, Event
from text_processor import text_pipeline


#
def create_ics_file(duration_directive_tuple):
    c = Calendar()
    e = Event()
    directive = duration_directive_tuple[0]
    duration = duration_directive_tuple[1]

    # Add Error Handling stuff
    medication = str(input("What would you like to call this medicine: "))
    while True:
        try:
            quantity = int(input("How many pills are in the bottle: "))
        except ValueError:
            print("Please Enter a whole number!!!")
            continue
        else:
            break

    if "HOURS" in duration:
        # Look for and extract the number range of hours
        hours = [hour for hour in duration if hour[0].isnumeric()]

        # Gets rid of any extra numbers left from the preprocessing step
        if len(hours) > 1:
            hours = hours[-1]
    if ("DAY" in duration) | ("EVERYDAY" in duration) | ("DAILY" in duration):
        frequency = {"ONCE": 1, "ONE": 1, "TWICE": 2, "THRICE": 3, "THREE": 3,  "FOUR": 4}

    # If the medication is to be taken daily
    # if duration.__contains__("EVERYDAY"):
    #     # duration[0] should be the number of pills taken each time since duration = "# EVERYDAY"
    #     # Use days_to_schedule to figure out how many events to add
    #     # 30 pills @ TWICE A DAY = 15 dosages/15 events
    #     days_to_schedule = quantity / int(duration[0])
    #     # What time would you like to start taking the medication
    #     print("Enter time 8AM as 8:00 and 8PM as 20:00 Exactly")
    #     time_to_take = input("What time would you like to start taking the medication: ")
    #
    #     e.name = directive + " of " + medication
    #     e.begin = '2020-06-26 00:00:00'  # This will be the current day as well as the medication taking time
    #
    #     while days_to_schedule > 1:
    #         c.events.add(e)
    #         # Figure out a way to add days to e.begin !!!
    #         days_to_schedule -= 1
    # # If the medication is to be taken hourly
    #
    # c.events
    # # [<Event 'My cool event' begin:2014-01-01 00:00:00 end:2014-01-01 00:00:01>]
    # # End the event based off of how many pills are in the bottles. QTY
    # # Ask for the users input on this
    # with open('prescription.ics', 'w') as my_file:
    #     my_file.writelines(c)
    # # and it's done !
    #


def main():
    create_ics_file(text_pipeline())


if __name__ == "__main__":
    main()
