class employee:
    def __init__(self,name,empid,base_salary):
        self.name=name
        self.empid=empid
        self.base_salary=base_salary

    def cal_salary(self):
        return self.base_salary
    
class developer(employee):
    def __init__(self, name, empid, base_salary, bonus):
        super().__init__(name, empid, base_salary)
        self.bonus=bonus

    def cal_salary(self):
        return self.base_salary+self.bonus
    
class manager(employee):
    def __init__(self, name, empid, base_salary,allowance):
        super().__init__(name, empid, base_salary) 
        self.allowance=allowance

    def cal_salary(self):
        return self.base_salary+self.allowance

class intern(employee):
    def __init__(self, name, empid, stipend):
        super().__init__(name, empid, 0)
        self.stipend=stipend

    def cal_salary(self):
        return self.stipend


if __name__ == "__main__":
    employee = [
        developer("Akshay", 101, 30000, 5000),
        manager("Rahul", 102, 40000, 10000),
        intern("Riya", 103, 15000)
    ]

    for empid in employee:
        print(f"{empid.name} ({empid.__class__.__name__}) Salary: {empid.cal_salary()}")             