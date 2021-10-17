class Foo:
   num_accounts = 0          

   def func1():           
            print("function 1")
   def func2(self):
            print(id(self))
            print("function 2")



# f_instance = Foo() 
# print(id(f_instance))
# f_instance.func2() 
# f_instance.func1()
Foo.func1()
Foo.func2()

#  https://blog.naver.com/sobrightlf/222539452200
