// Функция для фильтрации файлов
document.addEventListener('DOMContentLoaded', function () {
    const checkboxes = document.querySelectorAll('.filter-type');
    const rows = document.querySelectorAll('tbody tr');

    checkboxes.forEach(checkbox => {
        checkbox.addEventListener('change', filterTable);
    });

    function filterTable() {
        const selectedTypes = Array.from(checkboxes)
            .filter(checkbox => checkbox.checked)
            .map(checkbox => checkbox.value);

        // Если не выбраны типы, скрываем все строки
        if (selectedTypes.length === 0) {
            rows.forEach(row => {
                row.style.display = 'none';
            });
        } else {
            rows.forEach(row => {
                const rowType = row.querySelector('td:nth-child(3)').textContent.trim().toLowerCase();
                if (selectedTypes.includes(rowType)) {
                    row.style.display = '';
                } else {
                    row.style.display = 'none';
                }
            });
        }
    }
});
