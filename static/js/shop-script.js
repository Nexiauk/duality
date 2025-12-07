// Delay UI swap in the shop: hide loader after 2s, then reveal all shop cards
document.addEventListener("DOMContentLoaded", () => {
    setTimeout(() => {
        const loader = document.querySelector(".loader");
        const shopcards = document.querySelectorAll(".shop-card");
        loader.style.display = "none";
        shopcards.forEach(card => {
            card.style.display = "block";
        })

    }, 2000)
})

