var tts = {};
tts.Synth = window.speechSynthesis;
tts.Voices = [];
tts.Voices = tts.Synth.getVoices(); // get a list of available voices.
tts.DvIndex = 0; //Used to help identify the default tts voice for Chrome or FF on the users platform.
tts.DvRate = 0.85; // used to set speech rate between 0 and 2, 1 = 'normal'- there are other seemingly optional parameters like pitch, language, volume.
tts.On = false; //Set to false to prevent tts production.
tts.Cancel = true; // Set to true if you want reading to stop with a slide change. Otherwise, all readable text is queued for speech output.
tts.readPage  = false;
tts.readFrags = false; //Set to true to read fragment text content as it appears.
tts.readNotes = true; //set to true to read text content of any <aside class="notes">text content</aside> tag in a slide section

/*
https://stackoverflow.com/questions/21947730/chrome-speech-synthesis-with-longer-texts
*/
var timeoutResumeInfinity;
function resumeInfinity() {
    window.speechSynthesis.resume();
    timeoutResumeInfinity = setTimeout(resumeInfinity, 1000);
}

tts.ReadText = function(txt, last=false){
	
	console.log('read:>' + txt );
	// Use tts to read text. A new speech synthesis utterance instance is required for each tts output for FF.
	// Chrome lets you redefine the SpeechSynthesizerUtterance.txt property-
	// as needed without having to create a new object every time you want speech.
	let txt2 = txt.split(';').join('  ');
	
	let ttsSpeechChunk = new SpeechSynthesisUtterance(txt2);
	 ttsSpeechChunk.voice = tts.Voices[tts.DvIndex]; //use default voice -- some voice must be assigned for FF to work.
     ttsSpeechChunk.rate = tts.DvRate; 
     tts.Synth.speak(ttsSpeechChunk);	 
	 
	 if ( last )
	 {
		ttsSpeechChunk.onend = function(e){
		 //console.log('finished');
		 clearTimeout(timeoutResumeInfinity);
		 Reveal.next();
		 //console.log( e );
		 //console.log('next slide');
		}
	 }
	 else 
	 {
		ttsSpeechChunk.onend = function(event) {
			clearTimeout(timeoutResumeInfinity);
		};

	 }
	 
	 ttsSpeechChunk.onstart = function(event) {
		clearTimeout(timeoutResumeInfinity);
		resumeInfinity();
	 };


	 
};

tts.ReadVisElmts = function(){
	// Uses arguments[0] to denote a DOM element . Then read the innerText of the rest of the list of selectors that are contained in the arguments[0] element.
	// works in Chrome, Opera and FF.
	let txtToRead = [];
	let focusElmt = arguments[0];
	for (let i=1; i < arguments.length; i++) {
		let xElmts = focusElmt.querySelectorAll(arguments[i]);
		for (let k=0; k < xElmts.length; k++){
			txtToRead.push( xElmts[k].innerText );
			//tts.ReadText(xElmts[k].innerText, last);
		}
	}
	
	// check if our 'txt' is just all white spaces
	// use the \s quantifier to remove all white space
	let txtout = "";
	for (let i=0; i<txtToRead.length; i++)
	{
		txtout = txtout + txtToRead[i].replace(/\s/g, "")
	}
	
	//console.log( 'txtout:>' + txtout + '<' );
	
	if ( txtout.length > 1 )
	{
		for (let i=0; i<txtToRead.length; i++)
		{
			let last = false;
			if ( i==txtToRead.length-1) last = true;
			tts.ReadText(txtToRead[i], last);
		}
	}
	else 
	{
		//console.log('setting timeout for the next slide');
		setTimeout(function(){ Reveal.next(); }, 7000);
	}

	
	//Reveal.next();
	//console.log('all done');
};

tts.ReadAnyElmts = function(){
	// Uses arguments[0] to denote a DOM element . Then read the textContent of the rest of the list of selectors, even hidden ones, that are contained in the arguments[0] element.
	// works in Chrome, Opera and FF.
	let txtToRead = [];
	let focusElmt = arguments[0];
	for (let i=1; i < arguments.length; i++) {
		let xElmts = focusElmt.querySelectorAll(arguments[i]);
		for (let k=0; k < xElmts.length; k++){
			//tts.ReadText(xElmts[k].textContent);
			//txtToRead.push( xElmts[k].textContent );
			
			let prs = xElmts[k].textContent.split(';');
			for (let bb=0; bb<prs.length; bb++)
			{
				txtToRead.push( prs[bb] + '  ' );
			}
		}
	}
	
	
	// check if our 'txt' is just all white spaces
	// use the \s quantifier to remove all white space
	let txtout = "";
	for (let i=0; i<txtToRead.length; i++)
	{
		txtout = txtout + txtToRead[i].replace(/\s/g, "")
	}
	
	//console.log( 'txtout:>' + txtout + '<' );
	
	if ( txtout.length > 0 ) 
	{
		for (let i=0; i<txtToRead.length; i++)
		{
			let last = false;
			if ( i==txtToRead.length-1) last = true;
			tts.ReadText(txtToRead[i], last);
		}
	}
	else 
	{
		console.log('setting timeout for the next slide');
		setTimeout(function(){ Reveal.next(); }, 5000);
	}
	
	
};

tts.ToggleSpeech = function(){
	// turn tts on/off with status announced
	tts.On = !(tts.On);
	if (tts.On) {
		//tts.ReadText("speech On!")
	} else {
		clearTimeout(timeoutResumeInfinity);
		tts.Synth.cancel();
		//tts.ReadText("speech Off!")
	};
};



for (var ix = 0; ix < tts.Voices.length; ix++) { 
//find the default voice-- needed for FF, in Chrome voices[0] works as the default.
	if (tts.Voices[ix].default) {
		tts.DvIndex = ix;
	}
};

tts.Read = function()
{
	var thisSlide = Reveal.getCurrentSlide();
	if (tts.Cancel) tts.Synth.cancel(); //Stop reading anything still in the speech queue, if tts.Cancel.
	// Read the innerText for the listed elements of current slide after waiting 1 second to allow transitions to conclude.
	// The list of elements is read in the order shown. You can use other selectors like a ".readMe" class to simplify things.
	if (tts.On) {
		if (tts.readPage)  setTimeout(function(){tts.ReadVisElmts(thisSlide,"h1","h2","h3","p","li");}, 1000);
		if (tts.readNotes) setTimeout(function(){tts.ReadAnyElmts(thisSlide,".notes");}, 1000); // Then, conditionally, read hidden notes class.
		//setTimeout(function(){ tts.ReadText(' ', true); }, 1000);
	}
	//} );
}
	
Reveal.addEventListener( 'slidechanged', function( event ) {
	tts.Read();
}
);
	
	
Reveal.addEventListener( 'fragmentshown', function( event ) {
// This reads the text content of fragments as they are shown.
// event.fragment = the fragment element
	if (tts.readFrags && tts.On){
		let txt = event.fragment.textContent;
		tts.ReadText(txt);
	}
	} );
	
	
Reveal.configure({
  keyboard: {
    81: function() {tts.Synth.cancel()}, // press q to cancel speaking and clear speech queue.
	84: function() {tts.ToggleSpeech()}  // press t to toggle speech on/off
					 
  }
});