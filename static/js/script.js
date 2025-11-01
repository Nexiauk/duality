document.addEventListener("DOMContentLoaded", () => {
    setTimeout(() => {
        const loaders = document.querySelectorAll(".loader");
        const shopcards = document.querySelectorAll(".shop-card");

        loaders.forEach((loader, item) => {
            loader.style.display = "none";
            shopcards[item].style.display = "block";
        })

    }, 2000)




})