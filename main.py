# This is a reductive CLI tool which provides an easy, guided way of changing the AMD P-State EPP power preferences.

# Imports "os" to run bash scripts.
import os

# Inputs can be "default," "performance," "balance_performance," "balance_power," or "power." Self explanatory.
preference = input("Enter the preferred option for AMD's P-State: '1' for 'power,' '2' for 'balance_power,' '3' for 'balance_performance,' '4' for 'performance,' and '5' for 'default.'\n")

# Determine output.
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
    print("An unrecognized input has been made. Aborting.") # In the event of a non-answer.

