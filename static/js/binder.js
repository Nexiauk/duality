document.addEventListener("DOMContentLoaded", () => {
    setTimeout(() => {
        const loader = document.querySelector(".loader");
        const bindercards = document.querySelectorAll(".binder-card");
        loader.style.display = "none";
        bindercards.forEach(card => {
            card.style.display = "block";
        })
    }, 3000)
})