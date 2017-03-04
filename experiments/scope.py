

test = 1

def foo():
    global test
    print "foo test is: " + str(test)
    test = 2

def bar():
    global test
    print "bar test is: " + str(test)
    test = 3

foo()
bar()
foo()
