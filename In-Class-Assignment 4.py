#Student Name: Arjun Bindhu Suresh
#Student ID: 100990351
# COSC 1104 – In-Class 4




import json

# Function to load data from the JSON file
def load_ec2_data(file_name):
    try:
        with open(file_name, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
        return None
    except json.JSONDecodeError:
        print("Error: The file could not be decoded. Please check if it is a valid JSON file.")
        return None

# Function to get user input for CPU and memory requirements
def get_user_requirements():
    while True:
        try:
            min_cpu = int(input("Enter the minimum required CPU cores: "))
            break
        except ValueError:
            print("Please enter a valid number for minimum CPU cores.")

    max_cpu_input = input("Enter the maximum CPU cores (optional): ")
    max_cpu = int(max_cpu_input) if max_cpu_input else None

    while True:
        try:
            min_memory = float(input("Enter the minimum required memory in GiB: "))
            break
        except ValueError:
            print("Please enter a valid number for minimum memory.")

    max_memory_input = input("Enter the maximum memory in GiB (optional): ")
    max_memory = float(max_memory_input) if max_memory_input else None

    return min_cpu, max_cpu, min_memory, max_memory

# Function to filter instances based on user requirements
def filter_instances(ec2_data, min_cpu, max_cpu, min_memory, max_memory):
    filtered_instances = []
    for instance in ec2_data:
        cpu_cores = int(instance.get('vcpu', '0 vCPUs').split()[0])  
        memory = float(instance.get('memory', '0 GiB').split()[0]) 

        if cpu_cores >= min_cpu and (max_cpu is None or cpu_cores <= max_cpu) and \
           memory >= min_memory and (max_memory is None or memory <= max_memory):
            filtered_instances.append(instance)

    return filtered_instances

# Function to display the filtered EC2 instances
def display_filtered_instances(instances):
    if not instances:
        print("No instances found matching the criteria.")
        return

    print("\nFiltered EC2 Instances:")
    print('*' * 30)
    for instance in instances:
        print(f"Instance Type: {instance['name']}, CPU Cores: {instance['vcpu']}, Memory: {instance['memory']}")
    print('*' * 30)

# Main function
def main():
    ec2_data = load_ec2_data('ec2_instance_types.json')  

    if ec2_data is not None:
        min_cpu, max_cpu, min_memory, max_memory = get_user_requirements()
        filtered_instances = filter_instances(ec2_data, min_cpu, max_cpu, min_memory, max_memory)
        display_filtered_instances(filtered_instances)

if __name__ == "__main__":
    main()
