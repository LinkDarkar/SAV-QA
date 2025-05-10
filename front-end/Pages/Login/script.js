function loginSubmit(event) {
    event.preventDefault();

    const correctPassword = "password";
    const inputPassword = document.getElementById("password").value;

    if (inputPassword === correctPassword) {
    console.log("Success!")
    window.location.href = "../FilesList/filesList.html";
    return true;
    } else {
    console.log("Incorrect!")
    alert("Contraseña incorrecta");
    return false;
    }
}