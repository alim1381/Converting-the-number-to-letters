yekan = ["zero" , "one" , "two" , "three" , "four" , "five",  "six" , "seven" , "eight" , "nine", "ten" , "eleven" , "twelve" ,  "thirteen" , "fourteen" , "fifteen" , "sixteen" , "seventeen" , "eighteen" , "nineteen" , "twenty"]

dahgan = [" " , " " , "twenty" , "thirty" , "forty" , "fifty" , "sixty" , "seventy" , "eighty" , "ninety"]

saad = "hundred"
hezar = "thousand"



def numberstoletters(num):
    if num <= 1000 :
        adad = str(num)
        if num <= 20 :
            return yekan[num]
        c = len(adad)
        match c :
            case 2 :
                return zireSaad(num)
            case 3 :
                return toSaad(num)
            case 4 :
                return "one " + hezar
    else :
        return "Pleace enter a number in range 0 to 1000" 

def zireSaad(num) :
    adad = str(num)
    if num <= 20 :
        return yekan[num]
    if adad[1] == 0 :
        f = dahgan[int(adad[0])]
        return f
    else :
        f = dahgan[int(adad[0])] + ' ' + yekan[int(adad[1])]
        return f

def toSaad(num) :
    adad = str(num)
    if int(adad[1]) == 0  or int(adad[2]) == 0 :
        re = int(adad[1]) + int(adad[2])
        n = str(re)
    else :
        n = adad[1]+adad[2]
    f = yekan[int(adad[0])] + " " + saad + " " + "and" + " " + zireSaad(int(n))
    return f
inp = input("Enter Your Number : ")
print (numberstoletters(int(inp)))