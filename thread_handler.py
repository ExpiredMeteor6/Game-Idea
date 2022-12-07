import logging
import threading
import time

from pathfinding import PathFinder

class Threader:
    def __init__(self, startpos, endpos):
        self.pathfinder = PathFinder(startpos, endpos)

    def start_thread(self):
        self.thread = threading.Thread(target=self.pathfinder.find_route, name = "PathFinder")
        self.thread.start()

    def is_done(self):
        return self.pathfinder.is_done()

    def get_result(self):
        return self.pathfinder.route

    def destroy(self):
        self.thread.join()

