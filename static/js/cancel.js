/**
 * cancel.js
 * Handles shop page interactions:
 * - Prevents the default action of the cancel button
 * - Triggers moving the browser to move back one page in the history session
 */
 
 // A back button that navigates the browser history: acts as a cancel function on the card detail page.
    document.querySelectorAll(".cancel").forEach(button => {
        button.addEventListener("click", (e) => {
            e.preventDefault();
            history.back();
        });
    });