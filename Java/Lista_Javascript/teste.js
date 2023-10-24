const cor = ["alt seta pra cima ou pra baixo para mover um linha", "f8 - mostra onde esta o proximo erro", "alt.shift.f para organizar o", "f12 para saber onde a variavel foi declarada pela primerira vez", "ctrl,shift,K para apagar uma limha"]
cor.push('tetstando')
console.log(cor);

const lista = [];
lista.push(1);
lista.push(2);
function mostra() {
    console.log(lista[0] + lista[1]);
    console.log(lista);

}

for (let i = 0; i < cor.length; i++) {
    console.log(cor[i]);

}
mostra()

