from student import Student

class uni_student(student):

    def on_honour_roll(self):
        if(self.gpa < 4):
            return True
        else:
            return False


    def is_passed(self):
        print("is passed")