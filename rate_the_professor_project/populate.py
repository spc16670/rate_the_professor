import os

#TODO This simple population script will associate one professor with one course. The script needs to be improved so
# that more data is available along with the pictures


def populate():
    university = add_university('University of Glasgow', 'http://www.glasgow.ac.uk')

    department = add_department('School of Computing Science', university)

    from datetime import datetime
    course_internet_technology = add_course('Internet Technology', university, department, datetime.now())
    course_databases = add_course('Information Systems and Databases', university, department, datetime.now())
    course_programming = add_course('Programming', university, department, datetime.now())

    professor_leif = add_professor('Mr', 'Leif', 'Azzopardi', university)
    professor_ron = add_professor('Mr', 'Ron', 'Poet', university)
    professor_david = add_professor('Mr', 'David', 'Manlove', university)
    professor_alessandro = add_professor('Mr', 'Alessandro', 'Vinciarelli', university)

    rating_leif = add_rating(professor_leif, 'Comedian!')
    rating_ron = add_rating(professor_ron, 'Creepy!')
    rating_david = add_rating(professor_david, 'Ordnung must sein!')
    rating_alessndro = add_rating(professor_alessandro, 'Makes you feel the power!')

    # Update courses taught by a professor
    professor_leif.fk_courses_taught.add(course_internet_technology)
    professor_ron.fk_courses_taught.add(course_databases)
    professor_david.fk_courses_taught.add(course_programming)
    professor_alessandro.fk_courses_taught.add(course_programming)


    # Print out what we have added to the user.
    for u in University.objects.all():
        for p in Professor.objects.filter(fk_university=u):
            print "- {0} - {1}".format(str(u), str(p))


# ------------------------------------- FUNCTIONS ------------------------------------------------
def add_university(name, url):
    u = University.objects.get_or_create(uni_name=name, website_url=url)[0]
    return u


def add_professor(title, first_name, last_name, university):
    p = Professor.objects.get_or_create(title=title, first_name=first_name, last_name=last_name,
                                        fk_university=university)[0]
    return p


def add_rating(professor, comment):
    r = Rating.objects.get_or_create(fk_professor=professor, comment=comment)[0]
    return r


def add_department(name, university):
    d = Department.objects.get_or_create(department_name=name, fk_university=university)[0]
    return d


def add_course(course_name, university, department, start_date):
    c = Course.objects.get_or_create(course_name=course_name, fk_university=university, fk_department=department,
                                     start_date=start_date)[0]
    return c

# Start execution here!
if __name__ == '__main__':
    print "Starting RateTheProfessor population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rate_the_professor_project.settings')
    from rate_the_professor.models import Rating, University, Course, Professor, Department
    populate()