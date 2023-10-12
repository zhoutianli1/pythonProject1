# 时间序列数据 A指标全年xx，比上年增加/减少xx，比上年增长/减少xx.x%，达到近x年来最大值

#截面数据：A1指标占A指标xx.x%，A2指标占A指标xx.x%，

#面板数据：A1指标全年xx，比上年增长/减少xx.x%；A2指标全年xx，比上年增长/减少xx.x%

'''
1.对象没有(),class Employee,不是class Employee()
2.构造函数：第一种方法__init__()方法是一种特殊的方法，被称为类的构造函数或初始化方法，当创建了这个类的实例时就会调用该方法
3.第一种方法__init__()方法是一种特殊的方法，被称为类的构造函数或初始化方法，当创建了这个类的实例时就会调用该方法
4.emp1 = Employee("Zara", 2000) ,通过构造函数，给“实例对象”赋值
5.变量:
    类变量:
    实例变量:
    局部变量:

class Employee:
   '所有员工的基类'
   empCount = 0

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1


   def displayEmployee(self):
      print "Name : ", self.name,  ", Salary: ", self.salary


'''