services = ["Hive", "HDFS", "Impala", "Kafka"]
print(services[0])      # Hive
services.append("NiFi")
print(services[-1])     # NiFi

# List iteration
for s in services:
    print("Service:", s)