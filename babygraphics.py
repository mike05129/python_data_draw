"""
File: babygraphics.py
Name: 
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
from tkinter.constants import ANCHOR
from typing import Text
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    X_Coordinaate = CANVAS_WIDTH/len(YEARS)         
    return GRAPH_MARGIN_SIZE + (X_Coordinaate)*year_index


def get_y_coordinate(height, rank):
    """
    Given the height of the canvas and the rank of the current year
    returns the y coordinate where the rank should be drawn.

    Input:
        height (int): The height of the canvas
        rank (str): The rank number
    Returns:
        y_coordinate (int): The y coordinate of the rank.
    """
    pass


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #

    canvas.create_line(GRAPH_MARGIN_SIZE,GRAPH_MARGIN_SIZE,CANVAS_WIDTH-GRAPH_MARGIN_SIZE,GRAPH_MARGIN_SIZE)
    canvas.create_line(GRAPH_MARGIN_SIZE,CANVAS_HEIGHT-GRAPH_MARGIN_SIZE,CANVAS_WIDTH-GRAPH_MARGIN_SIZE,CANVAS_HEIGHT-GRAPH_MARGIN_SIZE)
    for Num_year in range (len(YEARS)):
        x_coordinate = get_x_coordinate(CANVAS_WIDTH,Num_year)
        canvas.create_line (x_coordinate,0,x_coordinate,CANVAS_HEIGHT) 
        canvas.create_text(x_coordinate+TEXT_DX,CANVAS_HEIGHT-GRAPH_MARGIN_SIZE,text =YEARS[Num_year],anchor=tkinter.NW)

def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # ----- Write your code below this line ----- #                                                                                           
    for draw_names in lookup_names:
        y_rank_coordiate=[]  
        for year in YEARS: # get rank heigh
            if str(year) in name_data[draw_names].keys(): #check year exist
                rank = name_data[draw_names][str(year)]
                y_rank_coordiate.append(round((int(rank)*14)/25+20,1))           
            else:
                y_rank_coordiate.append(str(CANVAS_HEIGHT-GRAPH_MARGIN_SIZE))
        for rank_coordiate in range(len(y_rank_coordiate)-1):
            First_x=get_x_coordinate(CANVAS_WIDTH,rank_coordiate)
            Sec_x=get_x_coordinate(CANVAS_WIDTH,rank_coordiate+1)
            canvas.create_line (First_x,y_rank_coordiate[rank_coordiate],Sec_x,y_rank_coordiate[rank_coordiate+1]) 
        
   
        
                
        #canvas.create_line(CANVAS_WIDTH,(name_data[draw_names][str(year)]))            
   #important!!!! year is int so u need to convert to str, otherwise it will show err key
   #important!!!! err key doesn't means key can't find,it jsut can't compare 
   # ----------------waste a lot of my time!!!! --------------------           
"""for draw_names in lookup_names:      #Don't need to check name exist     
        for dict_name_key,dict_year_key in name_data.items():
            if draw_names in dict_name_key:
                for year in YEARS:
                    for key in dict_year_key:
                        if  str(year) in key:
                            rank = name_data[draw_names][str(year)]
                            print(rank)"""             
                
    



# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
