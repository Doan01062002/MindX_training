const formLogin = document.getElementById("formLogin");
const emailElement = document.getElementById("login-email");
const passwordElement = document.getElementById("login-pass");

formLogin.addEventListener("submit", function (e) {
  e.preventDefault();

  const userLocal = JSON.parse(localStorage.getItem("users")) || [];

  const findUser = userLocal.find(
    (user) =>
      user.email === emailElement.value &&
      user.password === passwordElement.value
  );

  if (!findUser) {
    alert("Email hoặc mật khẩu không chính xác");
  } else {
    setTimeout(function () {
      window.location.href = "index.html";
    }, 1000);
  }
});
