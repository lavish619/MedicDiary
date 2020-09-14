AOS.init();
function toggleSideBar(){
	var x = document.getElementById("sidebar").style.marginLeft;
	if(x=="200px"){
		document.getElementById("sidebar").style.marginLeft='0';
		// document.getElementById("main-content").style.marginLeft='80px';	
	}
	else{
		document.getElementById("sidebar").style.marginLeft='200px';
		// document.getElementById("main-content").style.marginLeft='200px';
	}
}
