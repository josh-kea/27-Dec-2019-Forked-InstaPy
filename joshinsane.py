"""
This template is written by @Joshua

What does this quickstart script aim to do?
- My quickstart is just for follow/unfollow users.

NOTES:
- It uses schedulers to trigger activities in chosen hours and also, sends me
  messages through Telegram API.
"""

# -*- coding: UTF-8 -*-
import time
from datetime import datetime
import schedule
import requests

from instapy import InstaPy
from instapy import smart_run

insta_username = ''
insta_password = ''


def get_session():
    session = InstaPy(username=insta_username,
                      password=insta_password,
                      headless_browser=True,
                      nogui=True,
                      bypass_suspicious_attempt=True,
                      multi_logs=False)

    return session


def follow():
    # get a session!
    session = get_session()
    session.set_relationship_bounds(enabled=True,
                                    delimit_by_numbers=True,
                                    max_followers=4590,
                                    min_followers=45,
                                    min_following=77)

    # let's go!
    with smart_run(session):
                # settings
                session.set_relationship_bounds(enabled=True, potency_ratio=1.21)

                # activity
                session.follow_user_followers(['danibeautystore', 'chocorea.beauty', 'soaestheticshop'], amount=197, randomize=False, interact=False)


def unfollow():
    # get a session!
    session = get_session()

    # let's go!
    with smart_run(session):
        # settings
        session.set_relationship_bounds(enabled=False, potency_ratio=0.9)

        # actions
        session.unfollow_users(amount=521, InstapyFollowed=(True, "all"),style="FIFO",unfollow_after=12 * 60 * 60, sleep_delay=672)
      


# schedulers
schedule.every().day.at("09:30").do(follow)

schedule.every().day.at("00:05").do(unfollow)

#schedule.every().wednesday.at("03:00").do(xunfollow)

while True:
    schedule.run_pending()
    time.sleep(1)