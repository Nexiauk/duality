document.addEventListener("DOMContentLoaded", () => {
    document.querySelectorAll(".cancel").forEach(button => {
        button.addEventListener("click", (e) => {
            e.preventDefault();
            history.back();
        });
    });
});