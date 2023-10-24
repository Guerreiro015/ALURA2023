// O reduce consegue calclular as medias


const sala1 = [7, 8, 8, 7, 10, 6.5, 4, 10, 7];
const sala2 = [6, 5, 8, 9, 5, 6];
const sala3 = [7, 3.5, 8, 9.5];

function calculaMedia(notasDaSala) {

    const somaDasNotas = notasDaSala.reduce((acc, nota) => acc + nota, 0); //important colocar o zero para comecar do zero

    const media = somaDasNotas / notasDaSala.length;

    return media;
}

console.log(`A média da sala de JavaScript é ${calculaMedia(sala1)}`);
console.log(`A média da sala de Java é ${calculaMedia(sala2)}`);
console.log(`A média da sala de Python é ${calculaMedia(sala3)}`);