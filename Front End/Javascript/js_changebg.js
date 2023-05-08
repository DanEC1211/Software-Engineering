
let body=document.querySelector("body");;
let bclose = document.querySelector("#cls");
let winfloat = document.querySelector(".shadow");
let ch_bg = document.querySelector("#ch_bg");

bclose.onclick = function(){
  winfloat.classList.toggle("show");
}

bclose.onclick = function(){
  winfloat.classList.remove("show");
}



ch_bg.onclick = function(){
  winfloat.classList.add("show");
}

let data = null;
const radios= document.getElementsByName('bgs');
function chg_bg(){
  for(var i=0; i< radios.length;i++){
    if(radios[i].checked){
      data = radios[i].value;
    }
  }
  body.className="";
  body.classList.add('bg_'+data);
}      
