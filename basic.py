"""
This template is written by @cormo1990
What does this quickstart script aim to do?
- Basic follow/unfollow activity.
NOTES:
- I don't want to automate comment and too much likes because I want to do
this only for post that I really like the content so at the moment I only
use the function follow/unfollow.
- I use two files "quickstart", one for follow and one for unfollow.
- I noticed that the most important thing is that the account from where I
get followers has similar contents to mine in order to be sure that my
content could be appreciated. After the following step, I start unfollowing
the user that don't followed me back.
- At the end I clean my account unfollowing all the users followed with
InstaPy.
"""

# imports
from instapy import InstaPy
from instapy import smart_run

# login credentials
insta_username = ''
insta_password = ''

# get an InstaPy session!
# set headless_browser=True to run InstaPy in the background
session = InstaPy(username=insta_username,
                  password=insta_password,
                  bypass_suspicious_attempt=True,
                  headless_browser=True)
while True:
    with smart_run(session):
        """ Activity flow """
        # general settings
        session.set_relationship_bounds(enabled=True,
                                        delimit_by_numbers=True,
                                        max_followers=4590,
                                        min_followers=45,
                                        min_following=77)

        session.set_quota_supervisor(enabled=True,
                                sleep_after=["likes", "follows", "unfollows", "server_calls_h"],
                                sleepyhead=True,
                                stochastic_flow=True,
                                notify_me=True,
                                peak_likes=(57, None),
                                peak_follows=(48, 689),
                                peak_unfollows=(35, 402))

        session.set_do_like(True, percentage=33)
        session.set_dont_unfollow_active_users(enabled=True, posts=5)
        session.set_user_interact(amount=3, percentage=45, randomize=True, media='Photo')
        

        # activities

        """ Massive Follow of users followers (I suggest to follow not less than
        3500/4000 users for better results)...
        """
        session.follow_user_followers(['lonebrain', 'lauren_burch_', 'jazxsophie'], amount=800,
                                    randomize=False, interact=True)

        session.like_by_tags(['tumblraesthetics', 'softgrunge'], amount=200, interact=True)

        """ First step of Unfollow action - Unfollow not follower users...
        """
        session.unfollow_users(amount=421, InstapyFollowed=(True, "nonfollowers"),
                            style="FIFO",
                            unfollow_after=12 * 60 * 60, sleep_delay=642)

