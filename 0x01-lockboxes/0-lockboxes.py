#!/usr/bin/python3
"""
Method to determine if all boxes can be opened
Using prototype: def canUnlockAll(boxes)
"""

def canUnlockAll(boxes):
    n = len(boxes)
    opened_boxes = set([0])  # Start with the first box being opened
    keys = [0]  # Start with the keys in the first box

    while keys:
        current_key = keys.pop()

        for key in boxes[current_key]:
            if key not in opened_boxes and key < n:
                opened_boxes.add(key)
                keys.append(key)

    return len(opened_boxes) == n
