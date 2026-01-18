/** binder.js: 
 * Handles binder page interactions:
 * - Shows binder cards after loader to give the DOM time to load content fully
 * - Filters cards by rarity, alignment, and universe
 * - Flips cards on click to view front/back
 */

// Delay UI swap in the binder: hide loader after 2s, then reveal all shop cards
document.addEventListener("DOMContentLoaded", () => {
    setTimeout(() => {
        const loader = document.querySelector(".loader");
        const bindercards = document.querySelectorAll(".binder-card");
        loader.style.display = "none";
        bindercards.forEach(card => {
            card.style.display = "block";
        });
    }, 3000);

    // Filtering for the binder based on rarity, alignment and universe.
    // 'All' means no filter is applied for that category
    // Hides the card and its parent column so layout collapes properly.
    const cards = document.querySelectorAll(".binder-card");
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
});

// Grab article cards and toggle the flipped class on click, so that the cards will flip over and back again on all devices, and several can be flipped and compared at the same time. Css handles the flip animation.
const cards = document.querySelectorAll('article.binder-card');
cards.forEach(card => {
    card.addEventListener('click', () => {
        card.classList.toggle('flipped');
    });
});