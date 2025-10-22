import pandas as pd
import random
from datetime import datetime, timedelta

# Generate fake logs for insider threat simulation
data = {
    "timestamp": [datetime(2025, 10, 22, 2, i) for i in range(10)],
    "user_id": ["user123" for _ in range(10)],
    "file_name": ["Client_NAS.zip" for _ in range(10)],  # Changed from Client_SINs.zip
    "operation": random.choices(["download", "share", "access"], k=10),
    "dest_ip": ["172.16.254.1" if i % 2 else "192.168.1.100" for i in range(10)],
    "file_size": [random.randint(1000, 1000000) for _ in range(10)]
}
df = pd.DataFrame(data)
df.to_csv("data/fake_logs.csv", index=False)
print("Fake logs generated in data/fake_logs.csv")