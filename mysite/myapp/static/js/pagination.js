
$('#okf10').on('click',function(){
    const cv_list_records = JSON.parse('{{ cv_list_records | safe }}');


// const cv_list_records = JSON.parse('{{ cv_list_records | safe }}');

const itemsPerPage = 10;
let currentPage = 1;

// Function to render table rows for the current page
function renderTableRows(data) {
    const tableBody = document.querySelector('.table-list tbody');
    tableBody.innerHTML = '';

    const startIndex = (currentPage - 1) * itemsPerPage;
    const endIndex = startIndex + itemsPerPage;

    for (let i = startIndex; i < endIndex && i < data.length; i++) {
        // Create table rows as you did before
        // ...
    }
}

// Function to update the current page number display
function updateCurrentPageDisplay() {
    const currentPageSpan = document.getElementById('current-page');
    currentPageSpan.textContent = currentPage;
}

// Function to handle "Next" button click
function handleNextClick() {
    const totalPages = Math.ceil(cv_list_records.length / itemsPerPage);
    currentPage = Math.min(currentPage + 1, totalPages);
    renderTableRows(cv_list_records);
    updateCurrentPageDisplay();
}

// Function to handle "Previous" button click
function handlePrevClick() {
    currentPage = Math.max(currentPage - 1, 1);
    renderTableRows(cv_list_records);
    updateCurrentPageDisplay();
}

// Attach click event listeners to the "Next" and "Previous" buttons
document.getElementById('next-btn').addEventListener('click', handleNextClick);
document.getElementById('prev-btn').addEventListener('click', handlePrevClick);

// Initial rendering of the table and current page display
renderTableRows(cv_list_records);
updateCurrentPageDisplay();
});