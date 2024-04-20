// courses/static/js/courses.js

document.addEventListener('DOMContentLoaded', function() {
    // Fetch course data from the server using AJAX
    fetch('/api/courses/')
        .then(response => response.json())
        .then(data => {
            // Create course cards based on the fetched data
            const courseCardsContainer = document.getElementById('course-cards');
            data.forEach(course => {
                const courseCard = document.createElement('div');
                courseCard.className = 'bg-white p-4 rounded-lg shadow-md';
                courseCard.innerHTML = `
                    <h2 class="text-lg font-semibold">${course.title}</h2>
                    <p class="text-gray-600 mb-2">${course.description}</p>
                `;
                courseCardsContainer.appendChild(courseCard);
            });
        })
        .catch(error => {
            console.error('Error fetching course data:', error);
        });
});
