
    var ticketPriceElement = document.getElementById("ticketPrice");
    var totalPriceElement = document.getElementById("totalPrice");
    var quantityInput = document.querySelector('input[name="quantity"]');

    // Sayfa yüklendiğinde toplam fiyatı güncelle
    updateTotalPrice();

    function updateTotalPrice() {
        var ticketPrice = parseFloat(ticketPriceElement.innerText.replace("$", ""));
        var quantity = parseInt(quantityInput.value) || 0; // Başlangıç değeri belirle ve NaN durumunu kontrol et
        var totalPrice = ticketPrice * quantity;
        totalPriceElement.innerText = "Total: $" + totalPrice.toFixed(2);
    }

    function increment() {
        quantityInput.stepUp();
        updateTotalPrice();
    }

    function decrement() {
        quantityInput.stepDown();
        updateTotalPrice();
    }

    // Input değeri değiştiğinde toplam fiyatı güncelle
    quantityInput.addEventListener('input', updateTotalPrice);