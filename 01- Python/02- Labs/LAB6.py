import BIT_MATH 
import platform

x = BIT_MATH.SET_BIT(5,1)
print(x)

x = BIT_MATH.CLEAR_BIT(5,1)
print(x)

x = BIT_MATH.GET_BIT(5,1)
print(x)

x = BIT_MATH.TOGGLE_BIT(5,1)
print(x)

print(dir(BIT_MATH))

print(platform.system())        # Windows