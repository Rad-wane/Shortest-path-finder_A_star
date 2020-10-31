# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 15:50:10 2020

@author: Radwane
"""
#importations :
    #for visualizations
import pygame as pg 
    #for the A* algo
from A_star_algo import h, algorithm, reconstruct_path
    #in case there was no path possible
from tkinter import *
from tkinter import messagebox
    #colors needed
from colors import *
    #for proper quiting
import sys

#Pygame initialization  
pg.init()

#window dimensions 
w=800
win = pg.display.set_mode((w,w))
pg.display.set_caption('A* Path finding Algorithm')



#the square class
class Spot():
    def __init__(self, row, col, width, total_rows ):
        self.col=col
        self.row=row
        self.x=width*row
        self.y=width*col
        self.color=white
        self.neighbors=[]
        self.width=width
        self.total_rows=total_rows
    
    #cheking the state of the spot using it's color
    def is_closed(self):
        return self.color==red
    
    def is_open(self):
        return self.color==green
    
    def is_barrier(self):
        return self.color==black
    
    def is_start(self):
        return self.color==orange
    
    def is_end(self):
        return self.color==turquoise
    
    def reset(self):
        self.color=white
    
    #setting the state of the spot using it's color       
    def make_closed(self):
        self.color=red
    
    def make_open(self):
        self.color=green
    
    def make_barrier(self):
        self.color=black
    
    def make_start(self):
        self.color=orange
    
    def make_end(self):
        self.color=turquoise
    
    def make_path(self):
        self.color=purple
    
    
    #drawing and getting the spot's position 
    def get_pos(self):
       return self.row,self.col
    
    def draw(self,win):
        pg.draw.rect(win,self.color,(self.x,self.y,self.width,self.width))
    
    #Gathering the OPEN neighbors of said spot     
    def update_neighbors(self,grid):
        self.neighbors = []
        if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_barrier():#down
            self.neighbors.append(grid[self.row + 1][self.col])
            
        if self.row > 0 and not grid[self.row - 1][self.col].is_barrier():#up
            self.neighbors.append(grid[self.row - 1][self.col])
            
        if self.col < self.total_rows - 1 and not grid[self.row][self.col+1].is_barrier():#right
            self.neighbors.append(grid[self.row][self.col+1])
            
        if self.col > 0 and not grid[self.row][self.col-1].is_barrier():#left
            self.neighbors.append(grid[self.row][self.col-1])

            
#making the grid and the spots:
    #making the grid
def make_grid(rows,width):
    grid =[]
    gap=width//rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            spot=Spot(i,j,gap,rows)
            grid[i].append(spot)
    return grid
    #drawing the grid    
def draw_grid(win, rows, width):        
    gap=width//rows   
    for i in range(rows):
        pg.draw.line(win,grey,(0,i*gap),(width, i*gap))
    for j in range(rows):
        pg.draw.line(win,grey,(j*gap,0),(j*gap, width))
    #putting all together    
def draw(win, grid, rows, width):
    win.fill(white)
    for row in grid:
        for spot in row:
            gap=width//rows   
            if spot.x==0 or spot.y ==0 or spot.x==width-gap or spot.y ==width-gap:
                spot.make_barrier()
            spot.draw(win)    
    draw_grid(win, rows, width)
    pg.display.update()
        

#getting the mouse position in term of rows and columns:
def get_clicked_pos(pos, rows,width):
    gap=width//rows
    x,y=pos
    row=x//gap
    col=y//gap
    return row,col
        
def main(win,width):
    ROWS=50
    grid =make_grid(ROWS, width)
    start=None
    end=None    
    run=True
    started=False
    while run:
        draw(win,grid,ROWS,width)
        for event in pg.event.get():
            if event.type==pg.QUIT:
                run=False
            if started:
                continue
            if pg.mouse.get_pressed()[0]:
                pos=pg.mouse.get_pos()
                row,col= get_clicked_pos(pos, ROWS, width)
                spot=grid[row][col]
                if not start and spot != end:
                    start=spot
                    start.make_start()
                elif not end and spot != start:
                    end=spot
                    end.make_end()
                elif spot != end and spot != start:
                    spot.make_barrier()
            elif pg.mouse.get_pressed()[2]:
                pos=pg.mouse.get_pos()
                row,col= get_clicked_pos(pos, ROWS, width)
                spot=grid[row][col]
                spot.reset()
                if spot==start:
                    start=None
                if spot==end:
                    end=None
            if event.type==pg.KEYDOWN:
                if event.key==pg.K_SPACE and start and end:
                    for row in grid:
                        for spot in row:
                            spot.update_neighbors(grid)
                    algorithm(lambda: draw(win, grid, ROWS, width), grid, start, end)
                if event.key == pg.K_c:
                    start = None
                    end = None
                    grid = make_grid(ROWS, width)
    pg.quit()
    sys.exit()
    
    
main (win, w)    
    
    
    
    
    
        
        
        
        
        
        
        
        
    