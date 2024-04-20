document.addEventListener("DOMContentLoaded", function () {
    // Find all headings in the article content
    const headings = document.querySelectorAll("article h2, article h3");

    // Create the table of contents dynamically
    const sidebar = document.getElementById("sidebar");
    headings.forEach((heading) => {
        const id = heading.id;
        const text = heading.textContent;
        const listItem = document.createElement("li");
        const link = document.createElement("a");

        // Set the link href to the heading ID
        link.href = `#${id}`;
        link.textContent = text;
        listItem.appendChild(link);
        sidebar.appendChild(listItem);

        // Smooth scroll to the heading when the link is clicked
        link.addEventListener("click", function (e) {
            e.preventDefault();
            const targetHeading = document.getElementById(id);
            targetHeading.scrollIntoView({ behavior: "smooth" });
        });
    });
});
