import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')  # o'zingizning settings yo'lingizga o'zgartiring
django.setup()

from blog.models import Master, Mentor, Group, Student, StudentGroup  # o'zingizning app nomiga o'zgartiring


def run():
    print("Ma'lumotlar tozalanmoqda...")
    StudentGroup.objects.all().delete()
    Student.objects.all().delete()
    Group.objects.all().delete()
    Mentor.objects.all().delete()
    Master.objects.all().delete()

    print("Master (fanlar) yaratilmoqda...")
    math = Master.objects.create(subject="Matematika")
    physics = Master.objects.create(subject="Fizika")
    english = Master.objects.create(subject="Ingliz tili")
    programming = Master.objects.create(subject="Dasturlash")
    chemistry = Master.objects.create(subject="Kimyo")

    print("Mentor (o'qituvchilar) yaratilmoqda...")
    mentor1 = Mentor.objects.create(firstname="Alisher", lastname="Karimov", master=math)
    mentor2 = Mentor.objects.create(firstname="Dilnoza", lastname="Yusupova", master=math)
    mentor3 = Mentor.objects.create(firstname="Bobur", lastname="Rahimov", master=physics)
    mentor4 = Mentor.objects.create(firstname="Malika", lastname="Toshmatova", master=english)
    mentor5 = Mentor.objects.create(firstname="Sardor", lastname="Nazarov", master=programming)
    mentor6 = Mentor.objects.create(firstname="Nilufar", lastname="Ergasheva", master=programming)
    mentor7 = Mentor.objects.create(firstname="Jasur", lastname="Hamidov", master=chemistry)

    print("Talabalar yaratilmoqda...")
    students_data = [
        ("Azizbek", "Tursunov", 8),
        ("Barno", "Mirzayeva", 9),
        ("Doniyor", "Xoliqov", 7),
        ("Feruza", "Abdullayeva", 10),
        ("Husan", "Qodirov", 8),
        ("Iroda", "Salimova", 9),
        ("Javlon", "Normatov", 7),
        ("Kamola", "Razzaqova", 10),
        ("Lochin", "Boymurodov", 8),
        ("Maftuna", "Sotvoldiyeva", 9),
        ("Nodir", "Usmonov", 7),
        ("Oydin", "Hamroyeva", 10),
        ("Parviz", "Botirov", 8),
        ("Rohila", "Xasanova", 9),
        ("Sanjar", "Zokirov", 7),
        ("Umida", "Qalandarova", 10),
        ("Vohid", "Teshaboyev", 8),
        ("Xurshid", "Mavlonov", 9),
        ("Yulduz", None, 7),
        ("Zafar", "Islomov", 10),
        ("Abdulloh", "Rустамов", 8),
        ("Barcha", "Holiqova", 9),
        ("Comil", "Tojiboyev", 7),
        ("Dildora", "Nazarova", 10),
        ("Eldor", "Sobirov", 8),
    ]

    students = []
    for firstname, lastname, grade in students_data:
        s = Student.objects.create(firstname=firstname, lastname=lastname, grade=grade)
        students.append(s)

    print("StudentGroup (talaba-guruh bog'liqliklari) yaratilmoqda...")

    # group1 - Matematika A: 1-6 talabalar
    for student in students[0:6]:
        StudentGroup.objects.create(student=student, group=group1)

    # group2 - Matematika B: 6-11 talabalar
    for student in students[5:11]:
        StudentGroup.objects.create(student=student, group=group2)

    # group3 - Fizika: 3-8 talabalar
    for student in students[2:8]:
        StudentGroup.objects.create(student=student, group=group3)

    # group4 - Ingliz tili Starter: 0-5
    for student in students[0:5]:
        StudentGroup.objects.create(student=student, group=group4)

    # group5 - Ingliz tili Advanced: 10-15
    for student in students[10:15]:
        StudentGroup.objects.create(student=student, group=group5)

    # group6 - Python Boshlang'ich: 7-13
    for student in students[7:13]:
        StudentGroup.objects.create(student=student, group=group6)

    # group7 - Python Pro: 13-19
    for student in students[13:19]:
        StudentGroup.objects.create(student=student, group=group7)

    # group8 - Kimyo: 18-25
    for student in students[18:25]:
        StudentGroup.objects.create(student=student, group=group8)

    print("\n✅ Seed data muvaffaqiyatli yuklandi!")
    print(f"   Master      : {Master.objects.count()} ta")
    print(f"   Mentor      : {Mentor.objects.count()} ta")
    print(f"   Group       : {Group.objects.count()} ta")
    print(f"   Student     : {Student.objects.count()} ta")
    print(f"   StudentGroup: {StudentGroup.objects.count()} ta")


if __name__ == '__main__':
    run()