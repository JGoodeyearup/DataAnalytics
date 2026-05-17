# about_me = open("about_me.txt")
# print(about_me.read())
# print(about_me.read())
# for i in range(1, 5):
#    print(about_me.readline(-1))
#    print(about_me.readline(100))
# about_me.close()

about_me50 = open("about_me.txt")
print(about_me50.read(50))
about_me50.close()

about_me_output = open("about_me.txt")
for i in range(1, 4):
    print(about_me_output.readline())
about_me_output.close()

about_me100 = open("about_me.txt")
for i in range(1, 5):
    print(about_me100.readlines(100))
