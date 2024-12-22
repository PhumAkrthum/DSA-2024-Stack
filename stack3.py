# สร้างคลาส Stack
class Stack:
    def __init__(self):
        self.items = []  # ใช้ list เป็นตัวเก็บข้อมูลใน Stack

    def push(self, item):
        self.items += [item]  # เพิ่มข้อมูลเข้า Stack โดยไม่ใช้ append

    def pop(self):
        if not self.is_empty():
            item = self.items[-1]  # หยิบค่าตัวบนสุด
            self.items = self.items[:-1]  # เอาค่าออกจาก Stack โดยไม่ใช้ pop
            return item
        else:
            return None  # ถ้า Stack ว่างเปล่า

    def is_empty(self):
        return len(self.items) == 0  # ตรวจสอบว่า Stack ว่างเปล่าหรือไม่

# ฟังก์ชันแยกนิพจน์ Postfix โดยไม่ใช้ split()
def manual_split(expression, delimiter=" "):
    result = []
    temp = ""
    for char in expression:
        if char == delimiter:
            if temp != "":
                result += [temp]
                temp = ""
        else:
            temp += char
    if temp != "":
        result += [temp]
    return result

# ฟังก์ชันตรวจสอบว่าข้อมูลเป็นตัวเลขหรือไม่ โดยไม่ใช้ isdigit()
def is_number(value):
    for char in value:
        if not ('0' <= char <= '9'):  # ตรวจสอบว่าตัวอักษรไม่ใช่ตัวเลข
            return False
    return True

# ฟังก์ชันคำนวณนิพจน์ Postfix
def evaluate_postfix(expression):
    stack = Stack()
    operators = "+-*/"

    # แยกนิพจน์เป็นสัญลักษณ์ต่าง ๆ
    tokens = manual_split(expression, " ")

    # วนลูปประมวลผลแต่ละสัญลักษณ์
    for token in tokens:
        if is_number(token):  # ตรวจสอบว่าเป็นตัวเลข
            stack.push(int(token))
        elif token in operators:  # ถ้าเป็นเครื่องหมายดำเนินการ
            operand2 = stack.pop()
            operand1 = stack.pop()

            if token == '+':
                stack.push(operand1 + operand2)
            elif token == '-':
                stack.push(operand1 - operand2)
            elif token == '*':
                stack.push(operand1 * operand2)
            elif token == '/':
                stack.push(operand1 // operand2)  # การหารแบบจำนวนเต็ม
        else:
            print("พบสัญลักษณ์ที่ไม่ถูกต้อง:", token)
            return None

    return stack.pop()  # คืนค่าผลลัพธ์จาก Stack

# ฟังก์ชันทดสอบโปรแกรม
def main():
    print("=== โปรแกรมคำนวณนิพจน์ Postfix ===")
    print("ตัวอย่าง: 5 6 + 2 *")
    postfix_expression = input("กรุณาป้อนนิพจน์ Postfix: ")

    # เรียกใช้ฟังก์ชันคำนวณ
    result = evaluate_postfix(postfix_expression)
    if result is not None:
        print(f"ผลลัพธ์ของนิพจน์ Postfix '{postfix_expression}' คือ: {result}")
    else:
        print("ไม่สามารถคำนวณนิพจน์ได้ โปรดตรวจสอบความถูกต้องของนิพจน์")

# เรียกใช้งานโปรแกรม
if __name__ == "__main__":
    main()
