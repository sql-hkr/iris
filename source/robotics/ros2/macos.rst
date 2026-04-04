ROS2 (macos)
===============

- smach


.. code-block:: bash

    cd ~/ros2_ws/src
    git clone https://github.com/ros/executive_smach.git
    cd ..
    colcon build --packages-select executive_smach
    source install/setup.bash


- smach_viewer

ROS1用のため，ROS2では動作しない．

- tf_transformations

.. code-block:: bash

    pixi add transforms3d # 依存関係の追加
    pixi shell
    cd ~/ros2_ws/src
    git clone -b foxy https://github.com/DLu/tf_transformations.git
    cd ..
    colcon build --packages-select tf_transformations
    source install/setup.bash

