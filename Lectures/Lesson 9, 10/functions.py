def main():
    gpa=float(input("What is your GPA?"))
    age=int(input("What is your age?"))
    interview_score=int(input("What is your interview score?"))
    aptitude_score=int(input("What is your aptitude score?"))
    result=hire_manager(gpa, age, interview_score, aptitude_score)
    print(result)

def hire_manager(gpa, age, interview_score, aptitude_score):
    total_points=0
    if gpa>3.3 and age>24:
         total_points+=1
    if 6<interview_score<9:
         total_points+=1
    elif 9<=interview_score<=10:
         total_points+=2
    if aptitude_score>85:
        total_points+=1
    if total_points<=2:
        return "not hired"
    elif total_points==3:
        return "hired as a Junior Salesperson"
    else :
        return "Hired as a Manager-In-Training"
    
        
    

if __name__=="__main__":
    main()
