AUTHOR = "jhummer"
SITESLUG = "~"
SITENAME = "THE GIST"
# SITESUBTITLE = "Ramblings and notes for Python minded"
SITEURL = ""
# INTRO_CONTENT = "This is some intro content"

STATIC_PATHS = ["images", "extra/CNAME"]
EXTRA_PATH_METADATA = {"extra/CNAME": {"path": "CNAME"}}

PATH = "content"

TIMEZONE = "Europe/Rome"

DEFAULT_LANG = "en"

THEME = "theme/pelican-clean-blog"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

MENUITEMS = (("Tags", "/tags"),)

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (("fa-brands fa-github", "https://github.com/jhummer"),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
