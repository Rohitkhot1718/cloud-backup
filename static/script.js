function uploadFile() {
    let input = document.getElementById('fileInput');
    let file = input.files[0];

    if (!file) {
        alert("No file selected!");
        return;
    }

    let formData = new FormData();
    formData.append('file', file);

    fetch('/upload', {
        method: 'POST',
        body: formData
    }).then(response => response.json())
      .then(data => {
          if (data.error) {
              alert(data.error);
              return;
          }
          location.reload();
      });
}

function downloadFile(filename) {
    window.location.href = `/download/${filename}`;
}

function deleteFile(filename) {
    fetch(`/delete/${filename}`, { method: 'POST' })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
        location.reload();
    });
}
