import re
# Basic HTML generating class
class HTMLNode:
	tag = 'div'
	attrs = {}
	inner_html = {}
	short_tag = False
	close_tag = True
	verbose = True

	def __init__( self, tag, id = None ):
		self.tag = tag
		self.attrs = {}
		self.inner_html = {}
		self.short_tag = False
		self.close_tag = self.verbose = True;
		if( id is not None ):
			self.attr( 'id', id )

	def __str__( self ):
		eol = "\n" if self.verbose else ''
		ind = "\t" if self.verbose else ''
		output = '<' + self.tag
		if len( self.attrs ) > 0:
			output += ' '
			for attr in self.attrs:
				output += attr + '='
				output += '"' + str( self.attrs[attr] ) + '" ' if type( self.attrs[attr] ) != 'boolean' else str( self.attrs[attr] ) + ' '
			output = output[:-1]
		if self.short_tag is False and self.close_tag:
			output += '>' if len( self.inner_html ) == 0 else '>' + eol
			for name in self.inner_html:
				child_output = str( self.inner_html[name] )
				output += ind + re.sub( r'/\n/', "\n" + ind, child_output, re.DOTALL ) + eol
			output += '</' + self.tag + '>'
		else:
			output += '/>' if self.short_tag else '>'
		return output

	def attr( self, name, value ):
		self.attrs[name] = value

	def clear( self, name ):
		del self.attrs[name]

	def append( self, child, name = None ):
		key = name if name is not None else len( self.inner_html )
		self.inner_html[key] = child

	def drop( self, key ):
		del self.inner_html[key]

# Test
html = HTMLNode( 'div' )
html.attr( 'id', 'node-1' )
html.attr( 'style', 'color:black' )
print( html )
html.short_tag = True
print( html )
html.short_tag = html.close_tag = False
print( html )

child = HTMLNode( 'span' )
child.attr( 'info', 'true' )
html.append( child, 'select' )
print( html ) # Doesn't print child because there is no closing tag
html.close_tag = True
print( html )
html.verbose = False
print( html )
html.verbose = True
html.clear( 'style' )
html.append( 'Here is a text inner.' )
html.drop( 'select' )
print( html )
