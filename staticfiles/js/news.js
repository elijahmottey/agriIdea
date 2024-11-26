document.addEventListener('DOMContentLoaded', function () {
    const pageSizeSelector = document.getElementById('page_size');
    const prevPageButton = document.getElementById('prev_page');
    const nextPageButton = document.getElementById('next_page');

    const currentPage = parseInt('{{ current_page }}');
    const totalPages = parseInt('{{ total_pages }}');
    const pageSize = parseInt('{{ page_size }}');

    // Redirect with new page size on selection change
    pageSizeSelector.addEventListener('change', function () {
        const selectedPageSize = pageSizeSelector.value;
        window.location.href = `?page=1&page_size=${selectedPageSize}`;
    });

    // Navigate to the previous page
    prevPageButton.addEventListener('click', function () {
        if (currentPage > 1) {
            window.location.href = `?page=${currentPage - 1}&page_size=${pageSize}`;
        }
    });

    // Navigate to the next page
    nextPageButton.addEventListener('click', function () {
        if (currentPage < totalPages) {
            window.location.href = `?page=${currentPage + 1}&page_size=${pageSize}`;
        }
    });
});
