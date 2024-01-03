# Contents
1. <a href="#Description">Description</a>
2. <a href="#Libraries & Frameworks">Libraries & Frameworks</a>
3. <a href="#Setup">Setup</a>
4. <a href="#Requirements">Requirements</a>
5. <a href="#Running and Shutdown">Running and Shutdown</a>

# Description
This project seeks to provide a robust and lightweight viewer for transit routes, sidewalks, and other non-auto-centric infrastructure. This would allow users to plan their transit routes and explore transit options in a way that highlights stops and pedestrian friendly options. This project builds off of experience I gained with a previous project, <a href="https://github.com/collinkatz/sidewalkhelper/">sidewalkhelper</a>.

# Libraries & Frameworks
This project uses:
- Django
- React
- Postgresql

# Requirements
Since this application is containerized via Docker, the only requirement is that you have Docker installed on your machine. All requirements downloading and setup is handled when the application is run.

# Setup
### Configure backend
This application uses the maps javascript api to load google maps on the webpage. However, the google maps javascript api costs money and is connected to a billing account, so it is important to keep your api keys hidden and secure. For this reason, I am not uploading my maps api key to this github repository so you will have to configure your own api key.

**Set up google cloud project with maps javascript api**
1. Go to your <a href="https://console.cloud.google.com/">google cloud console</a>.
2. Create a new project and set up a billing account.
3. Select your project and on the sidebar click `Apis & Services`
4. Click the button `+ ENABLE APIS AND SERVICES`
5. Search for `Maps JavaScript API` and click the service that appears
6. Click enable and copy the API key it gives you

**Configure django application to use your api key**
1. Create a file named `maps_api_key.txt` in the django base directory.
2. Paste your api key into this file and save the file.
3. If you want to specify a different location for your api key, go into settings.py in the django base directory
4. Set the variable `MAPS_API_KEY_LOCATION = <your api key goes here>`

# Running and Shutdown
This application can be run by executing `docker compose up` in the command line.
Once all output has finished, visit <a href="http://localhost:3000/">localhost:3000</a> to access the react homepage of the application.
Additionally, the django backend can be accessed via <a href="http://localhost:8000/">localhost:8000</a>

Shut down this application using `docker compose down --rmi all` which will shutdown and remove running containers, and then it removes the images created.