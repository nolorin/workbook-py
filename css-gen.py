#Basic class for CSS styles. Note: property handling and casting functions ommitted in this example because I don't consider them within Python's zeitgeist
class Style:
	attrs = {}
	name = ''
	prefix = ''
	verbose = False

	def __init__( self, name, type = None ):
		self.attrs = {}
		self.name = name
		self.prefix = ''
		if type is not None:
			self.type( type )

	def __str__( self ):
		if self.verbose:
			[ eol, ind, spa ] = [ "\n", "\t", ' ' ]
		else:
			eol = ind = spa = ''
		output = self.prefix + self.name + spa + '{' + eol
		for attr in self.attrs:
			output += ind + attr + spa + ':' + spa + str( self.attrs[attr] ) + ';' + eol
		output += '}' + eol
		return output

	def type( self, type ):
		if type == 'class':
			self.type = '.'
		elif type == 'id':
			self.type = '#'
		else:
			self.type = ''

# Test
style = Style( 'block' )
style.attrs['style'] = 'color:green'
style.type( 'class' )
print( style )
style.verbose = True
style.attrs['font-family'] = 'Serif'
print( style )
