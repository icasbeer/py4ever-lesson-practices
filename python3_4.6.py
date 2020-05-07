hours = input("Enter Hours:")
rate = input("Enter Rate:")
def computepay(h,r):

    h = float(hours)
    r = float(rate)
    if h > 40:
        reg = h * r 
        # print(reg)
        otp = (h - 40.0) * (r * 0.5)
        # print(otp)
        xp = reg + otp
    else:
        xp = h * r
    return print('Pay' , xp)

computepay(hours, rate)

#learning how to commit to github