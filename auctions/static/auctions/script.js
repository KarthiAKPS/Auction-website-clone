const isDarkMode = localStorage.getItem('isDarkMode') === 'true';

document.addEventListener('DOMContentLoaded', () => {
    // Check for user's preference on page load
    if (isDarkMode) {
        enableDarkMode();
    }

    const activePage = window.location.pathname;
    const navLinks = document.querySelectorAll('.nav-link').forEach(link => {
        if (link.href.includes(`${activePage}`)) {
            link.classList.add('active');
        }
    });

    // Add event listeners to buttons
    document.querySelector('#dark-button').addEventListener('click', enableDarkMode);
    document.querySelector('#light-button').addEventListener('click', disableDarkMode);
}
);

function enableDarkMode() {
    // Add 'dark' class to bground element
    document.getElementById('bground').classList.add('dark');
    document.getElementById('bground').classList.remove('light');

    // Hide dark mode button and show light mode button
    document.querySelector('#dark-button').style.display = 'none';
    document.querySelector('#light-button').style.display = 'block';

    // Store user's preference in localStorage
    localStorage.setItem('isDarkMode', 'true');
}

function disableDarkMode() {
    // Add 'light' class to bground element
    document.getElementById('bground').classList.add('light');
    document.getElementById('bground').classList.remove('dark');

    // Hide light mode button and show dark mode button
    document.querySelector('#light-button').style.display = 'none';
    document.querySelector('#dark-button').style.display = 'block';

    // Store user's preference in localStorage
    localStorage.setItem('isDarkMode', 'false');
}
