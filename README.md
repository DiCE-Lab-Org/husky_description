# husky_description

Modular xacro description for **Clearpath Husky A200-0876** with:

- 2 × **UR5e** arms on a custom dual-arm bulkhead
- 2 × **Robotiq 2F-85** grippers (one per arm wrist)
- **Velodyne VLP-16** 3D lidar
- 2 × **Intel RealSense D435** (wrist-mounted)
- IMU and Swift GPS antenna
- Front bumper
- Optional `ros2_control` block for the Clearpath A200Hardware plugin
- Optional Gazebo (Ignition/gz) sensor plugins

---

## Layout

```
urdf/
├── robot.urdf.xacro              # top-level, composes everything
├── common/materials.xacro        # Clearpath color palette
├── platform/
│   ├── a200.urdf.xacro           # base_link, inertial, mounts, chassis
│   └── wheel.urdf.xacro          # wheel macro (called x4)
├── accessories/
│   ├── bumper.urdf.xacro
│   └── dual_arm_bulkhead.urdf.xacro
├── sensors/
│   ├── velodyne_vlp16.urdf.xacro
│   ├── realsense_d435.urdf.xacro
│   ├── imu.urdf.xacro
│   └── gps.urdf.xacro
├── manipulators/
│   ├── ur5e.urdf.xacro
│   └── robotiq_2f_85.urdf.xacro
└── control/a200_ros2_control.xacro
```

---

##  Meshes

All mesh references use `package://husky_description/meshes/...`.
The original auto-generated URDF used absolute paths like
`file:///home/hesam/Desktop/husky/meshes/...`.

Before building, copy (or symlink) the mesh trees into this package:

```bash
cd ~/Desktop/husky-dev/ros2_ws/src/husky_description
ln -s ~/Desktop/husky/meshes/clearpath_platform_description     meshes/clearpath_platform_description
ln -s ~/Desktop/husky/meshes/clearpath_sensors_description      meshes/clearpath_sensors_description
ln -s ~/Desktop/husky/meshes/velodyne_description                meshes/velodyne_description
ln -s ~/Desktop/husky/meshes/realsense2_description              meshes/realsense2_description
ln -s ~/Desktop/husky/meshes/ur_description                      meshes/ur_description
ln -s ~/Desktop/husky/meshes/robotiq_description                 meshes/robotiq_description
ln -s ~/Desktop/husky/meshes/a200_0876_description               meshes/a200_0876_description
```

> Use symlinks during development, replace with a real copy before
> distributing the package.

---

## Build & view

```bash
cd ~/Desktop/husky-dev/ros2_ws
colcon build --packages-select husky_description
source install/setup.bash

# RViz + jsp_gui (default)
ros2 launch husky_description view_robot.launch.py

# with Gazebo plugins embedded in the URDF
ros2 launch husky_description view_robot.launch.py use_gazebo:=true

# with ros2_control block embedded
ros2 launch husky_description view_robot.launch.py use_ros2_control:=true
```

Sanity-check the xacro without launching anything:

```bash
xacro src/husky_description/urdf/robot.urdf.xacro > /tmp/robot.urdf
check_urdf /tmp/robot.urdf
```

---

## Xacro args (top level)

| arg                | default                         | purpose                                  |
|--------------------|---------------------------------|------------------------------------------|
| `use_gazebo`       | `false`                         | Emit `<gazebo>` sensor/system plugins.   |
| `use_ros2_control` | `true`                          | Emit the `<ros2_control>` block.         |
| `serial_port`      | `/dev/clearpath/prolific`       | Serial device for A200Hardware plugin.   |
