import turtle
import square_grid as sq

if __name__ == '__main__':
    maze_grid = sq.Grid()
    maze_grid.build_grid()
    maze_grid.show_coordinates()
