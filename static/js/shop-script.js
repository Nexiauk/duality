
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
    // Filtering for the shop
    const cards = document.querySelectorAll(".shop-card")
    const Rarity = document.getElementById("rarities")
    Rarity.addEventListener("change", () => {
        let selectedRarity = chosenRarity.value
        cards.forEach((card) => {
            const cardCol = card.parentNode
            const dataTags = card.dataset.cardType.toLowerCase()
            const datatagArray = dataTags.split(" ")
            if (datatagArray.includes(selectedRarity) || selectedRarity === "all") {
                card.style.display = "block"
                cardCol.classList.remove("d-none")
            }
            else {
                card.style.display = "none"
                cardCol.classList.add("d-none")
            }

        })
    })
})
