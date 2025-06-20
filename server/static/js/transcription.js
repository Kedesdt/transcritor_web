

document.getElementById('uploadForm').onsubmit = async function(e) {
    e.preventDefault();
    const form = e.target;
    const formData = new FormData(form);
    document.getElementById('transcriptionText').innerText = 'Transcrevendo, aguarde...';

    const response = await fetch('/transcrever', {
        method: 'POST',
        body: formData
    });

    const data = await response.json();
    document.getElementById('transcriptionText').innerHTML = data.transcription;
}