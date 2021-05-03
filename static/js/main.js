var SubjectObject=
{
"AndraPradesh" : "Anantapur",
"Arunachal Pradesh" : "Anjaw"
}
  window.onload = function() {
	var subjectSel = document.getElementById("States");
	var topicSel = document.getElementById("Cities");
	for (var x in subjectObject) {
	  subjectSel.options[subjectSel.options.length] = new Option(x, x);
	}
	subjectSel.onchange = function() {
	  //empty Chapters- and Topics- dropdowns
	  chapterSel.length = 1;
	  topicSel.length = 1;
	  //display correct values
	  for (var y in subjectObject[this.value]) {
		topicSel.options[topicSel.options.length] = new Option(y, y);
	  }
	}
  }