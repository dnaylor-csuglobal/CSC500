# Here we define separate dictionaries to contain the data.
# If were to do this for real, then we would consolidate
# the values into an object and maintain only one dictionary.
course_rooms = {'CSC101': '3004', 'CSC102': '4501', 'CSC103': '6755',
                'NET110': '1244', 'COM241': '1411'}

course_instructors = {'CSC101': 'Haynes', 'CSC102': 'Alvarado', 'CSC103': 'Rich',
                      'NET110': 'Burke', 'COM241': 'Lee'}

course_meetings = {'CSC101': '8:00 a.m', 'CSC102': '9:00 a.m', 'CSC103': '10:00 a.m',
                   'NET110': '11:00 a.m', 'COM241': '1:00 p.m'}

while True:
    print('Please enter a course number, or type quit to exit')
    course = input()
    if course == 'quit':
        print("Goodbye!")
        break

    # check that the number exists. We just need to check one of the dictionaries
    if course not in course_rooms:
        print("Unknown course number, please try again.")
        continue

    room = course_rooms[course]
    instructor = course_instructors[course]
    meeting = course_meetings[course]
    print(f"Course number {course}: Room {room}, taught by Dr. {instructor} at {meeting}")
    print('')
