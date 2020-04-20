import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import random

class IA:
    @staticmethod
    # Create figure and axes
    def _draw_box(x_lo, x_up, y_lo, y_up, edgecolor='black', facecolor='blue', ax=None):
        if ax is None: ax = plt.gca()
        xy = (x_lo,y_lo)
        width  = x_up-x_lo
        height = y_up-y_lo
        # Create a Rectangle patch
        rect = patches.Rectangle(xy,width,height,linewidth=1,edgecolor=edgecolor,facecolor=facecolor)
        # Add the patch to the Axes
        ax.add_patch(rect)
        ax.autoscale()
        return ax

    @staticmethod
    def draw_box(b, edgecolor='black', facecolor='blue', ax=None):
        b_lo, b_up = b.lb(), b.ub()
        return _draw_box(b_lo[0], b_up[0], b_lo[1], b_up[1], edgecolor, facecolor, ax)

    @staticmethod
    def rand_interval(i):
        x = i.lb() + random.random()*(i.ub()-i.lb())
        return x


# Create figure and axes
def _draw_box(x_lo, x_up, y_lo, y_up, edgecolor='black', facecolor='blue', ax=None):
    if ax is None: ax = plt.gca()
    xy = (x_lo,y_lo)
    width  = x_up-x_lo
    height = y_up-y_lo
    # Create a Rectangle patch
    rect = patches.Rectangle(xy,width,height,linewidth=1,edgecolor=edgecolor,facecolor=facecolor)
    # Add the patch to the Axes
    ax.add_patch(rect)
    ax.autoscale()
    return ax

def draw_box(b, edgecolor='black', facecolor='blue', ax=None):
    return _draw_box(b.x.lo, b.x.up, b.y.lo, b.y.up, edgecolor, facecolor, ax)


def draw_paving(xmin, xmax, dx, ymin, ymax, dy, edgecolor='black', facecolor='blue'):
    x = np.arange(xmin, xmax, dx)
    y = np.arange(ymin, ymax, dy)
    xv, yv = np.meshgrid(x, y)
    for i in range(xv.shape[0]):
        for j in range(yv.shape[1]):
            _draw_box(xv[i,j], xv[i,j]+dx, yv[i,j], yv[i,j]+dy, edgecolor=edgecolor, facecolor=facecolor)

def draw_cell(x, y, dx, dy, edgecolor='black', facecolor='blue'):
    _draw_box(x, x+dx, y, y+dy, edgecolor=edgecolor, facecolor=facecolor)


# draws the allocation on the map
def draw_allocation(rxc_matrix, xmin, xmax, dx, ymin, ymax, dy, n_cells, n_robots, r_colors):
    for r_idx in range(0, n_robots):
        m_dy = -dy
        for c_idx in range(0, n_cells):
            m_dx = dx*(c_idx % round((xmax-xmin)/dx))
            if (c_idx % round((xmax-xmin)/dx) == 0):
                m_dy += dy*1
            if rxc_matrix[r_idx][c_idx] == 1:
                draw_cell(xmin+m_dx, ymin+m_dy, dx, dy, edgecolor=r_colors[r_idx], facecolor=r_colors[r_idx])



def fromCellToXY(c, x_lim, y_lim):
    """fromCellToXY:
       c: cell number,
       x_lim: (xmin, xmax, dx),
       y_lim: (ymin, ymax, dy),
    """
    xmin, xmax, dx = x_lim
    ymin, ymax, dy = y_lim

    Area = (xmax-xmin)*(ymax-ymin)
    n_cells = round(Area/(dx*dy))
    n_cells_x = round((xmax-xmin)/dx)
    n_cells_y = round((ymax-ymin)/dy)

    assert n_cells == n_cells_x*n_cells_y, f"n_cells:{n_cells}, n_cells_x:{n_cells_x}, n_cells_y:{n_cells_y}"

    x = (xmax-xmin)*(c%n_cells_x)/n_cells_x   # x:(xmax-xmin)=c:n_cells
    y = (ymax-ymin)*np.floor(c/n_cells_x)/n_cells_y

    return x, y


def fromXYToCell(x, y, x_lim, y_lim):
    """fromCellToXY:
       x, y: cell position,
       x_lim: (xmin, xmax, dx),
       y_lim: (ymin, ymax, dy),
    """
    xmin, xmax, dx = x_lim
    ymin, ymax, dy = y_lim

    Area = (xmax-xmin)*(ymax-ymin)
    n_cells = round(Area/(dx*dy))
    n_cells_x = round((xmax-xmin)/dx)
    n_cells_y = round((ymax-ymin)/dy)

    dY = np.floor(y*n_cells_y/(ymax-ymin))*n_cells_x
    c = int(np.floor(n_cells_x*x/(xmax-xmin)) + dY)

    return c
