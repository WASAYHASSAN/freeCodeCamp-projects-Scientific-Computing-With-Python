def arithmetic_arranger(problems, show_answer=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    line1 = ""
    line2 = ""
    line3 = ""
    line4 = ""
    for problem in problems:
        operands = problem.split()
        if not operands[0].isdigit() or not operands[2].isdigit():
            return "Error: Numbers must only contain digits."
        if len(operands[0]) > 4 or len(operands[2]) > 4:
            return "Error: Numbers cannot be more than four digits."
        if operands[1] != "+" and operands[1] != "-":
            return "Error: Operator must be '+' or '-'."

        width = max(len(operands[0]), len(operands[2])) + 2
        line1 += operands[0].rjust(width) + "    "
        line2 += operands[1] + " " + operands[2].rjust(width-2) + "    "
        line3 += "-" * width + "    "
        if show_answer:
            answer = str(eval(problem))
            line4 += answer.rjust(width) + "    "

    if show_answer:
        return line1.rstrip() + "\n" + line2.rstrip() + "\n" + line3.rstrip() + "\n" + line4.rstrip()
    else:
        return line1.rstrip() + "\n" + line2.rstrip() + "\n" + line3.rstrip()



print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))