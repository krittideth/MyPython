print("วิธีคํานวณ bmi ในการหาค่าดัชนีมวลกาย")
kg = int(input("นํ้าหนัก: "))
cm = int(input("ส่วนสูง: "))
bmi = kg/(cm/100)**2
if bmi<18.50:     
    print("นํ้าหนักน้อย")
elif bmi>=18.5 and bmi <=22.90:
    print("ปกติ")
elif bmi>=23 and bmi <=24.90:
    print("ท้วม")      
elif bmi>=25 and bmi <=29.90:
    print("อ้วน")      
elif bmi>=30:
    print("อ้วนมาก")      