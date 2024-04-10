Installation
Channels is available on PyPI - to install it run:

python -m pip install -U 'channels[daphne]'
This will install Channels together with the Daphne ASGI application server. If you wish to use a different application server you can pip install channels, without the optional daphne add-on.

Once that’s done, you should add daphne to the beginning of your INSTALLED_APPS setting:

INSTALLED_APPS = (
    "daphne",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    ...
)
This will install the Daphne’s ASGI version of the runserver management command.

You can also add "channels" for Channel’s runworker command.

Then, adjust your project’s asgi.py file, e.g. myproject/asgi.py, to wrap the Django ASGI application:

import os

from channels.routing import ProtocolTypeRouter
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
# Initialize Django ASGI application early to ensure the AppRegistry
# is populated before importing code that may import ORM models.
django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter({
    "http": django_asgi_app,
    # Just HTTP for now. (We can add other protocols later.)
})
And finally, set your ASGI_APPLICATION setting to point to that routing object as your root application:

ASGI_APPLICATION = "myproject.asgi.application"
That’s it! Once enabled, daphne will integrate itself into Django and take control of the runserver command. 