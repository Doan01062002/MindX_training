document.addEventListener("DOMContentLoaded", () => {
  const cartButtons = document.querySelectorAll("#cart");
  const cartBadge = document.querySelector(".badge");

  // Giỏ hàng trong localStorage
  const cart = JSON.parse(localStorage.getItem("cart")) || [];

  // Cập nhật số lượng trên badge
  const updateCartBadge = () => {
    const totalItems = cart.reduce((sum, item) => sum + item.quantity, 0);
    cartBadge.textContent = totalItems > 99 ? "99+" : totalItems;
  };

  // Xử lý thêm sản phẩm vào giỏ hàng
  const addToCart = (product) => {
    const existingProduct = cart.find((item) => item.name === product.name);
    if (existingProduct) {
      existingProduct.quantity += 1;
    } else {
      cart.push({ ...product, quantity: 1 });
    }
    localStorage.setItem("cart", JSON.stringify(cart));
    updateCartBadge();
  };

  cartButtons.forEach((button, index) => {
    button.addEventListener("click", () => {
      const productElement = button.parentElement;
      const product = {
        name: productElement.querySelector("h5").textContent.trim(),
        price: productElement.querySelector("h4").textContent.trim(),
        image: productElement.querySelector("img").src,
      };
      addToCart(product);
      alert(`${product.name} đã được thêm vào giỏ hàng!`);
    });
  });

  updateCartBadge();
});

// Các phần tử DOM
const formLogin = document.getElementById("formLogin");
const emailElement = document.getElementById("login-email");
const passwordElement = document.getElementById("login-pass");
const userInfoElement = document.getElementById("user-info");

// Hàm hiển thị ảnh đại diện hoặc nút đăng nhập
function displayUserAvatar(user) {
  if (user) {
    userInfoElement.innerHTML = `
            <div class="dropdown">
                <img
                    src="${
                      user.avatar ||
                      "https://png.pngtree.com/png-clipart/20210608/ourlarge/pngtree-dark-gray-simple-avatar-png-image_3418404.jpg"
                    }"
                    alt="User Avatar"
                    class="avatar"
                    id="dropdownMenuButton"
                    data-bs-toggle="dropdown"
                    aria-expanded="false"
                    style="width: 40px; height: 40px; border-radius: 50%; cursor: pointer;"
                />
                <ul class="dropdown-menu" aria-labelledby="dropdownMenuButton">
                    <li><a class="dropdown-item" href="#">Hồ sơ</a></li>
                    <li><button class="dropdown-item" id="logout-button">Đăng xuất</button></li>
                </ul>
            </div>
        `;
    document
      .getElementById("logout-button")
      .addEventListener("click", logoutUser);
  } else {
    userInfoElement.innerHTML = `
            <button class="normal"><a style="text-decoration: none;" href="./login.html">Đăng nhập</a></button>
            <button class="normal"><a style="text-decoration: none;" href="./register.html">Đăng ký</a></button>
        `;
  }
}
// Hàm xử lý đăng xuất
function logoutUser() {
  localStorage.removeItem("users");
  window.location.href = "login.html";
}

// Kiểm tra trạng thái đăng nhập khi tải trang
window.addEventListener("load", function () {
  const loggedInUser = JSON.parse(localStorage.getItem("users"));
  displayUserAvatar(loggedInUser);
});

const searchInput = document.querySelector('input[type="search"]');
const productList = document.querySelector("#product-list");

searchInput.addEventListener("input", function () {
  const query = searchInput.value.toLowerCase();

  const products = productList.querySelectorAll(".pro");

  products.forEach((product) => {
    const productName = product.getAttribute("data-name").toLowerCase();

    if (productName.includes(query)) {
      product.style.display = "block";
    } else {
      product.style.display = "none";
    }
  });
});
