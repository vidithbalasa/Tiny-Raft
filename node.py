from enum import Enum, auto

class Role(Enum):
    FOLLOWER = auto()
    CANDIDATE = auto()
    LEADER = auto()

class Node:
    def __init__(self, node_id, role):
        self.node_id = node_id
        self.term = 1 # Number of elections (including initial)
        self.role = role
        self.log = []
        self.voted_for = None

