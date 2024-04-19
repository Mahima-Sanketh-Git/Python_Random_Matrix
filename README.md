# Project Overview
This project explores the concept of percolation, the gradual movement of a liquid through a 
porous material. This project aims to develop a Python program that mimics this process within a 
two-dimensional grid. Coffee brewing serves as a real-world example, where water percolates 
through coffee grounds.
This program will generate a dynamic grid with random numbers and empty spaces. Each 
column will be analyzed to determine if percolation, the uninterrupted flow from top to bottom, 
is possible. Further, percolation is not possible for a column if the column consists of one or 
more empty spaces from top to bottom; the program will show the status of that column as "NO,” 
and percolation is possible for a column if the entire column consists of numbers from top to 
bottom; the program will show the status of that column In addition to that, the results and two-dimensional grid will be presented in the console and saved to a text file and an HTML file with 
a unique identifier.

## Addressing the following key aspects:
1. Grid Generation: The program will create a grid of user-specified dimensions with 
random two-digit numbers and randomly placed empty cells. The user can pass the grid 
size as a command-line argument. If the user does not choose a size, it will automatically 
make a 5x5 grid like a 5 by 5 square. The smallest grid can be 3x3, and the biggest grid 
can be 9x9. Further, if the user input grid size is not eligible for the above conditions, the 
program will show proper error messages.
2. Percolation Analysis: Each column will be evaluated to determine if a continuous path 
of numbers exists from the top to the bottom, indicating percolation.
3. Output: If user console arguments are eligible, the program will display the generated 
grid and report the percolation status as "OK" or "NO" for each column. The results will 
be shown on the console and saved to a different text file and an HTML file with a unique 
format. Also, the file format is year_month_day_4-digit random number.txt/html. For 
example, (2024_03_19_5565.txt, 2024_03_19_5565.html.)

# Clone this project and learn from it 🙌😍
you can clone this project and learn from it, if you have any new features please add a pull request.

# How to contribute 🐱‍👤🚀
 Guys and girls , You can easily add a pull request ( 🌠 geeks)
