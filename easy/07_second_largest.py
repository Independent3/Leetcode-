#Given a list of numbers, find and print the second largest number without using sort().


numbers = [3, 7, 2, 9, 4, 1, 8]

#xrisimopoiw 2 variables , 1 gia to max kai thn allh gia to epomeno meta tou max
mik = numbers[0]
meg = numbers[1]
if mik > meg:
    meg = numbers[0]
    mik = numbers[1]
for i in range(2,len(numbers)):
    if meg < numbers[i]:
        x = meg
        meg = numbers[i]
        mik = x
    elif mik < numbers[i]:
        mik = numbers[i]
print(mik)