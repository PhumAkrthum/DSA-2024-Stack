# สร้างคลาส Stack
class Stack:
    def __init__(self):
        self.items = []  # ใช้ list เป็นตัวเก็บข้อมูลใน Stack

    def push(self, item):
        self.items.append(item)  # เพิ่มข้อมูลเข้า Stack

    def pop(self):
        if not self.is_empty():
            return self.items.pop()  # เอาข้อมูลออกจาก Stack
        else:
            return None  # ถ้า Stack ว่างเปล่าให้คืนค่า None

    def is_empty(self):
        return len(self.items) == 0  # ตรวจสอบว่า Stack ว่างเปล่าหรือไม่

# ฟังก์ชันกลับลำดับข้อความโดยใช้ Stack
def reverse_string_with_stack(input_string):
    stack = Stack()  # สร้าง Stack ขึ้นมา
    reversed_string = ""  # ตัวแปรเก็บข้อความกลับลำดับ
    
    # ดันตัวอักษรแต่ละตัวลงใน Stack
    for char in input_string:
        stack.push(char)
    
    # นำตัวอักษรออกจาก Stack แล้วต่อกันเพื่อสร้างข้อความกลับลำดับ
    while not stack.is_empty():
        reversed_string += stack.pop()
    
    return reversed_string

# รับข้อความจากผู้ใช้งาน
user_input = input("กรุณากรอกข้อความที่ต้องการกลับลำดับ: ")

# เรียกใช้ฟังก์ชันและแสดงผลลัพธ์
reversed_result = reverse_string_with_stack(user_input)
print("ข้อความที่กลับลำดับคือ:", reversed_result)
