// Add event listener to buttons
document.addEventListener("DOMContentLoaded", function() {
    const buttons = document.querySelectorAll("button");
    buttons.forEach(function(button) {
        button.addEventListener("click", function() {
            alert("Thank you for taking action!");
        });
    });
});