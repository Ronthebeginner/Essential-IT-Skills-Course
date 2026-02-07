import matplotlib.pyplot as plt

def plot_smoothing(temps, smoothed_values, forecast):
    days = list(range(1, len(temps) + 1))
    plt.figure(figsize=(8, 5))
    plt.plot(days, temps, 'o-', label='Original Temperatures')
    plt.plot(days, smoothed_values, 's-', label='Smoothed Values (SES)')
    plt.plot(len(temps) + 1, forecast, 'r*', markersize=12, label='Forecast (Next Day)')
    plt.xlabel('Day')
    plt.ylabel('Temperature')
    plt.title('Single Exponential Smoothing and Forecast')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def read_alpha():
    while True:
        try:
            a = float(input("Please input the smoothing coefficient (0 ≤ a ≤ 1): "))
            if 0 <= a <= 1:
                return a
            else:
                print("Invalid input! The number must be between 0 and 1.")
        except ValueError:
            print("Invalid input! Please enter a numeric value.")

def read_temperatures():
    MIN_TEMP = -50  # lower bound
    MAX_TEMP = 60   # upper bound

    while True:
        temps = input(f"Please enter the average temperatures of past days (between {MIN_TEMP} and {MAX_TEMP} °C), separated by spaces: ").split()
        if len(temps) < 1:
            print("You must enter at least one temperature. Please try again.")
            continue
        try:
            temps_list = [float(t) for t in temps]
            # Check range
            if all(MIN_TEMP <= t <= MAX_TEMP for t in temps_list):
                return temps_list
            else:
                print(f"Error: All temperatures must be between {MIN_TEMP} and {MAX_TEMP} °C. Please try again.")
        except ValueError:
            print("Please enter valid numbers for temperatures.")


def exponential_smoothing(temps, alpha):
    smoothed_values = [temps[0]]
    for t in range(1, len(temps)):
        s = alpha * temps[t] + (1 - alpha) * smoothed_values[t-1]
        smoothed_values.append(s)
    forecast = smoothed_values[-1]
    return smoothed_values, forecast

def main():
    alpha = read_alpha()
    temps_list = read_temperatures()
    smoothed_values, forecast = exponential_smoothing(temps_list, alpha)

    print("Smoothed values:", [f"{v:.2f}" for v in smoothed_values])
    print(f"Forecast for next day: {forecast:.2f}")

    print("Displaying plot...")
    plot_smoothing(temps_list, smoothed_values, forecast)

if __name__ == "__main__":
    main()


   





