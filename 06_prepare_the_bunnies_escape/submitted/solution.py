from collections import namedtuple
import sys
import copy

Location = namedtuple('Location', 'row col')

IMPOSSIBLE = 20*20+1

class Maze:
    def __init__(self, maze):
        self.maze = copy.deepcopy(maze)
        self.WALL = 1
        self.OPEN = 0
        self.row_count = len(self.maze) 
        self.col_count = len(self.maze[0])
        self.start = Location(0,0)
        self.finish = Location(self.row_count-1, self.col_count-1)

        self.shortest_path_helper = [[IMPOSSIBLE for col in range(self.col_count)] for row in range(self.row_count)]
        for row in range(self.row_count):
            for col in range(self.col_count):
                if self.maze[row][col] == self.OPEN:
                    self.shortest_path_helper[row][col] = None

    def shortest_path_count(self):
        self.calc_best_paths_helper(self.finish,1,self.shortest_path_helper)
        shortest = self.shortest_path_helper[self.start.row][self.start.col]
        if shortest == None:
            shortest = IMPOSSIBLE
        #print "returning", shortest
        return shortest
    
    def is_valid_loc(self, loc):
        is_valid = ((loc.row >= 0 and (loc.row < self.row_count)) 
                 and (loc.col >= 0 and (loc.col < self.col_count))) 
        return is_valid

    def is_open_loc(self, loc):
        return self.is_valid_loc(loc) and (self.maze[loc.row][loc.col] == self.OPEN)
    
    def loc_options(self, loc):
        """
        Returns a list of locations that open for travel, given an input location. 
        Walls and edges are not open locations and will not be returned
        """
        up = Location(loc.row-1,loc.col)
        down = Location(loc.row+1,loc.col)
        left = Location(loc.row,loc.col-1)
        right = Location(loc.row,loc.col+1)    
        options = [x for x in [up,down,left,right] if self.is_open_loc(x)]
        return options
    
    def print_loc_map(self, loc):
        sys.stdout.write('\n')
        for row in range(self.row_count):
            for col in range(self.col_count):
                if (self.maze[row][col] == self.OPEN):
                    if (row==loc.row) and (col==loc.col):
                        sys.stdout.write('*')
                    else:
                        sys.stdout.write(str(self.OPEN))
                else:
                    if (row==loc.row) and (col==loc.col):
                        sys.stdout.write('#')
                    else:
                        sys.stdout.write(str(self.WALL))
            sys.stdout.write('\n')
        sys.stdout.write('\n')

    def print_helper(self):
        sys.stdout.write('\n')
        for row in range(self.row_count):
            for col in range(self.col_count):
                if (self.maze[row][col] == self.OPEN):
                    if (self.shortest_path_helper[row][col] == IMPOSSIBLE):
                        sys.stdout.write(' IMP')
                    elif (self.shortest_path_helper[row][col] == None):
                        sys.stdout.write('  ? ')
                    else:
                        sys.stdout.write('%3d ' % self.shortest_path_helper[row][col])
                else:
                    sys.stdout.write(str("--|-"))
            sys.stdout.write('\n')
        sys.stdout.write('\n')
        if self.shortest_path_helper[self.start.row][self.start.col] == IMPOSSIBLE:
            sys.stdout.write('IMPOSSIBLE\n')
        elif self.shortest_path_helper[self.start.row][self.start.col] == None:
            sys.stdout.write('Path not yet determined\n')
        else:
            sys.stdout.write('Shortest Path = %d\n' % self.shortest_path_helper[self.start.row][self.start.col])

        raw_input("Press ENTER to continue...")


    def calc_best_paths_helper(self, current, potential_best, helper):
        current_best = helper[current.row][current.col] # can be None or previous defined, but not IMPOSSIBLE
        if (current_best == None) or ((potential_best < current_best) and (current_best != IMPOSSIBLE)):
            helper[current.row][current.col] = potential_best
            options = self.loc_options(current)
            for step in options:
                self.calc_best_paths_helper(step, potential_best + 1, helper)

def answer(maze):
    my_maze = Maze(maze)
    shortest_path_length = my_maze.shortest_path_count()

    # debug
    #my_maze.print_helper()
    #print "Baseline:", shortest_path_length
    #raw_input("Press ENTER to continue...")

    if shortest_path_length == my_maze.row_count + my_maze.col_count - 1:
        return shortest_path_length

    for i in range(my_maze.row_count):
        for j in range(my_maze.col_count):
            if maze[i][j] == 1:
                maze[i][j] = 0 # change wall to open                                                                
                my_maze = Maze(maze)
                if len(my_maze.loc_options(Location(i,j))) > 0:
                    path_length = my_maze.shortest_path_count()
                    shortest_path_length = min(path_length, shortest_path_length)

                    # debug
                    #my_maze.print_helper()
                    #print "Changed -->",i,j
                    #print "Shortest so far:", shortest_path_length

                maze[i][j] = 1 # change back to wall
                if shortest_path_length == my_maze.row_count + my_maze.col_count - 1:
                    return shortest_path_length
    return shortest_path_length
