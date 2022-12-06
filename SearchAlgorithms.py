from Space import *
from Constants import *

def DFS(g:Graph, sc:pygame.Surface):
    print('Implement DFS algorithm')

    open_set = [g.start]
    closed_set = []
    father = [-1]*g.get_len()

    while (len(open_set) > 0):
        current = open_set.pop(-1)
        if (current in closed_set):
            continue
        closed_set.append(current)
        current.set_color(yellow)
        g.draw(sc)
        if (g.is_goal(current)):
            print("bingo")
            break
        for element in g.get_neighbors(current):
            if (element in closed_set):
                continue
            else:
                open_set.append(element)
                father[element.value] = current
                element.set_color(red)
                g.draw(sc)
        current.set_color(blue)
        g.draw(sc)

    #TODO: Implement BFS algorithm using open_set, closed_set, and father
    #raise NotImplementedError('Not implemented')
    current = g.goal
    while (current != g.start):
        current.set_color(grey)
        current.drawline(sc, father[current.value])
        current = father[current.value]
        g.draw(sc)
    pass

def BFS(g:Graph, sc:pygame.Surface):
    print('Implement BFS algorithm')

    open_set = [g.start]
    closed_set = []
    father = [-1]*g.get_len()

    while (len(open_set) > 0):
        current = open_set.pop(0)
        if (current in closed_set):
            continue
        closed_set.append(current)
        current.set_color(yellow)
        g.draw(sc)
        if (g.is_goal(current)):
            print("bingo")
            break
        for element in g.get_neighbors(current):
            if (element in closed_set):
                continue
            else:
                open_set.append(element)
                father[element.value] = current
                element.set_color(red)
                g.draw(sc)
        current.set_color(blue)
        g.draw(sc)

    #TODO: Implement BFS algorithm using open_set, closed_set, and father
    #raise NotImplementedError('Not implemented')
    current = g.goal
    while (current != g.start):
        current.set_color(grey)
        current.drawline(sc, father[current.value])
        current = father[current.value]
        g.draw(sc)
    pass

def UCS(g:Graph, sc:pygame.Surface):
    print('Implement UCS algorithm')

    open_set = {}
    open_set[g.start.value] = 0
    closed_set:list[int] = []
    father = [-1]*g.get_len()
    cost = [100_000]*g.get_len()
    cost[g.start.value] = 0

    #TODO: Implement UCS algorithm using open_set, closed_set, and father
    raise NotImplementedError('Not implemented')
