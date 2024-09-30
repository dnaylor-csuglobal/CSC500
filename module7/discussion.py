import pandas as pd

course_rooms = {'CSC101': '3004', 'CSC102': '4501', 'CSC103': '6755',
                'NET110': '1244', 'COM241': '1411'}

course_instructors = {'CSC101': 'Haynes', 'CSC102': 'Alvarado', 'CSC103': 'Rich',
                      'NET110': 'Burke', 'COM241': 'Lee'}

course_meetings = {'CSC101': '8:00 a.m', 'CSC102': '9:00 a.m', 'CSC103': '10:00 a.m',
                   'NET110': '11:00 a.m', 'COM241': '1:00 p.m'}


def consolidate_dictionaries(course_rooms, course_instructors, course_meetings):
    result = {}  # define the result
    for course_number in course_rooms:
        room = course_rooms[course_number]
        instructor = course_instructors[course_number]
        meeting = course_meetings[course_number]
        result[course_number] = {
            'room': room,
            'instructor': instructor,
            'meeting': meeting
        }
    return result


consolidated = consolidate_dictionaries(course_rooms, course_instructors, course_meetings)
print(consolidated)

data = {'room': course_rooms, 'instructor': course_instructors, 'meeting': course_meetings}
consolidated = pd.DataFrame.from_dict(data, orient='columns').to_dict(orient='index')
print(consolidated)


