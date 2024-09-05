var a,b=0

x=[a,b]
c="testando"

x[0]=c
x[1]='dia'
console.log(x[0])
console.log(x[1])

console.log(x)

for(i=0;i<x.length;i++)(
    console.log(x[i])
)

  document.getElementById("diasDireito").innerHTML = dia2;
  document.getElementById("valorDireito").innerHTML = sal_trabalhado.toLocaleString('pt-BR', { style: 'currency', currency: 'BRL' });;
  document.getElementById("insal").innerHTML = adicional_recebido;
  document.getElementById("insalV").innerHTML = adici_trabalhado.toLocaleString('pt-BR', { style: 'currency', currency: 'BRL' });;
  document.getElementById("notuV").innerHTML = valNot.toLocaleString('pt-BR', { style: 'currency', currency: 'BRL' });;
  document.getElementById("heV").innerHTML = valHe.toLocaleString('pt-BR', { style: 'currency', currency: 'BRL' });;