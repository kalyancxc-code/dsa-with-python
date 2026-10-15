"""Lesson 37: Stacks: Last In, First Out

All runnable code from this lesson, combined in order.
"""

def is_valid(s):
    pairs = {")": "(", "]": "[", "}": "{"}
    stack = []
    for ch in s:
        if ch in pairs:
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()
        else:
            stack.append(ch)
    return not stack

for t in ["{[()]}", "([)]", "((", "", "]"]:
    print(repr(t), is_valid(t))


class Editor:
    def __init__(self):
        self.text, self.history = "", []
    def type(self, s):
        self.history.append(self.text)
        self.text += s
    def undo(self):
        if self.history:
            self.text = self.history.pop()

e = Editor()
e.type("Hello"); e.type(" World")
print(e.text)
e.undo()
print(e.text)
e.undo(); e.undo()
print(repr(e.text))


def reverse(s):
    st = list(s)
    out = []
    while st:
        out.append(st.pop())
    return "".join(out)
print(reverse("stack"))


class MinStack:
    def __init__(self):
        self.s = []
    def push(self, x):
        self.s.append((x, min(x, self.s[-1][1]) if self.s else x))
    def pop(self):
        return self.s.pop()[0]
    def top(self):
        return self.s[-1][0]
    def get_min(self):
        return self.s[-1][1]

m = MinStack()
for x in (5, 3, 7, 2):
    m.push(x)
print(m.get_min()); m.pop(); print(m.get_min()); m.pop(); m.pop(); print(m.get_min())


def eval_rpn(tokens):
    st = []
    for t in tokens:
        if t in "+-*/" and len(t) == 1:
            b, a = st.pop(), st.pop()
            st.append(a + b if t == "+" else a - b if t == "-" else a * b if t == "*" else int(a / b))
        else:
            st.append(int(t))
    return st[0]
print(eval_rpn(["2", "1", "+", "3", "*"]), eval_rpn(["4", "13", "5", "/", "+"]))


def decode(s):
    stack, cur, num = [], "", 0
    for ch in s:
        if ch.isdigit():
            num = num * 10 + int(ch)
        elif ch == "[":
            stack.append((cur, num))
            cur, num = "", 0
        elif ch == "]":
            prev, k = stack.pop()
            cur = prev + cur * k
        else:
            cur += ch
    return cur
print(decode("3[a2[c]]"), decode("2[ab]3[x]"))
