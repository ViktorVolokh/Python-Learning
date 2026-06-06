path = r"C:\python\name.txt"
print(path)
example = 'example'
c0 = example[0]
c_last = example[-1]
result = (c0 == c_last)
print(result)
text = 'hello, you have to eat, sleep and work'
print(text[7:29])
name = 'Anton'
age = 31
family = 'separated'
info = name + ' ' + str(age) + ' ' + family
info_modern = f"{name} {age} {family}"
print(info)
print(info_modern)
text1 = 'Where are you? I\'m seeking\n'
print(text1 * 10)
text2 = "exAmPLeTEXt"
print(text2)
print(text2.upper())
print(text2.lower())
print(text2)
print(ord('A'))
print(ord('a'))
text3 = "the"
log_row = "[2026-06-06 14:23:11] [SERVER_1] [ERROR] Database connection lost!"
is_broken = "ERROR" in log_row or "CRITICAL" in log_row
print(is_broken)