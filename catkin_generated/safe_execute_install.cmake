execute_process(COMMAND "/home/justin/ros_catkin_ws/src/rqt_offloading_controls/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/justin/ros_catkin_ws/src/rqt_offloading_controls/catkin_generated/python_distutils_install.sh) returned error code ")
endif()
