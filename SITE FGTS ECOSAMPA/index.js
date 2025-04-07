function calcular() {

    ano = document.getElementById("ano").value
    mes = document.getElementById("mes").value
   
    mes = String(mes)
    ano = String(ano)

    data = ("fgts" + mes + ano + ".json")
    console.log(data)



    fetch(data)
      .then(resp => resp.json())
      .then((dados) => {

        var fgtsnormal = document.getElementById("fgtsnormal")
        var fgts13 = document.getElementById("fgts13")
        var fgtsferias = document.getElementById("fgtsferias")
        var fgtsdissidio = document.getElementById("fgtsdissidio")
        var fgtsrecolhido = document.getElementById("fgtsrecolhido")
        var fgts8 = document.getElementById("fgts8")
        var fgts8total = document.getElementById("fgts8total")


        var fgtsnormalj = document.getElementById("fgtsnormalj")
        var fgts13j = document.getElementById("fgts13j")
        var fgtsferiasj = document.getElementById("fgtsferiasj")
        var fgtsdissidioj = document.getElementById("fgtsdissidioj")
        var fgtsrecolhidoj = document.getElementById("fgtsrecolhidoj")
        var fgts2j = document.getElementById("fgts2j")
        var fgts2totalj = document.getElementById("fgts2totalj")

        var totalFGTS = document.getElementById("totalFGTS")


        var somafgtsnormal = 0
        var somafgts13 = 0
        var somafgtsferias = 0
        var somafgtsdissidio = 0
        var somafgtsrecolhido = 0
        var somafgts8 = 0
        var somafgts8total = 0

        var somafgtsnormalj = 0
        var somafgts13j = 0
        var somafgtsferiasj = 0
        var somafgtsdissidioj = 0
        var somafgtsrecolhidoj = 0
        var somafgts2j = 0
        var somafgts2totalj = 0


        dados.map((key) => {

          //valores totais                

          if (key.Verba__1 == "Base do FGTS Normal" && key["Ano - Referência"] == ano && key["Mês - Referência"] == mes) {
            somafgtsnormal += parseFloat(key["Valor da Verba"])
          }

          if (key.Verba__1 == "Base do FGTS 13º Salário" && key["Ano - Referência"] == ano && key["Mês - Referência"] == mes) {
            somafgts13 += parseFloat(key["Valor da Verba"])
          }

          if (key.Verba__1 == "Base INSS/FGTS Férias do Mês" && key["Ano - Referência"] == ano && key["Mês - Referência"] == mes) {
            somafgtsferias += parseFloat(key["Valor da Verba"])
          }

          if (key.Verba__1 == "Base FGTS Normal Dif Dis" && key["Ano - Referência"] == ano && key["Mês - Referência"] == mes) {
            somafgtsdissidio += parseFloat(key["Valor da Verba"])
          }

          if (key.Verba__1 == "Valor do FGTS - GRFF" && key["Ano - Referência"] == ano && key["Mês - Referência"] == mes) {
            somafgtsrecolhido += parseFloat(key["Valor da Verba"])
          }


          //valores dos jovens aprendizes

          if (key.Verba__1 == "Base do FGTS Normal" && key.Cargo == "MENOR/JOVEM APRENDIZ" && key["Ano - Referência"] == ano && key["Mês - Referência"] == mes) {
            somafgtsnormalj += parseFloat(key["Valor da Verba"])
          }

          if (key.Verba__1 == "Base do FGTS 13º Salário" && key.Cargo == "MENOR/JOVEM APRENDIZ" && key["Ano - Referência"] == ano && key["Mês - Referência"] == mes) {
            somafgts13j += parseFloat(key["Valor da Verba"])
          }

          if (key.Verba__1 == "Base INSS/FGTS Férias do Mês" && key.Cargo == "MENOR/JOVEM APRENDIZ" && key["Ano - Referência"] == ano && key["Mês - Referência"] == mes) {
            somafgtsferiasj += parseFloat(key["Valor da Verba"])
          }

          if (key.Verba__1 == "Valor do FGTS - GRFF" && key.Cargo == "MENOR/JOVEM APRENDIZ" && key["Ano - Referência"] == ano && key["Mês - Referência"] == mes) {
            somafgtsrecolhidoj += parseFloat(key["Valor da Verba"])
          }

        })


        //calculos
        somafgtsnormal = somafgtsnormal - somafgtsnormalj;
        somafgts13 = somafgts13 - somafgts13j;
        subtotalfgts8 = (somafgtsnormal + somafgts13 + somafgtsferias+ somafgtsdissidio)
        subtotalfgts2 = (somafgtsnormalj + somafgts13j + somafgtsferiasj)
        subtotalfgts8 = subtotalfgts8 * 0.08
        subtotalfgts2 = subtotalfgts2 * 0.02
        subtotaldissidio = somafgtsdissidio * 0.08          
        totalfgtsrecolhido = (somafgtsrecolhido - somafgtsrecolhidoj)
        totalfgts2 = subtotalfgts2 - somafgtsrecolhidoj
        totalfgts8 = (subtotalfgts8 - totalfgtsrecolhido)
        totalfgtsdissidio = subtotaldissidio

        totalguia = totalfgts2 + totalfgts8

        // impressão na tela
        fgtsnormal.innerHTML = somafgtsnormal.toLocaleString('pt-BR', { style: 'currency', currency: 'BRL' });
        fgts13.innerHTML = somafgts13.toLocaleString('pt-BR', { style: 'currency', currency: 'BRL' });
        fgtsferias.innerHTML = somafgtsferias.toLocaleString('pt-BR', { style: 'currency', currency: 'BRL' });
        fgtsdissidio.innerHTML = somafgtsdissidio.toLocaleString('pt-BR', { style: 'currency', currency: 'BRL' });
        totalbase.innerHTML = (somafgtsnormal + somafgts13 + somafgtsferias + somafgtsdissidio).toLocaleString('pt-BR', { style: 'currency', currency: 'BRL' });
        fgtsrecolhido.innerHTML = totalfgtsrecolhido.toLocaleString('pt-BR', { style: 'currency', currency: 'BRL' });
        fgts8.innerHTML = subtotalfgts8.toLocaleString('pt-BR', { style: 'currency', currency: 'BRL' });
        fgts8total.innerHTML = totalfgts8.toLocaleString('pt-BR', { style: 'currency', currency: 'BRL' });


        fgtsnormalj.innerHTML = somafgtsnormalj.toLocaleString('pt-BR', { style: 'currency', currency: 'BRL' });
        fgts13j.innerHTML = somafgts13j.toLocaleString('pt-BR', { style: 'currency', currency: 'BRL' });
        fgtsferiasj.innerHTML = somafgtsferiasj.toLocaleString('pt-BR', { style: 'currency', currency: 'BRL' });
        fgtsdissidioj.innerHTML = somafgtsdissidioj.toLocaleString('pt-BR', { style: 'currency', currency: 'BRL' });
        totalbasej.innerHTML = (somafgtsnormalj + somafgts13j + somafgtsferiasj).toLocaleString('pt-BR', { style: 'currency', currency: 'BRL' });
        fgtsrecolhidoj.innerHTML = somafgtsrecolhidoj.toLocaleString('pt-BR', { style: 'currency', currency: 'BRL' });
        fgts2j.innerHTML = subtotalfgts2.toLocaleString('pt-BR', { style: 'currency', currency: 'BRL' });
        fgts2totalj.innerHTML = totalfgts2.toLocaleString('pt-BR', { style: 'currency', currency: 'BRL' });

        totalFGTS.innerHTML = totalguia.toLocaleString('pt-BR', { style: 'currency', currency: 'BRL' });

      })

  }

