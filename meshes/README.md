# Meshes

Drop the following subdirectories here (or symlink them from wherever you
currently keep them — e.g. `~/Desktop/husky/meshes/...`):

```
meshes/
├── a200_0876_description/meshes/dual_arm_bulkhead.dae
├── a200_0876_description/meshes/dual_arm_bulkhead_collision.stl
├── clearpath_platform_description/meshes/a200/base_link.dae
├── clearpath_platform_description/meshes/a200/top_chassis.dae
├── clearpath_platform_description/meshes/a200/wheel.dae
├── clearpath_platform_description/meshes/a200/attachments/bumper.dae
├── clearpath_sensors_description/meshes/swift_antenna.stl
├── realsense2_description/meshes/d435.dae
├── robotiq_description/meshes/visual/2f_85/*.dae
├── robotiq_description/meshes/collision/2f_85/*.stl
├── ur_description/meshes/ur5e/visual/*.dae
├── ur_description/meshes/ur5e/collision/*.stl
├── velodyne_description/meshes/VLP16_base_1.dae
├── velodyne_description/meshes/VLP16_base_2.dae
└── velodyne_description/meshes/VLP16_scan.dae
```

All URDF references use `package://husky_description/meshes/...`, so no
source-file edits are needed once these are in place.
