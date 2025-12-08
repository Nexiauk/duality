
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
    const selects = document.querySelectorAll(".filter")

    const rarity = document.getElementById("rarities")
    const alignment = document.getElementById("alignment")
    const universe = document.getElementById("universe")

    selects.forEach((select) => {
        select.addEventListener("change", () => {
           let selectedRarity = rarity.value
            let selectedAlignment = alignment.value
            let selectedUniverse = universe.value

            cards.forEach((card) => {
                const cardCol = card.parentNode

                if (
                    (card.dataset.rarity == selectedRarity || selectedRarity === "all")&&
                    (card.dataset.alignment == selectedAlignment || selectedAlignment === "all")&&
                    (card.dataset.universe == selectedUniverse || selectedUniverse === "all")
                ) {
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

})
