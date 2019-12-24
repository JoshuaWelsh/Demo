#Joshua Welsh Gold #3
#Competition instructions provided at: https://www.seminolestate.edu/computers/competition/samples/2019
def findSum(num):
    total = 0
    p = 1
    for i in num:
        total+=int(i)*p
        p+=1
    return total

def main():
    num = input("Enter the number: ")
    total = findSum(num)
    print("weighted sum is",total)

def test():
    valid = True
    samples = {"57":19,"482178":113,"32058":67} #Provided by Judges
    for sample in samples:
        result = findSum(sample)
        expected = samples[sample]
        if result!=expected:
            print("Error at",sample)
            print("Expected:",expected,"Result:",result)
            valid = False
            break
    if valid:
        print("All tests passed")

debug = False
if debug:
    test()
else:
    main()
