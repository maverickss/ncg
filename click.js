function foldall () {
   var foldall = document.getElementsByClassName('foldall');
   for(var i=0; i<foldall.length; i++) {
      var foldthis = foldall[i];			
      if (foldthis.display == "block") { 
	 foldthis.display = "none";
      }
   }
};

function foldout(fold) {
   foldall(); // collapse everything
   if (document.getElementById) {
      var fold = document.getElementById(fold).style;
      if (fold.display == "block") {
	 fold.display = "none";
      } else {
	 fold.display= "block";
      }
      return false;
   } else {
      return true;
   }

};
