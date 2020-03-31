#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Koren Nyles, Chris Wilson, Sean Bailey"

import logging
import datetime
import time
import argparse
import signal
import os

logger = logging.getLogger(__file__)
exit_flag = False
watching_files = {}

def watch_directory(args):
    logger.info('Watching Directory: {}, File Ext: =  {}, Polling Interval: {}, Magic Text: {}'.format(
                args.path, args.ext, args.interval, args.magic
    ))

    # Keys are the actual filename and the values are where to begin seaching

    # Look at directory and get a list of files from it.
    # Add those to dictionary if not already present, and log as new file

    # Look through your "watching _files" dict and compare
    # that to a list of files that is in the directory

    # If file is not in your dict anymore you have
    # to log the file and remove it from your dict

    # Iterate through dict, open each file at the last line that you read from,
    # Start reading from that point looking for any "magic" text

    # Update the last position that you read from in the dict

    while True:
        try:
            logger.info('Inside Watch Loop')
            time.sleep(args.interval)
        except KeyboardInterrupt:
            break


def find_magic(filename, starting_line, magic_word):
    pass


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-e', '--ext', type=str, default='.txt',
                        help='Text file extension to watch')
    parser.add_argument('-i', '--interval', type=float,
                        default=1.0, help='Number of seconds between polling')
    parser.add_argument('path', help='Directory path to watch')
    parser.add_argument('magic', help='String to watch for')
    return parser

def main():
    logging.basicConfig(
        format='%(asctime)s.%(msecs)03d %(name)-12s %(levelname)-8s [%(threadName)- 12s] %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    logger.setLevel(logging.DEBUG)
    app_start_time = datetime.datetime.now()
    logger.info(
        '\n'
        '------------------------------------------------------------\n'
        '       Running{0}\n'
        '       Started on {1}\n'
        '------------------------------------------------------------\n'
        .format(__file__, app_start_time.isoformat())
    )
    parser = create_parser()
    args = parser.parse_args()
    watch_directory(args)
    uptime = datetime.datetime.now() - app_start_time
    logger.info(
        '\n'
        '------------------------------------------------------------\n'
        '       Stopped{0}\n'
        '       Uptime was {1}\n'
        '------------------------------------------------------------\n'
        .format(__file__, str(uptime))
    )


if __name__ == '__main__':
    main()
