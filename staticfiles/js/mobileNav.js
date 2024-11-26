// JavaScript to toggle the mobile menu and close when clicking outside
document.addEventListener('DOMContentLoaded', function () {
    const menuBtn = document.getElementById('menu-btn');
    const mobileMenu = document.getElementById('mobile-menu');
    const body = document.body;

    // Toggle mobile menu visibility
    menuBtn.addEventListener('click', function (e) {
        e.stopPropagation(); // Prevent click event from reaching the body
        mobileMenu.classList.toggle('hidden');
    });

    // Close the mobile menu when clicking outside of it
    body.addEventListener('click', function () {
        if (!mobileMenu.classList.contains('hidden')) {
            mobileMenu.classList.add('hidden');
        }
    });

    // Prevent clicks inside the mobile menu from closing it
    mobileMenu.addEventListener('click', function (e) {
        e.stopPropagation();
    });
});