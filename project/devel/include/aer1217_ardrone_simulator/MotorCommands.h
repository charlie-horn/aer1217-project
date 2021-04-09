// Generated by gencpp from file aer1217_ardrone_simulator/MotorCommands.msg
// DO NOT EDIT!


#ifndef AER1217_ARDRONE_SIMULATOR_MESSAGE_MOTORCOMMANDS_H
#define AER1217_ARDRONE_SIMULATOR_MESSAGE_MOTORCOMMANDS_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace aer1217_ardrone_simulator
{
template <class ContainerAllocator>
struct MotorCommands_
{
  typedef MotorCommands_<ContainerAllocator> Type;

  MotorCommands_()
    : motor_cmd()  {
      motor_cmd.assign(0.0);
  }
  MotorCommands_(const ContainerAllocator& _alloc)
    : motor_cmd()  {
  (void)_alloc;
      motor_cmd.assign(0.0);
  }



   typedef boost::array<double, 4>  _motor_cmd_type;
  _motor_cmd_type motor_cmd;





  typedef boost::shared_ptr< ::aer1217_ardrone_simulator::MotorCommands_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::aer1217_ardrone_simulator::MotorCommands_<ContainerAllocator> const> ConstPtr;

}; // struct MotorCommands_

typedef ::aer1217_ardrone_simulator::MotorCommands_<std::allocator<void> > MotorCommands;

typedef boost::shared_ptr< ::aer1217_ardrone_simulator::MotorCommands > MotorCommandsPtr;
typedef boost::shared_ptr< ::aer1217_ardrone_simulator::MotorCommands const> MotorCommandsConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::aer1217_ardrone_simulator::MotorCommands_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::aer1217_ardrone_simulator::MotorCommands_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace aer1217_ardrone_simulator

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': True, 'IsMessage': True, 'HasHeader': False}
// {'aer1217_ardrone_simulator': ['/home/charlie/aer1217/labs/src/aer1217_ardrone_simulator/msg'], 'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::aer1217_ardrone_simulator::MotorCommands_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::aer1217_ardrone_simulator::MotorCommands_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::aer1217_ardrone_simulator::MotorCommands_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::aer1217_ardrone_simulator::MotorCommands_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::aer1217_ardrone_simulator::MotorCommands_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::aer1217_ardrone_simulator::MotorCommands_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::aer1217_ardrone_simulator::MotorCommands_<ContainerAllocator> >
{
  static const char* value()
  {
    return "424a0da2970783751aa94563cd70d0bb";
  }

  static const char* value(const ::aer1217_ardrone_simulator::MotorCommands_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x424a0da297078375ULL;
  static const uint64_t static_value2 = 0x1aa94563cd70d0bbULL;
};

template<class ContainerAllocator>
struct DataType< ::aer1217_ardrone_simulator::MotorCommands_<ContainerAllocator> >
{
  static const char* value()
  {
    return "aer1217_ardrone_simulator/MotorCommands";
  }

  static const char* value(const ::aer1217_ardrone_simulator::MotorCommands_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::aer1217_ardrone_simulator::MotorCommands_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# MotorCommands\n\
#\n\
# Rikky Duivenvoorden 2017-01-30 -- For use in AER1217 Winter 2017\n\
#\n\
# Data communicates the motor commands in RPM as a four element array in the\n\
# following order [front_left, front_right, rear_left, rear_right]\n\
\n\
float64[4] motor_cmd\n\
";
  }

  static const char* value(const ::aer1217_ardrone_simulator::MotorCommands_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::aer1217_ardrone_simulator::MotorCommands_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.motor_cmd);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct MotorCommands_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::aer1217_ardrone_simulator::MotorCommands_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::aer1217_ardrone_simulator::MotorCommands_<ContainerAllocator>& v)
  {
    s << indent << "motor_cmd[]" << std::endl;
    for (size_t i = 0; i < v.motor_cmd.size(); ++i)
    {
      s << indent << "  motor_cmd[" << i << "]: ";
      Printer<double>::stream(s, indent + "  ", v.motor_cmd[i]);
    }
  }
};

} // namespace message_operations
} // namespace ros

#endif // AER1217_ARDRONE_SIMULATOR_MESSAGE_MOTORCOMMANDS_H
