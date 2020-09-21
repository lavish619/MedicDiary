AOS.init();
$(document).ready(function(){
	$('#scrollDown').click(function(){
	$('html, body').animate({scrollTop: 0/*$("#scrollDown").scrollTop()*/ }, 1000);
	});
});
function toggleSideBar(){
	var x = document.getElementById("sidebar").style.marginLeft;
	if(x=="200px"){
		document.getElementById("sidebar").style.marginLeft='0';
		document.getElementById("main-content").style.marginLeft='80px';	
	}
	else{
		document.getElementById("sidebar").style.marginLeft='200px';
		document.getElementById("main-content").style.marginLeft='200px';
	}
}

    // acc[i].classList.toggle("active");
    //   var panel = sectionName.nextElementSibling;
    //   if (panel.style.maxHeight) {
    //     panel.style.maxHeight = null;
    //   } else {
    //     panel.style.maxHeight = panel.scrollHeight + "px";
    //   } 
    // }
    // acc[i].addEventListener("click", function() {
      
    // });
  

// alert('welcome');
// var acc = document.getElementsByClassName("accordion");
// var i;

// for (i = 0; i < acc.length; i++) {
//   acc[i].addEventListener("click", function() {
//    this.classList.toggle("active");
//      var panel = this.nextElementSibling;
//    if (panel.style.maxHeight) {
//       panel.style.maxHeight = null;
//     } else {
//     panel.style.maxHeight = panel.scrollHeight + "px";
//     } 
//     alert('hey there');
//   });
// }
