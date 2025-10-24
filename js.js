// Função para criptografar
function criptografar() {
    const texto = document.getElementById("input").value;
    const chave = document.querySelector("#encryptKey").value;
    if (!texto || !chave) {
      alert("Por favor, insira o texto e a chave!");
      return;
    }
  
    const resultado = [...texto]
      .map((char, i) => String.fromCharCode(char.charCodeAt(0) ^ chave.charCodeAt(i % chave.length)))
      .join("");
  
    document.getElementById("output").value = btoa(resultado); // Codifica em Base64 para tornar legível
    document.getElementById("input").value = ""; // Limpa apenas o campo de entrada "Texto para criptografar"
  }
  
  // Função para descriptografar
  function descriptografar() {
    const codigo = document.getElementById("output").value;
    const chave = document.querySelector("#decryptKey").value;
    if (!codigo || !chave) {
      alert("Por favor, insira o código e a chave!");
      return;
    }
  
    try {
      const textoCodificado = atob(codigo); // Decodifica o Base64
      const resultado = [...textoCodificado]
        .map((char, i) => String.fromCharCode(char.charCodeAt(0) ^ chave.charCodeAt(i % chave.length)))
        .join("");
  
      document.getElementById("input").value = resultado;
    } catch (error) {
      alert("Erro ao descriptografar. Verifique o código e a chave.");
    }
  }
  