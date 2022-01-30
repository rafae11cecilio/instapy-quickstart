# imports
from instapy import InstaPy
from instapy import smart_run

# login credentials
insta_username = 'oiboston'
insta_password = '2Adrecega'

comments = [
    u'✨✨✨✨',
    u'👊👊👊👊',
    u'👏👏👏👏',
    u'🙌🙌🙌🙌',
    u'👍👍👍👍',
    u'👍👊',
    u'👊👊',
    u'👏👏',
    u'👏👏👏',
    u'🙌🙌🙌'
    ]

# get an InstaPy session!
# set headless_browser=True to run InstaPy in the background
session = InstaPy(username=insta_username,
                  password=insta_password,
                  want_check_browser=False,
                  headless_browser=True,
                  disable_image_load=True)

with smart_run(session):
  """ Activity flow """		
  # general settings		
  #session.set_dont_include(["friend1", "friend2", "friend3"])
  session.set_skip_users(   skip_private=False,
                            skip_no_profile_pic=True,
                            skip_business=True)

  
  # activity		
  #session.like_by_tags(["natgeo"], amount=10)
  session.follow_commenters(['myworldbydaniela'], amount=120, daysold=100, max_pic=10, sleep_delay=500, interact=True)

    """ Joining Engagement Pods...
    """
    session.join_pods()
