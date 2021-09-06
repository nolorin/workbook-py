# Integer multiplication function that uses lambda function arguments. Note: in PHP lambda functions are variable scope function definitions.
class Object:
	def __init__( self, prop ):
		self.value = prop
	def __mul__( self, toMult ):
		n = len( vars( self ) )
		setattr( self, 'child_' + str(n), toMult );
		return self
	def __str__( self ):
		output = 'Object(value=' + str( self.value ) + ') {' + "\n"
		for prop, obj in vars( self ).items():
			if prop is 'value': continue
			output += "\t" + str( obj ) + "\n"
		output += '}'
		return output

multScalar = lambda base, out : base + out
multObj = lambda base, out : out * base
negScalar = lambda out : out*-1 if type( out ) is int else out[::-1] if type( out ) is str else arrayIter( out ) if type( out ) is list or tuple else False
arrayIter = lambda out : tuple( [ negScalar( i ) for i in list( out ) ] ) if type( out ) is tuple else [ negScalar( i ) for i in out ]
negObj = lambda out : out

def multiply( base, multiplicant ):
	if type( base ) is not int:
		output = '' if type( base ) is str else Object( 'Shell' ) if type( base ) is Object else base if type( base ) is list or tuple else None
		iterant = multObj if type( base ) is Object else multScalar if type( base ) is str or list or type else None
		negative = negObj if type( base ) is Object else negScalar if type( base ) is str or list or tuple else None
		if iterant is not None:
			for i in range( 0, abs( multiplicant ) ):
				output = iterant( base, output )
			if multiplicant < 0:
				output = negative( output )
			return output
		else:
			return False
	else:
		return base*multiplicant

# Test
print( multiply( 5, 5 ) )
print( multiply( 'Harp', 4 ) )
print( multiply( '*deer', -5 ) )
print( multiply( [ 1, 2, 3, 4 ], 2 ) )
print( multiply( ( 2, 34, 11, 7 ), 3 ) )
print( multiply( ( 1, -2, 4 ), -4 ) )
print( multiply( Object( 'Item' ), 2 ) )
