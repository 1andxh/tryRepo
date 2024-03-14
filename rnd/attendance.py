import datetime as dt 



today = dt.date.today()
print("\nAttendance Sheet\n".ljust(60,'='))
print("\nEnter your information below\n".ljust(60, '='))
print(f"\nDate : {today}")
#  an attendance system to keep records, takes name, id number sign in/out times and date

def name(attendance):
    student_name = input(str("Enter name: "))
    attendance[student_name] = False
    if len(student_name) > 4:
        attendance = []
    print(f"{student_name}\n ")
    # if student_name == " ":
    #     print("Name cannot be left blank")
    # else:
    #     print(student_name.upper)
    # return student_name

    # print(student_name.upper)

def id(attendance):
    student_id = input("Enter ID: \n")
    attendance[student_id] = False
    if len(student_id) in range(9):
        print(f"Student Id: {student_id} ")
    else:
        print("ID cannot be more than 8 numbers")

def main():
    attendance = {}

    while True:
        name(attendance)
        id(attendance)
    
    if attendance:
        # print()
        print("Attendance successfully recorded for today!")
      

       
       

if __name__ =="__main__":
    main()
     
