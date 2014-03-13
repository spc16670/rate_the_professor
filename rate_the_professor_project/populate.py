import os
import random
from datetime import datetime

#TODO This simple population script will associate one professor with one course. The script needs to be improved so
# that more data is available along with the pictures



def populate():

#Adding 6 universities for the database
    university_gla = add_university('University of Glasgow', 'http://www.glasgow.ac.uk')
    university_edi = add_university('University of Edinburgh', 'http://www.ed.ac.uk/')
    university_aber = add_university('University of Aberdeen', 'www.abdn.ac.uk/')
    university_dun = add_university('University of Dundee', 'http://www.dundee.ac.uk/')

#Adding all the data for the University of Glasgow

    gla_department_comp= add_department('School of Computing Science', university_gla)
    gla_department_math = add_department('School of Mathematics and Statistics', university_gla)

    course_internet_technology = add_course('Internet Technology', university_gla, gla_department_comp, datetime.now())
    course_databases = add_course('Information Systems and Databases', university_gla, gla_department_comp, datetime.now())
    course_programming = add_course('Programming', university_gla, gla_department_comp, datetime.now())
    course_se = add_course('Software Engineering', university_gla, gla_department_comp, datetime.now())
    course_ap = add_course('Advanced Programming', university_gla, gla_department_comp, datetime.now())
    course_re = add_course('Requirements Engineering', university_gla, gla_department_comp, datetime.now())
    course_ads = add_course('Algorithms and Data Structures', university_gla, gla_department_comp, datetime.now())
    course_cs = add_course('Cyber Security', university_gla, gla_department_comp, datetime.now())
    
    course_tlac = add_course('Topics in Linear Algebra and Calculus', university_gla, gla_department_math, datetime.now())
    course_mrdb = add_course('Mechanics of Rigid and Deformable Bodies', university_gla, gla_department_math, datetime.now())
    course_mm = add_course('Mathematical methods', university_gla, gla_department_math, datetime.now())
    course_aa = add_course('Abstract Algebra', university_gla, gla_department_math, datetime.now())
    course_mc = add_course('Multivariable Calculus', university_gla, gla_department_math, datetime.now())

    #Adding prrofessors from the computing science department
    professor_leif = add_professor('Dr.', 'Leif', 'Azzopardi','l_azzopardi.jpg','www.dcs.gla.ac.uk/~leif/', university_gla)
    professor_ron = add_professor('Dr.', 'Ron', 'Poet', 'r_poet.jpg', 'http://www.dcs.gla.ac.uk/~ron/', university_gla)
    professor_david = add_professor('Dr.', 'David', 'Manlove','d_manlove.jpg', 'http://www.dcs.gla.ac.uk/~davidm/', university_gla)
    professor_alessandro = add_professor('Dr.', 'Alessandro', 'Vinciarelli','a_vinciarelli.jpg', 'http://www.dcs.gla.ac.uk/vincia/', university_gla)
    professor_julie = add_professor('Dr.', 'Julie', 'Williamson','j_williamson.jpg', 'http://www.juliericowilliamson.com/', university_gla)
    professor_simon = add_professor('Dr.', 'Simon', 'Gay', 's_gay.jpg', 'http://www.dcs.gla.ac.uk/~simon/', university_gla)
    professor_inah = add_professor('Dr.', 'Inah', 'Omoronyia','i_omoronyia.gif', 'http://www.dcs.gla.ac.uk/~inah/', university_gla)
    professor_davidw = add_professor('Dr.', 'David', 'Watt', 'd_watt.jpg', 'http://www.dcs.gla.ac.uk/~daw/', university_gla)

    #Adding professors from the mathematics department
    professor_tara = add_professor('Dr.', 'Tara', 'Brendle', 't_brendle.jpg', 'www.maths.gla.ac.uk/~tbrendle/', university_gla)
    professor_andrewbaggaley = add_professor('Dr.', 'Andrew', 'Baggaley', '', 'http://www.gla.ac.uk/schools/mathematicsstatistics/staff/andrewbaggaley/', university_gla)
    professor_davidbourne = add_professor('Dr.', 'David', 'Bourne', 'd_bourne.jpg', 'http://www.maths.gla.ac.uk/~dbourne/', university_gla)
    professor_christina = add_professor('Dr.', 'Christina', 'Cobbold', 'c_cobbold.jpg', 'http://www.maths.gla.ac.uk/~cc/', university_gla)

    #Sample ratings
    rating_leif = add_rating(professor_leif, get_random(),get_random(),get_random(),get_random(),get_random(),get_random(), 'Comedian!')
    rating_ron = add_rating(professor_ron, get_random(),get_random(),get_random(),get_random(),get_random(),get_random(), 'Creepy!')
    rating_ron2 = add_rating(professor_ron, get_random(),get_random(),get_random(),get_random(),get_random(),get_random(),'Boring')
    rating_ron3 = add_rating(professor_ron, get_random(),get_random(),get_random(),get_random(),get_random(),get_random(), 'I want to go to sleep')
    rating_david = add_rating(professor_david, get_random(),get_random(),get_random(),get_random(),get_random(),get_random(),'Ordnung must sein!')
    rating_david2 = add_rating(professor_david, get_random(),get_random(),get_random(),get_random(),get_random(),get_random(),'Pedantic')
    rating_alessndro = add_rating(professor_alessandro, get_random(),get_random(),get_random(),get_random(),get_random(),get_random(), 'Makes you feel the power!')
    rating_julie = add_rating(professor_julie, get_random(),get_random(),get_random(),get_random(),get_random(),get_random(),'Ok')
    rating_julie2 = add_rating(professor_julie, get_random(),get_random(),get_random(),get_random(),get_random(),get_random(),'Ok')
    rating_simon = add_rating(professor_simon, get_random(),get_random(),get_random(),get_random(),get_random(),get_random(),'Bad notes')
    rating_inah = add_rating(professor_inah, get_random(),get_random(),get_random(),get_random(),get_random(),get_random(),'Confusing')
    rating_inah2 = add_rating(professor_inah, get_random(),get_random(),get_random(),get_random(),get_random(),get_random(),'I dont know what to write')
    rating_davidw = add_rating(professor_davidw, get_random(),get_random(),get_random(),get_random(),get_random(),get_random(),'Everything fine')
    
    # Update courses taught by a professor
    professor_leif.courses_taught.add(course_internet_technology)
    professor_ron.courses_taught.add(course_databases)
    professor_ron.courses_taught.add(course_cs)
    professor_david.courses_taught.add(course_programming)
    professor_alessandro.courses_taught.add(course_programming)
    professor_julie.courses_taught.add(course_se)
    professor_simon.courses_taught.add(course_ap)
    professor_inah.courses_taught.add(course_re)
    professor_davidw.courses_taught.add(course_ads)
    
    #Mathematics dep
    professor_davidbourne.courses_taught.add(course_tlac)
    professor_davidbourne.courses_taught.add(course_mrdb)
    professor_andrewbaggaley.courses_taught.add(course_mm)
    professor_tara.courses_taught.add(course_aa)
    professor_christina.courses_taught.add(course_mc)

#Adding all the data for the University of Edinburgh

    edi_department_info = add_department('School of Informatics', university_edi)
    edi_department_art = add_department('College of Art', university_edi)

    course_robotics = add_course('Robotics: Science and Systems', university_edi, edi_department_info, datetime.now())
    course_graphic = add_course('Graphic Design', university_edi, edi_department_art, datetime.now())

    professor_liz = add_professor('Ms.', 'Liz', 'Adamson','l_adamson.jpg','http://www.eca.ed.ac.uk/school-of-art/liz-adamson', university_edi)
    professor_sub = add_professor('Mr.', 'Subramanian ', 'Ramamoorthy', 's_ramamoorthy.jpg', 'http://homepages.inf.ed.ac.uk/sramamoo/index.html', university_edi)

    rating_liz = add_rating(professor_liz, get_random(),get_random(),get_random(),get_random(),get_random(),get_random(), 'That woman changed my life and showed me what true graphic design was all about. '                                                                                                                        'I could have never become a master adobe jedi without her.')
    rating_liz = add_rating(professor_liz, get_random(),get_random(),get_random(),get_random(),get_random(),get_random(), 'Meh, it was ok. She has weird hair and it was really distracting.')
    rating_sub = add_rating(professor_sub, get_random(),get_random(),get_random(),get_random(),get_random(),get_random(), 'I loved the guy. He was explaining really well and we built a simple robot during the course. Awesome!')

    professor_liz.courses_taught.add(course_graphic)
    professor_sub.courses_taught.add(course_robotics)

#Adding all the data for the University of Aberdeen

    aber_department_biz = add_department('Bussiness School', university_aber)
    aber_department_bio = add_department('The School of Biological Sciences', university_aber)

    course_biz_dev = add_course('Business Development', university_aber, aber_department_biz, datetime.now())
    course_mar_bio = add_course('Marine Biology', university_aber, aber_department_bio, datetime.now())

    professor_ian = add_professor('Dr.', 'Ian', 'Heywood', 'i_heywood.jpg','http://www.abdn.ac.uk/business/disciplines/management/profiles/i.heywood', university_aber)
    professor_cath = add_professor('Dr.', 'Catherine', 'Hambly', 'c_hambly.jpg', 'http://www.abdn.ac.uk/sbs/people/profiles/c.hambly', university_aber)

    rating_ian = add_rating(professor_ian, get_random(),get_random(),get_random(),get_random(),get_random(),get_random(),'Such a great guy. I loved the course project and how easy it was to understand while he was talking about business theory.')
    rating_ian = add_rating(professor_ian, get_random(),get_random(),get_random(),get_random(),get_random(),get_random(),'He was really funny without being goofy. I liked that')
    rating_cath = add_rating(professor_cath, get_random(),get_random(),get_random(),get_random(),get_random(),get_random(),'She was such a sweetheart. I just loved her lectures so much')
    rating_cath = add_rating(professor_cath, get_random(),get_random(),get_random(),get_random(),get_random(),get_random(), 'She was really nice but the materials was incredibly dull. I couldn`t help but not go to her lectures')

    professor_ian.courses_taught.add(course_biz_dev)
    professor_cath.courses_taught.add(course_mar_bio)

#Add all the date for the University of Dundee

    dun_department_human = add_department('School of Humanities', university_dun)
    dun_department_dent = add_department('School of Dentistry', university_dun)

    course_film = add_course('Film Studies', university_dun, dun_department_human, datetime.now())
    course_ortho = add_course ('Orthodontics', university_dun, dun_department_dent, datetime.now())

    professor_jen = add_professor('Ms.', 'Jennifer', 'Barnes', 'j_barnes.jpg', 'http://www.dundee.ac.uk/humanities/staff/profile/jennifer-barnes', university_dun)
    professor_fel = add_professor('Dr.', 'Felicity', 'Borrie', 'f_borrie.jpg', 'http://dentistry.dundee.ac.uk/staff-member/dr-felicity-r-p-borrie', university_dun)

    rating_jen = add_rating(professor_jen, get_random(),get_random(),get_random(),get_random(),get_random(),get_random(), 'Her class was amazing. She was so well-spoken and her insights about the Godfather were so deep I had to close myself into my room for 3 days with nothing but candles and incense to really fathom their profoundness.')
    rating_fel = add_rating(professor_fel, get_random(),get_random(),get_random(),get_random(),get_random(),get_random(), 'She was really professional and explained the material really well. God bless her.')

    professor_jen.courses_taught.add(course_film)
    professor_fel.courses_taught.add(course_ortho)


    # Print out what we have added to the user.
    for u in University.objects.all():
        for p in Professor.objects.filter(university=u):
            print "- {0} - {1}".format(str(u), str(p))


# ------------------------------------- FUNCTIONS ------------------------------------------------
def add_university(name, url):
    u = University.objects.get_or_create(uni_name=name, website_url=url)[0]
    return u


def add_professor(title, first_name, last_name, picture, website_url, university):
    p = Professor.objects.get_or_create(title=title, first_name=first_name, last_name=last_name, picture=picture,
                                        website_url=website_url, university=university)[0]

    return p


def add_rating(professor,communication, knowledge, approachability, enthusiasm, clarity, awesomeness, comment):
    r = Rating.objects.get_or_create(professor=professor, communication=communication, knowledge=knowledge,
                                     approachability=approachability, enthusiasm=enthusiasm, clarity=clarity,
                                     awesomeness=awesomeness, comment=comment)[0]
    return r


def add_department(name, university):
    d = Department.objects.get_or_create(department_name=name, university=university)[0]
    return d


def add_course(course_name, university, department, start_date):
    c = Course.objects.get_or_create(course_name=course_name, university=university, department=department,
                                     start_date=start_date)[0]
    return c

# A function which returns a random number between 1 and 5 in order to give values for the ratings
def get_random():
    return random.randrange(1,6)

# a new comment
# Start execution here!
if __name__ == '__main__':
    print "Starting RateTheProfessor population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rate_the_professor_project.settings')
    from rate_the_professor.models import Rating, University, Course, Professor, Department
    populate()
