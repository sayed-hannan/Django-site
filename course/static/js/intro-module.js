
const moduleHeaders = document.querySelectorAll('.module-header');

moduleHeaders.forEach(header => {
    header.addEventListener('click', () => {
        const content = header.nextElementSibling;
        const icon = header.querySelector('svg');
        header.classList.toggle('active');
        content.classList.toggle('active');
        icon.classList.toggle('rotate-180');
        if (content.classList.contains('active')) {
            content.style.maxHeight = content.scrollHeight + 'px';
        } else {
            content.style.maxHeight = '0';
        }
    });
});