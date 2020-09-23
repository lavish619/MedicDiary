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
		document.getElementById("main-content").style.marginLeft='auto';
	}
	else{
		document.getElementById("sidebar").style.marginLeft='200px';
		document.getElementById("main-content").style.marginLeft='auto';
	}
}