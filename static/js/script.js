// After 2 seconds, hides the loaders and displays the cards.
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