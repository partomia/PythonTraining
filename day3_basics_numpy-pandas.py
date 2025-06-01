import numpy as np
import pandas as pd

# numpy first
# Create array
cpu_cores = np.array([2, 4, 8, 16])
ram_gb = np.array([8, 16, 32, 64])

# Element-wise operations
print(cpu_cores + 2)      # Add 2 to each element
print(cpu_cores * ram_gb) # Multiply arrays element-wise
print(ram_gb > 16)        # Boolean mask

# pandas now

data = {
    "hostname": ["worker1", "worker2", "worker3"],
    "cpu_cores": [4, 2, 8],
    "ram_gb": [16, 8, 64]
}

df = pd.DataFrame(data)
print(df)

# Filter rows
high_capacity = df[(df['cpu_cores'] >= 4) & (df['ram_gb'] >= 16)]
print("Eligible Nodes:\n", high_capacity)

df = pd.read_csv("cluster_nodes.csv")

df["poc_ready"] = (df["cpu_cores"] >= 4) & (df["ram_gb"] >= 16)
print("Eligible Nodes:\n", df[df["poc_ready"]])

# Save result
df[df["poc_ready"]].to_csv("poc_ready_nodes.csv", index=False)

