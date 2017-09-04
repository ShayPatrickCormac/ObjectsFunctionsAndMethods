"""
This module lets you practice  ** using objects **, including:
  -- CONSTRUCTING objects,
  -- applying METHODS to them, and
  -- accessing their DATA via INSTANCE VARIABLES

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Zijian Huang.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    two_circles()
    circle_and_rectangle()
    lines()

    """ Calls the other functions to demonstrate and/or test them. """
    # Test your functions by putting calls to them here:


def two_circles():
    window=rg.RoseWindow(400,300,"1")
    center_point=rg.Point(200,200)
    circle_1=rg.Circle(center_point,30)
    circle_1.fill_color="blue"
    circle_2=rg.Circle(center_point,100)
    circle_1.attach_to(window)
    circle_2.attach_to(window)
    window.render()
    window.close_on_mouse_click()
    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws two rg.Circle objects on the window
         such that:
           -- They fit in the window and are easily visible.
           -- They have different radii.
           -- One is filled with some color and one is not filled.
    -- Waits for the user to press the mouse, then closes the window.
    """
    # ------------------------------------------------------------------
    # DONE: 2. Implement this function, per its doc-string above.
    #    -- ANY two rg.Circle objects that meet the criteria are fine.
    #    -- File  COLORS.txt  lists all legal color-names.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    # ------------------------------------------------------------------


def circle_and_rectangle():
    window = rg.RoseWindow(500, 500, "2")
    circle=rg.Circle(rg.Point(200,100),50)
    circle.fill_color="blue"
    rect=rg.Rectangle(rg.Point(65,80),rg.Point(200,240))
    circle.attach_to(window)
    rect.attach_to(window)
    print("circle","outline","thickness",circle.outline_thickness)
    print("circle","color",circle.fill_color)
    print("circle","center",circle.center)
    print("circle","center's","x","coordinate",circle.center.x)
    print("circle","center's","y","coordinate",circle.center.y)
    print("rect","outline","thickness",rect.outline_thickness)
    print("rect","color",rect.fill_color)
    print("rect","center",rect.get_center())
    print("rect","center's","x",rect.get_center().x)
    print("rect","center's","y",rect.get_center().y)
    window.render()
    window.close_on_mouse_click()

    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws a rg.Circle and rg.Rectangle
       on the window such that:
          -- They fit in the window and are easily visible.
          -- The rg.Circle is filled with 'blue'
    -- Prints (on the console, on SEPARATE lines) the following data
         associated with your rg.Circle:
          -- Its outline thickness.
          -- Its fill color.
          -- Its center.
          -- Its center's x coordinate.
          -- Its center's y coordinate.
    -- Prints (on the console, on SEPARATE lines) the same data
         but for your rg.Rectangle.
    -- Waits for the user to press the mouse, then closes the window.

    Here is an example of the output on the console,
    for one particular circle and rectangle:
           1
           blue
           Point(180.0, 115.0)
           180
           115
           1
           None
           Point(75.0, 150.0)
           75.0
           150.0
    """
    # ------------------------------------------------------------------
    # DONE: 3. Implement this function, per its doc-string above.
    #   -- ANY objects that meet the criteria are fine.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    #
    # IMPORTANT: Use the DOT TRICK to guess the names of the relevant
    #       instance variables for outline thickness, etc.
    # ------------------------------------------------------------------


def lines():
    window=rg.RoseWindow(500,500)
    line_1=rg.Line(rg.Point(30,60),rg.Point(180,60))
    line_1.attach_to(window)
    line_2=rg.Line(rg.Point(30,200),rg.Point(180,200))
    line_2.thickness=10
    line_2.get_midpoint()
    line_2.attach_to(window)
    print("line_2","midpoint",line_2.get_midpoint())
    print("line_2","midpoint","x",line_2.get_midpoint().x)
    print("line_2","midpoint","y",line_2.get_midpoint().y)
    window.render()
    window.close_on_mouse_click()
    """
    -- Constructs a rg.RoseWindow.
    -- Constructs and draws on the window two rg.Lines such that:
          -- They both fit in the window and are easily visible.
          -- One rg.Line has the default thickness.
          -- The other rg.Line is thicker (i.e., has a bigger width).
    -- Uses a rg.Line method to get the midpoint (center) of the
         thicker rg.Line.
    -- Then prints (on the console, on SEPARATE lines):
         -- the midpoint itself
         -- the x-coordinate of the midpoint
         -- the y-coordinate of the midpoint

       Here is an example of the output on the console, if the two
       endpoints of the thicker line are at (100, 100) and (121, 200):
            Point(110.5, 150.0)
            110.5
            150.0

    -- Waits for the user to press the mouse, then closes the window.
    """
    # ------------------------------------------------------------------
    # DONE: 4. Implement and test this function.
    # ------------------------------------------------------------------


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
