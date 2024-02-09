(() => {
    'use strict'

    const forms = document.querySelectorAll('.needs-validation')

    Array.from(forms).forEach(form => {
        form.addEventListener('submit', event => {
            if (!form.checkValidity()) {
                event.preventDefault()
                event.stopPropagation()
            }

            form.classList.add('was-validated')
        }, false)
    })
})();

window.addEventListener('scroll', function () {
    document.getElementById('header-nav').classList.toggle('headernav-scroll', window.scrollY > 135);
});

const offcanvasCartEl = document.getElementById('offcanvasCart');
const offcanvasCart = new bootstrap.Offcanvas(offcanvasCartEl);

document.getElementById('cart-open').addEventListener('click', (e) => {
    e.preventDefault();
    offcanvasCart.toggle();
});

document.querySelectorAll('.closecart').forEach(item => {
    item.addEventListener('click', (e) => {
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
                items: 1
            },
            500: {
                items: 2
            },
            700: {
                items: 3
            },
            1000: {
                items: 4
            }
        }
    });
});