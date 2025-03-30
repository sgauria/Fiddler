# Me: "I want to write a python script to create an animation to display a sequence of rectangles. Could you provide some code for that."
# ChatGPT: Most of the Code below.
# Me: Tweaks to actually do fiddler stuff.

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.animation as animation
import random

# Create a figure and a set of subplots
fig, ax = plt.subplots()

# Set the limits of the plot
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)

# Function to initialize the animation
def init():
    # Clear the current plot
    ax.clear()
    # Set the limits again because clearing the plot will remove them
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    return []


# List of rectangles in format (x,y,w,h)
my_rects = []
idxLo = -1
idxHi = -1


# Function to update the animation at each frame
def update(frame):
    global my_rects
    global idxLo
    global idxHi
    print(frame)
    # Clear the current plot to draw the new rectangle
    ax.clear()

    # Set the limits again because clearing the plot will remove them
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_title(f"Frame {frame}")

    if (frame > 0):
        for i in range(idxLo, idxHi+1):
            if (frame > 1):
                oldx, oldy, oldw, oldh = my_rects[i]
            else:
                oldx, oldy, oldw, oldh = 0,0,1,0

            # Split the old_w and create a new rectangle above.
            neww = random.random() * oldw
            newh = oldw - neww
            newx = oldx
            newy = oldy + oldh
            my_rects.append((newx,newy,neww,newh))
            
            if (frame > 1):
                # Split the old_h and create a new rectangle to the right.
                newh = random.random() * oldh
                neww = oldh - newh
                newx = oldx + oldw
                newy = oldy
                my_rects.append((newx,newy,neww,newh))
            
        
        idxLo, idxHi = idxHi+1, idxHi+(2**(frame-1))

    # Add the rectangles to the plot
    rects = []
    for my_rect in my_rects:
        x,y,w,h = my_rect
        rect = patches.Rectangle((x, y), w, h, linewidth=1, edgecolor='r', facecolor=(0,w,h)) 
        rects.append(rect)
        ax.add_patch(rect)

    return rects

# Create the animation object
ani = animation.FuncAnimation(fig, update, frames=range(13), init_func=init, blit=True, interval=500, repeat=False)

if (1):
    # Write the output file.
    ani.save("Fiddler_2024_05_31_anim_color.mp4")
else :
    # Show the animation
    plt.show()

