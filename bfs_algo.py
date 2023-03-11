from collections import deque
"""
Graph example:
    graph = {}
    graph['you'] = ['nik', 'ita', 'ashira']
    graph['nik'] = ['vasya', 'josh']
    graph['ita'] = []
    graph['ashira'] = ['kirya', 'danym']
    graph['vasya'] = []
    graph['josh'] = []
    graph['kirya'] = []
    graph['danym'] = []
Queue creation for searching:
    search_deque = deque()
    search_deque += graph['you']
"""

def person_is_seller(person: str):
    if person[-1] == 'm':
        return True
    return False

def bfs_search(graph: dict, search_deque: deque):
    while search_deque:
        person = search_deque.popleft()
        if person_is_seller(person):
            print(f"> We found it!\n> {person} is seller!")
            return 0
        else:
            search_deque += graph[person]
    print("> We didn't find it")
    return -1
