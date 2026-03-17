 const users = {
  admin: "111111111",     
  alex: "ecosampa@alex123",
  vandecir: "vandecir@123",
  fabio: "fabio@2025ecosampa",
  renato: "renato@2025ecosampa",
  fgts: "123",
  inss: "123",
  encargos: "123",
  grafico: "123"
};

// Certifique-se de que o ID 'loginForm' foi adicionado à tag <form> no HTML
document.getElementById("loginForm").addEventListener("submit", function (e) {
  e.preventDefault();

  const username = document.getElementById("username").value.trim();
  const password = document.getElementById("password").value.trim();
  const errorMsg = document.getElementById("error-msg");
  const loginBox = document.getElementById("loginBox"); // Precisa do ID no HTML

  if (users[username] && users[username] === password) {
    errorMsg.textContent = "";
    loginBox.innerHTML = `
      <div style="padding: 40px; text-align: center;">
        <h2>Olá Sr. ${username.charAt(0).toUpperCase() + username.slice(1)}!</h2>
        <p style="margin-top: 1rem;">Preparando acesso...</p>
      </div>`;

    setTimeout(() => {
      const destinos = {
        admin: "menu_geral.html",
        alex: "menu_geral.html",
        vandecir: "menu_vandecir.html",
        fabio: "menu_fabio.html",
        renato: "menu_renato.html",
        encargos: "indexEncargos.html",
        fgts: "indexFgts.html",
        inss: "indexInss.html",
        grafico: "graficos.html"
      };
      window.location.href = destinos[username];
    }, 2000);

  } else {
    errorMsg.textContent = "Usuário ou senha incorretos.";
    document.getElementById("username").value = "";
    document.getElementById("password").value = "";
    
    // Removido o 'return' que estava aqui impedindo o shake
    loginBox.classList.add("shake");
    setTimeout(() => loginBox.classList.remove("shake"), 400);
  }
});
