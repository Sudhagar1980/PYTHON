class AllinOne():
    def Subfields():
        a="Sub-feild in AI are :"
        course=["Machine Learing","Neural Networks","Vission","Robetics","Speech Processing","Natuarl Language"]
        print(a)
        for i in course:
            print(i)
            result=i
       
    def OddEven():
        num=int(input("Enter a number :"))
        if num%2==0:
            print("{0} is Even number".format(num))
        else:
            print("{0} is Odd number".format(num))

    def Eligible():
        gender=str(input("Enter the Gender :"))
        age=int(input("Enter the Age :"))
        if gender=="Female":
            if age>18:
                print("ELIGIBLE")
            else:
                print("NOT ELIGIBLE")
        if gender=="Male":
            if age>21:
                print("ELIGIBLE")
            else:
                print("NOT ELIGIBLE") 
 
    def percentage():
        Subject1=int(input("Subject1 :" ))
        Subject2=int(input("Subject2 :" ))
        Subject3=int(input("Subject3 :" ))
        Subject4=int(input("Subject4 :" ))
        Subject5=int(input("Subject5 :" ))
        total=Subject1+Subject2+Subject3+Subject4+Subject5
        avg=float(total/5)
        result=avg
        print("Total  :",total)
        print("Percentage    :",float(avg))

    def triangle():
        Height=int(input("Height :"))
        Breadth=int(input("Breath :"))
        area=(Height*Breadth)/2
        msg=area
        print("Area of Triangle  :",area)
        Height1=int(input("Height1 :"))
        Height2=int(input("Height2 :"))
        Breadth=int(input("Breath :"))
        perimeter=Height1+Height2+Breadth
        msg=perimeter
        print("Perimeter of Triangle  :",msg)


