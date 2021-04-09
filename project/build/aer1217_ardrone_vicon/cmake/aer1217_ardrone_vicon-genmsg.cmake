# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "aer1217_ardrone_vicon: 3 messages, 0 services")

set(MSG_I_FLAGS "-Iaer1217_ardrone_vicon:/home/charlie/project/project/src/aer1217_ardrone_vicon/msg;-Istd_msgs:/opt/ros/kinetic/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(aer1217_ardrone_vicon_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/charlie/project/project/src/aer1217_ardrone_vicon/msg/MotorCommands.msg" NAME_WE)
add_custom_target(_aer1217_ardrone_vicon_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "aer1217_ardrone_vicon" "/home/charlie/project/project/src/aer1217_ardrone_vicon/msg/MotorCommands.msg" ""
)

get_filename_component(_filename "/home/charlie/project/project/src/aer1217_ardrone_vicon/msg/GazeboState.msg" NAME_WE)
add_custom_target(_aer1217_ardrone_vicon_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "aer1217_ardrone_vicon" "/home/charlie/project/project/src/aer1217_ardrone_vicon/msg/GazeboState.msg" ""
)

get_filename_component(_filename "/home/charlie/project/project/src/aer1217_ardrone_vicon/msg/DesiredStateMsg.msg" NAME_WE)
add_custom_target(_aer1217_ardrone_vicon_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "aer1217_ardrone_vicon" "/home/charlie/project/project/src/aer1217_ardrone_vicon/msg/DesiredStateMsg.msg" ""
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(aer1217_ardrone_vicon
  "/home/charlie/project/project/src/aer1217_ardrone_vicon/msg/MotorCommands.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/aer1217_ardrone_vicon
)
_generate_msg_cpp(aer1217_ardrone_vicon
  "/home/charlie/project/project/src/aer1217_ardrone_vicon/msg/GazeboState.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/aer1217_ardrone_vicon
)
_generate_msg_cpp(aer1217_ardrone_vicon
  "/home/charlie/project/project/src/aer1217_ardrone_vicon/msg/DesiredStateMsg.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/aer1217_ardrone_vicon
)

### Generating Services

### Generating Module File
_generate_module_cpp(aer1217_ardrone_vicon
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/aer1217_ardrone_vicon
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(aer1217_ardrone_vicon_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(aer1217_ardrone_vicon_generate_messages aer1217_ardrone_vicon_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/charlie/project/project/src/aer1217_ardrone_vicon/msg/MotorCommands.msg" NAME_WE)
add_dependencies(aer1217_ardrone_vicon_generate_messages_cpp _aer1217_ardrone_vicon_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/charlie/project/project/src/aer1217_ardrone_vicon/msg/GazeboState.msg" NAME_WE)
add_dependencies(aer1217_ardrone_vicon_generate_messages_cpp _aer1217_ardrone_vicon_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/charlie/project/project/src/aer1217_ardrone_vicon/msg/DesiredStateMsg.msg" NAME_WE)
add_dependencies(aer1217_ardrone_vicon_generate_messages_cpp _aer1217_ardrone_vicon_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(aer1217_ardrone_vicon_gencpp)
add_dependencies(aer1217_ardrone_vicon_gencpp aer1217_ardrone_vicon_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS aer1217_ardrone_vicon_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(aer1217_ardrone_vicon
  "/home/charlie/project/project/src/aer1217_ardrone_vicon/msg/MotorCommands.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/aer1217_ardrone_vicon
)
_generate_msg_eus(aer1217_ardrone_vicon
  "/home/charlie/project/project/src/aer1217_ardrone_vicon/msg/GazeboState.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/aer1217_ardrone_vicon
)
_generate_msg_eus(aer1217_ardrone_vicon
  "/home/charlie/project/project/src/aer1217_ardrone_vicon/msg/DesiredStateMsg.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/aer1217_ardrone_vicon
)

### Generating Services

### Generating Module File
_generate_module_eus(aer1217_ardrone_vicon
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/aer1217_ardrone_vicon
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(aer1217_ardrone_vicon_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(aer1217_ardrone_vicon_generate_messages aer1217_ardrone_vicon_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/charlie/project/project/src/aer1217_ardrone_vicon/msg/MotorCommands.msg" NAME_WE)
add_dependencies(aer1217_ardrone_vicon_generate_messages_eus _aer1217_ardrone_vicon_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/charlie/project/project/src/aer1217_ardrone_vicon/msg/GazeboState.msg" NAME_WE)
add_dependencies(aer1217_ardrone_vicon_generate_messages_eus _aer1217_ardrone_vicon_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/charlie/project/project/src/aer1217_ardrone_vicon/msg/DesiredStateMsg.msg" NAME_WE)
add_dependencies(aer1217_ardrone_vicon_generate_messages_eus _aer1217_ardrone_vicon_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(aer1217_ardrone_vicon_geneus)
add_dependencies(aer1217_ardrone_vicon_geneus aer1217_ardrone_vicon_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS aer1217_ardrone_vicon_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(aer1217_ardrone_vicon
  "/home/charlie/project/project/src/aer1217_ardrone_vicon/msg/MotorCommands.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/aer1217_ardrone_vicon
)
_generate_msg_lisp(aer1217_ardrone_vicon
  "/home/charlie/project/project/src/aer1217_ardrone_vicon/msg/GazeboState.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/aer1217_ardrone_vicon
)
_generate_msg_lisp(aer1217_ardrone_vicon
  "/home/charlie/project/project/src/aer1217_ardrone_vicon/msg/DesiredStateMsg.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/aer1217_ardrone_vicon
)

### Generating Services

### Generating Module File
_generate_module_lisp(aer1217_ardrone_vicon
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/aer1217_ardrone_vicon
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(aer1217_ardrone_vicon_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(aer1217_ardrone_vicon_generate_messages aer1217_ardrone_vicon_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/charlie/project/project/src/aer1217_ardrone_vicon/msg/MotorCommands.msg" NAME_WE)
add_dependencies(aer1217_ardrone_vicon_generate_messages_lisp _aer1217_ardrone_vicon_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/charlie/project/project/src/aer1217_ardrone_vicon/msg/GazeboState.msg" NAME_WE)
add_dependencies(aer1217_ardrone_vicon_generate_messages_lisp _aer1217_ardrone_vicon_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/charlie/project/project/src/aer1217_ardrone_vicon/msg/DesiredStateMsg.msg" NAME_WE)
add_dependencies(aer1217_ardrone_vicon_generate_messages_lisp _aer1217_ardrone_vicon_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(aer1217_ardrone_vicon_genlisp)
add_dependencies(aer1217_ardrone_vicon_genlisp aer1217_ardrone_vicon_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS aer1217_ardrone_vicon_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(aer1217_ardrone_vicon
  "/home/charlie/project/project/src/aer1217_ardrone_vicon/msg/MotorCommands.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/aer1217_ardrone_vicon
)
_generate_msg_nodejs(aer1217_ardrone_vicon
  "/home/charlie/project/project/src/aer1217_ardrone_vicon/msg/GazeboState.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/aer1217_ardrone_vicon
)
_generate_msg_nodejs(aer1217_ardrone_vicon
  "/home/charlie/project/project/src/aer1217_ardrone_vicon/msg/DesiredStateMsg.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/aer1217_ardrone_vicon
)

### Generating Services

### Generating Module File
_generate_module_nodejs(aer1217_ardrone_vicon
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/aer1217_ardrone_vicon
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(aer1217_ardrone_vicon_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(aer1217_ardrone_vicon_generate_messages aer1217_ardrone_vicon_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/charlie/project/project/src/aer1217_ardrone_vicon/msg/MotorCommands.msg" NAME_WE)
add_dependencies(aer1217_ardrone_vicon_generate_messages_nodejs _aer1217_ardrone_vicon_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/charlie/project/project/src/aer1217_ardrone_vicon/msg/GazeboState.msg" NAME_WE)
add_dependencies(aer1217_ardrone_vicon_generate_messages_nodejs _aer1217_ardrone_vicon_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/charlie/project/project/src/aer1217_ardrone_vicon/msg/DesiredStateMsg.msg" NAME_WE)
add_dependencies(aer1217_ardrone_vicon_generate_messages_nodejs _aer1217_ardrone_vicon_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(aer1217_ardrone_vicon_gennodejs)
add_dependencies(aer1217_ardrone_vicon_gennodejs aer1217_ardrone_vicon_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS aer1217_ardrone_vicon_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(aer1217_ardrone_vicon
  "/home/charlie/project/project/src/aer1217_ardrone_vicon/msg/MotorCommands.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/aer1217_ardrone_vicon
)
_generate_msg_py(aer1217_ardrone_vicon
  "/home/charlie/project/project/src/aer1217_ardrone_vicon/msg/GazeboState.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/aer1217_ardrone_vicon
)
_generate_msg_py(aer1217_ardrone_vicon
  "/home/charlie/project/project/src/aer1217_ardrone_vicon/msg/DesiredStateMsg.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/aer1217_ardrone_vicon
)

### Generating Services

### Generating Module File
_generate_module_py(aer1217_ardrone_vicon
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/aer1217_ardrone_vicon
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(aer1217_ardrone_vicon_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(aer1217_ardrone_vicon_generate_messages aer1217_ardrone_vicon_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/charlie/project/project/src/aer1217_ardrone_vicon/msg/MotorCommands.msg" NAME_WE)
add_dependencies(aer1217_ardrone_vicon_generate_messages_py _aer1217_ardrone_vicon_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/charlie/project/project/src/aer1217_ardrone_vicon/msg/GazeboState.msg" NAME_WE)
add_dependencies(aer1217_ardrone_vicon_generate_messages_py _aer1217_ardrone_vicon_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/charlie/project/project/src/aer1217_ardrone_vicon/msg/DesiredStateMsg.msg" NAME_WE)
add_dependencies(aer1217_ardrone_vicon_generate_messages_py _aer1217_ardrone_vicon_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(aer1217_ardrone_vicon_genpy)
add_dependencies(aer1217_ardrone_vicon_genpy aer1217_ardrone_vicon_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS aer1217_ardrone_vicon_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/aer1217_ardrone_vicon)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/aer1217_ardrone_vicon
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(aer1217_ardrone_vicon_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/aer1217_ardrone_vicon)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/aer1217_ardrone_vicon
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(aer1217_ardrone_vicon_generate_messages_eus std_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/aer1217_ardrone_vicon)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/aer1217_ardrone_vicon
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(aer1217_ardrone_vicon_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/aer1217_ardrone_vicon)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/aer1217_ardrone_vicon
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(aer1217_ardrone_vicon_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/aer1217_ardrone_vicon)
  install(CODE "execute_process(COMMAND \"/usr/bin/python2\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/aer1217_ardrone_vicon\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/aer1217_ardrone_vicon
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(aer1217_ardrone_vicon_generate_messages_py std_msgs_generate_messages_py)
endif()
