a = 10
class chalkAndDusterException(Exception):
    pass
try:
    # print(a/10)
    if a % 2 == 0:
        raise chalkAndDusterException()
except chalkAndDusterException:
    print("Exception caught")
else:
    print("hello form else block/there was no exceptions")
finally:
    print("this get executed in any condition")

print("Program terminated")