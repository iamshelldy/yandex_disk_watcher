// Обработчик для кнопки скачивания
document.getElementById("downloadSelected").addEventListener("click", function() {
    // Собираем все выбранные файлы
    const selectedFiles = [];
    document.querySelectorAll('.file-checkbox:checked').forEach(function(checkbox) {
        selectedFiles.push(checkbox.value);
    });

    // Если есть выбранные файлы
    if (selectedFiles.length > 0) {
        let openTabs = [];
        let blocked = false;
        // Открываем каждый файл поочередно

    selectedFiles.forEach(function(fileUrl, index) {
            if (fileUrl) {
                const newTab = window.open(fileUrl, '_blank');  // Пытаемся открыть вкладку

                if (!newTab) {
                    blocked = true;  // Если вкладка не открыта, значит, браузер заблокировал попытку
                } else {
                    openTabs.push(newTab);  // Если вкладка открыта, добавляем ее в массив
                }
            }
        });

        if (blocked) {
            alert('Your browser has blocked pop-up windows. Please allow pop-ups for this site.');
        } else {
            // Если все вкладки открыты
            let checkTabs = setInterval(function() {
                if (openTabs.every(tab => tab.closed)) {
                    clearInterval(checkTabs);
                    alert("All files have been downloaded.");
                }
            }, 1000);
        }
    } else {
        alert('Please select at least one file to download.');
    }
});
