
"""
quick file to generate the template presentation files/structure/layout
prior to the polished content (added manually)
"""

titles=["Problem Space",
		"Literature Review",
		"Prototyping",
		"Introduction to Justinmind",
		"Prototyping with Justinmind",
		"Task Analysis",
		"Users and User Requirements",
		"Design Thinking",
		"Human AI Interaction"];
		
		
template = 'template.html'
rep0 = '{topic}'
rep1 = '{lectureno}'


for i in range( 0, len(titles) ):
	no = i + 1;
	filename = 'Lecture %02d - %s.html' % ( no, titles[i] )
	
	fp = open( template, 'rt' )
	txt = fp.read()
	fp.close()
	fp = 0
	
	txt = txt.replace( rep0, titles[i] )
	txt = txt.replace( rep1, ('%02d' % (no)) )
	
	fp = open( filename, 'w' )
	fp.write( txt )
	fp.close()
	fp = 0
	
	
	