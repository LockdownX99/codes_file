const sophia = {
  name: "Sophia",
  version: 1.0,
  isOnline: true
};

function user(){
  let userInput = document.querySelector("#user_input");
  let message = userInput.value.toLowerCase();
  if ( message.includes("hello")){
    document.querySelector("#box").innerHTML = `${sophia.name}: hi there!`;
    //document.querySelector("#box").innerHTML =" who am i talking to ?";
    
  }
  // Optional: Clear the input after sending
  userInput.value = "";
}