function generatePDF() {
    var xhr = new XMLHttpRequest();
    xhr.open('GET', '/api/generate_pdf/', true);
    xhr.responseType = 'blob';

    xhr.onload = function () {
        if (xhr.status === 200) {
            var blob = new Blob([xhr.response], { type: 'application/pdf' });
            var link = document.createElement('a');
            link.href = window.URL.createObjectURL(blob);
            console.log('Date:', link.href)
            link.download = 'CVPR.pdf'; // Change the file name as needed
            link.click();
            var pdfURL = window.URL.createObjectURL(blob);
            window.open(pdfURL, '_blank');

            window.close();
        }
    };
    xhr.send();
}

window.onload=generatePDF();