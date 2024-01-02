# Contents
1. <a href="#Description">Description</a>
2. <a href="#Requirements">Requirements</a>
3. <a href="#Running and Shutdown">Running and Shutdown</a>

# Description
This project seeks to provide a robust and lightweight viewer for transit routes, sidewalks, and other non-auto-centric infrastructure. This would allow users to plan their transit routes and explore transit options in a way that highlights stops and pedestrian friendly options. This project builds off of experience I gained with a previous project, <a href="https://github.com/collinkatz/sidewalkhelper/">sidewalkhelper</a>.

# Requirements
Since this application is containerized via Docker, the only requirement is that you have Docker installed on your machine. All requirements downloading and setup is handled when the application is run.

# Running and Shutdown
This application can be ran by executing `docker compose up` in the command line.
Once all output has finished, visit <a href="http://localhost:3000/">localhost:3000</a> to access the react homepage of the application.
Additionally, the django backend can be accessed via <a href="http://localhost:8000/">localhost:8000</a>

Shut down this application using `docker compose down --rmi all` which will shutdown and remove running containers, and then it removes the images created.