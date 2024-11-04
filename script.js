document.addEventListener('DOMContentLoaded', () => {
    // Handle navigation items expansion
    document.querySelectorAll('.nav-item').forEach(item => {
        if (item.nextElementSibling && item.nextElementSibling.tagName === 'UL') {
            item.addEventListener('click', (e) => {
                e.stopPropagation();
                item.classList.toggle('expanded');
                item.nextElementSibling.classList.toggle('show');
            });
        }
    });

    // Mobile menu toggle
    const mobileToggle = document.querySelector('.mobile-toggle');
    const sidebar = document.querySelector('.sidebar');

    mobileToggle.addEventListener('click', () => {
        sidebar.classList.toggle('show');
    });

    // Close sidebar when clicking outside on mobile
    document.addEventListener('click', (e) => {
        if (window.innerWidth <= 768 && 
            !sidebar.contains(e.target) && 
            !mobileToggle.contains(e.target)) {
            sidebar.classList.remove('show');
        }
    });
});

// Add to script.js
async function loadImages() {
    try {
        const response = await fetch('/allImages.json');
        const imageData = await response.json();
        const imageGrid = document.getElementById('imageGrid');
        
        Object.values(imageData).forEach(imagePath => {
            const imageItem = document.createElement('div');
            imageItem.className = 'image-item';
            
            const img = document.createElement('img');
            img.src = imagePath;
            img.loading = 'lazy';
            img.alt = 'Group Photo';
            
            imageItem.appendChild(img);
            imageGrid.appendChild(imageItem);
        });
    } catch (error) {
        console.error('Error loading images:', error);
    }
}

document.addEventListener('DOMContentLoaded', loadImages);

// Add to script.js
document.addEventListener('DOMContentLoaded', () => {
    const sidebarToggle = document.getElementById('sidebarToggle');
    const sidebar = document.querySelector('.sidebar');
    
    // Create overlay element
    const overlay = document.createElement('div');
    overlay.className = 'sidebar-overlay';
    document.body.appendChild(overlay);

    sidebarToggle.addEventListener('click', () => {
        sidebar.classList.toggle('active');
        sidebarToggle.classList.toggle('active');
        overlay.classList.toggle('active');
    });

    // Close sidebar when clicking overlay
    overlay.addEventListener('click', () => {
        sidebar.classList.remove('active');
        sidebarToggle.classList.remove('active');
        overlay.classList.remove('active');
    });
});