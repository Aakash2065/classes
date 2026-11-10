name=input("enter student name:")
n=int(input("enter number of subject:"))
total=0
for i in range(1,n+1):
      mark=float(input(f"enter mark for subject{i}:"))
      total+=mark
      percentage=total/n
      if percentage >=90:
       grade="A+"
       performance="outstandinng"
      elif percentage>=80:
       grade="A"
       performance="excellent"
      elif percentage>=70:
       grade="B"
       performance="Very Good"
      elif percentage>=60:
       grade="C"
       performance+"Good"
      elif percentage>=50:
       grade="D"
      performance="Average"
else:
 grade="F"
performance="Need improvement"
print("\n---Academic Performance---")
print("student Name:",name)
print("Total marks:",total)
print("percentage:",round(percentage,2),"%")
print("Grade:",grade)
print("performance:",performance)


