Sure, here is the simplified README with only the requested sections:

````markdown
# Portfolio Site Deployment with Docker

This repository contains the Docker setup for deploying the portfolio site. The Docker image is available on Docker Hub and can be pulled and run on any system with Docker installed.

## Prerequisites

- Docker installed on your system. You can download Docker from [here](https://www.docker.com/products/docker-desktop).

## Pulling the Docker Image

To pull the Docker image from Docker Hub, use the following command:

```sh
docker pull vinci7813/capstone:v2
```
````

## Running the Docker Container

Once the image is pulled, you can run it using the following command:

```sh
docker run -d -p 8000:8000 vinci7813/capstone:v2
```

### Explanation of the Command

- `-d`: Run the container in detached mode (in the background).
- `-p 8000:8000`: Map port 8000 on your local machine to port 8000 on the container.
- `vinci7813/capstone:v2`: The name and tag of the Docker image.

After running the command, your portfolio site will be accessible at `http://localhost:8000`.

## Stopping the Container

To stop the running container, use the following command:

```sh
docker stop container_name_or_id
```

Replace `container_name_or_id` with the actual name or ID of your running container. You can find the container ID by running:

```sh
docker ps
```

This README provides instructions for pulling and running the Docker image for the portfolio site. Follow these steps to deploy the site on any system with Docker installed.

```

This version includes only the sections for downloading Docker, pulling the image, running the image, and stopping the container.

# capstone

portfolio_site/ # Main project directory
│
├── portfolio_site/ # Django project settings
│ ├── **init**.py
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
│
├── core/ # Main app (for landing page, base templates, etc.)
│ ├── migrations/
│ ├── templates/
│ │ └── base.html # Base template for entire site
│ ├── **init**.py
│ ├── admin.py
│ ├── apps.py
│ ├── models.py
│ ├── tests.py
│ └── views.py # Views for landing page, about me, etc.
│
├── autobiography/ # App for autobiographic essays
│ ├── migrations/
│ ├── templates/
│ │ └── autobiography/
│ │ └── autobiography.html # Template for autobiographies
│ ├── **init**.py
│ ├── admin.py
│ ├── apps.py
│ ├── models.py
│ ├── tests.py
│ └── views.py # Views for managing autobiographies
│
├── photography/ # App for photographic essays
│ ├── migrations/
│ ├── templates/
│ │ └── photography/
│ │ └── photo_essay.html # Template for photo essays
│ ├── **init**.py
│ ├── admin.py
│ ├── apps.py
│ ├── models.py
│ ├── tests.py
│ └── views.py # Views for managing photo essays
│
├── cv/ # App for CVs
│ ├── migrations/
│ ├── templates/
│ │ └── cv/
│ │ └── cv.html # Template for CVs
│ ├── **init**.py
│ ├── admin.py
│ ├── apps.py
│ ├── models.py
│ ├── tests.py
│ └── views.py # Views for managing CVs
│
├── videos/ # App for videos
│ ├── migrations/
│ ├── templates/
│ │ └── videos/
│ │ └── videos.html # Template for videos
│ ├── **init**.py
│ ├── admin.py
│ ├── apps.py
│ ├── models.py
│ ├── tests.py
│ └── views.py # Views for managing videos
│
├── static/ # Directory for static files (CSS, JS, images)
│ ├── css/
│ │ └── styles.css # Custom CSS styles
│ ├── img/
│ └── js/
│
├── media/ # Directory for uploaded media files (CVs, videos)
│
└── manage.py # Django's command-line utility for administrative tasks
```
# capstone2
# capstone
