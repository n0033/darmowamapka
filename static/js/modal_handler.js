
let cookiesFirstExitBtn = document.getElementById('cookies-exit-btn-1');

let cookiesSecondExitBtn = document.getElementById('cookies-exit-btn-2');

cookiesFirstExitBtn.addEventListener('click', function(){
    $('#cookies').modal('hide')
})

cookiesSecondExitBtn.addEventListener('click', function(){
    $('#cookies').modal('hide')
})



let privacyFirstExitBtn = document.getElementById('privacy-exit-btn-1');

let privacySecondExitBtn = document.getElementById('privacy-exit-btn-2');

privacyFirstExitBtn.addEventListener('click', function(){
    $('#privacy').modal('hide')
})

privacySecondExitBtn.addEventListener('click', function(){
    $('#privacy').modal('hide')
})