# class Human:
# 	heigh = 170
# 	_name = "John Doe"
# 	__age = 20

# 	def hello(self):
# 		print("Hello")

# 	def how_old(self):
# 		return Human.__age

# class Student(Human):
# 	heigh = 185

# class Worker(Human):
# 	heigh = 185

# nick = Student()
# ann = Worker()

# nick.hello()
# age = nick.how_old()
# print(nick._name, nick.heigh)
# print(age)


# print("ann", ann.heigh)
# 		





class ClassName:
	def __init__(self, model, *args, **kwargs):
		super().__init__(*args, **kwargs)