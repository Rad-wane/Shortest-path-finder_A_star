# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 17:14:33 2020

@author: radwane
"""
   
from queue import PriorityQueue
import pygame as pg
 #in case there was no path possible
from tkinter import *



#h_score function (heuristic, using L distance)
def h(p1,p2):
    x1,y1=p1
    x2,y2=p2
    return abs(x1-x2)+abs(y1-y2)

# the A* star algo
def algorithm(draw, grid, start, end):
    count=0
    open_set=PriorityQueue()
    open_set.put((0, count, start))
    came_from={}
    #setting the g and f scores to infinity of all the grid except for start and end
    g_score={spot: float("inf") for row in grid for spot in row}
    g_score[start]=0
    f_score={spot: float("inf") for row in grid for spot in row}
    f_score[start] = h(start.get_pos(), end.get_pos())
    
    # Hashing the open_set
    open_set_hash = {start}
    
    while not open_set.empty():
        #In case we close during algo
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
        
        current=open_set.get()[2]
        open_set_hash.remove(current)
        if current == end:
            reconstruct_path(came_from, end, draw)
            end.make_end()
            start.make_start()
            return True
        
        for neighbor in current.neighbors:
            temp_g_score = g_score[current] + 1 #g score is just 1 for each spot 
            if temp_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = temp_g_score
                f_score[neighbor] = temp_g_score + h(neighbor.get_pos(), end.get_pos())
                if neighbor not in open_set_hash:
                    count += 1
                    open_set.put((f_score[neighbor], count, neighbor))
                    open_set_hash.add(neighbor)
                    neighbor.make_open()
        draw()
        if current != start:
            current.make_closed()
    Tk().wm_withdraw() #to hide the main window
    messagebox.showinfo('Path is impossible','Path is impossible to find\nTo clear all, press \'c\'')
    return False

#when found, func to reconstruct the shortest path
def reconstruct_path(came_from, current, draw):
	   while current in came_from:
		    current = came_from[current]
		    current.make_path()
		    draw()