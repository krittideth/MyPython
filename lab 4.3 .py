x = {
    "name": "Krittideth",
     "age":18,
     "wt":67,
     "h": 162
     }
print(x)
print("สวัสดีครับคุณ %s" % x["name"])
print("พ.ศ.เกิด %d อายุ %d" % (2567-x["age"], x["age"]))
print("นํ้าหนัก %d ส่วนสูง %d" % (x["wt"], x["h"]))