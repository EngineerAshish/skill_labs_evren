class User:
    student=1
    working_professional=2
    MSME_user=3
    active =1
    inactive = 0
    otp_validity = 300
    
    class Student:
        intern =1
        other_serices = 2
    
    class working_experience:
        mentor_an_intern =1
        other_professional_services =2
    
    class MSME:
        map_an_intern = 1
        other_services= 2

class abb:
    class mentornship:
        accepted=1
        pending=2
        rejected=3
