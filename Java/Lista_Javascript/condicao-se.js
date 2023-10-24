let num = 18;

if (num >= 0 && num <= 10) {
    console.log('número entre zero e dez');
} else if (num > 10 && num <= 20) {
    console.log(`número entre dez e vinte  = ${num}`)
} else if (num > 20 && num <= 30) {
    console.log('número entre vinte e trinta');
} else {
    console.log('outro número');
}
console.log(`_----------------------------numero certo é ${num}`)