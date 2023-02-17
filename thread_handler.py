import logging
import threading
import time

from pathfinding import PathFinder

class Threader:
    def __init__(self, startpos, endpos, level):
        self.pathfinder = PathFinder(startpos, endpos, level)

    #Starts the processing the thread
    def start_thread(self):
        self.thread = threading.Thread(target=self.pathfinder.find_route, name = "PathFinder")
        self.thread.start()

    #Checks if pathfinder has found the route
    def is_done(self):
        return self.pathfinder.is_done()

    #Gets the route found by the path finder
    def get_result(self):
        return self.pathfinder.route

    #Joins the thread to the main process (destroying it)
    def destroy(self):
        self.thread.join()

