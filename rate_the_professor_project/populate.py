import os

#TODO This simple population script will associate one professor with one course. The script needs to be improved so
# that more data is available along with the pictures


def populate():
    university = add_university('University of Glasgow', 'http://www.glasgow.ac.uk')

    department = add_department('School of Computing Science', university)
    department_math = add_department('School of Mathematics and Statistics', university)

    from datetime import datetime
    course_internet_technology = add_course('Internet Technology', university, department, datetime.now())
    course_databases = add_course('Information Systems and Databases', university, department, datetime.now())
    course_programming = add_course('Programming', university, department, datetime.now())
    course_se = add_course('Software Engeneering', university, department, datetime.now())
    course_ap = add_course('Advanced Programming', university, department, datetime.now())
    course_re = add_course('Requirements Engineering', university, department, datetime.now())
    course_ads = add_course('Algorithms and Data Structures', university, department, datetime.now())
    
    course_tlac = add_course('Topics in Linear Algebra and Calculus', university, department_math, datetime.now())
    course_mrdb = add_course('Mechanics of Rigid and Deformable Bodies', university, department_math, datetime.now())
    course_mm = add_course('Mathematical methods', university, department_math, datetime.now())
    course_aa = add_course('Abstract Algebra', university, department_math, datetime.now())
    course_mc = add_course('Multivariable Calculus', university, department_math, datetime.now())
    
    professor_leif = add_professor('Mr', 'Leif', 'Azzopardi', university)
    professor_ron = add_professor('Mr', 'Ron', 'Poet', university)
    professor_david = add_professor('Mr', 'David', 'Manlove', university)
    professor_alessandro = add_professor('Mr', 'Alessandro', 'Vinciarelli', university)
    professor_julie = add_professor('Dr.', 'Julie', 'Williamson', university)
    professor_simon = add_professor('Dr.', 'Simon', 'Gay', university)
    professor_inah = add_professor('Dr.', 'Inah', 'Omoronyia', university)
    professor_davitw = add_professor('Dr.', 'David', 'Watt', university)
    
    professor_tara = add_professor('Dr.', 'Tara', 'Brendle', university)
    professor_andrewbaggaley = add_professor('Dr.', 'Andrew', 'Baggaley', university)
    professor_davidbourne = add_professor('Dr.', 'David', 'Bourne', university)
    professor_christina = add_professor('Dr.', 'Christina', 'Cobbold', university)
    
    rating_leif = add_rating(professor_leif, 'Comedian!')
    rating_ron = add_rating(professor_ron, 'Creepy!')
    rating_ron2 = add_rating(professor_ron, 'Boring')
    rating_ron3 = add_rating(professor_ron, 'I want to go to sleep')
    rating_david = add_rating(professor_david, 'Ordnung must sein!')
    rating_david2 = add_rating(professor_david, 'Pedantic')
    rating_alessndro = add_rating(professor_alessandro, 'Makes you feel the power!')
    rating_julie = add_rating(professor_julie, 'Ok')
    rating_julie2 = add_rating(professor_julie, 'Ok')
    rating_simon = add_rating(professor_simon, 'Bad notes')
    rating_inah = add_rating(professor_inah, 'Confusing')
    rating_inah2 = add_rating(professor_inah, 'I dont know what to write')
    rating_davidw = add_rating(professor_davidw, 'Everything fine')
    
    # Update courses taught by a professor
    professor_leif.fk_courses_taught.add(course_internet_technology)
    professor_ron.fk_courses_taught.add(course_databases)
    professor_david.fk_courses_taught.add(course_programming)
    professor_alessandro.fk_courses_taught.add(course_programming)
    professor_julie.fk_courses_taught.add(course_se)
    professor_simon.fk_courses_taught.add(course_ap)
    professor_inah.fk_courses_taught.add(course_re)
    professor_davidw.fk_courses_taught.add(course_ads)
    
    #Mathematics dep
    professor_davidbourne.fk_courses_taught.add(course_tlac)
    professor_davidbourne.fk_courses_taught.add(course_mrdb)
    professor_andrewbaggaley.fk_courses_taught.add(course_mm)
    professor_tarabrendle.fk_courses_taught.add(course_aa) 
    professor_christinacobbold.fk_courses_taught.add(course_mc) 
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
# a new comment
# Start execution here!
if __name__ == '__main__':
    print "Starting RateTheProfessor population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rate_the_professor_project.settings')
    from rate_the_professor.models import Rating, University, Course, Professor, Department
    populate()
