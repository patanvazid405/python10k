class Company:
    def __init__(self,comp_name,location):
        self.comp_name = comp_name
        self.location = location
    
    def comp_details(self):
        print(f'Company is {self.comp_name} Located at {self.location}')

class Manager(Company):
    def __init__(self, exp,team_size,comp_name, location):
        Company.__init__(self,comp_name, location)
        self.exp = exp
        self.team_size = team_size
    
    def manager_details(self):
        print(f"Manager having {self.exp}yr experience and team size is {self.team_size} ")

class Developer(Company):
    def __init__(self, name,skill,comp_name, location):
        Company.__init__(self,comp_name, location)
        self.name = name
        self.skill = skill
    
    def Developer_Details(self):
        print(f"Dev Name is {self.name} and having skills {self.skill}")


class Project(Manager,Developer):
    def __init__(self,Project_name,comp_name,location,exp,team_size,name,skill):
        self.Project_name = Project_name
        Manager.__init__(self,exp,team_size,comp_name,location)
        Developer.__init__(self,skill,name,comp_name,location)
    
    def project_details(self):
        print(f"Company name is {self.comp_name} at {self.location}")
        print(f"Manager Experience is {self.exp} and team size {self.team_size}")
        print(f"Project name is {self.Project_name}")
        print(f"Developer name is {self.name} skill {self.skill}")


p1 = Project("Red Bus","L&T","Hyderabad",10,6,"Vazid","python")
p1.project_details()
p1.comp_details()

