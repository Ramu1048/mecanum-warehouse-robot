# 🚀 Autonomous Mecanum Robot Simulation and Mapping

<div align="center">

![ROS2](https://img.shields.io/badge/ROS2-Humble-blue)
![Gazebo](https://img.shields.io/badge/Gazebo-Classic-green)
![RViz](https://img.shields.io/badge/RViz2-Visualization-orange)
![SLAM](https://img.shields.io/badge/SLAM-Toolbox-red)
![License](https://img.shields.io/badge/License-Educational-lightgrey)

</div>

## 📌 Overview

This project was developed for the **Rookies ROS Hackathon 2026**.

The objective is to design, simulate, visualize, and control an autonomous four-wheel mecanum drive robot equipped with a LiDAR sensor using **ROS 2 Humble** and **Gazebo Classic**.

The robot is capable of omnidirectional motion, environment perception using LiDAR, and occupancy grid map generation using SLAM Toolbox.

---

# ✨ Features

- Four-Wheel Mecanum Drive Robot
- ROS 2 Humble
- Gazebo Classic Simulation
- Custom Warehouse Environment
- URDF/Xacro Robot Description
- LiDAR Sensor Integration
- RViz Visualization
- TF Tree Generation
- Keyboard Teleoperation
- SLAM Toolbox Mapping
- Occupancy Grid Map Generation

---

# 📂 Repository Structure

```
mecanum-warehouse-robot
│
├── src
│   ├── mecanum_description
│   ├── mecanum_gazebo
│   └── ...
│
├── worlds
├── maps
├── rviz
├── screenshots
├── README.md
└── .gitignore
```

---

# 🛠 Technologies Used

- ROS 2 Humble
- Gazebo Classic
- RViz2
- URDF
- Xacro
- SLAM Toolbox
- TF2
- Nav2 Map Server
- Teleop Twist Keyboard

---

# ⚙️ Installation

```bash
cd ~/mecanum-warehouse-robot

source /opt/ros/humble/setup.bash

colcon build

source install/setup.bash
```

---

# ▶️ Running the Simulation

## Launch Gazebo

```source /opt/ros/humble/setup.bash

source ~/mecanum-warehouse-robot/install/setup.bash

ros2 launch mecanum_gazebo gazebo.launch.py
```

## Teleoperation

```source /opt/ros/humble/setup.bash

ros2 run teleop_twist_keyboard teleop_twist_keyboard
```

## Launch SLAM

```
source /opt/ros/humble/setup.bash

source ~/mecanum-warehouse-robot/install/setup.bash

ros2 launch mecanum_gazebo slam.launch.py

```

## Save the Map

```source /opt/ros/humble/setup.bash

ros2 run nav2_map_server map_saver_cli \
-f ~/mecanum-warehouse-robot/mecanum_gazebo/maps/warehouse_map
```

---

# 📷 Deliverables

- Robot Description (URDF/Xacro)
- Gazebo World
- Gazebo Simulation
- RViz Visualization
- LiDAR Integration
- TF Tree
- SLAM Mapping
- Occupancy Grid Map
- Demonstration Video

---

# 🎯 Hackathon Challenge

**Autonomous Mecanum Robot Simulation and Mapping**

Design and simulate a four-wheel mecanum drive robot capable of omnidirectional movement and environment mapping using ROS 2, Gazebo, LiDAR, and SLAM Toolbox.

---

# 📋 Project Status

| Task | Status |
|------|--------|
| Robot Description | ✅ |
| Gazebo Simulation | ✅ |
| Warehouse World | ✅ |
| RViz Visualization | ✅ |
| LiDAR Integration | ✅ |
| Teleoperation | ✅ |
| SLAM Mapping | ✅ |
| Map Generation | ✅ |

---

# 👥 Team

Developed by the project team for the **Rookies ROS Hackathon 2026**.

---

# 📄 License

This project is developed for educational and hackathon purposes.
