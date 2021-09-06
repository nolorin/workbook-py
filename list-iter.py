import re

tuple1 = ( 'Tom', 'Jane', 'Mary', 'Farouk', 'Elizabeth', 'Pat' )
tuple2 = ( 'Worker', 'Manager', 'Contractor', 'Executive' )
tuple3 = ( 'Experienced', 'Skilled', 'Novice' )
tuple4 = ( 'Boston', 'Chicago', 'Los Angeles', 'San Francisco', 'Seattle', 'Atlanta', 'Austin', 'Houston' )

loc = {
	'Illinois' : [ 'Chicago' ],
	'California' : [ 'Los Angeles', 'San Francisco' ],
	'Georgia' : [ 'Atlanta' ],
	'Washington' : [ 'Seattle' ],
	'Texas' : [ 'Austin', 'Houston' ]
}

eigenKey = (
	( 0, 1, 1, 3 ),
	( 1, 2, 1, 4 ),
	( 2, 0, 2, 6 ),
	( 2, 0, 0, 2 ),
	( 3, 1, 1, 0 ),
	( 4, 2, 1, 5 ),
	( 5, 0, 1, 4 ),
	( 5, 0, 2, 4 )
)

output = ''
template = "{} is a&?{} {} from {}"
for vector in eigenKey:
	output += template.format( tuple1[vector[0]], tuple3[vector[2]], tuple2[vector[1]], tuple4[vector[3]] )
	for state, cities in loc.items():
		if tuple4[vector[3]] in cities:
			output += ', ' + state;
	output += ".\n"

output = re.sub( r'(&\?)(?=[^aeio])', ' ', output, re.I|re.DOTALL )
output = re.sub( r'(&\?)([aeio])', 'n ', output, re.I|re.DOTALL )

print( output );
