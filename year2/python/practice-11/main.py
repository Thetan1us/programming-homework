import numpy as np

def main():
    pressures = np.random.normal(loc=70.0, scale=10, size=50_000)
    cleaned_pressures = np.where(pressures < 0, 0.0, pressures)

    emergency_mask = (cleaned_pressures < 40.0) | (cleaned_pressures > 95.0)
    emergencies = cleaned_pressures[emergency_mask]
    emergency_percentage = (emergencies.size / cleaned_pressures.size) * 100

    normal_pressures = cleaned_pressures[~emergency_mask]
    normal_mean = float(np.mean(normal_pressures))
    normal_median = float(np.median(normal_pressures))

    print(f"Total normal measures: {normal_pressures.size}")
    print(f"Normal Mean: {normal_mean:.2f}, Median: {normal_median:.2f}")
    print(f"Emergencies: {emergencies.size} ({emergency_percentage:.2f}%)")

if __name__ == "__main__":
    main()