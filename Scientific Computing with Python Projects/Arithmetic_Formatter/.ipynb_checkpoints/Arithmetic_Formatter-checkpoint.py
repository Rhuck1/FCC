'''
Students in primary school often arrange arithmetic problems vertically to make them easier to solve. For example, "235 + 52" becomes:

  235
+  52
-----

Create a function that receives a list of strings that are arithmetic problems and returns the problems arranged vertically and side-by-side. The function should optionally take a second argument. When the second argument is set to True, the answers should be displayed.
Example

Function Call:

arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])

Output:

   32      3801      45      123
+ 698    -    2    + 43    +  49
-----    ------    ----    -----

Function Call:

arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)

Output:

  32         1      9999      523
+  8    - 3801    + 9999    -  49
----    ------    ------    -----
  40     -3800     19998      474

Rules

The function will return the correct conversion if the supplied problems are properly formatted, otherwise, it will return a string that describes an error that is meaningful to the user.

    Situations that will return an error:
        * If there are too many problems supplied to the function. The limit is five, anything more will return: Error: Too many problems.
        * The appropriate operators the function will accept are addition and subtraction. Multiplication and division will return an error. Other operators not mentioned in this bullet point will not need to be tested. The error returned will be: Error: Operator must be '+' or '-'.
        * Each number (operand) should only contain digits. Otherwise, the function will return: Error: Numbers must only contain digits.
        * Each operand (aka number on each side of the operator) has a max of four digits in width. Otherwise, the error string returned will be: Error: Numbers cannot be more than four digits.
    If the user supplied the correct format of problems, the conversion you return will follow these rules:
        1) There should be a single space between the operator and the longest of the two operands, the operator will be on the same line as the second operand, both operands will be in the same order as provided (the first will be the top one and the second will be the bottom).
        2) Numbers should be right-aligned.
        3) There should be four spaces between each problem.
        4) There should be dashes at the bottom of each problem. The dashes should run along the entire length of each problem individually. (The example above shows what this should look like.)
'''

def arithmetic_formatter(problems, answers=False):
    
    if len(problems) > 5: # Handling problem limit of 5
        return("Error: Too many problems.")
    
    operators = []
    numbers = []
    solutions = []

    for problem in problems:
        
        pieces = problem.split()
        
        if pieces[1] not in ['+', '-']: # Handling non '+' or '-' problem instances
            return("Error: Operator must be '+' or '-'.") 

        elif not pieces[0].isnumeric() or not pieces[2].isnumeric(): # Handling non numeric problem instances
            return("Error: Numbers must only contain digits.")

        elif len(pieces[0]) > 4 or len(pieces[2]) > 4: # Handling digit width limit of 4
            return("Error: Numbers cannot be more than four digits.")
        
        operators.append(pieces[1]) # Adding operators to a collection list
        numbers.extend([pieces[0], pieces[2]]) # Adding numbers to a collection list
        solutions.append(eval(problem)) # Adding solutions to a collection list
        
    top_row = ''
    dashes = ''
    solution_row = ''
    bottom_row = ''
    
    # Looping through the range of the length of numbers to determine spacing of problem by each row
    for idx in range(0, len(numbers), 2):
        top_spacing = max(len(numbers[idx]), len(numbers[idx + 1])) + 2
        top_row += numbers[idx].rjust(top_spacing)
        dashes += '-' * top_spacing
        solution_row += str(solutions[idx // 2]).rjust(top_spacing)
        if idx != len(numbers) - 2:
            top_row += ' ' * 4
            dashes += ' ' * 4
            solution_row += ' ' * 4
        
        bottom_spacing = max(len(numbers[idx]), len(numbers[idx + 1])) + 1
        bottom_row += operators[idx // 2]
        bottom_row += numbers[idx + 1].rjust(bottom_spacing)
        if idx + 1 != len(numbers) - 1:
            bottom_row += ' ' * 4
    
    if answers:
        arranged_problems = '\n'.join((top_row, bottom_row, dashes, solution_row))
        
    else:
        arranged_problems = '\n'.join((top_row, bottom_row, dashes))
        
    return arranged_problems
