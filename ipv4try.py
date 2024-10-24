def ipv4():
    ipnum = input("Enter IP address: ")

    # Validate the input IP address format
    if not all(part.isdigit() for part in ipnum.split('.')) or len(ipnum.split('.')) != 4:
        print("Invalid IP address format.")
        return

    first_octet = int(ipnum.split('.')[0])  # Get the first octet directly

    # Determine the class of the IP address
    if first_octet <= 126:
        print("It's Class A.")
        print("Default Subnet Mask: 255.0.0.0")
        class_ip = 1
        subnet_bits = 8  # Class A default subnet bits
    elif 128 <= first_octet <= 191:
        print("It's Class B.")
        print("Default Subnet Mask: 255.255.0.0")
        class_ip = 2
        subnet_bits = 16  # Class B default subnet bits
    elif 192 <= first_octet <= 223:
        print("It's Class C.")
        print("Default Subnet Mask: 255.255.255.0")
        class_ip = 3
        subnet_bits = 24  # Class C default subnet bits
    else:
        print("IP address is not in Class A, B, or C.")
        return

    # Input for number of subnets
    try:
        sub = int(input("Enter number of subnets required: "))
    except ValueError:
        print("Invalid input for number of subnets.")
        return

    j = 0
    ans = 1

    # Calculate extra bits required for the number of subnets
    while ans < sub:
        ans *= 2
        j += 1

    print("Number of extra bits required = " + str(j))
    new_sub = j + subnet_bits
    print("New Subnet Mask: /" + str(new_sub))

    # Calculate total addresses per subnet
    total_addresses_per_subnet = 2 ** (32 - new_sub)  # Total addresses per subnet
    available_hosts_per_subnet = total_addresses_per_subnet - 2  # Subtract network and broadcast
    print("Available hosts in each subnet = " + str(available_hosts_per_subnet))

    # Calculate and display subnet ranges
    print("\nSubnet Ranges:")
    for i in range(sub):
        # Calculate subnet start and end addresses
        subnet_start = (int(ipnum.split('.')[0]) << 24) + (int(ipnum.split('.')[1]) << 16) + \
                       (int(ipnum.split('.')[2]) << 8) + (int(ipnum.split('.')[3]) + (i * total_addresses_per_subnet))

        subnet_end = subnet_start + available_hosts_per_subnet

        # Format and display the subnet range
        start_ip = f"{(subnet_start >> 24) & 0xFF}.{(subnet_start >> 16) & 0xFF}.{(subnet_start >> 8) & 0xFF}.{subnet_start & 0xFF}"
        end_ip = f"{(subnet_end >> 24) & 0xFF}.{(subnet_end >> 16) & 0xFF}.{(subnet_end >> 8) & 0xFF}.{subnet_end & 0xFF}"

        print(f"Subnet {i + 1}: {start_ip} to {end_ip}")


# Call the function
ipv4()
