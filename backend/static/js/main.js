function loadHome(){
	$("#main").load("../templates/backend/home.html");
};

function license(){
	let year = new Date();
	let currentY = year.getFullYear();
	return currentY + ' - All Rights with Manet Reference';
}

$(document).ready(function(){	
	$("#home").click(function(){
		$("#main").load("./home.html");
	});

	$("#login").click(function(){
		$("#main").load("./login.html");
	});

	$("#t-simulators").click(function(){
		$("#main").load("./t-simulators.html");
	});

	$("#t-scripts").click(function(){
		$("#main").load("./t-scripts.html");
	});

	$("#t-plugins").click(function(){
		$("#main").load("./t-plugins.html");
	});

	$("#ralgos").click(function(){
		$("#main").load("./ralgorithms.html");
	});

	$("#handson").click(function(){
		$("#main").load("./handson.html");
	});

	$("#biblio").click(function(){
		$("#main").load("./biblio.html");
	});

	$("#license").text(license());

	$("#fContact").click(function(){
		$("#main").load("./contact.html");
	});
})
