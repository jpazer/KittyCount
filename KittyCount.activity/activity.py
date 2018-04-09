from olpcgames import activity
from gettext import gettext as _

class Activity(activity.PyGameActivity):
    """Your Sugar activity"""
    
    game_name = 'main:main'
    game_title = _('KittyCount')
    game_size = None
