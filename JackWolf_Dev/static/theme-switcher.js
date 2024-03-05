function switchTheme(theme) {
    if (theme === 'dark') {
        document.getElementById('stylesheet').href = '/static/dark-theme.css';
    } else {
        document.getElementById('stylesheet').href = '/static/light-theme.css';
    }
    // Save the theme preference in local storage or send to the server
    localStorage.setItem('theme', theme);
}

// Check for saved theme preference on load
document.addEventListener('DOMContentLoaded', () => {
    const savedTheme = localStorage.getItem('theme') || 'light';
    switchTheme(savedTheme);
});
