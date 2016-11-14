import inspect, ast

class AdditionFlipper( ast.NodeTransformer ):
    # Flip addition to subtraction, and vice versa
    def visit_BinOp( self, node ):
        if type( node.op ).__name__ == "Sub":
            node.op = ast.Add()
        elif type( node.op ).__name__ == "Add":
            node.op = ast.Sub()
        return node

def flipaddition( f ):
    src = inspect.getsource( f ) # Get source code
    tree = ast.parse( src ) # Convert source to AST
    tree.body[0].decorator_list = [] # Remove decorator

    transformer = AdditionFlipper()
    transformer.visit( tree )

    myScope = {} # Create new namespace to compile tree in
    exec( compile( tree, '', 'exec' ), myScope, myScope )

    f.__code__ = myScope[ f.__name__ ].__code__
    return f
