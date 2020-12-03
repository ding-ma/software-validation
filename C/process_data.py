import os

import pandas as pd

base_path = os.path.join("test_data")

sys_logs = pd.read_csv(os.path.join(base_path, "system_logs.csv"))
# drop cpu logs that are 0
sys_logs.drop(sys_logs.index[sys_logs['cpu_usage(%)'] == 0], inplace=True)

# read from a list later
add_cat = pd.read_csv(os.path.join(base_path, "add_category_time_stamps_t1.csv"))

for iteration in add_cat.itertuples():
    start_index = abs(sys_logs['time'] - iteration.Time_start).idxmin()
    end_index = abs(sys_logs['time'] - iteration.Time_end).idxmin()
    # data_point = sys_logs.loc[[start_index,end_index]]

    print(start_index, iteration.Time_start, end_index, iteration.Time_end)
    print(sys_logs[start_index:end_index])
    # print(data_point['total_used_memory(bytes)'])
    # print(data_point['cpu_usage(%)'])
    # print(sys_logs[end_index - 5: end_index])
    print("----------------------")
print(sys_logs.shape)
