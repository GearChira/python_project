def computepay (hour, rate) :
    
    std_pay = hour * rate
    
    if hour > 40:
        ot_hour = hour - 40 
        ot_rate = 1.5

        normal_pay = (hour - ot_hour) * rate
        ot_pay = normal_pay + (ot_hour * (rate * ot_rate))

        print("Your pay will be " + str(ot_pay) + " USD.")

    else:
        print("Your pay will be " + str(std_pay) + " USD.")


try:
    wh = float(input("Enter your working hour: "))
    wr = float(input("Enter your working rate: "))
except:
    print('Please make sure to input numeric only for hour and rate.')
    quit()

computepay(wh, wr)
