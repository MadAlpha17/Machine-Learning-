document.addEventListener("DOMContentLoaded", function() {
    var anxietyInput = document.getElementById("anxietyInput");
    var selfEsteemInput = document.getElementById("selfEsteemInput");

    anxietyInput.addEventListener("input", function() {
        var inputValue = parseInt(anxietyInput.value);
        if (isNaN(inputValue) || inputValue < 0 || inputValue > 21) {
            anxietyInput.setCustomValidity("Please enter a number between 0 and 21.");
        } else {
            anxietyInput.setCustomValidity("");
        }
    });

    selfEsteemInput.addEventListener("input", function() {
        var inputValue = parseInt(selfEsteemInput.value);
        if (isNaN(inputValue) || inputValue < 0 || inputValue > 30) {
            selfEsteemInput.setCustomValidity("Please enter a number between 0 and 30.");
        } else {
            selfEsteemInput.setCustomValidity("");
        }
    });

    depressionInput.addEventListener("input", function() {
        var inputValue = parseInt(depressionInput.value);
        if (isNaN(inputValue) || inputValue < 0 || inputValue > 27) {
            depressionInput.setCustomValidity("Please enter a number between 0 and 27.");
        } else {
            depressionInput.setCustomValidity("");
        }
    });
});

