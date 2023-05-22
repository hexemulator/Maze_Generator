class Square:
    """
    each location on the Grid is represented by a square with an x and y coordinate
    the coordinates are held as an attribute in the class

    for coding purposes-- the coordinate can be thought of as sitting in the direct center of the square
    where 'top', 'bottom', 'left' and 'right' are in relation to the center of the square

    for drawing purposes-- the coordinate can be thought of as being sitting at the top-left of the square
    each edge of the square is 50px
    """

    def __init__(self, x, y):
        self.x_coord = x
        self.y_coord = y

        self.top = False
        self.bottom = False
        self.left = False
        self.right = False

    def grab_coordinates(self):
        """
        simple output function that shows that all coordinates of the given square
        :return: None
        """
        return "(" + str(self.x_coord) + ", " + str(self.y_coord) + ")"


class Grid:
    """
    the grid is a collection of squares with coordinates
    """

    def __init__(self):
        x_given = 0
        while x_given < 5:
            x_given = int(input("x? "))

        self.x_dimension = x_given

        y_given = 0
        while y_given < 5:
            y_given = int(input("y? "))

        self.y_dimension = y_given

        self.square_list = []

    def build_grid(self):
        # initialize counters
        x_count = 0
        y_count = 0

        # build the maze
        for y in range(0, self.y_dimension):
            for x in range(0, self.x_dimension):
                self.square_list.append(Square(x_count, y_count))
                x_count += 1

            x_count = 0
            y_count += 1

    def find_square(self) -> bool:
        """
        looks up a square by its given x and y coordinate, checks whether the square exists
        :return: bool
        """

        x, y = input("which square?").split()

        x = int(x)
        y = int(y)

        # calculates the possible index of the square by the user-given x and y coordinate
        index = x + (y * self.y_dimension)

        # checks to make sure the index isn't out of range before looking it up
        if index >= self.x_dimension * self.y_dimension or index < 0:
            return False

        # grabs the given square from the list by using index lookup (this is optimal, as it is O(1) time)
        square = self.square_list[index]

        # verifies that the square has the user-specified coordinates, and returns True or False
        if square.x_coord == x and square.y_coord == y:
            return True
        else:
            return False

    def show_coordinates(self):
        display_line = ""
        line_cutoff = 0
        for square in self.square_list:
            line_cutoff += 1
            if line_cutoff >= self.x_dimension:
                display_line += f'{square.grab_coordinates()}\n'
                line_cutoff = 0
            else:
                display_line += f'{square.grab_coordinates()}, '

        print(display_line)