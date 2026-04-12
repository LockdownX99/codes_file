let count = 1;
switch(count){
  case 1 : document.write("Nunber 01");
  break
  case 2 : document.write("number 02")
  break 
  
};




function user()
{
document.querySelector("#submit").style.color="red";
}

document.write("<h1>This is an example of heading.</h1>");
document.write("<p>this is a example of paragraph.</p>");


alert("hello")

/*
let d = new Date();
let theDay =d.getDay();
document.write(theDay);
document.write("   ")
let theHour = d.getTime()
document.write(theHour)
*/

confirm("ok");


function show_confirm(){
  let r = confirm("Press a button");
  if (r==true){alert("you press okay");}
  else{alert("you press cancel");}
}
show_confirm();



prompt("your name ? ","Miraj")