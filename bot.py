#!/usr/bin/env python

import argparse
import logging
import praw


def main(args):
    # Setup logging
    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)
    logger = logging.getLogger('prawcore')
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)

    # Create a new praw instance
    reddit = praw.Reddit(args.bot)

    # Your code goes here ...


if __name__ == "__main__":
    # Command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-b', '--bot',
        required=False,
        default='bot1',
        help='Name of the bot to use from praw.ini. Default: bot1'
    )
    args = parser.parse_args()

    main(args)
