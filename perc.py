# Import modules
from colorama import init
import sys
import Mypackage.myfunctions as myfunctions

# initialize colorama
init()

# initialize variable
row_count = 0
column_count = 0
choice_items = []

# Main programme

# call Store_Choices function inside the mufunction module
choice_items = myfunctions.Store_Choices()

try:
    # consols arguments
    argument = str(sys.argv[1])
    # argument split with x
    list_args_value = argument.lower().split("x")
except IndexError:
    print("\n")
    print("Created default 5x5 grid")
    list_args_value = [5, 5]

# check argument length
if len(sys.argv) > 2:
    print("\n")
    print("Argument length is wrong ,you want only one argument! ")
else:
    # check argument split is correct
    try:
        # convert string argument into integer
        row_count = int(list_args_value[0])
        column_count = int(list_args_value[1])
        if row_count < 3 or column_count < 3:
            print("\n")
            print("The lowest dimensions must be 3x3")
        elif row_count > 9 or column_count > 9:
            print("\n")
            print("The highest dimension must be 9x9")
        else:
            # display create grid values
            if row_count != 5 or column_count != 5:
                print("\n")
                print(f"Created {row_count}x{column_count} grid")
            # call Add_Random_Choices function inside the myfunctions module
            number_matrix = myfunctions.Add_Random_Choices(
                row_count, column_count, choice_items
            )

            # call Add_Rows_Columns function inside the myfunctions module
            number_table_grid = myfunctions.Add_Rows_Columns(
                row_count, column_count, number_matrix
            )

            # call Check_Result function inside the myfunctions module
            result_table_grid, result_table_grid_file = myfunctions.Check_Result(
                column_count, row_count, number_matrix
            )
            # display table grid and result
            print("\n")
            print(number_table_grid)
            print(result_table_grid)
            print("\n")

            # call File_generator function inside the myfunctions module
            myfunctions.File_Generator(number_table_grid, result_table_grid_file)

    except:
        print("\n")
        print("Your argument is wrong, format should be like 5x5 ")

        sys.exit()
