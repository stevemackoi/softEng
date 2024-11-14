// Wait for the DOM to fully load before running scripts
document.addEventListener('DOMContentLoaded', () => {

    // BOOK A VACATION BUTTON
    const vacationButton = document.querySelector('#vacationButton');
    const bookingModal = document.querySelector('#bookingModal'); // Ensure this modal exists
    const closeModalButton = document.querySelector('#closeModal');

    // Show modal on "Book a Vacation Now" button click
    if (vacationButton) {
        vacationButton.addEventListener('click', (event) => {
            event.preventDefault(); // Prevent any default link behavior if it's an <a> element
            if (bookingModal) {
                bookingModal.style.display = 'block';
                document.body.style.overflow = 'hidden'; // Prevent page scroll when modal is open
            } else {
                console.error("Booking modal not found. Please make sure it exists in your HTML.");
            }
        });
    }

    // Close modal when the close button is clicked
    if (closeModalButton) {
        closeModalButton.addEventListener('click', () => {
            bookingModal.style.display = 'none';
            document.body.style.overflow = ''; // Re-enable page scroll
        });
    }

    // Close modal if the user clicks outside of it
    window.addEventListener('click', (event) => {
        if (event.target === bookingModal) {
            bookingModal.style.display = 'none';
            document.body.style.overflow = '';
        }
    });

    // SMOOTH SCROLL FOR NAV LINKS
    const navLinks = document.querySelectorAll('.navbar a');
    navLinks.forEach(link => {
        link.addEventListener('click', (event) => {
            const targetId = link.getAttribute('href');
            if (targetId.startsWith('#')) {
                event.preventDefault();
                document.querySelector(targetId).scrollIntoView({
                    behavior: 'smooth'
                });
            }
        });
    });

    // TOGGLE NAVBAR ON SMALL SCREENS
    const navbarToggler = document.querySelector('.navbar-toggler');
    const navbarResponsive = document.querySelector('#navbarResponsive');

    if (navbarToggler && navbarResponsive) {
        navbarToggler.addEventListener('click', () => {
            navbarResponsive.classList.toggle('show'); // Toggles visibility on small screens
        });
    }

    // ADD ACTIVE CLASS TO NAV LINKS BASED ON SCROLL POSITION
    const sections = document.querySelectorAll('section');
    const navItems = document.querySelectorAll('.navbar-nav .nav-link');

    window.addEventListener('scroll', () => {
        let currentSection = '';
        
        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            if (pageYOffset >= sectionTop - 50) { // 50px offset for navbar height
                currentSection = section.getAttribute('id');
            }
        });

        navItems.forEach(item => {
            item.classList.remove('active');
            if (item.getAttribute('href') === `#${currentSection}`) {
                item.classList.add('active');
            }
        });
    });

    // LOG CONSOLE MESSAGE TO INDICATE SCRIPTS ARE LOADED SUCCESSFULLY
    console.log("Taniti Island scripts loaded successfully.");

});
