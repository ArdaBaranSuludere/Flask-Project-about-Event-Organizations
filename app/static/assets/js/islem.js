// quantity.js

// Başlangıçta sayıyı 1 olarak ayarla
var quantity = 1;

// Sayfa yüklendiğinde çalışacak olan fonksiyon
document.addEventListener("DOMContentLoaded", function () {
    // Başlangıçta total fiyatı güncelle
    updateTotalPrice();
});

function increment() {
    // Sayı 10'dan küçükse ve toplam fiyat 2000'den küçükse sayıyı artır
    if (quantity < 10) {
        quantity++;
        updateTotalPrice();
    }
}

function decrement() {
    // Sayıyı azalt, minimum değer 1
    if (quantity > 1) {
        quantity--;
        updateTotalPrice();
    }
}

function updateTotalPrice() {
    // H4 başlığını güncelle
    var totalElement = document.getElementById("totalPrice");
    var totalPrice = quantity * 210;
    totalElement.innerText = "Total: $" + totalPrice.toFixed(2);
}
