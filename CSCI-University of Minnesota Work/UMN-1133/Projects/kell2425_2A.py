#  CSci 1133 HW 2
#  Jack Kelly
#  HW Problem 2A

#This funtion calculates the BMI based on W and H (weight and height respectivly)
# BMI = W/H**2
#input: weight W in kilos, H height in meters
#output BMI
def get_BMI(W,H):
    bmi = W/(H**2);
    return bmi
#This funtion calculates the BMI  Status based BMI 
#input: BMI
#output BMI category as a string
def get_BMI_status(BMI):
    if BMI<18.5:
        return "UnderWeight"
    if BMI>18.5 and BMI<25:
        return "Normal"
    if BMI>=25 and BMI<30:
        return "OverWeight"
    if BMI>=30.0:
        return "Obese"

#start program
print("Welcome to the BMI Calculator!");
weight = float(input('Enter body weight, in kilograms: '));
height = float(input('Enter body height, in meters: '));
#gets user input for weight and height
print('The BMI is: ', "{:.1f}".format(get_BMI(weight, height)))
print('The corresponding weight status is:', get_BMI_status(get_BMI(weight, height)))
#gets bmi and prints by calling function 'get_BMI_status'