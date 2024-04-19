# Import modules
import random
from prettytable import PrettyTable
from colorama import Fore
from datetime import date


# store choices into list
def Store_Choices():
    choice_items = []
    for digit in range(10, 100):
        choice_items.append(digit)
    for i in range(10):
        choice_items.append("")
    return choice_items


# add random choices into number_matrix function
def Add_Random_Choices(row_count, column_count, choice_items):
    number_matrix = []
    for i in range(row_count):
        row = []
        for x in range(column_count):
            random_choice = random.choice(
                choice_items,
            )
            row.append(random_choice)
        number_matrix.append(row)
    return number_matrix


# add rows and columns for number_table_grid
def Add_Rows_Columns(row_count, column_count, number_matrix):
    # make instance for pretty table
    number_table_grid = PrettyTable()
    # style pretty tables
    number_table_grid.header = False
    number_table_grid.padding_width = 2
    for row in range(row_count):
        new_row = []
        for column in range(column_count):
            new_row.append(number_matrix[row][column])
        number_table_grid.add_row(new_row, divider=True)
    return number_table_grid


# check number_table_grid result function
# this function check result column by column
def Check_Result(column_count, row_count, number_matrix):

    # make instance for pretty table for console
    result_table_grid = PrettyTable()

    # make instance for pretty table for html and
    result_table_file_grid = PrettyTable()

    # style pretty tables
    result_table_grid.padding_width = 2
    result_table_grid.border = False
    result_table_grid.header = False
    result_table_file_grid.padding_width = 2
    result_table_file_grid.border = False
    result_table_file_grid.header = False
    column_check = []
    result_list = []
    result_list_file = []
    for column in range(column_count):
        new_column = []
        for row in range(row_count):
            new_column.append(number_matrix[row][column])
        column_check.append(new_column)
        check_result = (
            Fore.LIGHTGREEN_EX + " OK"
            if not any(check == "" for check in new_column)
            else Fore.LIGHTRED_EX + " NO"
        )
        check_result_file = (
            " OK" if not any(check == "" for check in new_column) else " NO"
        )
        result_list.append(check_result)
        result_list_file.append(check_result_file)
    result_table_grid.add_row(result_list, divider=False)
    result_table_file_grid.add_row(result_list_file, divider=False)
    return result_table_grid, result_table_file_grid


def File_Generator(number_table_grid, result_table_grid_file):
    # generate 4 digit number for file names
    random_digit = random.randint(1000, 9999)

    # create txt file and html file
    file_name_txt = f"{date.today()}-{random_digit}.txt"
    file_name_html = f"{date.today()}-{random_digit}.html"
    create_text_file = open(file_name_txt, "x")
    create_html_file = open(file_name_html, "x")

    # get number_table_grid value and result_table_grid value
    number_table_text = number_table_grid.get_string()
    number_table_text_result = result_table_grid_file.get_string()
    number_table_html = number_table_grid.get_html_string()
    number_table_html_result = result_table_grid_file.get_html_string(
        attributes={"id": "result_table"}
    )

    # write txt  files
    with open(file_name_txt, "w") as text_file:
        text_file.write(number_table_text + "\n")
        text_file.write(number_table_text_result)

    # write html file and add html format ,css style and javascript for html file

    # open html_format file inside the Mypackage
    html_format_txt = open(r"Mypackage\html_format.txt", "r")
    read_lines = html_format_txt.readlines()

    # read html format file
    html_top_tags = read_lines[0:15]
    html_bottom_tags = read_lines[15:32]

    with open(file_name_html, "w") as html_file:
        for i in html_top_tags:
            html_file.write(i)
        html_file.write(number_table_html)
        html_file.write(number_table_html_result)
        for i in html_bottom_tags:
            html_file.write(i)
