function switchTheme() {
    const html = document.documentElement;
    html.classList.toggle('theme-dark');
    html.classList.toggle('theme-light');
    const icon = document.getElementById('themeIcon');
    icon.textContent = icon.textContent === 'light_mode' ? 'dark_mode' : 'light_mode';
}