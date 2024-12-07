// Функция для переключения состояния потомков
document.addEventListener("DOMContentLoaded", function () {
    function toggleDescendants(checkbox, path) {
        const isChecked = checkbox.checked;

        document.querySelectorAll("tr").forEach(function (row) {
            const childPath = row.querySelector(".path-cell")?.textContent.trim();
            const childCheckbox = row.querySelector("input[type='checkbox']");

            // Если путь дочерний (начинается с текущего) и глубже на уровне
            if (
                childPath &&
                childPath.startsWith(path + "/") &&
                childPath.split("/").length === path.split("/").length + 1 &&
                childCheckbox
            ) {
                childCheckbox.checked = isChecked;
                toggleDescendants(childCheckbox, childPath); // Рекурсивно переключаем
            }
        });
    }

    // Функция для обновления состояния родителя
    function updateParentState(path) {
        const parentPath = path.substring(0, path.lastIndexOf("/"));
        if (parentPath) {
            const parentRow = Array.from(document.querySelectorAll("tr")).find((row) => {
                const cellPath = row.querySelector(".path-cell")?.textContent.trim();
                return cellPath === parentPath;
            });

            if (parentRow) {
                const parentCheckbox = parentRow.querySelector("input[type='checkbox']");
                const siblingCheckboxes = Array.from(document.querySelectorAll("tr")).filter((row) => {
                    const siblingPath = row.querySelector(".path-cell")?.textContent.trim();
                    return (
                        siblingPath &&
                        siblingPath.startsWith(parentPath + "/") &&
                        siblingPath.split("/").length === path.split("/").length + 1
                    );
                });

                const allChecked = siblingCheckboxes.every((row) =>
                    row.querySelector("input[type='checkbox']").checked
                );
                const anyChecked = siblingCheckboxes.some((row) =>
                    row.querySelector("input[type='checkbox']").checked
                );

                // Если все дочерние элементы выбраны
                parentCheckbox.checked = allChecked;
                // Если хотя бы один дочерний элемент выбран, но не все
                parentCheckbox.indeterminate = !allChecked && anyChecked;

                // Рекурсивно обновляем родителя
                updateParentState(parentPath);
            }
        }
    }

    // Обработчик для чекбоксов
    document.querySelectorAll("input[type='checkbox']").forEach(function (checkbox) {
        checkbox.addEventListener("change", function () {
            const row = checkbox.closest("tr");
            const path = row.querySelector(".path-cell")?.textContent.trim();

            if (path) {
                if (path === "/") {
                    // При выборе "root" выбираем все дочерние элементы
                    const isChecked = checkbox.checked;
                    document.querySelectorAll("input[type='checkbox']").forEach(function (childCheckbox) {
                        childCheckbox.checked = isChecked;
                        toggleDescendants(childCheckbox, path); // Переключаем потомков
                    });
                } else {
                    toggleDescendants(checkbox, path); // Переключаем потомков
                }
                updateParentState(path); // Обновляем родителей
            }
        });
    });
});
