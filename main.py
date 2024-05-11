# This is a reductive CLI tool which provides an easy, guided way of changing the AMD P-State EPP power preferences.

# Imports "os" to run bash scripts.
import os

# Inputs can be "power," "balance_power," "balance_performance," "performance," or "default." Self explanatory.
print("Input the number value for the preferred AMD P-State power preference:")
print("1. power")
print("2. balance_power")
print("3. balance_performance")
print("4. performance")
print("5. default")

preference = input("Input: ")

# Determine output and P-State setting.
if preference == "1":
    os.system("echo 'AMD P-State power preference set to:' $(echo 'power' | tee /sys/devices/system/cpu/cpu*/cpufreq/energy_performance_preference)")
elif preference == "2":
    os.system("echo 'AMD P-State power preference set to:' $(echo 'balance_power' | tee /sys/devices/system/cpu/cpu*/cpufreq/energy_performance_preference)")
elif preference == "3":
        os.system("echo 'AMD P-State power preference set to:' $(echo 'balance_performance' | tee /sys/devices/system/cpu/cpu*/cpufreq/energy_performance_preference)")
elif preference == "4":
        os.system("echo 'AMD P-State power preference set to:' $(echo 'performance' | tee /sys/devices/system/cpu/cpu*/cpufreq/energy_performance_preference)")
elif preference == "5":
        os.system("echo 'AMD P-State power preference set to:' $(echo 'default' | tee /sys/devices/system/cpu/cpu*/cpufreq/energy_performance_preference)")
else:
    print("An unrecognized input has been made: aborting.") # In the event of a non-answer.

