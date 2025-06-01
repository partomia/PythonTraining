import logging

# Logging setup
logging.basicConfig(
    filename='poc_validation.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Function for validation
def check_poc_eligibility(cpu_cores, ram_gb):
    if cpu_cores >= 4 and ram_gb >= 16:
        return "✅ Eligible for Cloudera PoC"
    else:
        return "❌ Not eligible. Upgrade system."

# Function to read config from file
def read_config(filepath):
    config = {}
    try:
        with open(filepath, 'r') as f:
            for line in f:
                key, value = line.strip().split("=")
                config[key.strip()] = value.strip()
    except Exception as e:
        logging.error(f"Error reading config file: {e}")
        print("❌ Could not read config file.")
    return config

# ---- Run Logic ----
config = read_config("node_config.txt")

# Convert values safely and validate
try:
    cpu = int(config.get("cpu_cores", 0))
    ram = float(config.get("ram_gb", 0))

    result = check_poc_eligibility(cpu, ram)
    print(result)
    logging.info(f"Validation result for CPU={cpu}, RAM={ram}: {result}")

except Exception as e:
    print("❌ Validation failed.")
    logging.exception(f"Validation error: {e}")