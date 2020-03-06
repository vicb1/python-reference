def evaluate_arithmetic_string(s):
    s = s.strip()
    print('-' * 40)
    print('evaluating string: ' + s)

    lis = []
    last_operator = 0
    for i in range(len(s)):
        if i == len(s) - 1:
            lis.append(s[last_operator:i + 1])
        elif s[i] in ['*', '/', '+', '-']:
            lis.append(s[last_operator:i])
            lis.append(s[i])
            last_operator = i + 1

    i = 0
    while i < len(lis):
        if lis[i] == '*':
            tmp = float(lis[i - 1]) * float(lis[i + 1])
            lis[i - 1] = str(tmp)
            lis.pop(i)
            lis.pop(i)
            i -= 1
        elif lis[i] == '/':
            tmp = float(lis[i - 1]) / float(lis[i + 1])
            lis[i - 1] = str(tmp)
            lis.pop(i)
            lis.pop(i)
            i -= 1
        i += 1

    i = 0
    while i < len(lis):
        if lis[i] == '+':
            tmp = float(lis[i - 1]) + float(lis[i + 1])
            lis[i - 1] = str(tmp)
            lis.pop(i)
            lis.pop(i)
            i -= 1
        elif lis[i] == '-':
            tmp = float(lis[i - 1]) - float(lis[i + 1])
            lis[i - 1] = str(tmp)
            lis.pop(i)
            lis.pop(i)
            i -= 1
        i += 1

    ret = float(lis[0])
    print('solution is: ' + str(ret))
    return ret

test = "1+2"
assert evaluate_arithmetic_string(test) == 3
test = "34-5*100"
assert evaluate_arithmetic_string(test) == -466
test = "10-20*30+40/50"
assert evaluate_arithmetic_string(test) == -589.2
test = "10-123+20*30+40/3/50-5*56"
assert 207.2667 > evaluate_arithmetic_string(test) > 207.2666


#
# Your previous JavaScript content is preserved below:
#
# // Click "Settings" in the lower-right corner to set editor preferences
# //
# // Click "Run" in the top-left corner to run your code
# //
# // If you're not comfortable with JavaScript, click the pulldown labeled
# // "JavaScript" near the top-middle and select something different
# //
# // When done, just stop & email your recruiter. There's no "submit" button
# // in CoderPad.
# //
# // Interview question:
# // Write a function that parses and evaluates an arithmetic string
# // Ex. "1+2", "34-5*100", "10-20*30+40/50"
# // Positive integers separated by +, -, * or /. No parentheses
# // You must respect the order of operations: *, / take precedence over +, -
# // Please limit yourself to about 60 minutes. Good luck!
# //
#
# console.log('Hello, world!');
