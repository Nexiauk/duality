// Bind all cancel buttons to go back, instead of following their default link
document.addEventListener("DOMContentLoaded", () => {
    document.querySelectorAll(".cancel").forEach(button => {
        button.addEventListener("click", (e) => {
            e.preventDefault();
            history.back();
            console.log("Hello")
        });
    });
});