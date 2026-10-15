console.log("Admin dashboard loaded");

const navigationLinks = document.querySelectorAll("nav a");
const contentSection = document.getElementById("content");

navigationLinks.forEach(function (link) {
    link.addEventListener("click", function (event) {
        event.preventDefault();

        const section = link.dataset.section;

        if (section === "dashboard") {
            contentSection.innerHTML = `
                <h2>Dashboard</h2>
                <p>Manage your portfolio content.</p>

                <div>
                    <div>
                        <h3>Skills</h3>
                        <p>0</p>
                    </div>

                    <div>
                        <h3>Projects</h3>
                        <p>0</p>
                    </div>

                    <div>
                        <h3>Experience</h3>
                        <p>0</p>
                    </div>
                </div>
            `;
        }

        if (section === "profile") {
            contentSection.innerHTML = `
                <h2>Profile</h2>
                <p>Manage your personal information.</p>
            `;
        }

        if (section === "skills") {
            contentSection.innerHTML = `
                <h2>Skills</h2>
                <p>Manage your technical skills.</p>
            `;
        }

        if (section === "projects") {
            contentSection.innerHTML = `
                <h2>Projects</h2>
                <p>Manage your portfolio projects.</p>
            `;
        }

        if (section === "experience") {
            contentSection.innerHTML = `
                <h2>Experience</h2>
                <p>Manage your professional experience.</p>
            `;
        }
    });
});