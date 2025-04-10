export function navbarScroll() {
    let prevScrollpos = window.pageYOffset;
    const navbar = document.querySelector('.navbar');

    window.addEventListener('scroll', () => {
        let currentScrollPos = window.pageYOffset;

        if (currentScrollPos > 50 && currentScrollPos > prevScrollpos) {
            navbar.style.top = '-80px';
        } else {
            navbar.style.top = '0';
        }
        prevScrollpos = currentScrollPos;
    });
}