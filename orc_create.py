Code1= "NY091330" 
Transaction_number= "0000003"
Settlement_date= "010523"
Sentral_id= "02"
Day_code= "01"
Partial_settlement_number= "1"
Serial_number= "61901"
Sign="0"
Amount= "00000000000010000" # The amount to be paid *need to put two zero after the amount
KID= "              03422962047" #give tkHelse KID 
Card_user= "00"
zeros = "0000"

Code2= "NY091331"
# Transaction_number= "0000053"
Form_number= "0000146912" #last two digits same transaction number
Agreement_id= "391009312"  # same as trans last two digits
leave_zeros1 = "0000000"
Assignment_date= "020523"
Debit_account= "39106361751" #last digits as KID

leave_zeros2 = "0000000000000000000000" 


# Open a file for writing
with open('OCR.D180523.txt', 'w') as f:
  
  # Write some values to the file
  f.write("NY000010000080803541911002300610000000000000000000000000000000000000000000000000\n"+
    "NY090020001520965000000132073186349000000000000000000000000000000000000000000000\n")
  f.write(Code1+Transaction_number+Settlement_date+Sentral_id+Day_code+Partial_settlement_number+
Serial_number+Sign+Amount+KID+Card_user+zeros+"\n")
  f.write(Code2+Transaction_number+Form_number+Agreement_id+leave_zeros1+Assignment_date+
Debit_account+leave_zeros2+"\n")
  f.write("NY090088000000670000013600000000002776900201222201222201222000000000000000000000\n"+
    "NY000089000000670000013800000000002776900201222000000000000000000000000000000000\n")

# Print a message to indicate that the file has been created
print('Output file generated successfully!')
