# AdditionFlipper
This is a small proof of concept I created while playing around with the AST module. It's a decorator that replaces all instances of `+` with `-` in a function, and vice versa. For example, the following function:

"""python
@flipaddition
def addtester( x ):
    for i in range( 10 ):
        print x + i, x - i
    return x + 1
"""

Becomes:

"""python
def addtester( x ):
    for i in range( 10 ):
        print x - i, x + i
    return x - 1
"""

Usage is simple, not that anyone would ever want to use this: just `from addflipper import flippadition` and decorate whatever function you'd like with `@flipaddition`. 
