import re
import operator


def isValidProblems(problem_list):
  # No more than 5 problems
  if (len(problem_list) > 5):
    return {"status": False, "message": "Error: Too many problems."}

  for problem in problem_list:
    [num1, op, num2] = problem.split(" ")

    # Only addition and subtraction
    allowed_operators = ['+', '-']
    if (not (op in allowed_operators)):
      return {
        "status": False,
        "message": "Error: Operator must be '+' or '-'."
      }

    # Only contain max 4 digits
    regexpDigitMax = r'^[\d\w]{0,4}$'
    if (not (re.match(regexpDigitMax, num1)
             and re.match(regexpDigitMax, num2))):
      return {
        "status": False,
        "message": "Error: Numbers cannot be more than four digits."
      }

    # Numbers only
    regexpNumberOnly = r'^\d+$'
    if (not (re.match(regexpNumberOnly, num1)
             and re.match(regexpNumberOnly, num2))):
      return {
        "status": False,
        "message": "Error: Numbers must only contain digits."
      }

  return {"status": True, "message": "Good."}


def arithmetic_arranger(problems, displayResult=False):
  if (isValidProblems(problems)["status"]):
    num1_list = []
    num2_list = []
    separator_list = []
    result_list = []

    for problem in problems:
      [num1, op, num2] = problem.split(" ")
      maxLen = len(max([num1, op, num2], key=len))

      num1_list.append(' ' * (maxLen + 2 - len(num1)) + str(num1))
      num2_list.append(op + ' ' * (maxLen + 1 - len(num2)) + str(num2))
      separator_list.append('-' * (maxLen + 2))

      if displayResult:
        ops = {"+": operator.add, "-": operator.sub}

        op_result = ops[op](int(num1), int(num2))
        result_list.append(' ' * (maxLen + 2 - len(str(op_result))) +
                           str(op_result))
    problem_separator = " " * 4

    first_line = problem_separator.join(num1_list)
    second_line = problem_separator.join(num2_list)
    third_line = problem_separator.join(separator_list)
    fourth_line = (
      "\n" + problem_separator.join(result_list)) if displayResult else ""

    arranged_problems = "\n".join([first_line, second_line, third_line
                                   ]) + fourth_line

    return arranged_problems

  else:
    return isValidProblems(problems)["message"]


print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]),
      end='\n\n')

print(
  arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))
