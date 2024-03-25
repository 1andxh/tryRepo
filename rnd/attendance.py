import datetime as dt 
from time import strftime



today = dt.datetime.today()
print("\nAttendance Sheet\n".ljust(60,'='))
print("\nEnter your information below\n".ljust(60, '='))
print(f"\nDate : {today}")
#  an attendance system to keep records, takes name, id number sign in/out times and date

def name(attendance):
    student_name = input(str("Enter name: "))
    attendance[student_name] = False
    if len(student_name) > 3:
        attendance = []
    print(f"{student_name} \n")
    # for char in student_name:
    #     if student_name == " ":
    #         print("Name cannot be left blank")
    # else:
    # #     print(student_name.upper)
    #     print(student_name)

    # # print(student_name.upper)

def id(attendance):
    student_id = input("Enter ID: \n")
    attendance[student_id] = False
    if len(student_id) in range(9):
        print(f"Student Id: {student_id} \n")
    else:
        print("ID cannot be more than 8 numbers")





def clockout(attendance):
    print("press q to quit\n")
    user_choice = input()
    if user_choice == "q":
        # print(dt.timedelta.min)
        print("exiting application...")
    
        

def main():
    attendance = {}

    while True:
        name(attendance)
        id(attendance)
        print("Attendance recorded successfully")
        print(f"clocked-out at: {dt.time.strftime}")
        clockout(attendance)
        break
        
if __name__ =="__main__":
    main()
     
