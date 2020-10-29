# create the initial variables below
age = 28
sex = 0
BMI = 26.2
num_of_children = 3
smoker = 0

insurance_cost = 250 * age - 128 * sex + 370 * BMI + 425 * num_of_children + 24000 * smoker - 12500

print("This person's insurance cost is " + str(insurance_cost) + " dollars.")

age = 28
age += 4
print(age)

new_insurance_cost  = 250 * age - 128 * sex + 370 * BMI + 425 * num_of_children + 24000 * smoker - 12500

change_in_insurance_cost = new_insurance_cost - insurance_cost

print("The change in cost of insurance after increasing the age by 4 years is " + str(change_in_insurance_cost) + " dollars")

age = 28
BMI += 3.1

new_insurance_cost = 250 * age - 128 * sex + 370 * BMI + 425 * num_of_children + 24000 * smoker - 12500

change_in_insurance_cost = new_insurance_cost - insurance_cost

print("The change in estimated insurance cost after increasing BMI by 3.1 is " + str(change_in_insurance_cost) + " dollars")

BMI = 26.2
sex = 1

new_insurance_cost = 250 * age - 128 * sex + 370 * BMI + 425 * num_of_children + 24000 * smoker - 12500

change_in_insurance_cost = new_insurance_cost - insurance_cost

print("The change in estimated insurance cost for being male instead of female is " + str(change_in_insurance_cost) + " dollars")



smoker = 1

new_insurance_cost = 250 * age - 128 * sex + 370 * BMI + 425 * num_of_children + 24000 * smoker - 12500

change_in_insurance_cost = new_insurance_cost - insurance_cost

print("The change in estimated insurance cost for being a smoker instead of a nonsmoker is " + str(change_in_insurance_cost) + " dollars")

smoker = 0
num_of_children = 0

new_insurance_cost = 250 * age -128 * sex + 370 * BMI + 425 * num_of_children + 24000 * smoker - 12500

change_in_insurance_cost = new_insurance_cost - insurance_cost

print("The change in estimated insurance cost for having 0 children instead of 3 children is " + str(change_in_insurance_cost) + " dollars")