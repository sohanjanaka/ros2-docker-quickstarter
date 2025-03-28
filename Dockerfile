FROM ros:humble

RUN apt-get update

# Customize your ROS environment by installing additional packages as needed.
RUN apt-get install -y ros-${ROS_DISTRO}-demo-nodes-py
RUN apt-get install -y ros-${ROS_DISTRO}-rqt

RUN rm -rf /var/lib/apt/lists/*
RUN echo 'source "/opt/ros/$ROS_DISTRO/setup.bash"' >> ~/.bashrc


SHELL ["/bin/bash", "-c"]

WORKDIR /app

COPY ros2_ws ros2_ws/
RUN cd ros2_ws && \
    source /opt/ros/${ROS_DISTRO}/setup.bash && \
    colcon build

ADD ros_entrypoint.sh /

ENTRYPOINT ["/ros_entrypoint.sh"]

CMD ["ros2", "launch", "my_python_package", "run.launch.py"]
