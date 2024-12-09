function calcule() {

    const nota = parseFloat(window.document.querySelector("#nota").value);
    const faltas = parseInt(window.document.querySelector("#faltas").value);

    let conceito;
    
    if (faltas <= 10) {
        if (nota < 60) {
            conceito = "C";
        } else if (nota >= 60 && nota < 85) {
            conceito = "B";
        } else {
            conceito = "A";
        }
    } else {
        if (nota < 60) {
            conceito = "D";
        } else if (nota >= 60 && nota < 85) {
            conceito = "C";
        } else {
            conceito = "B";
        }
    }
    window.document.querySelector("#resultado").textContent = `Seu conceito é ${conceito}.`;
}
