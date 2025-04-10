import { navbarScroll } from './navbar.js';
import { dropdownMenu } from './dropdown.js';
import './slider.js';  // 새로 추가한 슬라이더 기능

document.addEventListener('DOMContentLoaded', () => {
    navbarScroll();
    dropdownMenu();
});