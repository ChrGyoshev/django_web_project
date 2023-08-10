function test() {
    let menu_logo = document.querySelector('#menulogo');
    let Menu = document.querySelector('.Menu');
    let rect1 = document.querySelector('.rect1');
    let rect2 = document.querySelector('.rect2');
    let rect3 = document.querySelector('.rect3');
    let ul = document.querySelector('.ul');
    let profile_li = document.querySelectorAll('.lia.profile')
    profile_li.forEach(profile_li => {
        profile_li.addEventListener('click', profileBtn);
    });



    // profile_li.addEventListener('click', profileBtn)

    menu_logo.addEventListener('click', tester);

     function profileBtn() {
        let button = this
        let p = button.querySelectorAll('.profile-btns')
        if (!button.classList.contains('active')) {
            button.classList.add('active')
            p.forEach(element => {
                element.style.display = 'block'
            })


            button.addEventListener('mouseleave', function () {
                button.classList.remove('active')
                p.forEach(element => {
                    element.style.display = 'none'

                })
            })

        } else {

            button.classList.remove('active')
            p.forEach(element => {
                element.style.display = 'none'
            })

        }


    }



    rect1.style.opacity = 0;
    rect2.style.transform = 'rotate(45deg) translate(6px, -15px)';
    rect3.style.transform = 'rotate(-45deg) translate(-20px, 0px)';
    ul.style.marginTop = '0px';
    menu_logo.style.marginTop = '35px';

    function tester() {
        if (Menu.classList.contains('hover')) {
            Menu.classList.remove('hover');
            menu_logo.style.marginTop = '25px';
            rect1.style.opacity = 1;
            rect2.style.transform = 'rotate(0deg) translate(0px, 0px)';
            rect3.style.transform = 'rotate(0deg) translate(0px, 0px)';
            ul.style.marginTop = '-100px';


        } else {
            Menu.classList.toggle('hover');
            rect1.style.opacity = 0;
            rect2.style.transform = 'rotate(45deg) translate(6px, -15px)';
            rect3.style.transform = 'rotate(-45deg) translate(-20px, 0px)';
            ul.style.marginTop = '0px';
            menu_logo.style.marginTop = '35px';
        }
    }
}
    // show file when upload in edit profile
    // document.getElementById("file-upload").onchange = function() {
    // document.getElementById("uploadFile").value = this.value;}
test();
