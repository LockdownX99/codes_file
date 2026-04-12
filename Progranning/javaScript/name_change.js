console.log("hello");
japanese = {a:"ka",b:"tu",c:"mi",d:"ti",e:"ku",f:"lu",g:"ji",h:"ri",i:"mi",j:"ju",k:"ki",l:"no",m:"mo",n:"to",o:"rin",p:"ta",q:"chu",r:"sai",s:"ttu",t:"ari",u:"du",v:"ru",w:"fu",x:"ji",y:"mei",z:"na"};

const inputfield = document.getElementById("user_input");
const button = document.getElementById("btn");
const result = document.querySelector("p");

button.addEventListener("click", ()=>{
  const text = inputfield.value.toLowerCase();
  let japanese_name = "";
  for(const char of text){
    //alert(char)
    const translated = japanese[char] || char;
    japanese_name += translated;  
    result.innerText = japanese_name;
    //result.style.color="red";
    
}
});