from math import sqrt
import time


# static function
def get_room(x, y, r):
    return (x // r)*r + (y // r) + 1


max_iterations = 100


class SudokuSolver:
    def __init__(self, input_board):
        # initial data collection
        self.input_board = input_board
        self.d_len = len(self.input_board)  # size of table
        self.rank = int(sqrt(self.d_len))  # Rank of table
        self.comp_table = self.create_table()  # cell as val object in table
        self.room_obj = self.get_room_obj()  # dict of sub square blocks as room object
        self.row_obj = self.get_row_obj()    # dict of row as object
        self.col_obj = self.get_col_obj()    # dict of column as object
        self.num_obj = NumObj(self.d_len, self.comp_table)  # self.get_num_obj()

        # initial display of input
        print("")
        print(" - Sudoku Solver - ")
        print("Input Puzzle : ")
        self.display_comp_room()

        # compute
        start_time = time.time()
        iterations = self.solve()
        end_time = time.time()

        # final display results
        print("")
        print("Solved puzzle : ")
        print(" - iterations : " + str(iterations))
        print(" - time : %.3f sec" % (end_time - start_time))
        self.display_comp_room()

    def display_comp_room(self):
        out_list = []
        for i in range(len(self.comp_table)):
            out_list.append([])
            for j in range(len(self.comp_table[i])):
                out_list[-1].append(str(self.comp_table[i][j]))
        print(*out_list, sep="\n")

    def create_table(self):
        op = []
        for i in range(len(self.input_board)):
            op.append([])
            for j in range(len(self.input_board[i])):
                op[-1].append(ValObj(self.input_board[i][j], i, j, self.rank))
        return op

    def get_room_obj(self):
        out_list = {}
        for i in range(1, self.d_len+1):
            out_list[str(i)] = RoomObj(i, self.rank, self.comp_table)
        return out_list

    def get_row_obj(self):
        out_list = {}
        for i in range(1, self.d_len+1):
            out_list[str(i)] = RowObj(i-1, self.d_len, self.comp_table)
        return out_list

    def get_col_obj(self):
        out_list = {}
        for i in range(1, self.d_len+1):
            out_list[str(i)] = ColObj(i-1, self.d_len, self.comp_table)
        return out_list

    def get_num_obj(self):
        out_list = {}
        for i in range(1, self.d_len+1):
            z = self.d_len
            for x in range(self.d_len):
                for y in range(self.d_len):
                    if self.comp_table[x][y].__str__() == str(i):
                        z -= 1
                        break
            out_list[str(i)] = z
        return out_list

    def solve(self):
        # start with minimum value required number
        iter_count = 0
        num_list = [*range(1, 10)]
        n1 = self.num_obj.get_next_least_num(num_list)
        while n1 is not None:
            iter_count += 1
            if iter_count == max_iterations:
                print("")
                print(" - Interrupt : ")
                print("MAX ITERATIONS REACHED. Full solution not found.")
                break

            # check for rooms
            for room in self.room_obj.values():
                rows = [self.row_obj[str(i)] for i in room.x]
                cols = [self.col_obj[str(j)] for j in room.y]
                if room.evaluate(n1, rows, cols):
                    self.num_obj.update_num(n1)

            # check for rows
            for row in self.row_obj.values():
                if row.evaluate(n1, self.col_obj, self.room_obj):
                    self.num_obj.update_num(n1)

            # check for columns
            for col in self.col_obj.values():
                if col.evaluate(n1, self.row_obj, self.room_obj):
                    self.num_obj.update_num(n1)

            # finally check for next least number
            num_list.remove(int(n1))
            if len(num_list) == 0:
                num_list = [*range(1, 10)]
                z0 = self.num_obj.get_zero_num_list()
                for z1 in z0:
                    num_list.remove(z1)
            n1 = self.num_obj.get_next_least_num(num_list)
            if n1 is None:
                break

        return iter_count


class ValObj:
    def __init__(self, val, x, y, r):
        self._value = val
        self.x = x + 1  # real index in X
        self.y = y + 1  # real index in y
        self.r = get_room(x, y, r)  # room index
        self._is_input = val is not None  # bool to store if value is input

    def __str__(self):
        return str(self._value) + ("" if self._is_input else "+")

    def set_value(self, val):
        if not self._is_input:  # so as not to change original input value
            self._value = val

    def is_null(self):
        return self._value is None

    def is_equal(self, val):
        return self._value == val


class RoomObj:
    def __init__(self, i, rank, ot):
        # initial data collection
        self.index = i
        self.rank = rank
        self.x = self.get_x(rank)
        self.y = self.get_y(rank)
        self.comp_room = self.get_comp_room(ot)  # table val object of room

    def display_comp_room(self):
        out_list = []
        for i in range(len(self.comp_room)):
            out_list.append([])
            for j in range(len(self.comp_room[i])):
                out_list[-1].append(str(self.comp_room[i][j]))
        print(*out_list, sep="\n")

    # list of row indices for this room
    def get_x(self, rank):
        x = ((self.index-1) // rank)*rank + 1
        return [*range(x, x+rank)]

    # list of col indices for this room
    def get_y(self, rank):
        y = (((self.index-1) % rank)*rank) + 1
        return [*range(y, y+rank)]

    # get this room object from input table
    def get_comp_room(self, ot):
        op = []
        for i in self.x:
            op.append([])
            for j in self.y:
                op[-1].append(ot[i-1][j-1])
        return op

    def room_contain(self, num):
        for rm_val_in_x in self.comp_room:
            for rm_val_in_y in rm_val_in_x:
                if rm_val_in_y.is_equal(int(num)):
                    return True
        return False

    def is_room_row_full(self, r_ind):
        for rm_val_in_y in self.comp_room[r_ind]:
            if rm_val_in_y.is_null():
                return False
        return True

    def is_room_col_full(self, c_ind):
        for rm_val_in_x in self.comp_room:
            if rm_val_in_x[c_ind].is_null():
                return False
        return True

    def evaluate(self, n1, full_rows, full_cols):
        if not self.room_contain(int(n1)):
            possible_place = []
            for r_ind in range(self.rank):
                if not self.is_room_row_full(r_ind) and not full_rows[r_ind].contain(n1):
                    for c_ind in range(self.rank):
                        if not self.is_room_col_full(c_ind) and not full_cols[c_ind].contain(n1):
                            possible_place.append((r_ind, c_ind))
            if len(possible_place) == 1:
                # print(" + adding value -> " + str(n1) + " at room " + str(self.index) + " @ " +
                #       str(possible_place[0][0]+1) + " && " + str(possible_place[0][1]+1))
                self.comp_room[possible_place[0][0]][possible_place[0][1]].set_value(int(n1))
                return True

        return False


class RowObj:
    def __init__(self, x, rank, ot):
        # initial data collection
        self.x = x
        self.rank = rank
        self.comp_row = ot[x]

    def contain(self, num):
        for r_val in self.comp_row:
            if str(num) in str(r_val):
                return True
        return False

    def _row_contain(self, num):
        for val1 in self.comp_row:
            if val1.is_equal(int(num)):
                return True
        return False

    def is_row_full(self):
        for r_val in self.comp_row:
            if r_val.is_null():
                return False
        return True

    def evaluate(self, n1, full_cols, full_rooms):
        if not self.is_row_full() and not self._row_contain(n1):
            possible_place = []
            for c_ind in range(self.rank):
                if self.comp_row[c_ind].is_null() \
                        and not full_cols[str(c_ind+1)].contain(n1)\
                        and not full_rooms[str(get_room(self.x, c_ind, int(sqrt(self.rank))))].room_contain(n1):
                    possible_place.append(c_ind)
            if len(possible_place) == 1:
                # print(" + adding value -> " + str(n1) + " at row " + str(self.x+1) + " @ " + str(possible_place[0]+1))
                self.comp_row[possible_place[0]].set_value(int(n1))
                return True

        return False


class ColObj:
    def __init__(self, y, rank, ot):
        # initial data collection
        self.y = y
        self.rank = rank
        self.comp_col = self.get_comp_col(ot)

    # list of column objects from input
    def get_comp_col(self, ot):
        op = []
        for i in ot:
            op.append(i[self.y])
        return op

    def contain(self, num):
        for c_val in self.comp_col:
            if str(num) in str(c_val):
                return True
        return False

    def _col_contain(self, num):
        for val1 in self.comp_col:
            if val1.is_equal(int(num)):
                return True
        return False

    def is_col_full(self):
        for c_val in self.comp_col:
            if c_val.is_null():
                return False
        return True

    def evaluate(self, n1, full_rows, full_rooms):
        if not self.is_col_full() and not self._col_contain(n1):
            possible_place = []
            for r_ind in range(self.rank):
                if self.comp_col[r_ind].is_null() \
                        and not full_rows[str(r_ind+1)].contain(n1)\
                        and not full_rooms[str(get_room(r_ind, self.y, int(sqrt(self.rank))))].room_contain(n1):
                    possible_place.append(r_ind)
            if len(possible_place) == 1:
                # print(" + adding value -> " + str(n1) + " at col " + str(self.y+1) + " @ " + str(possible_place[0]+1))
                self.comp_col[possible_place[0]].set_value(int(n1))
                return True
        return False


class NumObj:
    def __init__(self, d_len, ot):
        self.num_obj = self.get_num_obj(d_len, ot)

    @staticmethod
    def get_num_obj(d_len, ot):
        op = {}
        for i in range(1, d_len + 1):
            z = d_len
            for x in range(d_len):
                for y in range(d_len):
                    if ot[x][y].__str__() == str(i):
                        z -= 1
                        break
            op[str(i)] = z
        return op

    def get_next_least_num(self, num_list):
        test_obj = sorted(self.num_obj.items(), key=lambda x: x[1])
        for item in test_obj:
            if item[1] == 0:
                continue
            if int(item[0]) in num_list:
                return item[0]

        return None

    def get_zero_num_list(self):
        output = []
        for item in self.num_obj:
            if self.num_obj[item] == 0:
                output.append(int(item))
        return output

    def update_num(self, num):
        self.num_obj[str(num)] -= 1
