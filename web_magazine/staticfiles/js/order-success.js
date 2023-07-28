  $(document).ready(function() {

          setTimeout(function() {
            $('.circle-loader').toggleClass('load-complete');
            $('.checkmark').toggle();


            setTimeout(function() {
                window.location.href = 'http://127.0.0.1:8000/book/catalogue/';
            }, 2000);
        }, 800);
    });
