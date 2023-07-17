 document.addEventListener('DOMContentLoaded', function() {
    let inputFile = document.querySelector('input[type="file"]');
    inputFile.addEventListener('change', function(e) {
        let fileName = e.target.files[0].name;
        let span = document.createElement('span')
        span.textContent = " is the selected file."
        let h4 =document.querySelector('h4')
        h4.textContent = fileName
        h4.appendChild(span)
    });
});