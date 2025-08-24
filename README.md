# About this repo

---

Welcome to this AI repo. This is meant to be a bunch of EDA's from popular datasets where machine learning was applied. A whole bunch of different algorithms are going to be / were used to explore diffent paths of solving real-world puzzles.

To run it locally, it is recommended to use Docker as it is already configured in the  `./infra` folder. Otherwise, you can run it locally using your own python virtual everonment, making sure the dependencies in `./infra/requirements.txt` are properly installed.

# How to run with Docker

---

You can run it via docker compose, or manually building up the image and running the container in your local machine.

- Note: Jupyter runs by default on port 8888, so make sure there is no other process using that port. It may be experienced issues with other running containers running on that port.

### **Running with Dockerfile**

* Build an image
  * `docker build -f infra/Dockerfile -t <your_image_name> .`
* Run the container
  * `docker run -p 8888:888 <your_image_name>`

### Running with docker compose

- Build and run the container
  - `docker compose up --build`
- Stop the container from running
  - `docker stop ml_notebooks`
- Start the container again (this can also be used when running with Dockerfile)
  - `docker start -ai ml_notebooks`

## Using .venv

---

* Create a venv inside the source directory
  * python3 -m venv `<your_venv_ name>`

- Enter the virtual enverionment

  - source `your_venv_name/bin/python`
- Install the the project's dependencies

  - `pip install -r requirement.txt`
- Now choose the kernel to run the notebook and that is done!
