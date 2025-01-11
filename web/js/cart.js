document.addEventListener("DOMContentLoaded", () => {
  const cartTableBody = document.querySelector("#cart tbody");
  const subtotalElement = document.querySelector(
    "#subtotal table tr:nth-child(1) td:nth-child(2)"
  );
  const totalElement = document.querySelector(
    "#subtotal table tr:nth-child(3) td:nth-child(2)"
  );

  // Lấy giỏ hàng từ localStorage
  let cart = JSON.parse(localStorage.getItem("cart")) || [];

  // Hiển thị giỏ hàng
  const renderCart = () => {
    cartTableBody.innerHTML = "";
    let cartSubtotal = 0;

    cart.forEach((item, index) => {
      const row = document.createElement("tr");

      row.innerHTML = `
          <td><a href="#" class="remove-item" data-index="${index}"><i class="fa-regular fa-circle-xmark"></i></a></td>
          <td><img src="${
            item.image
          }" alt="" style="width: 50px; height: 50px;"></td>
          <td>${item.name}</td>
          <td>${item.price}</td>
          <td><input type="number" class="quantity" data-index="${index}" value="${
        item.quantity
      }" min="1" style="width: 60px;"></td>
          <td>${(parseFloat(item.price.slice(1)) * item.quantity).toFixed(
            2
          )}</td>
        `;
      cartTableBody.appendChild(row);

      // Tính tổng phụ
      cartSubtotal += parseFloat(item.price.slice(1)) * item.quantity;
    });

    subtotalElement.textContent = `$${cartSubtotal.toFixed(2)}`;
    totalElement.textContent = `$${cartSubtotal.toFixed(2)}`;
  };

  // Xóa sản phẩm
  cartTableBody.addEventListener("click", (e) => {
    if (e.target.closest(".remove-item")) {
      const index = e.target.closest(".remove-item").dataset.index;
      cart.splice(index, 1);
      localStorage.setItem("cart", JSON.stringify(cart));
      renderCart();
    }
  });

  // Cập nhật số lượng
  cartTableBody.addEventListener("input", (e) => {
    if (e.target.classList.contains("quantity")) {
      const index = e.target.dataset.index;
      const newQuantity = parseInt(e.target.value, 10);

      if (newQuantity > 0) {
        cart[index].quantity = newQuantity;
        localStorage.setItem("cart", JSON.stringify(cart));
        renderCart();
      }
    }
  });

  // Áp dụng mã giảm giá
  document.querySelector("#coupon button").addEventListener("click", () => {
    const couponInput = document.querySelector("#coupon input");
    const couponCode = couponInput.value.trim();

    if (couponCode === "DISCOUNT10") {
      const currentTotal = parseFloat(totalElement.textContent.slice(1));
      const discountedTotal = (currentTotal * 0.9).toFixed(2);
      totalElement.textContent = `$${discountedTotal}`;
      alert("Mã giảm giá đã được áp dụng!");
    } else {
      alert("Mã giảm giá không hợp lệ!");
    }
  });

  renderCart();
});
