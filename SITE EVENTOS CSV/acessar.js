 const users = {
      admin: "111111111",     
      alex: "ecosampa@alex123",
      gustavo: "gustavo@ecosampa123",
      joao: "joao@2024ecosampa",
      fgts: "123",
      inss: "123",
      encargos: "123",
      grafico: "123"
    };

    document.getElementById("loginForm").addEventListener("submit", function (e) {
      e.preventDefault();

      const username = document.getElementById("username").value.trim();
      const password = document.getElementById("password").value.trim();
      const errorMsg = document.getElementById("error-msg");
      const loginBox = document.getElementById("loginBox");

      if (users[username] && users[username] === password) {
        errorMsg.textContent = "";
        loginBox.innerHTML = `
          <h2>Olá Sr. ${username.charAt(0).toUpperCase() + username.slice(1)}!</h2>
          <p style="margin-top: 1rem;">Preparando acesso...</p>`;

        setTimeout(() => {
          switch (username) {
            case "admin":
            case "alex":
              window.location.href = "menu_geral.html";
              break;
            case "joao":
              window.location.href = "contato.html";
              break;
            case "gustavo":
              window.location.href = "contato.html";
              break;
            case "encargos":
              window.location.href = "indexEncargos.html";
              break;
            case "fgts":
              window.location.href = "indexFgts.html";
              break;
            case "inss":
              window.location.href = "indexInss.html";
              break;
            case "grafico":
              window.location.href = "graficos.html";
              break;
          }
        }, 2000);
      } else {
        errorMsg.textContent = "Usuário ou senha incorretos.";
        document.getElementById("username").value = "";
        document.getElementById("password").value = "";
        return;
        loginBox.classList.add("shake");
        setTimeout(() => loginBox.classList.remove("shake"), 400);
      }
    
    });
