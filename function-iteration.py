# Recursively iterating lambda functions

# Checks if variable is contained within the scope or any sub-scope of an array object (i.e., sub-arrays, sub-sub-arrays, sub-sub-sub-arrays, etc.).
def array_check( needle, haystack ):
	def iterator( needle, haystack ):
		for hay in haystack:
			if hay == needle:
				return True
			elif type( hay ) is array:
				result = iterator( needle, hay ):
				if result:
					return True;
		return False

# Checks whether a lambda function results in a constant value after being applied to itself over and over.
def n_to_infinity( func, num_iterations, depth = 1 ):
	i = d = 0
	def iteration( f, prev ):
		global i, d, num_iterations, depth
		if i < num_iterations:
			result = globals()[f]( prev )
			if result == prev:
				d += 1
				if d >= depth:
					return True
			return iteration( f, result )
		else:
			return None
	result = iteration( func, None )
	if result:
		return True
	else:
		return False

# Apply a lambda function over and over to a variable for a set number of times and until a specific result is achieved, whichever comes first
def func_iterate( var, func, num_iterations, goal = None ):
	if var is not goal:
		result = var
		for i in range( 0, num_iterations ):
			result = globals()[func]( result )
			if result == goal:
				break
		return result
	else:
		return None
