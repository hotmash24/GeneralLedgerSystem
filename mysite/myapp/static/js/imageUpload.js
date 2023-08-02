const imgInput = document.getElementById('imgfiles');
const imgPreview = document.getElementById('imgPreview');

imgInput.addEventListener('change', function (event) {
  const file = event.target.files[0];
  if (file) {
    const reader = new FileReader();
    reader.onload = function () {
      imgPreview.src = reader.result;
    };
    reader.readAsDataURL(file);
  }
});

const pdfInput = document.getElementById('pdfInput');
const pdfPreviewContainer = document.getElementById('pdfPreviewContainer');

pdfInput.addEventListener('change', function (event) {
  const file = event.target.files[0];
  if (file) {
    const reader = new FileReader();
    reader.onload = function () {
      const embed = document.createElement('embed');
      embed.src = reader.result;
      embed.type = 'application/pdf';
      embed.width = '150px';
      embed.height = '150px';

      // Remove any previously displayed PDF content
      while (pdfPreviewContainer.firstChild) {
        pdfPreviewContainer.removeChild(pdfPreviewContainer.firstChild);
      }

      pdfPreviewContainer.appendChild(embed);
    };
    reader.readAsDataURL(file);
  }
});



// const imgInput = document.getElementById('imgfiles');
//     const imgPreview = document.getElementById('imgPreview');

//     imgInput.addEventListener('change', function (event) {
//       const file = event.target.files[0];
//       if (file) {
//         const reader = new FileReader();
//         reader.onload = function () {
//           imgPreview.src = reader.result;
//         }
//         reader.readAsDataURL(file);
//       }
//     });

//     // PDF preview
//     const pdfInput = document.getElementById('pdfInput');
//     const pdfPreview = document.getElementById('pdfPreview');

//     pdfInput.addEventListener('change', function (event) {
//       const file = event.target.files[0];
//       if (file) {
//         const reader = new FileReader();
//         reader.onload = function () {
//           pdfPreview.src = reader.result;
//         }
//         reader.readAsDataURL(file);
//       }
//     });