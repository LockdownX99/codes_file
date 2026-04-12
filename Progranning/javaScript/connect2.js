function b(){ document.querySelector("#switch").addEventListener("click",function(){
  let value = document.querySelector("#switch");
  if(value.innerHTML ==="OFF"){
    value.innerHTML = "ON";}else{
    value.innerHTML = "OFF";}
})};

document.addEventListener("DOMContentLoaded",b);