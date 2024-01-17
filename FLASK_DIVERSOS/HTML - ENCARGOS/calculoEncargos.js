dias_avos = 0
function somar() {
  let val1 = parseFloat(document.getElementById("valor1").value)
  let val2 = parseFloat(document.getElementById("valor2").value)
  let val3 = parseFloat(document.getElementById("valor3").value)
  let val4 = parseFloat(document.getElementById("valor4").value)
  let val5 = parseFloat(document.getElementById("valor5").value)
 
  

  let totalEncargos = val1+val2+val3+val4+val5
  

  if(totalEncargos < 1412){
    inss=totalEncargos*7.5/100

  }
  else if(totalEncargos < 2666.68){
    inss1=(totalEncargos*9/100)-21.18
  }

  else if(totalEncargos < 4000.03){
    inss1=(totalEncargos*12/100)-101.18
  }

  else if(totalEncargos < 7786.02){
    inss1=(totalEncargos*14/100)-181.18
  }

  else if(totalEncargos > 7786.02){
    inss1=908.85
  }

  let base_irrf1=totalEncargos-inss1

  if(base_irrf1 < 2112){
    irrf1=0

  }
  else if(base_irrf1 < 2826.66){
    irrf1=(base_irrf1*7.5/100)-158.4
  }

  else if(base_irrf1 < 3751.06){
    irrf1=(base_irrf1*15/100)-370.40
  }

  else if(base_irrf1 < 4664.69){
    irrf1=(base_irrf1*22.5/100)-651.73
  }

  else if(base_irrf1 > 4664.68){
    irrf1=(base_irrf1*27.5/100)-884.96
  }

  
  
  document.getElementById("inss1").innerHTML = 'Valor do inss1      R$: ' + inss1.toFixed(2);
  document.getElementById("irrf1").innerHTML = 'Valor do irrf1      R$: ' + irrf1.toFixed(2);

  



}
