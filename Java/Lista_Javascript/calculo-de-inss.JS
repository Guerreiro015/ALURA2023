const salariobruto = 9000;
const valorfaltas = 0;
const depe = 0;
const pensao = 0;
let inss = 0;
const salarioliquido = (salariobruto - valorfaltas);

let aliquotainss = [7.5, 9, 12, 14];

let deducaoinss = [0, 19.8, 96.94, 174.08];

let basesalario = [1.320, 2571.29, 3856.94, 7507.49];

let baseir = [2112.01, 2826.66, 3751.06, 4664.68, 2000000];

let aliquotair = [7.5, 15, 22.5, 27.5];

let parceladeduzir = [158.4, 370.4, 651.73, 884.96]

let deducaodependenteir = 189.59;

let valordeducaoir = deducaodependenteir * depe;

// Cálculo do INSS

for (i = 0; i < aliquotainss.length; i++) {

    if (salarioliquido > basesalario[3]) {
        inss = 876.95;
        break;
    }
    else {
        if (salarioliquido <= basesalario[i]) {
            inss = ((salarioliquido * aliquotainss[i])) / 100 - deducaoinss[i]


            break;
        }
    }
}
console.log(`O valor da base de cálculo do INSS e ............:  ${salarioliquido}`);
console.log(`O Valor do INSS será é...........................:  ${inss} `);

// Cálculo de Imposto de Renda
let baseDeducao = 0
let deducaoSimplificada = 528;
if ((pensao + inss + valordeducaoir) < deducaoSimplificada){
    baseDeducao = deducaoSimplificada;
}
else{
    baseDeducao = (pensao + inss + valordeducaoir);
}

let baserenda = salarioliquido - baseDeducao;

for (i = 0; i < parceladeduzir.length; i++) {

    if (baserenda < baseir[i]) {
        impostoderenda = 0
        break;
    }
    else {
        if (baserenda > baseir[i] && baserenda < baseir[i + 1]) {
            impostoderenda = ((baserenda * aliquotair[i]) / 100) - parceladeduzir[i]
            break;
        }
    }
}
console.log(`Neste caso o Valor da base de Imposto de Renda é..:  ${baserenda} `)

console.log(`O Valor do Imposto de Renda é.                   .:  ${impostoderenda} `)

console.log(baseir[i])
console.log(parceladeduzir[i])
console.log(aliquotair[i])


