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

// function openTab(evt, tabName) {
// 		var i, tabcontent, tablinks;
// 		tabcontent = document.getElementsByClassName("tabcontent");
// 	for (i = 0; i < tabcontent.length; i++) {
// 		tabcontent[i].style.display = "none";
// 	}
// 	tablinks = document.getElementsByClassName("tablinks");
// 	for (i = 0; i < tablinks.length; i++) {
// 		tablinks[i].className = tablinks[i].className.replace(" active", "");
// 	}
// 	document.getElementById(tabName).style.display = "block";
// 	evt.currentTarget.className += " active";
// }