# Task 6 Gas Bill Calculator 

When  you submit a gas meter reading it converts the units used to kilowatt  hours (kWh).  When receiving a bill your previous and current reading is  used to calculate the number of imperial units and then this number is  converted to kilowatt hours. Each kilowatt hour costs  3.74p. VAT is also charged on the total due at 5%. 

Create  a function that will allow you to pass in the previous reading, current  reading , calculate the number of kilowatt hours used (see formula  below) and return the amount due (rounded to two decimal places). 

Previous Reading: **4805** 

Current Reading:  **5061** 

You have used **256** units 

This is **8,087.96** kilowatt hours 

Your bill is: **£317.61** 

The formula for it is: 

**256.00** imperial units used 
 **x 1.022640** volume correction 
 **x 2.83** to convert to metric 
 = 740.88 metric units 
 **x 39.3** calorific value 
 **÷ 3.6** to convert to kWh 
 = 8,087.96 kWh 

**Top Level Design and Data Flow** 

**Main Steps                       In**       **Out** 

**1** Get Input Data 

**2** Calculate Amount Due 

**3** Display BIll Details 