import py5
import random

"""
CONTROLES:
Aprieta 'B' para activar el Bubble Sort
Aprieta 'S' para activar el Selection Sort
Aprieta 'R' para activar el SetUp
"""


width = 600
height = 400
bar_width = 30
bars = []
steps = []

@py5.setup
def setup():
    global bars, steps
    py5.size(width, height)
    bars = [random.randint(10, height) for _ in range(width // bar_width)]
    steps = []

@py5.draw
def draw():
    py5.background(255)

    if steps:
        state, i, j = steps.pop(0)
        draw_bars(state, i, j)
    else:
        py5.no_loop()

def draw_bars(state, i, j):
    for idx, value in enumerate(state):
        if idx == i or idx == j:
            py5.fill(255, 0, 0)
        else:
            py5.fill(0, 0, 255)

        py5.rect(idx * bar_width, height - value, bar_width, value)

def start_bubble_sort():
    global bars, steps
    steps = bubblesort(bars)
    py5.loop()

def start_selection_sort():
    global bars, steps
    steps = selectionsort(bars)
    py5.loop()

def bubblesort(list, i=0, j=0, steps=[]):
    n = len(list)

    if i == n-1:
        return steps

    if j == n - i - 1:
        return bubblesort(list, i + 1, 0, steps)
    
    steps.append((list[:], j, j + 1))
    if list[j] > list[j + 1]:
        list[j], list[j + 1] = list[j + 1], list[j]
    
    steps.append((list[:], j, j + 1))
    return bubblesort(list, i, j + 1, steps)

def selectionsort(list, i=0, steps=[]):
    n = len(list)

    if i == n - 1:
        return steps

    x = find_x(list, i, i + 1, n)
    
    steps.append((list[:], i, x))
    list[i], list[x] = list[x], list[i]
    
    steps.append((list[:], i, x))
    return selectionsort(list, i + 1, steps)

def find_x(list, j, x, n):
    if j >= n:
        return x
    
    if list[j] < list[x]:
        x = j

    return find_x(list, j + 1, x, n)

@py5.key_pressed
def key_pressed():
    if py5.key == 'b':
        start_bubble_sort()
    elif py5.key == 's':
        start_selection_sort()
    elif py5.key == 'r':
        setup()

py5.run_sketch()
