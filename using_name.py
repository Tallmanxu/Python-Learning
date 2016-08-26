#!/usr/bin/python
# -*- coding: UTF-8 -*-
# #Filename: using_name.py

def test():
    for letter in 'Python':     # First Example
       if letter == 'h':
          #break
          continue

       var = 10                    # Second Example
       while var > 0:

           if var == 5:
              #break
              var = var -1
              #continue
              return
           print 'Current variable value :', var
           var = var -1

       print 'Current Letter :', letter


test()
print "Good bye!"

fo = open("foo.txt", "r+")
str = fo.read(10);
print "读取的字符串是 : ", str

# 查找当前位置
position = fo.tell();
print "当前文件位置 : ", position

# 把指针再次重新定位到文件开头
position = fo.seek(0, 0);
str = fo.read(10);
print "重新读取字符串 : ", str
# 关闭打开的文件
fo.close()



class Employee:
   '所有员工的基类'
   empCount = 0

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1

   def displayCount(self):
     print "Total Employee %d" % Employee.empCount

   def displayEmployee(self):
      print "Name : ", self.name,  ", Salary: ", self.salary

"创建 Employee 类的第一个对象"
emp1 = Employee("Zara", 2000)
"创建 Employee 类的第二个对象"
emp2 = Employee("Manni", 5000)

emp1.displayCount()
emp2.displayCount()
emp1.displayEmployee()
emp2.displayEmployee()

if __name__ == '__main__':
    print 'The program is being run by itself'
else:
    print 'I am being imported from another module'