
const categorySelect = document.getElementById('category');
const levelSelect = document.getElementById('level');
const courseContainer = document.querySelector('.course-container');

function filterCourses() {
    const selectedCategory = categorySelect.value;
    const selectedLevel = levelSelect.value;

    // Implement AJAX logic here to fetch filtered course data from the server.
    // Replace the following code with your actual AJAX request.
    // Example using fetch:
    // fetch(`/api/courses?category=${selectedCategory}&level=${selectedLevel}`)
    //     .then(response => response.json())
    //     .then(data => updateCourseCards(data));

    // Dummy code to simulate updating course cards.
    const dummyCourses = [
        // Replace with actual course data.
        // Format: { title: 'Course Title', category: 'programming', level: 'beginner', imageUrl: '...' }
        { title: 'Filtered Course 1', category: 'programming', level: 'beginner', imageUrl: 'https://via.placeholder.com/400x250' },
        // Add more courses as needed.
    ];

    updateCourseCards(dummyCourses);
}

function updateCourseCards(courses) {
    courseContainer.innerHTML = ''; // Clear existing cards
    courses.forEach(course => {
        const courseCard = `
                <div class="bg-white p-4 rounded-lg shadow-md">
                    <img src="${course.imageUrl}" alt="${course.title}" class="w-full h-40 object-cover rounded-md mb-4">
                    <h2 class="text-lg font-semibold">${course.title}</h2>
                    <p class="text-gray-600 mb-2">Course description...</p>
                    <p class="text-blue-500 font-medium">${course.level}</p>
                </div>`;
        courseContainer.insertAdjacentHTML('beforeend', courseCard);
    });
}

categorySelect.addEventListener('change', filterCourses);
levelSelect.addEventListener('change', filterCourses);

// Initial filtering when the page loads
filterCourses();

