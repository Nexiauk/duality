
/**
 * shop.js
 * Handles shop page interactions:
 * - Shows shop cards after loader (waits 3 seconds for DOM/content)
 * - Filters cards by rarity, alignment, and universe
 * - Handles "cancel" buttons to navigate back in browser history
 */

// Delay UI swap in the shop and on the card-detail template: hide loader after 3s, then reveal all cards
document.addEventListener("DOMContentLoaded", () => {
    setTimeout(() => {
        const loader = document.querySelector(".loader");
        const shopcards = document.querySelectorAll(".shop-card");
        loader.style.display = "none";
        shopcards.forEach(card => {
            card.style.display = "block";
        });

    }, 3000);
    
    // Filtering for the shop based on rarity, alignment and universe.
    // 'All' means no filter is applied for that category
    // Hides the card and its parent column so layout collapes properly.
    const cards = document.querySelectorAll(".shop-card");
    const selects = document.querySelectorAll(".filter");
    const rarity = document.getElementById("rarities");
    const alignment = document.getElementById("alignment");
    const universe = document.getElementById("universe");

    selects.forEach((select) => {
        select.addEventListener("change", () => {
            let selectedRarity = rarity.value;
            let selectedAlignment = alignment.value;
            let selectedUniverse = universe.value;
            cards.forEach((card) => {
                const cardCol = card.parentNode;
                if (
                    (card.dataset.rarity == selectedRarity || selectedRarity === "all") &&
                    (card.dataset.alignment == selectedAlignment || selectedAlignment === "all") &&
                    (card.dataset.universe == selectedUniverse || selectedUniverse === "all")
                ) {
                    card.style.display = "block";
                    cardCol.classList.remove("d-none");
                }
                else {
                    card.style.display = "none";
                    cardCol.classList.add("d-none");
                }

            });
        });
    });
    // A back button that navigates the browser history: acts as a cancel function on the card detail page.
    document.querySelectorAll(".cancel").forEach(button => {
        button.addEventListener("click", (e) => {
            e.preventDefault();
            history.back();
        });
    });
});
