class employee:
    name = "sabbir ahmed rony" #This is a class attribute
    language = "Javascript"
    salary = 12000
    initialized = False

    def __init__(self,salary=None):
        if salary is not None:
             self.salary = salary
        if not employee.initialized:
            print("Sabbir And Mahir Is Relatives")
            employee.initialized = True



sabbirs = employee() #This is a object attribute
mahir = employee(13000)
mahir.name = "Saimon Islam Mahir"
mahir.language = "Python"
print(sabbirs.name,sabbirs.language,sabbirs.salary)
print(mahir.name,mahir.language,mahir.salary)



