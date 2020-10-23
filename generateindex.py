
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
		"Users and User Requirements",
		"Task Analysis",
		"Usability",
		"Testing and Evaluation",
		"Design Thinking",
		"Human AI Interaction",
		"Revision" ];

		
videos = { "Introduction"       : "https://www.youtube.com/embed/wVtebjGk190?start=5&autoplay=1",
           "Interaction Design" : "https://www.youtube.com/embed/MDRJLk-ojx4?start=5&autoplay=1",
		   "Problem Space"      : "https://www.youtube.com/embed/QNwFCXUhMg4?start=5&autoplay=1",
		   "Literature Review"  : "https://www.youtube.com/embed/C5CfRFG9lWE?start=5&autoplay=1",
		   "Prototyping"        : "https://www.youtube.com/embed/Ac8KdFEVljI?start=5&autoplay=1"
		 }

extra = {	"Literature Review" : ["https://www.youtube.com/watch?v=zIYC6zG265E",
                                   "https://www.youtube.com/watch?v=S3xo6ZjBV6U"],
								    	  
			"Prototyping" : ["https://youtu.be/JMjozqJS44M"],
							 
			"Users and User Requirements" : ["https://www.youtube.com/watch?time_continue=23&v=lYkC6qaRBe4",
											 "https://www.youtube.com/watch?v=W91-jzWg_vo"]
		}

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
<td>                </td>
<td>Video 			</td>
<td>Extra           </td>
<td>                </td>
<td>        		</td>
<td>Notes   		</td>
<td>Labs    		</td>
<td>Revision 		</td>
</tr>
"""

def FileExist(fn):
	import os.path
	return os.path.exists( fn )

def VideoExist(fn):
	return 0


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

	
	if ( topic == 'Interaction Design' ):
		wkno = wkno - 1;
	
	filename = 'Lecture %02d - %s.html' % ( no, topic )
	
	
	
	lectureurl = "-"
	lecturefilename = './material/lectures/Lecture %02d - %s.html' % ( no, topic )
	if ( FileExist( lecturefilename ) ):
		lectureurl = "<a href='" + lecturefilename + "'> Slides </a>"
	
	videourl = "-"
	if ( topic in videos ):
		videourl = "<a href='" + videos[ topic ] + "'>Video</a>"
	
	extraurl = "-"
	if ( topic in extra ):
		extraurl = ''
		for ii in range(0, len(extra[ topic ]) ):
			kk = extra[topic][ii]
			extraurl += "<a href='" + kk + "' target='_blank'>Link</a> &nbsp;"
		
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
	<td>&nbsp</td>
	<td>%s          </td>
	<td>%s          </td>
	<td>&nbsp</td>
	<td>        	</td>
	<td>%s          </td>
	<td>%s    		</td>
	<td>%s     		</td>
	</tr>
	""" % (wkno, unit, topic, lectureurl, videourl, extraurl, notesurl, labsurl, quizsurl  )

	unit += 1
		
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
		


