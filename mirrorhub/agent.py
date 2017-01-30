"""Submodule of mirrorhub.

Control and sync Agent which runs inside the mirror container.
"""
import time
from datetime import datetime as dt
from datetime import timedelta as td
from mirrorhub.utils import exec_rsync


class Agent():
    """Agent class to control the container."""

    def __init__(self, sync_source, sync_dest, sync_offset=60):
        """Initialize a new Agent object."""
        self.sync_source = sync_source
        self.sync_dest = sync_dest
        self.sync_offset = sync_offset/60
        self.last_sync = None

    def run(self):
        """Start the agent in an endless loop."""
        self.sync_mirror()
        while True:
            if (dt.now() - self.last_sync) >= td(hours=self.sync_offset):
                self.sync_mirror()
            time.sleep(1)

    def sync_mirror(self):
        """Sync the mirrors data via rsync."""
        # TODO check whether the source is available
        exec_rsync(self.sync_source, self.sync_dest)
        self.last_sync = dt.now()
