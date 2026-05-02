#Create a list of employees with their name and year of service
#Remove duplicate names and print only the names once
#do it in classes (list of objects)

class employee:
    def __init__(self, name , years):
        self.name = name
        self.years = years

em1 = employee("Nikos", 4)
em2 = employee("Nikos", 5)
em3 = employee("Giannis", 6)

employees = [em1, em2, em3]

seen = set()
for x in employees:
    if x.name not in seen:
        seen.add(x.name)
        print(x.name)


