temp = float(input("Enter temperature: "))
choice = str(input("Enter unit in F/f or C/c: "))
if choice == 'f' or choice == 'F':
  celsius = (temp - 32) * 5/9
  print(f"{temp}° in Fahrenheit is equivalent to {celsius}° Celsius.")
elif choice == 'c' or choice == 'C':
  faren = (temp * 9/5) + 32
  print(f"{temp}° in Celsius is equivalent to {faren}° Fahrenheit.")
else:
  print("Invalid unit(bad).")