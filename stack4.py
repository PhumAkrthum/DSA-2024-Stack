# สร้างคลาส Stack
class Stack:
    def __init__(self):
        self.items = []  # ใช้ list เป็นตัวเก็บข้อมูลใน Stack

    def push(self, item):
        self.items += [item]  # เพิ่มข้อมูลเข้า Stack โดยไม่ใช้ append

    def pop(self):
        if not self.is_empty():
            top = self.items[-1]  # เอาค่าด้านบนสุด
            self.items = self.items[:-1]  # เอาออกจาก Stack โดยไม่ใช้ pop
            return top
        return None  # ถ้า Stack ว่างเปล่า

    def peek(self):
        if not self.is_empty():
            return self.items[-1]  # ดูค่าสูงสุดใน Stack
        return None

    def is_empty(self):
        return len(self.items) == 0  # ตรวจสอบว่า Stack ว่างเปล่า

# ฟังก์ชันตรวจสอบความถูกต้องของ JSON string
def is_valid_json(json_string):
    stack = Stack()
    in_string = False  # ตรวจสอบว่ากำลังอยู่ในเครื่องหมายคำพูดหรือไม่
    escape = False     # ตรวจจับอักขระ escape เช่น \"
    
    for char in json_string:
        if escape:  # ถ้าเจอ escape character ข้ามตัวถัดไป
            escape = False
            continue

        if char == '\\':  # ตรวจจับ escape character เช่น \"
            escape = True
            continue

        if char == '"':  # ตรวจจับเปิด-ปิดเครื่องหมายคำพูด
            in_string = not in_string
            continue

        if in_string:  # ถ้าอยู่ในเครื่องหมายคำพูด ไม่ต้องตรวจสอบวงเล็บ
            continue

        # ตรวจสอบวงเล็บเปิด
        if char in '{[':
            stack.push(char)

        # ตรวจสอบวงเล็บปิด
        elif char in '}]':
            if stack.is_empty():
                return False  # ถ้าพบวงเล็บปิดแต่ไม่มีเปิดมาก่อน
            top = stack.pop()
            if char == '}' and top != '{':
                return False  # ตรวจสอบคู่ของวงเล็บ
            elif char == ']' and top != '[':
                return False

    # ตรวจสอบว่ามีวงเล็บค้างอยู่ใน Stack หรือไม่
    if not stack.is_empty() or in_string:
        return False

    return True  # ถ้าทุกอย่างถูกต้อง

# ฟังก์ชันทดสอบโปรแกรม
def main():
    print("=== โปรแกรมตรวจสอบความถูกต้องของ JSON string ===")
    print("ตัวอย่าง JSON: {\"name\": \"John\", \"age\": 30, \"city\": \"New York\"}")
    json_string = input("กรุณาป้อน JSON string: ")

    # เรียกใช้ฟังก์ชันตรวจสอบความถูกต้อง
    if is_valid_json(json_string):
        print("JSON string ถูกต้อง ✅")
    else:
        print("JSON string ไม่ถูกต้อง ❌")

# เรียกใช้งานโปรแกรม
if __name__ == "__main__":
    main()
