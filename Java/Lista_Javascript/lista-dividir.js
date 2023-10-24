let nomes = ['João', 'Juliana', 'Ana', 'Caio', 'Lara', 'Marjorie', 
'Guilherme', 'Aline', 'Fabiana', 'Andre', 'Carlos', 'Paulo', 'Bia', 'Vivian', 'Isabela', 'Vinícius', 'Renan', 'Renata', 'Daisy', 'Camilo']
console.log(nomes.length)

nor = nomes.slice(0,10)// dividir do 10 ao 20
nor1 = nomes.slice(10,20)// diidir do 0 ao 10
nor2 = nomes.slice(0) // Se não colocar o 2º paramêntro e separa o restante;
nor3 = nomes.slice(0,nomes.length/2) // divindo pela metade da lista

console.log(nor)
console.log(nor1)
console.log(nor2)
console.log(nor3)