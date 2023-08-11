function hideErrors() {
    let element = document.querySelector('.errors')
     let computedStyle = window.getComputedStyle(element);
     if (computedStyle.display === "block") {
        element.style.display = "none";
}
}

function passHide() {
      let passInputs = document.querySelectorAll('.pass');
      passInputs.forEach(function (input) {
         if (input.type === 'password') {
             input.type = 'text'
         } else {
             input.type = 'password'
         }
      })
      
    
}





