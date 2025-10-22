import pandas as pd
import matplotlib.pyplot as plt

# Read fake logs
df = pd.read_csv("data/fake_logs.csv")

# Find suspicious shares (2 AM, external IP starting with 172.)
suspicious = df[(df['operation'] == 'share') & (df['timestamp'].str.contains('02:')) & (df['dest_ip'].str.startswith('172.'))]
print("Suspicious shares:", suspicious)

# Create a simple plot to mimic Splunk dashboard
df['timestamp'] = pd.to_datetime(df['timestamp'])
df['hour'] = df['timestamp'].dt.hour
activity_by_hour = df.groupby('hour').size()
activity_by_hour.plot(kind='bar', title='Activity by Hour', color='#1f77b4')
plt.xlabel('Hour of Day')
plt.ylabel('Number of Events')
plt.savefig('reports/activity_plot.png')
plt.close()
print("Plot saved in reports/activity_plot.png")