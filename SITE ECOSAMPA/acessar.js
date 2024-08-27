var usuario = document.getElementById("menu")
var senha = document.getElementById('senha')
var usuario_valor = usuario.value


function validar() {
  
  if (usuario.value === 'wilson' && senha.value === "wilson@12345ecosampa") {
    localStorage.setItem('Apelido', 'Olá Wilson');
    return window.location.href = './relatorio_geral.html'; // Página após o login   
  }

  else if (usuario.value === 'wilson' && senha.value === "111111111") {
    localStorage.setItem('Apelido', 'Olá Wilson');
    return window.location.href = './relatorio_geral.html'; // Página após o login   
  }

  else if (usuario.value === 'alex' && senha.value === "ecosampa@alex123") {
    localStorage.setItem('Apelido', 'Olá, Alex');
    return window.location.href = 'relatorio_geral.html'; // Página após o login   
  }

  else if (usuario.value === 'alex' && senha.value === "111111111") {
    localStorage.setItem('Apelido', 'Olá, Alex');
    return window.location.href = 'relatorio_geral.html'; // Página após o login   
  }


  else if (usuario.value === 'gustavo' && senha.value === "gustavo@ecosampa123") {
    localStorage.setItem('Apelido', 'Olá, Gustavo');
    return window.location.href = 'relatorio_gustavo.html'; // Página após o login
  }

  else if (usuario.value === 'gustavo' && senha.value === "111111111") {
    localStorage.setItem('Apelido', 'Olá, Gustavo');
    return window.location.href = 'relatorio_gustavo.html'; // Página após o login
  }

  else if (usuario.value === 'joao' && senha.value === "joao@2024ecosampa") {
    localStorage.setItem('Apelido', 'Olá, João Sales');
    return window.location.href = 'relatorio_joao.html'; // Página após o login

  }

  else if (usuario.value === 'joao' && senha.value === "111111111") {
    localStorage.setItem('Apelido', 'Olá, João Sales');
    return window.location.href = 'relatorio_joao.html'; // Página após o login

  }
  else {
    usuario.value = ""
    senha.value = ""
    alert('Gerencia não Encontrada ou senha inválida')
  }


}

function alertar() {
  alert('Esta funcionalidade ainda não esta disponível, por favor procure o Antonio do DP')
}
