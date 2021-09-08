# Recursively iterating lambda functions

# Checks if variable is contained within the scope or any sub-scope of an array object (i.e., sub-arrays, sub-sub-arrays, sub-sub-sub-arrays, etc.).
def array_check( needle, haystack ):
	def iterator( n, h ):
		for hay in h:
			if hay == n:
				return True
			elif type( hay ) is list:
				result = iterator( n, hay )
				if result:
					return True
		return False
	return iterator( needle, haystack )

# Checks whether a lambda function results in a constant value after being applied to itself over and over.
def n_to_infinity( initial, func, num_iterations, depth = 1 ):
	prev = initial
	d = 0
	for i in range( 0, num_iterations ):
		result = func( prev )
		d += 1 if result == prev else 0
		if d >= depth:
			return True
		else:
			prev = result
	return False

# Apply a lambda function over and over to a variable for a set number of times and until a specific result is achieved, whichever comes first
def func_iterate( var, func, num_iterations, goal = None ):
	if var is not goal:
		result = var
		for i in range( 0, num_iterations ):
			result = func( result )
			if result == goal:
				break
		return result
	else:
		return None

# Test1
array = [ 8, 203, [ 31, 2, [ 17, 23 ], 58, 2, 12 ], 4, [ 12, 1, 0, 0, 172 ], [ 1, [ 3, 17, 2 ], [ 36, 28, 583, 2 ], 1, 90 ] ]
print( array_check( 0, array ) ) # Returns True
print( array_check( 112, array ) ) # Returns False
print( array_check( 'Subject', array ) ) # Returns False
print( array_check( 583, array ) ) # Returns True

print()

# Test2
func = lambda x : round( int( x or 0 )/2, 0 )

print( n_to_infinity( 10, func, 10 ) ) # Returns True
print( n_to_infinity( 10, func, 1 ) ) # Returns False
print( n_to_infinity( 10, func, 4 ) ) # Returns False
print( n_to_infinity( 10, func, 5 ) ) # Returns True (Five is the number of times required to get the same result twice for depth of 1)
print( n_to_infinity( 10, func, 5, 2 ) ) # Returns False
print( n_to_infinity( 10, func, 6, 2 ) ) # Returns True (When depth is 2, another iteration is needed to get same result)

print()

# Test3
print( func_iterate( 10, func, 2, 1 ) ) # Returns 2.0, the result of func after two iterations
print( func_iterate( 10, func, int( 1e15 ), 1 ) ) # Returns 1.0 without running through 1e15 iterations
