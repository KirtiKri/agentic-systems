import numpy as np

def analyze_dau(dau_list):
    arr = np.array(dau_list)
    mean_daun = np.mean(arr)
    trend_delta = arr[-3:].mean() - arr[0:2].mean() 
    is_uptrend = trend_delta> 0
    result = {
        "mean_daun": mean_daun,
        "trend_delta" : trend_delta ,
        "is_uptrend" : is_uptrend
    }
    return result

data = [120, 118, 125, 130, 128, 135, 140]
output = analyze_dau(data)
print(output)