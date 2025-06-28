

document.addEventListener('DOMContentLoaded', function() {
    const burgerMenu = document.getElementById('burger-menu');
    const mainNav = document.getElementById('main-nav');

    // Проверяем, что элементы существуют
    if (burgerMenu && mainNav) {
        burgerMenu.addEventListener('click', function() {
            // Переключаем класс 'active' на навигации
            mainNav.classList.toggle('active');
        });
    }
});



// script.js
document.getElementById('js-show-all').addEventListener('click', function() {
  const grid = document.getElementById('js-cards');
  grid.classList.remove('collapsed');
  this.style.display = 'none';
});


// static/js/preloader.js
