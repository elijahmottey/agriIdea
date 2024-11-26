document.addEventListener("DOMContentLoaded", () => {
    const openModalBtn = document.getElementById("openModalBtn");
    const openModalBtnMobile = document.getElementById("openModalBtnMobile");
    const ideaModal = document.getElementById("ideaModal");
    const ideaModalOverlay = document.getElementById("ideaModalOverlay");
    const closeModalBtn = document.getElementById("closeModalBtn");

    // Show the modal and overlay
    const openModal = () => {
        ideaModal.style.display = "flex";
        ideaModalOverlay.style.display = "block";
    };

    // Hide the modal and overlay
    const closeModal = () => {
        ideaModal.style.display = "none";
        ideaModalOverlay.style.display = "none";
    };

    // Attach event listeners to buttons
    openModalBtn.addEventListener("click", openModal);
    openModalBtnMobile.addEventListener("click", openModal);
    closeModalBtn.addEventListener("click", closeModal);
    ideaModalOverlay.addEventListener("click", closeModal);
});
