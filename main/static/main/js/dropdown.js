export function dropdownMenu() {
    const menuItems = document.querySelectorAll('.menu-item');

    menuItems.forEach((item) => {
        item.addEventListener('mouseenter', () => {
            item.querySelector('.submenu').style.display = 'block';
        });
        item.addEventListener('mouseleave', () => {
            item.querySelector('.submenu').style.display = 'none';
        });
    });
}