let slider = document.getElementById("myRange");
let output = document.getElementById("output");
let mySvg = document.querySelectorAll(".mysvg");

slider.value = 0;
output.innerHTML += 0;

slider.oninput = function() {
  output.innerText = "Max ingredients:" + Math.floor( this.value / 10 );
}

mySvg.addEventListener("click", function() {
  if(mySvg.style.fill == "white"){
    mySvg.style.fill = "gold";
  } else {
    mySvg.style.fill = "white";
  }
})

