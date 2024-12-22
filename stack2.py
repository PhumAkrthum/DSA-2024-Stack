# สร้างคลาส Stack
class Stack:
    def __init__(self):
        self.items = []  # ใช้ list เก็บข้อมูลใน Stack

    def push(self, item):
        self.items.append(item)  # เพิ่มข้อมูลเข้า Stack

    def pop(self):
        if not self.is_empty():
            return self.items.pop()  # เอาข้อมูลออกจาก Stack
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0  # ตรวจสอบว่า Stack ว่างเปล่าหรือไม่

# ฟังก์ชันแปลงเลขฐาน 10 เป็นเลขฐาน 2 โดยใช้ Stack
def decimal_to_binary(decimal_number):
    stack = Stack()
    while decimal_number > 0:
        remainder = decimal_number % 2  # หาเศษจากการหารด้วย 2
        stack.push(remainder)  # ดันเศษเข้า Stack
        decimal_number = decimal_number // 2  # หารเลขฐาน 10 ด้วย 2

    binary_result = ""
    while not stack.is_empty():
        binary_result += str(stack.pop())  # ดึงตัวเลขออกจาก Stack
    return binary_result

# ฟังก์ชันแปลงเลขฐาน 10 เป็นเลขฐาน 16 โดยใช้ Stack
def decimal_to_hexadecimal(decimal_number):
    stack = Stack()
    hex_digits = "0123456789ABCDEF"  # ตัวเลขและตัวอักษรสำหรับฐาน 16

    while decimal_number > 0:
        remainder = decimal_number % 16  # หาเศษจากการหารด้วย 16
        stack.push(hex_digits[remainder])  # ดันตัวเลข/ตัวอักษรเข้า Stack
        decimal_number = decimal_number // 16  # หารเลขฐาน 10 ด้วย 16

    hexadecimal_result = ""
    while not stack.is_empty():
        hexadecimal_result += stack.pop()  # ดึงตัวเลข/ตัวอักษรออกจาก Stack
    return hexadecimal_result

# ฟังก์ชันทดสอบโปรแกรม
def main():
    try:
        # รับค่าตัวเลขฐาน 10 จากผู้ใช้งาน
        decimal_number = int(input("กรุณากรอกตัวเลขฐาน 10: "))

        # แปลงเป็นเลขฐาน 2
        binary_result = decimal_to_binary(decimal_number)
        print(f"เลขฐาน 2 ของ {decimal_number} คือ: {binary_result}")

        # แปลงเป็นเลขฐาน 16
        hexadecimal_result = decimal_to_hexadecimal(decimal_number)
        print(f"เลขฐาน 16 ของ {decimal_number} คือ: {hexadecimal_result}")
    except ValueError:
        print("กรุณากรอกตัวเลขฐาน 10 ที่ถูกต้องเท่านั้น!")

# เรียกใช้งานโปรแกรม
if __name__ == "__main__":
    main()
