
"""
quick file to generate the index homepage 

files/names follow a consistent format, so easier to generate each time new content is added (e.g., new notes file, or new quiz questions)

Naming example:
Lecture 00 - Introduction.html
Notes 00 - Introduction.html

Example:
\> python generateindex.py > index.html

"""

titles=["Introduction",
		'Interaction Design',
        "Problem Space",
		"Literature Review",
		"Prototyping",
		"Prototyping Tools",
		"Task Analysis",
		"Usability Part 1",
		"Usability Part 2",
		"Design Thinking",
		"Human AI Interaction",
		"Revision" ];
		

txt = ""

# header
txt += """
<link rel="shortcut icon" type="image/x-icon" href="./favicon.ico" />

<br>
<table align="center"><tr><td>

F27ID - <a href='https://www.macs.hw.ac.uk/students/cs/courses/f27id-introduction-to-interaction-design/'>Introduction to Interaction Design</a>
<br>
<br>

<table>
<tr>
<td>Wk      		</td>
<td>Unit            </td>
<td>Topic   		</td>
<td>Lecture 		</td>
<td>        		</td>
<td>Notes   		</td>
<td>Labs    		</td>
<td>Revision 		</td>
</tr>
"""

def FileExist(fn):
	import os.path
	return os.path.exists( fn )


wkno  = 0
unit  = 0
	
for i in range( 0, len(titles) + 1 ): # + 1 is due to week 6 skip
	
	wkno += 1
	
	# hack - nothing happens in week 6
	if ( wkno == 6 ):
		txt += """
		<tr>
		  <td>%d      		</td>
          <td align="center" colspan="7"> --- </td>
		</tr>
		""" % (wkno)
		continue
		
	
	no = unit
	topic = titles[no]
	unit += 1
	filename = 'Lecture %02d - %s.html' % ( no, topic )
	
	
	
	lectureurl = "-"
	lecturefilename = './material/lectures/Lecture %02d - %s.html' % ( no, topic )
	if ( FileExist( lecturefilename ) ):
		lectureurl = "<a href='" + lecturefilename + "'> Slides </a>"
	
	notesurl = '-'
	notesfilename = './material/notes/Notes %02d - %s.html' % ( no, topic )
	if ( FileExist( notesfilename ) ):
		notesurl = "<a href='" + notesfilename + "'> Notes </a>"
	
	labsurl = '-'
	labfilename = './material/labs/Lab %02d - %s.html' % ( no, topic )
	if ( FileExist( labfilename ) ):
		labsurl = "<a href='" + labfilename + "'> Lab </a>"
		

	quizsurl = '-'
	quizfilename = './material/quizzes/Quiz %02d - %s.html' % ( no, topic )
	if ( FileExist( quizfilename ) ):
		quizsurl = "<a href='" + quizfilename + "'> Quiz </a>"
	
	
		
	haslabs = '-' # Labs
	hasquiz = '-' # Quiz
	
	val = """
	<tr>
	<td>%d      	</td>
	<td>%d      	</td>
	<td>%s          </td>
	<td>%s          </td>
	<td>        	</td>
	<td>%s          </td>
	<td>%s    		</td>
	<td>%s     		</td>
	</tr>
	""" % (wkno, unit, topic, lectureurl, notesurl, labsurl, quizsurl  )

	txt += val
	

	
	

# footer
txt += """
</table>

<br>
Assessment:<br>Exam 60% <br>Coursework (40%) 
</table>
<br>
"""

print( txt )

if 0:
	fp = open( 'index.html', 'w' )
	fp.write( txt )
	fp.close()
	fp = 0
		


