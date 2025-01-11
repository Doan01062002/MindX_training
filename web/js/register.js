const formRegister = document.getElementById("formRegister");
const emailElement = document.getElementById("login-email");
const passwordElement = document.getElementById("login-pass");
const repasswordElement = document.getElementById("relogin-pass");
const repasswordError = document.getElementById("repasswordError");

const userLocal = JSON.parse(localStorage.getItem("users")) || [];

formRegister.addEventListener("submit", function (e) {
  e.preventDefault();

  //kiểm tra lại mật khẩu

  if (passwordElement.value !== repasswordElement.value) {
    repasswordError.style.display = "block";
    repasswordError.innerHTML = "Mật khẩu không chính xác";
  }

  //gửi dữ liệu lên localstorage

  if (passwordElement.value === repasswordElement.value) {
    const user = {
      userId: Math.ceil(Math.random() * 1000000000),
      email: emailElement.value,
      password: passwordElement.value,
      name: "John Doe",
      avatar: "./img/people1.png",
    };

    userLocal.push(user);

    localStorage.setItem("users", JSON.stringify(userLocal));

    setTimeout(function () {
      window.location.href = "login.html";
    }, 1000);
  }
});
