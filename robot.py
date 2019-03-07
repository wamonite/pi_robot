#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, absolute_import
from gpiozero import CamJamKitRobot
from controller import Controller


THRESHOLD = 0.2


def run_robot():
    robot = CamJamKitRobot()
    controller = Controller('/dev/input/js0', debug = True)
    pos_l = 0.0
    pos_r = 0.0
    while True:
        event_info = controller.process_event()
        if event_info:
            event_name, event_value = event_info

            updated = False
            if event_name == 'y':
                pos_l = -event_value if event_value > THRESHOLD or event_value < -THRESHOLD else 0.0
                updated = True

            if event_name == 'ry':
                pos_r = -event_value if event_value > THRESHOLD or event_value < -THRESHOLD else 0.0
                updated = True

            if updated:
                robot.value = (pos_l, pos_r)


if __name__ == '__main__':
    run_robot()
