# v1
# from apps.students import get_users
# from apps.db.rating import get_middle, max_rating


# if __name__ == '__main__':
#     get_users()
#     get_middle()


#v2
from apps import students
from apps.db import rating

if __name__ == '__main__':
    students.get_users()
    rating.get_middle()
