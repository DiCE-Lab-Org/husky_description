# Meshes

All URDF references use `package://husky_description/meshes/...`, so no
source-file edits are needed once the contents below are in place.

## Subfolder inventory

```
meshes/
├── a200_0876_description/meshes/
│   ├── dual_arm_bulkhead.dae
│   └── dual_arm_bulkhead_collision.stl
│
├── clearpath_platform_description/meshes/a200/
│   ├── base_link.dae
│   ├── top_chassis.dae
│   ├── wheel.dae
│   └── attachments/bumper.dae
│
├── clearpath_sensors_description/meshes/
│   └── swift_antenna.stl
│
├── mount_description/                       # custom pan-tilt neck mount
│   ├── camera_mount.stl                     # neck base plate on bulkhead
│   ├── fr12_h103gm.stl                      # Robotis FR12 base bracket
│   ├── 2XL_430.stl                          # Dynamixel 2XL430 servo body
│   ├── FR12-H104.stl                        # Robotis FR12 pan bracket
│   └── neck_camera_holder.stl               # rigid camera holder
│
├── realsense2_description/meshes/
│   └── d435.dae
│
├── robotiq_description/meshes/
│   ├── visual/2f_85/*.dae
│   └── collision/2f_85/*.stl
│
├── ur_description/meshes/ur5e/
│   ├── visual/*.dae
│   └── collision/*.stl
│
└── velodyne_description/meshes/
    ├── VLP16_base_1.dae
    ├── VLP16_base_2.dae
    └── VLP16_scan.dae
```