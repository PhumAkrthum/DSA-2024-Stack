# สร้างคลาส Stack
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items += [item]  # เพิ่มข้อมูลเข้า Stack โดยไม่ใช้ append

    def pop(self):
        if not self.is_empty():
            top = self.items[-1]
            self.items = self.items[:-1]
            return top
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        return len(self.items) == 0

# ฟังก์ชันกำหนดความสำคัญของเครื่องหมายดำเนินการ
def precedence(op):
    if op in ('+', '-'):
        return 1
    if op in ('*', '/'):
        return 2
    return 0

# ฟังก์ชันดำเนินการคำนวณตามเครื่องหมาย
def apply_operation(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        return a // b  # การหารแบบจำนวนเต็ม

# ฟังก์ชันตรวจสอบว่าข้อมูลเป็นตัวเลขหรือไม่
def is_number(value):
    for char in value:
        if not ('0' <= char <= '9'):
            return False
    return True

# ฟังก์ชันประเมินผลนิพจน์ Infix
def evaluate_infix(expression):
    operand_stack = Stack()   # Stack สำหรับตัวเลข
    operator_stack = Stack()  # Stack สำหรับเครื่องหมายดำเนินการ
    i = 0
    while i < len(expression):
        char = expression[i]

        # ข้ามช่องว่าง
        if char == ' ':
            i += 1
            continue

        # ถ้าพบตัวเลข อ่านเลขเต็ม
        if '0' <= char <= '9':
            num = 0
            while i < len(expression) and '0' <= expression[i] <= '9':
                num = num * 10 + int(expression[i])
                i += 1
            operand_stack.push(num)
            i -= 1  # เลื่อนกลับมาหนึ่งตำแหน่งหลังจากวนจบ

        # ถ้าพบวงเล็บเปิด
        elif char == '(':
            operator_stack.push(char)

        # ถ้าพบวงเล็บปิด
        elif char == ')':
            while not operator_stack.is_empty() and operator_stack.peek() != '(':
                op = operator_stack.pop()
                b = operand_stack.pop()
                a = operand_stack.pop()
                operand_stack.push(apply_operation(a, b, op))
            operator_stack.pop()  # เอาวงเล็บเปิด '(' ออกจาก Stack

        # ถ้าพบเครื่องหมายดำเนินการ
        elif char in ('+', '-', '*', '/'):
            while (not operator_stack.is_empty() and
                   precedence(operator_stack.peek()) >= precedence(char)):
                op = operator_stack.pop()
                b = operand_stack.pop()
                a = operand_stack.pop()
                operand_stack.push(apply_operation(a, b, op))
            operator_stack.push(char)

        i += 1

    # ประมวลผลเครื่องหมายที่เหลือใน Stack
    while not operator_stack.is_empty():
        op = operator_stack.pop()
        b = operand_stack.pop()
        a = operand_stack.pop()
        operand_stack.push(apply_operation(a, b, op))

    return operand_stack.pop()

# ฟังก์ชันทดสอบโปรแกรม
def main():
    print("=== โปรแกรมประเมินผลนิพจน์ Infix ===")
    print("ตัวอย่าง: (1 + 2) * 3 - 4 / 2")
    expression = input("กรุณาป้อนนิพจน์ Infix: ")
    result = evaluate_infix(expression)
    print(f"ผลลัพธ์ของนิพจน์ '{expression}' คือ: {result}")

# เรียกใช้งานโปรแกรม
if __name__ == "__main__":
    main()

