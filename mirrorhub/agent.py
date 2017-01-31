"""Submodule of mirrorhub.

Control and sync Agent which runs inside the mirror container.
"""
import socket
import time
from datetime import datetime as dt
from datetime import timedelta as td
from mirrorhub.api import APIClient
from mirrorhub.utils import exec_rsync


class Agent():
    """Agent class to control the container."""

    def __init__(self, api_token):
        """Initialize a new Agent object."""
        self.apiclient = APIClient(api_token)
        self.update()
        self.last_sync = None

    def run(self):
        """Start the agent in an endless loop."""
        self.sync_mirror()
        while True:
            if (dt.now() - self.last_sync) >= td(hours=self.sync_offset):
                self.sync_mirror()
            time.sleep(1)

    def update(self):
        """Fetch new data from the API."""
        data = self.apiclient.get_mirror_info()
        self.sync_source = data['source']
        self.sync_dest = data['dest']
        self.sync_offset = data['offset']/60

    def check_sync_source(self):
        """Check whether the rsync port is open at source.

        Returns:
            bool: true  if rsync port is open
        """
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        return bool(sock.connect_ex((self.sync_source, 873)) == 0)

    def sync_mirror(self):
        """Sync the mirrors data via rsync."""
        if self.check_sync_source():
            exec_rsync(self.sync_source, self.sync_dest)
            self.last_sync = dt.now()
        else:
            # recheck in 10min
            self.last_sync += td(hours=1/6)
