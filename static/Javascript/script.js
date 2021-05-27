


 const dropdown = document.getElementById("dropdown");
 var navItem = document.getElementsByClassName("t");


 dropdown.style.display = "none";
 
 for(var i = 0; i < navItem.length; i++){
 
 navItem[i].addEventListener("hover", function helloWorld(){


    console.log("hello unvicsere")
 })
 }
 
