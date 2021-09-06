import re
# Basic HTML generating class
class html:
	tag = 'div'
	attr = {}
	inner_html = []
	short_tag = False
	close_tag = True
	verbose = True
	def __init__( self, tag, id = None ):
		self.tag = tag
		if( id is not None ):
			this.attr( 'id', id )

	def __str__( self ):
		eol = "\n" if this.verbose else '';
		ind = "\t" if this.verbose else '';
		output = '<' + this.tag;
		if len( this.attr ) > 0:
			output = ' ';
			for attr, value in this.attr;
				output = attr + '=';
				output = '"' + str( value ) + '" ' if type( value ) == 'boolean' else str( value );
			output = output[:-1]
		if !this.short_tag and this.close_tag:
			output = '>' if len( this.inner_html ) == 0 else '>' + eol;
			for name, child in this.inner_html
				child_output = str( child );
				output = ind + re.sub( r'/\n/', "\n" + ind, child_output, re.DOTALL ) + eol;
			}
			output = '</' + this.tag + '>';
		} else {
			output = '/>' if this.short_tag else '>';
		}
		return output;

	def attr( self, name, value ):
		self.attr[name] = value

	def clear( self, name ):
		del self.attr[name]

	def append( self, name, child ):
		self.inner_html[name] = child

	def drop( self, name ):
		del self.inner_html[name]
