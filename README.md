 ** How to run **
---
- You can run it via docker compose, or manually building up the image and running the container in your local machine.
** How to run with Dockerfile**
 - Building an image
	- docker build -f infra/Dockerfile -t <your_image_name> .
 - Running the container
	- docker run -p 8888:888 <your_image_name> 
--
- Running with docker compose 
	- docker compose up --build
- Stop the container from running
	- docker start -ai ml_notebooks
	- docker stop ml_notebooks
