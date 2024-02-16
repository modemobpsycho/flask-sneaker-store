(() => {
    "use strict";

    const forms = document.querySelectorAll(".needs-validation");

    Array.from(forms).forEach((form) => {
        form.addEventListener(
            "submit",
            (event) => {
                if (!form.checkValidity()) {
                    event.preventDefault();
                    event.stopPropagation();
                }

                form.classList.add("was-validated");
            },
            false
        );
    });
})();

document.addEventListener("DOMContentLoaded", function () {
    var flashMessages = document.querySelectorAll(
        ".flash-message[data-auto-dismiss]"
    );

    flashMessages.forEach(function (message) {
        var duration = 3000;
        setTimeout(function () {
            message.style.display = "none";
        }, duration);
    });
});

document.addEventListener("DOMContentLoaded", function () {
    var flashModal = document.getElementById("flash-modal");
    var flashModalMessage = document.querySelector(".flash-modal-message");
    var flashModalBackground = document.createElement("div");
    flashModalBackground.classList.add("flash-modal-background");

    function showFlashModal(message) {
        flashModalMessage.textContent = message;
        flashModal.style.display = "block";
        document.body.appendChild(flashModalBackground);
        setTimeout(hideFlashModal, 3000);
    }

    function hideFlashModal() {
        flashModal.style.display = "none";
        flashModalBackground.remove();
    }

    function checkFlashDisplayed() {
        return new Promise(function (resolve) {
            var isFlashDisplayed = localStorage.getItem("flashDisplayed");
            resolve(isFlashDisplayed === "true");
        });
    }

    function setFlashDisplayed() {
        localStorage.setItem("flashDisplayed", "true");
    }

    checkFlashDisplayed().then(function (isDisplayed) {
        if (isDisplayed) {
            showFlashModal();
        } else {
            setFlashDisplayed();
        }
    });
});

window.addEventListener("scroll", function () {
    document
        .getElementById("header-nav")
        .classList.toggle("headernav-scroll", window.scrollY > 135);
});

const offcanvasCartEl = document.getElementById("offcanvasCart");
const offcanvasCart = new bootstrap.Offcanvas(offcanvasCartEl);

document.getElementById("cart-open").addEventListener("click", (e) => {
    e.preventDefault();
    offcanvasCart.toggle();
});

document.querySelectorAll(".closecart").forEach((item) => {
    item.addEventListener("click", (e) => {
        e.preventDefault();
        offcanvasCart.hide();
        let href = item.dataset.href;
        document.getElementById(href).scrollIntoView();
    });
});

$(document).ready(function () {
    $(".owl-carousel-full").owlCarousel({
        margin: 20,
        responsive: {
            0: {
                items: 1,
            },
            500: {
                items: 2,
            },
            700: {
                items: 3,
            },
            1000: {
                items: 4,
            },
        },
    });
});
