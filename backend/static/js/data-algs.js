console.log("he sido cargad");
$(function(){
	$("#rateYo").rateYo({
		rating: 3.6
	});
});
console.log("he llegado al final");

$(document).ready(function(){	
	console.log("entor en dr");
	$("#backToCategories").click(function(){
		console.log("435yutkgjh");
		$("#main").load("biblio.html");
	});
	
})