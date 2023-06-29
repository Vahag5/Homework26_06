def power_of(n) :
    def power(x) :
        return  x ** n
    return power


power_qarakusi = power_of(2)  
power_xoranard = power_of(3)

print(power_qarakusi(2))  # 4
print(power_qarakusi(10)) # 100
print(power_xoranard(3))  # 27
print(power_xoranard(5))  # 125  
