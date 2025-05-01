class BatteryMonitor:
    def __init__(self, battery_capacity_kwh=10.0, avg_power_consumption_kw=2.0, efficiency=0.85):
        """Initialize the battery monitor with system specifications.
        
        Args:
            battery_capacity_kwh (float): Total battery capacity in kilowatt-hours
            avg_power_consumption_kw (float): Average power consumption in kilowatts
            efficiency (float): Battery discharge efficiency (0-1)
        """
        self.battery_capacity = battery_capacity_kwh
        self.avg_power_consumption = avg_power_consumption_kw
        self.efficiency = efficiency
    
    def calculate_runtime(self, battery_percentage):
        """Calculate estimated runtime based on current battery percentage.
        
        Args:
            battery_percentage (float): Current battery percentage (0-100)
            
        Returns:
            float: Estimated runtime in hours
        """
        if not 0 <= battery_percentage <= 100:
            raise ValueError("Battery percentage must be between 0 and 100")
        
        # Calculate available energy in kWh
        available_energy = (self.battery_capacity * battery_percentage / 100) * self.efficiency
        
        # Calculate runtime in hours
        runtime = available_energy / self.avg_power_consumption
        
        return round(runtime, 2)
        
    def calculate_required_percentage(self, desired_runtime):
        """Calculate required battery percentage for desired runtime.
        
        Args:
            desired_runtime (float): Desired runtime in hours
            
        Returns:
            float: Required battery percentage (0-100)
        """
        if desired_runtime <= 0:
            raise ValueError("Desired runtime must be greater than 0")
        
        # Calculate required energy in kWh
        required_energy = desired_runtime * self.avg_power_consumption
        
        # Calculate required battery percentage
        required_percentage = (required_energy / (self.battery_capacity * self.efficiency)) * 100
        
        if required_percentage > 100:
            raise ValueError(f"Desired runtime of {desired_runtime} hours requires {round(required_percentage, 2)}% battery capacity, which exceeds 100%")
        
        return round(required_percentage, 2)
    
    def calculate_optimal_power(self, desired_runtime, battery_percentage=100):
        """Calculate optimal power consumption for desired runtime.
        
        Args:
            desired_runtime (float): Desired runtime in hours
            battery_percentage (float): Available battery percentage (0-100), defaults to 100
            
        Returns:
            float: Optimal power consumption in kilowatts
        """
        if desired_runtime <= 0:
            raise ValueError("Desired runtime must be greater than 0")
        if not 0 <= battery_percentage <= 100:
            raise ValueError("Battery percentage must be between 0 and 100")
            
        # Calculate available energy in kWh
        available_energy = (self.battery_capacity * battery_percentage / 100) * self.efficiency
        
        # Calculate optimal power consumption in kW
        optimal_power = available_energy / desired_runtime
        
        return round(optimal_power, 2)

def main():
    print("\nEnter system specifications:")
    print("----------------------------")
    
    # Get system specifications from user
    try:
        battery_capacity = float(input("Enter battery capacity (kWh): "))
        power_consumption = float(input("Enter average power consumption (kW): "))
        efficiency = float(input("Enter battery efficiency (0-1): "))
        
        if not 0 < efficiency <= 1:
            raise ValueError("Efficiency must be between 0 and 1")
        if battery_capacity <= 0:
            raise ValueError("Battery capacity must be greater than 0")
        if power_consumption <= 0:
            raise ValueError("Power consumption must be greater than 0")
            
        # Create battery monitor instance with user specifications
        monitor = BatteryMonitor(battery_capacity, power_consumption, efficiency)
        
        while True:
            try:
                print("\nSelect calculation mode:")
                print("1. Calculate runtime from battery percentage")
                print("2. Calculate required battery percentage for desired runtime")
                print("3. Calculate optimal power consumption for desired runtime")
                print("4. Exit")
                
                mode = input("Enter mode (1-4): ")
                
                if mode == "4":
                    print("Exiting program...")
                    break
                elif mode == "1":
                    percentage = float(input("Enter current battery percentage (0-100): "))
                    runtime = monitor.calculate_runtime(percentage)
                    print(f"\nEstimated runtime at {percentage}% battery:")
                    print(f"Hours: {runtime}")
                    print(f"Days: {round(runtime/24, 2)}")
                elif mode == "2":
                    hours = float(input("Enter desired runtime in hours: "))
                    percentage = monitor.calculate_required_percentage(hours)
                    print(f"\nRequired battery percentage for {hours} hours runtime:")
                    print(f"Battery percentage needed: {percentage}%")
                elif mode == "3":
                    hours = float(input("Enter desired runtime in hours: "))
                    battery_percent = float(input("Enter available battery percentage (0-100, default 100): ") or 100)
                    optimal_power = monitor.calculate_optimal_power(hours, battery_percent)
                    print(f"\nOptimal power consumption for {hours} hours runtime at {battery_percent}% battery:")
                    print(f"Power consumption needed: {optimal_power} kW")
                else:
                    print("Invalid mode selection. Please try again.")
                
            except ValueError as e:
                print(f"Error: {str(e)}")
            except Exception as e:
                print(f"An unexpected error occurred: {str(e)}")
                
    except ValueError as e:
        print(f"Error in system specifications: {str(e)}")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    print("Solar Battery Runtime Calculator")
    print("================================")
    main()