x = "awesome"

def myfunc():
    x = "fantastic"
    global z
    z = "good"
    print("Python is", x, '&', z)

myfunc()
print("Python is", x, "&", z, end = '')

