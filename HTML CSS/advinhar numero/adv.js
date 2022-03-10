var random= Math.floor(Math.random()*100)
function lol(random){
var chute=parseInt(document.getElementById("entrada").value)
var status=(document.getElementById("status"))

if(chute>random){
  status.innerHTML="Seu chute é maior que o número pensado"
  status.style.setProperty("background-color", "red");
}
if(chute<random){
  status.innerHTML="Seu chute é menor que o número pensado"
  status.style.setProperty("background-color", "blue");

}
if(chute===random){
  status.innerHTML="Parabéns, você acertou o número pensado"
  status.style.setProperty("background-color", "green");
}
console.log(random)
}


