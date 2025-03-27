# ros2-docker-quickstarter

ros2-docker-quickstarter is a lightweight template repository designed to bootstrap your ROS2 projects in a Docker environment. It comes with pre-configured Dockerfiles and scripts to eliminate boilerplate code, enabling you to get started quickly and focus on developing your robotics applications.

## Project structure

```bash
├── docker-compose.yml
├── Dockerfile
├── gitignore
├── README.md
├── ros2_ws
│   └── src
│       └── my_python_package
│           ├── launch
│           │   └── run.launch.py
│           ├── my_python_package
│           │   ├── __init__.py
│           │   └── my_node.py
│           ├── package.xml
│           ├── resource
│           │   └── my_python_package
│           ├── setup.cfg
│           ├── setup.py
│           ├── test
│           │   ├── test_copyright.py
│           │   ├── test_flake8.py
│           │   └── test_pep257.py
│           └── urdf
│               └── robot.urdf.xacro
└── ros_entrypoint.sh
8 directories, 16 files
```


# How to Run the Project

## Using the Dockerfile

Build the Docker Image:
```bash
sudo docker build -t ros2_docker .
```

Run the Docker Container:
```bash
sudo docker run -it --rm ros2_docker
```
## Using the docker composer

Build and run

```bash
sudo docker compose build && sudo docker compose up -d
```

# How this was created

```bash
mkdir -p ros2_ws/src
cd ros2_ws/src
ros2 pkg create my_python_package --build-type ament_python --dependencies rclpy

```
After setting up the initial workspace, the following changes were made:
- A `my_node.py` file was created inside the my_python_package with a sample subscriber implementation.
- The `setup.py` file was updated accordingly to my_node.
- Then Docker file and docker-compose.yml file was created

# Contributing

Contributions are welcome! Feel free to fork the repository and submit pull requests with improvements or additional features.
