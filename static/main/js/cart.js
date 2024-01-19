

document.querySelectorAll(".add-to-cart-button").forEach((button) =>
    button.addEventListener("mouseover", (e) => {
        if (!button.classList.contains("loading")) {
            button.classList.add("loading");
            setTimeout(() => button.classList.remove("loading"), 3700);
        }

    })
);