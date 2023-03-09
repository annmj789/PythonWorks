class A:
    var1 = None # public
    _var2 = None # protected
    __var3 = None # private

    def __init__(self, var1, var2, var3):
        self.var2 = var2
        self.var1 = var1
        self.var3 = var3

    def display_public(self):
        print(self.var1)

    def _display_protected(self):
        print(self._var2)

    def __display_private(self):
        print(self.__var3)

    def access_private(self):
        self.__display_private()

#derived class

class B(A):
    def __init__(self, var1, var2, var3):
        A.__init__(self, var1, var2, var3)
    def access_protected(self):
        self._display_protected()

obj=B("pub_red","pro_white","pvt_gree")

obj.display_public()
obj._display_protected()
obj.__display_private()

print("object is accessing public member",obj.var1)
print("object is accessing protects member",obj.var2)
print("object is accessing private member",obj._A__var2)
"""
name mandling
Aprocess in which any given identifier with one trailing underscore and two leading underscore
is textually replaced with the _ClassName__identifier is known as Name mangling 
in _ClassName__identifier name, ClassName is the name if current class where identifier is present
"""