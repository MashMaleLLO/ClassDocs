class translater:
    def decToRoman(self,num):
        num = int(num)
        roman = ""
        dec = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
        sym = ["I", "IV", "V", "IX", "X", "XL","L", "XC", "C", "CD", "D", "CM", "M"]
        i = 12
        while num > 0:
            div = num // dec[i]
            num = num % dec[i]
            while div > 0:
                roman += sym[i]
                div -= 1
            i -= 1        
        return roman

    def romanToDec(self,rom):
        sym = {"I":1, "IV":4, "V":5, "IX":9, "X":10, "XL":40,"L":50, "XC":90, "C":100, "CD":400, "D":500, "CM":900, "M":1000}
        num = 0
        i = 0
        while i < len(rom):
            if i+1<len(rom) and rom[i:i+2] in sym:
                num += sym[rom[i:i+2]]
                i += 2
                pass
            else:
                num += sym.get(rom[i])
                i += 1
        return num

            


                        
inp = int(input("Enter number to translate : "))
c = translater()
print(c.decToRoman(inp))
print(c.romanToDec(c.decToRoman(inp)))

