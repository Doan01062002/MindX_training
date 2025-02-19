######################## Kiến thức slide 1 ########################################

# 1. Để chạy chương trình sử dụng câu lệnh: python <tên chương trình> vd: python app.py

# 2. lệnh nhập xuất: print()
print("Hello") # có thể hiển thị nhiều dữ liệu một lúc được ngăn cách bằng dấu phẩy print("Hello", "Hi", 25)

# 3. lệnh nhập xuất: input()
name = input("Enter name: ") # Dữ liệu trả về là kiểu string, giá trị được lưu vào biến name

# 4. Các kiểu dữ liệu: int (số nguyên), float (số thực), string (chuỗi), boolean (true, false)

# 5. Toán tử logic: and, or , not

# 6. Toán tử điều kiện: if-elif-else
a = 0
b = 1

if a>b:
    print("a is agrater")
elif b>a:
    print("b is agrater")
else:
    print("a and b is equal")

# 7. Vòng lặp for được sử dụng khi biết trước số lần lặp: for <counter> in <dãy>: <khối lệnh>
for i in range(1,11,2):
    print(i)

# 8. Vòng lặp while được sử dụng khi chưa biết số lần lặp: while <điều kiện>: <khối lệnh> (Lưu ý: vòng lặp while có khả năng lặp vô tận)
i = 1
while i < 11:
    print(i)
    i += 1

########################## Kiến thức slide 2 ###################################

# 1. Danh sách List: list_name = [<phần tử 1>, <phần tử 2>,...]
    # chứa các phần tử có thứ tự, có giá trị là bất kỳ kiểu dữ liệu nào
    # có thể truy cập giá trị của phần tử bằng chỉ số vị trí (index)
    # có kích thước thay đổi được khi thực thi trương trình

# khai báo list
nums = [1,2,3,4]

# truy cập phần tử
print(nums[1])

# độ dài của list
print(len(nums))

# thay đổi giá trị của phần tử
animals = ["dog", "cat", "bear"]
animals[1] = "fish"

# xóa phần tử
mixed = [2,True,"python",5.5]
del mixed[0]

# thêm phần tử
mixed.append([1,2]) # thêm vào cuối của mảng mixed mảng [1,2]

# duyệt phần tử
for item in mixed:
    print(item)

for i in range(len(mixed)):
    print(mixed[i])

# 2. Hàm: Hàm là tập hợp các câu lệnh dùng để thực hiện các chức năng nào đó. Hàm cho phép sử dụng lại code, khiến code dễ đọc và hỗ trợ viên khi chương trình trở nên dài và phức tạp.

# Cú pháp: def <tên hàm> (<các tham số>): <khối lệnh> return <giá trị trả về>

# vd: Hàm chào người dùng
def greeting(username: str):
    print("hello", username, "!")

greeting("MindX")

# 3. Xử lý file là phương pháp lưu dữ liệu chương trình vào bộ nhớ cứng và thao tác mở, đọc và viết thêm vào những file này.

# Mở file: open(<tên file>, <mode>) với mode = "r" có nghĩa là read(đọc)
file = open("grades", "r")

# Đọc file: có thể dùng các phương thức như read(), readline(), readlines().
content = file.read() # Đọc toàn bộ nội dung file

line = file.readline() # Đọc một dòng

lines = file.readlines() # Đọc tất cả các dòng

# Viết/Thêm file: sử dụng phương thức write(). Tuy nhiên phải đọc file với mode = "w" hoặc mode = "a"(append) mới được phép viết vào file.
file = open("grades.txt", "w")
file.write(9.5, "\n")

file = open("grades.txt", "a")
file.write(9.5, "\n")

# Đóng file: để giải phóng các tài nguyên hệ thống liên quan đến file đó (Khi có lệnh mở file phải có lệnh đóng file)
file = open("grades.txt", "w")
file.close() # Đóng file

# Đóng mở file rút gọn
with open("grades.txt", "a") as file:
    file.write(10)

# 4. Xử lý lỗi: để tránh trường hợp vd file không tồn tại trên máy tính, sử dựng cấu trúc try - except - finally.
try:
    file = open("grades.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found!")
finally:
    file.close()

############################ Kiến thức slide 3 và 4 #############################

# 1. Lập trình hướng đối tượng (OOP) là một bộ quy tắc xoay quanh các đối tượng
    # Đặc điểm: thành phần trong chương trình là các đối tượng object, mỗi đối tượng có thuộc tính(Đặc điểm của đối tượng) và phương thức tương ứng(chỉ những hành động mà đối tượng có thể thực hiện)

# 2. Lớp (class) cho phép lập trình viên thiết kế cấu trúc để mô tả đối tượng. Lớp còn gọi là bản vẽ để tạo nên đối tượng

# dog.py
class Dog:
    def __init__(self, name, age): # __init__ là hàm khởi tạo, self là đối tượng
        self.name = name # self.name là thuộc tính
        self.age = age # self.age là thuộc tính

# main.py
from dog import Dog

my_dog = Dog("lu", 3) # my_dog là đối tượng tạo từ lớp Dog, lu và 3 sẽ lần lượt được gán cho thuộc tính name và age

print(my_dog.name) # Dấu chấm ( . ) có tác dụng truy cập vào thuộc tính name của đối tượng my_dog

# 3. Bốn nguyên lý lập trình hướng đối tượng

    # Tính đóng gói(Encapsulation) che giấu thông tin và chi tiết bên trong đối tượng
class Dog:
    def __init__(self, name, age):
        self.name = name 
        self.age = age 
        self.__sound = "Woof"
    def speak(self):
        return self.__sound # không thể truy cập trực tiếp đến thuộc tính __sound mà phải thông qua đối tượng và sử dụng phương thức speak

    # Tính kế thừa(Inheritance) cho phép một lớp thừa hưởng các thuộc tính và phương thức từ lớp khác, lớp thừa hưởng gọi là lớp con lớp cho thừa hưởng là lớp cha
class Dog:
    def __init__(self, name, age):
        self.name = name 
        self.age = age 
        self.__sound = "Woof"

    def get_description(self):
        return f"{self.name} is {self.age} -year-old"
    def speak(self):
        return self.__sound
    
class Shiba(Dog): # Shiba kế thừa từ Dog
    def __init__(self, name, age):
        super().__init__(name, age) # là hàm khởi tạo lớp cha nhưng nằm trong lớp con

    # Tính đa hình(Polymorphism) cho phép các đối tượng thuộc các lớp khác nhau thực hiện phương thức theo cách riêng
class Dog:
    def __init__(self, name, age):
        self.name = name 
        self.age = age 
        self.__sound = "Woof"

    def get_description(self):
        return f"{self.name} is {self.age} -year-old"
    def speak(self):
        return self.__sound

class Corgi(Dog):
    tail = "short"
    def __init__(self, name, age):
        super().__init__(name, age)
    def get_description(self):
        return f"{self.name} is {self.age} -year-old corgi"

    # Tính trừu tượng(Abstraction) tập trung vào những thông tin quan trọng của đối tượng bỏ qua những chi tiêt không cần thiết.
class Dog:
    def __init__(self, name, age):
        self.name = name 
        self.age = age 
    def speak(self): # phương thức speak của lớp Dog là phương thức trừu tượng không có nội dung
        pass
class Shiba(Dog):
    def __init__(self, name, age):
        super().__init__(name, age)
    def speak(self): # kế thừa và cụ thể hóa phương thức speak
        print("woof")

################################# Tổng hợp kiến thức slide 5 ######################################

# 1. Thuật toán là một dãy hữu hạn các bước cần thực hiện để giải quyết một vấn đề
    # Các đặc trưng của thuật toán: có đầu vào, đầu ra, tính chính xác, tính hữu hạn, tính đơn vị và tính tổng quát
    # Thuật toán tốt: Đơn giản, dễ hiểu, dễ cài đặt. Hiệu quả về thời gian thực hiện và dung lượng bộ nhớ cần để lưu trữ

# 2. Độ phức tạp thuật toán (Big O) cho biết thuật toán nhanh hay chậm: Độ phức tạp(O) = n*số phép toán

################################ Tổng hợp kiến thức slide 6 ########################################

# 1. Tìm kiếm là quá trình tìm một phần tử từ trong một tập hợp các phần tử dựa vào yêu cầu nào đó
    # tập hợp một phần tử có thể là mảng, danh sách...
    # mục tiêu tìm kiếm chính là vị trí của phần tử cần tìm

# 2. Tìm kiếm tuần tự

# 3. Tìm kiếm nhị phân (Lưu ý: mảng phải được sắp xếp trước khi thực hiện phép toán)
    # ý tưởng: B1: chia đôi mảng làm hai lấy phần tử cần tìm so sánh với phần tử ở giữa nếu đúng trả về kết quả nếu sai -> B2
             # B2: So sánh giá trị cần tìm với phần tử giữa nếu lớn hơn thì tiếp tục với phần bên phải, nếu nhỏ hơn hơn tiếp tục với phần bên trái
             # B3: cứ lặp lại B1 -> B2 nếu tìm thấy phần tử cần tìm thì dừng còn không tìm thấy thì trả về null không tồn tại.

############################### Tổng hợp kiến thức slide 7 #########################################

# 1. Sắp xếp chèn (O(n^2))
    # B1: Tạo danh sách rỗng
    # B2: Tìm giá trị lớn nhất
    # B3: Chuyển giá trị lớn nhất vào danh sách mới
    # B4: Xóa khỏi danh sách cũ
    # Cứ lặp lại như vậy cho đến khi danh sách cũ trống.

# 2. Sắp xếp bong bóng (sắp xếp nỏi bọt) (O(n^2))
    # ý tưởng: liên tục xét hai phần tử liền kề và hoán đổi vị trí của chúng sao cho các phần tử lớn hơn nổi lên ở cuối mảng

############################### Tổng hợp kiến thức slide 10 #######################################

# 1. Tập hợp (Set) là một dạng cấu trúc dữ liệu
    # dùng để lưu trữ các phần tử không trung lặp
    # các phần tử không có thứ tự
    # thay đổi được (mutable)

fruit_basket = {"apple", "banana", "cherry", "apple"}

for fruit in fruit_basket:
    print(fruit)

fruit_basket.add("orange") #thêm
fruit_basket.update({"kiwi", "peach"}) #thêm

fruit_basket.remove("apple") #xóa
fruit_basket.discard("apple") #xóa

lunch = {"soup", "sandwich", "omelet"}
dinner = {"soup", "steak"}

meals = lunch.union(dinner) # phép hợp
meals = lunch | dinner # phép hợp

meals = lunch.intersection(dinner) # phép giao
meals = lunch & dinner # phép giao

# 2. Ánh xạ (mapping) giống như một cỗ máy biến đổi. Có thể hiểu ánh xạ là một hàm tính toán được áp dụng lên các phần tử trong danh sách
map(function, itertable) # funtion: là hàm đển biến đổi phân tử. itertable là đối tượng có thể duyệt(list, set...)

students = ["Hieu", "My Anh", "Tuan Anh"]
students_upper = map(str.upper, students)
print(list(students_upper))

# 3. Ánh xạ: Dictinary
    # cấu trúc dữ liệu dict trong python cũng hoạt động dựa trên cơ chế ánh xạ
    # Đặc điểm: các key là độc nhất, mỗi key là ánh xạ đến một value duy nhất(ánh xạ 1-1)

phone_book = {} # or
phone_book = dict()

phone_book['John'] = '12323456'
phone_book['Alice'] = '0987654'

print(phone_book.get("Alice"))
del phone_book["John"]

################################## Tổng hợp kiến thức slide 11 ##################################

# 1. Ngăn xếp (Stack) là một kiểu danh sách mà thao tác thêm và xóa phần tử được thực hiện ở cuối dánh sách
    # là kiểu dữ liệu Last In - First Out (LIFO)

stack = [1,2,3]
stack.append(4) # stack = [1,2,3,4]

top = stack.pop() # stack = [1,2,3]
print(top) # 4

################################## Tổng hợp kiến thức slide 12 ###################################3

# 1. Hàng đợi(Queue) là một kiểu danh sách mà thêm phần tử ở cuối dánh sách còn loại bỏ ở đầu danh sách.
    # First In - First Out (FIFO)

queue = [1,2,3]
queue.append(4) # queue = [1,2,3,4]

front = queue.pop(0) # queue = [2,3,4]
print(front) # 1

