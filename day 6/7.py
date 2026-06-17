phone_number = "7777777777"
otp = "2513165"

if phone_number == "7777777777" and otp == "251365":
    print("Login successful")
elif phone_number == "7777777777" and otp != "251365":
    print("Invalid OTP")
else:
    print("Invalid phone number")