from PIL import Image
img = Image.open("path/to/Ambatucumit.jpg")

# ฟังก์ชันแสดงรายชื่อมังงะทั้งหมดในระบบ
def show_manga(manga_list):
    for manga in manga_list:
        print(f"ชื่อ : {manga['manga_name']} , ราคา : {manga['manga_price']}")

#ฟังก์ชันตรวจสอบอายุตามข้อจำกัดของมังงะ
def check_age(user_age, age_restriction):
     if (user_age > age_restriction):
         print("age pass")
         if (user_age == "g"):
             print("age pass")
         else:
             print("too young")
         return user_age

# ฟังก์ชันคำนวณราคาตั๋วโดยขึ้นกับประเภทหนัง
# def calculate_price(base_price, genre):
     #if (genre == "Romantic" ):
         #base_price + 30
         #if (genre == "Gore"):
             #base_price + 40

def main():
    # TODO: สร้างรายการหนังเป็น list ของ dict โดยเก็บข้อมูล manga_name, manga_price, genre, age_restriction
    movies = [
        {'manga_name': 'Berserk', 'manga_price': 300, 'genre': 'Gore', 'age_restriction': '20'},
        {'manga_name': 'DragonBall', 'manga_price': 280, 'genre': 'Action', 'age_restriction': '13'},
        {'manga_name': 'Onepiece', 'manga_price': 180, 'genre': 'Action', 'age_restriction': '13'},
        {'manga_name': 'Pokemon', 'manga_price': 250, 'genre': 'Romantic', 'age_restriction': '13'},
        {'manga_name': 'My hero', 'manga_price': 260, 'genre': 'Adventure', 'age_restriction': '13'}
    ]
    movies_notpass = [
        {'manga_name': 'DragonBall', 'manga_price': 280, 'genre': 'Action', 'age_restriction': '13'},
        {'manga_name': 'Onepiece', 'manga_price': 180, 'genre': 'Action', 'age_restriction': '13'},
        {'manga_name': 'Pokemon', 'manga_price': 250, 'genre': 'Romantic', 'age_restriction': '13'},
        {'manga_name': 'My hero', 'manga_price': 260, 'genre': 'Adventure', 'age_restriction': '13'}
    ]

    # TODO: แสดงเมนูให้ผู้ใช้เลือก
    # 1. แสดงหนังทั้งหมด
    # 2. ซื้อตั๋วหนัง
    # รับค่าตัวเลือกเมนูจากผู้ใช้
    print("-----------------------------------------Welcome to Manga World-----------------------------------------")
    print("[1] เข้าร้านมังงะ")
    print("[2] ออกจากร้านมังงะ")
    menu = input("เลือกเมนู: ")
    if (menu == '1'):
        show_manga(movies)
    elif (menu == '2'):
        print("ขอบคุณที่มาเยี่ยมชมร้านมังงะ")
    
    age = int(input("กรุณากรอกอายุของคุณ: "))
    if ( age > 12 and age < 20):
         print("ซื้อได้หมดยกเว้น Gore")
         show_manga(movies_notpass)

    elif (age >= 20):
         print("ซื้อได้ทุกเรื่อง")
         show_manga(movies)
    else:
         print("อายุน้อยเกินไป กรุณาเลือกมังงะที่เหมาะสมกับอายุของคุณ")
    
    something = input("จะซื้อเรื่องอะไร : ")
    if something in [manga['manga_name'] for manga in movies]:
        print(f"คุณได้ซื้อมังงะเรื่อง {something} ราคา {next(manga['manga_price'] for manga in movies if manga['manga_name'] == something)} บาท")
    else:
        print("มังงะที่คุณเลือกไม่มีในร้าน")

    img.show()


main()