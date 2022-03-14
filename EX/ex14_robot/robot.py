"""Robot."""
from FollowerBot import FollowerBot


def test_run(robot: FollowerBot):
    """
    Make the robot move, doesnt matter how much, just as long as it has moved from the starting position.

    :param FollowerBot robot: instance of the robot that you need to make move
    """
    robot.set_wheels_speed(30)
    robot.sleep(2)
    robot.set_wheels_speed(0)
    robot.done()


def drive_to_line(robot: FollowerBot, is_done: bool = True):
    """
    Drive the robot until it meets a perpendicular black line, then drive forward 25cm.

    There are 100 pixels in a meter.

    :param FollowerBot robot: instance of the robot that you need to make move
    :param is_done:
    """
    while robot.get_second_line_sensor_from_left() != 0 and robot.get_second_line_sensor_from_right() != 0:
        robot.set_wheels_speed(100)
        robot.sleep(0.05)

    if is_done:
        robot.set_wheels_speed(25)
        robot.sleep(1)

        robot.set_wheels_speed(0)
        robot.done()


def out_of_bounds(robot: FollowerBot):
    """Check if robot is still on track."""
    for sensor in range(6):
        if robot.get_line_sensors()[sensor] == 0:
            return False

    return True


def follow_the_line(robot: FollowerBot, is_done: bool = True):
    """
    Create a FollowerBot that will follow a black line until the end of that line.

    The robot's starting position will be just short of the start point of the line.

    :param FollowerBot robot: instance of the robot that you need to make move
    :param is_done:
    """
    drive_to_line(robot, False)

    while not out_of_bounds(robot):
        robot.set_wheels_speed(100)

        if robot.get_left_line_sensor() != 0 and robot.get_right_line_sensor() != 0 and robot.get_third_line_sensor_from_right() == 0:
            robot.set_left_wheel_speed(-50)

        elif robot.get_right_line_sensor() != 0 and robot.get_left_line_sensor() != 0 and robot.get_third_line_sensor_from_left() == 0:
            robot.set_right_wheel_speed(-50)

        elif robot.get_second_line_sensor_from_left() != 0:
            robot.set_left_wheel_speed(65)

        elif robot.get_second_line_sensor_from_right() != 0:
            robot.set_right_wheel_speed(65)

        elif robot.get_left_line_sensor() != 0:
            robot.set_left_wheel_speed(75)

        elif robot.get_right_line_sensor() != 0:
            robot.set_right_wheel_speed(75)

        robot.sleep(0.01)

    if is_done:
        robot.set_wheels_speed(0)
        robot.done()


def the_true_follower(robot: FollowerBot):
    """
    Create a FollowerBot that will follow the black line on the track and make it ignore all possible distractions.

    :param FollowerBot robot: instance of the robot that you need to make move
    """
    did_cross = False

    while robot.get_left_line_sensor() != 642:
        while out_of_bounds(robot):
            robot.set_wheels_speed(100)
            robot.sleep(0.7)

        follow_the_line(robot, False)

    robot.set_left_wheel_speed(-100)
    robot.set_right_wheel_speed(100)
    robot.sleep(2)

    while not did_cross:
        if out_of_bounds(robot):
            robot.set_wheels_speed(100)
            robot.sleep(0.8)
            did_cross = True

        follow_the_line(robot, did_cross)
