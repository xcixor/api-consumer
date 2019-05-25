"""App entry point."""

import os

from  app import create_app

API = create_app('development')

if __name__ == '__main__':
    API.run()