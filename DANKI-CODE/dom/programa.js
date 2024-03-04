var p = document.getElementsByTagName('p');
// o P vira um array lista
alert(p.length);
alert(p[0].innerHTML)

p[0].innerHTML = "Conteúdo Manipulado"

for (i = 0; i < p.length; i++){
    p[i].innerHTML = "Conteúdo Manipulado "+i
    
}