const dropArea = document.getElementById('drop-area');
const fileInput = document.getElementById('audio');
const fileLabel = document.getElementById('file-label');

// Clique na área ativa o input
dropArea.addEventListener('click', () => fileInput.click());

// Arrastar e soltar
dropArea.addEventListener('dragover', (e) => {
    e.preventDefault();
    dropArea.style.background = '#f0f0f0';
});
dropArea.addEventListener('dragleave', (e) => {
    e.preventDefault();
    dropArea.style.background = '';
});
dropArea.addEventListener('drop', (e) => {
    e.preventDefault();
    dropArea.style.background = '';
    if (e.dataTransfer.files.length) {
        fileInput.files = e.dataTransfer.files;
        fileLabel.textContent = e.dataTransfer.files[0].name;
    }
});

// Atualiza label ao escolher arquivo pelo input
fileInput.addEventListener('change', () => {
    if (fileInput.files.length) {
        fileLabel.textContent = fileInput.files[0].name;
    }
});