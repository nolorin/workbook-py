#Basic class for CSS styles. Note: property handling and casting functions ommitted because they are not in the style of Python
class Style:
	attr = {}
	name = ''
	type = ''
	verbose = False

	def __str__( self ):
		if self.verbose:
			[ eol, ind, spa ] = [ "\n", "\t", ' ' ]
		else:
			eol = ind = spa = ''
		output = self.type + self.name + spa + '{' + eol
		for a, v in this.attr:
			output += ind + a + spa + ':' + spa + str( v ) + ';' + eol
		output += '}' + eol
		return output
