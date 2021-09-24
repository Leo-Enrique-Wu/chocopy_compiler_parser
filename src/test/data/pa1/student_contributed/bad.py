class Foo(object):
  
  x1:int = 9
  # found a syntax error on the var def x2
  x2;[int] = []
  # the parser could recover from errors parsing a variable declaration
  # and continue parsing the rest of the declarations
  s:string = "Hello"
  
  def set(self:"Foo", x:int) -> object:
    self.x = x

  # found a syntax error on the func def bar1
  def bar1() <- int:
    1
  
  # the parser could recover from errors parsing a function declaration
  # and continue parsing the rest of the declarations and statements.
  def bar3(z1:int, True, z3:[str], z4;bool, z5:int) -> int:
    y:int = 88
    say(x)
		

#def xar1() <- int:
#  1

# Evne found serval syntax errors in the arguments,
# the parser could recover from those errors and continue 
# parsing the rest of arguments
def Xoo(g1:int, True, g3:[str], g4;bool, g5:int) -> int:
	x:bool = True
		print(x)
		
		# Found a syntax error on a statement in a function 
		# denifition
		drink;True)
		# The parser could recover from errors within a statement 
		# and continue parsing following statements
		laugh(False)
		
y = 999

# Found a syntax error on a statement at the top level
print)x)
# The parser could recover from errors within a statement 
# and continue parsing following statements
print(y)

# Found a syntax error in one argument
# The parser could recover from the error and continue 
# parsing following arguments
Bar.loo(x != y, z !! y, False)

return True