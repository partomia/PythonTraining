# day1_assigment.py

import logging
logging.basicConfig(
    filename='trace_env.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

try:
    user_input_cores = int(input("number of cpu cores: ").strip())
    user_input_ram = float(input("size of ram in gb: ").strip())

    if user_input_ram >=16 and user_input_cores >=4:
        print ("Ready for Cloudera PoC")
    else:
        print("Upgrade the System for PoC")
except ValueError as a:
    print("Invalid input. Please enter numeric value")
    logging.error(f"Invalid input error: {a}")

try:
    age = int(input("Enter your age: ").strip())  # if you enter "abc", it crashes
    print("You are", age, "years old.")
except ValueError as e:
    print("Invalid input. Please enter numeric value")
    logging.exception(f"Invalid input error: {e}")
