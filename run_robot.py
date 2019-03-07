#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
rsync and run robot script PyCharm run configuration
"""

from __future__ import print_function, absolute_import
import sys
import subprocess


def do_run_robot():
    subprocess.check_output(
        ['rsync', '-av', '/Users/warren/Development/src/pi_robot/', 'pi@chobot:pi_robot/']
    )
    # -t -t to ensure python process is killed when ssh is
    # python -u to ensure output is not buffered
    subprocess.call(
        ['ssh', '-t', '-t', 'pi@chobot', '/home/pi/.virtualenvs/pi_robot/bin/python -u pi_robot/robot.py'],
    )


def run():
    try:
        do_run_robot()

    except Exception as e:
        print('Error: ({}) {}'.format(e.__class__.__name__, e), file = sys.stderr)
        sys.exit(1)

    except KeyboardInterrupt:
        sys.exit(1)


if __name__ == "__main__":
    run()
