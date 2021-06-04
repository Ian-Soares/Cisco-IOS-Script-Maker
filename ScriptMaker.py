global commands_int_input, ip_selected
commands_int_input = 0
commands_int_range_input = 0

'''
Variable "layer" defines which block of permission I stoped, just like an
(config-if)# 
or an
(config-line)#
'''

def printCommandList():
    print('''
    ================================
      Welcome to the Script Maker!
    ================================
    To choose your script commands, you must input your options like that: 1,2,3,6,8,10,13
    (no use of spaces or [])

    [1] Change Hostname

    [2] Set a password 

    [3] Set a enable secret

    [4] Set a banner for the equipment

    [5] Create VLANs

    [6] Select a interface

    [7] Select a interface range

    [8] Create a SSH Remote Access
    
    [9] IP Routing

    [10] Subinterface
    ''')

def printInterfaceCommandList():
    print('''
    [11] Set IP Address (for Routers or SW L3)

    [12] Set a switchport mode (for Switches)

    [13] Shutdown

    [14] No shutdown
    ''')

def printVlanmodeInterface():
    print('''
    >>> In this interface(s) <<<

    [15] For access mode

    [16] For trunk mode
    ''')

def printIpRoutingCommands():
    print('''
    >>> Ip routing <<<

    [17] For a Static Routing

    [18] For a Default Routing
    ''')

def init_script():
    print('enable')
    global layer
    layer = '#'

def finish_script():
    print('end')
    print('wr')

def hostname(name):
    global layer
    if layer == '#':
        print('configure terminal')
        print(f'hostname {name}')
    elif layer == '(config)#':
        print(f'hostname {name}')
    elif layer == '(config-if)#' or layer == '(config-line)#':
        print('exit')
        print(f'hostname {name}')
    layer = '(config)#'

def password(psswrd):
    global layer
    if layer == '#':
        print('configure terminal')
        print('line console 0')

    elif layer == '(config)#' or layer == '(config-line)#':
        print('line console 0')

    elif layer == '(config-if)#':
        print('line console 0')
    print('service password-encryption')
    layer = '(config)#'

def secret(secret):
    global layer
    if layer == '#':
        print('configure terminal')

    elif layer == '(config)#':
        pass

    elif layer == '(config-if)#' or layer == '(config-line)#':
        print('exit')

    print(f'enable secret {secret}')
    layer = '(config)#'

def banner(motd):
    global layer
    if layer == '#':
        print('configure terminal')
        print('line console 0')
    
    elif layer == '(config)#':
        print('line console 0')
    
    elif layer == '(config-line)#':
        pass
    
    elif layer == '(config-if)#':
        print('exit')
        print('line console 0')

    print(f'banner motd "{motd}"')
    layer = '(config)#'

def createVlans(number, name):
    global layer
    if layer == '#':
        print('configure terminal')
    
    elif layer == '(config)#':
        pass

    elif layer == '(config-line)#' or layer == '(config-if)#':
        print('exit')

    for i in range(0, len(number)):
        print(f'vlan {number[i]}')
        print(f'name {name[i]}')
    layer = '(config-if)#'

def ip_interface(interface,ip):
    global layer
    if layer == '#':
        print('configure terminal')
    else:
        pass 
    print(f'interface {interface}')
    print(f'ip address {ip[0]} {ip[1]}')
    layer = '(config-if)#'

def vlan_access_interface(interface,vlan):
    global layer
    if layer == '#':
        print('configure terminal')
    else:
        pass
    print(f'interface {interface}')
    print('switchport mode access')
    print(f'switchport access vlan {vlan}')
    layer = '(config-if)#'

def vlan_trunk_interface(interface,native,allowed):
    global layer
    if layer == '#':
        print('configure terminal')
    print(f'interface {interface}')
    print('switchport mode trunk')
    print(f'switchport trunk native vlan {native}')
    print(f'switchport trunk allowed vlan {allowed}')
    layer = '(config-if)#'

def shutdown_interface(interface):
    global layer
    if layer == '#':
        print('configure terminal')
    print(f'interface {interface}')
    print('shutdown')
    layer = '(config-if)#'

def no_shutdown_interface(interface):
    global layer
    if layer == '#':
        print('configure terminal')
    print(f'interface {interface}')
    print('no shutdown')
    layer = '(config-if)#'

def ip_interface_range(interface_range, ip):
    global layer
    if layer == '#':
        print('configure terminal')
    print(f'interface range {interface_range}')
    print(f'ip address {ip[0]} {ip[1]}')
    layer = '(config-if)#'

def vlan_access_interface_range(interface_range, vlan):
    global layer
    if layer == '#':
        print('configure terminal')
    print(f'interface range {interface_range}')
    print('switchport mode access')
    print(f'switchport access vlan {vlan}')
    layer = '(config-if)#'

def vlan_trunk_interface_range(interface_range, native, allowed):
    global layer 
    if layer == '#':
        print('configure terminal')
    print(f'interface range {interface_range}')
    print('switchport mode trunk')
    print(f'switchport trunk native vlan {native}')
    print(f'switchport trunk allowed vlan {allowed}')
    layer = '(config-if)#'

def shutdown_interface_range(interface_range):
    global layer
    if layer == '#':
        print('configure terminal')
    print(f'interface range {interface_range}')
    print('shutdown')
    layer = '(config-if)#'

def no_shutdown_interface_range(interface_range):
    global layer
    if layer == '#':
        print('configure terminal')
    print(f'interface range {interface_range}')
    print('no shutdown')
    layer = '(config-if)#'

def ssh_lineVty(ipDomainName, modulusKey, lineVTYrange, userInfo):
    global layer
    if layer == '#':
        print('configure terminal')
    
    elif layer == '(config-if)#' or layer == '(config-line)#':
        print('exit')
    print(f'ip domain-name {ipDomainName}')
    print(f'crypto key generate rsa general-keys modulus {modulusKey}')
    print(f'line vty {lineVTYrange}')
    print(f'username {userInfo[0]} privilege {userInfo[1]} secret {userInfo[2]}')
    layer = '(config-line)#'

def static_routing(id_mask_destiny,who_knows_this_network):
    global layer
    if layer == '#':
        print('configure terminal')
    
    elif layer == '(config-line)#' or layer == '(config-if)#':
        print('exit')
    print(f'ip route {id_mask_destiny[0]} {id_mask_destiny[1]} {who_knows_this_network}')
    layer = '(config)#'

def default_routing(int_or_ip):
    global layer
    if layer == '#':
        print('configure terminal')
    
    elif layer == '(config-line)#' or layer == '(config-if)#':
        print('exit')
    print(f'ip route 0.0.0.0 0.0.0.0 {int_or_ip}')
    layer = '(config)#'

def subinterface_config(subint, vlan_subint, ip_subint):
    global layer
    if layer == '#':
        print('configure terminal')
    print(f'interface {subint}')
    print(f'encapsulation dot1q {vlan_subint}')
    print(f'ip address {ip_subint[0]} {ip_subint[1]}')
    layer = '(config-if)#'

##############################
#         INPUT AREA         #
##############################

while True:
    try:
        printCommandList()
        commands1_input = input('>>> ').strip().split(',')
    except:
        print('Try again, something went wrong!')
        print('The input must be like this: "1,2,3,5,7,8"')
    for i in commands1_input:
        if i == '1':
            print('>>> Hostname configuration <<<')
            hostname_chose = input('What is gonna be the hostname?: ').strip()

        elif i == '2':
            print('>>> Password configuration <<<')
            password_chose = input('What password will you use?: ').strip()

        elif i == '3':
            print('>>> Secret configuration <<<')
            secret_chose = input('What will be your secret?: ').strip()

        elif i == '4':
            print('>>> Banner configuration <<<')
            banner_chose = input('What will be your banner?: ').strip()
        
        elif i == '5':
            while True:
                try:    
                    print('>>> Creating VLANs <<<')
                    vlanNumbers_chose = input('Insert the vlan numbers you will need. (example: 10,20,30,40,50,60): ').strip().split(',')
                    vlanNames_chose = input('Insert now the name for those VLANs, in the same order (example: IT,ADMIN,STUDENTS): ').strip().split(',')
                    if len(vlanNames_chose) == len(vlanNumbers_chose):
                        break
                    else:
                        print('You need to enter the same amount of values in the VLAN numbers and VLAN names.')
                except:
                    print('Sorry, but the value for your VLAN number or name is not available.')
        elif i == '6':
            print('>>> Interface selection <<<')
            interface_selected = input('What will be your interface selected? (example: g0/1 or g1/0/24): ').strip()
            printInterfaceCommandList()
            try:
                commands_int_input = input('>>> ').strip().split(',')
                for i in commands_int_input:
                    if i == '11':

                        while True:
                            try:
                                print('>>> Interface IP configuration <<<')
                                print('What will be the IP Address and Subnet Mask?')
                                ip_selected = input('example: 172.16.1.1 255.255.255.0): ').strip().split(' ')
                                if len(ip_selected) == 2:
                                    break
                                else:
                                    print('----- You need to enter the IP Address and the Subnet Mask. -----')
                                    print('----- Try something like this: 192.168.0.138 255,255,255,128 -----')
                            except:
                                print('Something went wrong, try a input like this: 10.128.0.1 255.128.0.0')
                    
                    elif i == '12':
                        while True:
                            printVlanmodeInterface()
                            interface_vlan_mode = input('>>> ').strip()
                            if interface_vlan_mode == '15':
                                print('>>> Access interface configuration <<<')
                                access_interface = input('Which will be the vlan? (example: 10): ').strip()
                                break
                            elif interface_vlan_mode == '16':
                                print('>>> Trunk interface configuration <<<')
                                trunk_native_interface = input('Insert the native vlan(example: 99): ').strip()
                                trunk_allowed_interface = input('Insert the allowed vlans(like this: 10,20,30,99): ').strip()
                                break
                            else:
                                print('Sorry, that is not an option.')
                    
                    elif i == '13':
                        continue
                    
                    elif i == '14':
                        continue
                    
                    else:
                        print(f'Number {i} could not be reached.')
            
            except:
                print('Could not understand it.')

        elif i == '7':
            print('>>> Interface range configuration <<<')
            interface_range_selected = input('Enter your interface range selected (example: f0/0-24): ').strip()
            printInterfaceCommandList()
            
            try:
                commands_int_range_input = input('>>> ').strip().split(',')
            
                for i in commands_int_range_input:
                    if i == '11':
            
                        while True:
                            try:
                                print('What will be the IP Address and Subnet Mask?')
                                ip_range_selected = input('example: 172.16.1.1 255.255.255.0): ').strip().split(' ')
                                if len(ip_range_selected) == 2:
                                    break
                                else:
                                    print('You need to enter the IP Address and the Subnet Mask.')
                                    print('Try something like this: 192.168.0.138 255.255.255.128')
                            except:
                                print('Something went wrong, try a input like this: 10.128.0.1 255.128.0.0')
                    
                    elif i == '12':
                        while True:
                            printVlanmodeInterface()
                            interface_range_vlan_mode = input('>>> ').strip()
                            if interface_range_vlan_mode == '15':
                                print('>>> Access interfaces configuration <<<')
                                access_interface_range = input('Which will be the VLAN? (example: 10): ').strip()
                                break
                            elif interface_range_vlan_mode == '16':
                                print('>>> Trunk interfaces configuration <<<')
                                trunk_native_interface_range = input('Insert the native VLAN(example: 99): ').strip()
                                trunk_allowed_interface_range = input('Insert the allowed VLANs(like this: 10,20,30,99): ').strip()
                                break
                            else:
                                print('Sorry, that is not an option.')

                    elif i == '13':
                        continue

                    elif i == '14':
                        continue

                    else:
                        print(f'Number {i} could not be reached.')

            except:
                print('Could not understand it.')

        elif i == '8':
            while True:
                try:
                    print('>>> SSH Configuration <<<')
                    ip_domain_name_chose = input('Enter the ip domain-name: ')
                    encryptionModulusSSH = input('Enter the amount of bits in your key encryptation(example: 1024): ')
                    lineVTY_chose = input('Select the line VTY range (example: 0 15): ').strip()
                    username_priv_secret = input('Enter the username, the privilege and the secret in sequence (example: ADMIN 15 Secret*00): ').strip().split(' ')
                    if len(username_priv_secret) == 3: 
                        break
                    else:
                        print('You need to enter the username, the privilege and the secret. (example: Admin 15 Secret*Admin)')
                except:
                    print('Something went wrong, try again.')

        elif i == '9':
            while True:
                try:
                    printIpRoutingCommands()
                    commands_ipRouting_input = input('Which command(s) do you want to define?(example: 17,18): ').strip().split(',')
                    for i in commands_ipRouting_input:
                        if i == '17':
                            print('>>> Static ip routing <<<')
                            destiny_id_and_mask = input('Enter the id and mask of the destiny network (example: 172.16.0.0 255.255.0.0): ').strip().split(' ')
                            who_knows_the_net = input('Enter the interface or next host neighbour (example: s0/0/1 or 200.100.0.1): ').strip()
                        elif i == '18':
                            print('>>> Default ip routing <<<')
                            default_who_knows_the_net = input('Enter the interface or next host neighbour (example: s0/0/1 or 200.100.0.1): ').strip()
                    if len(destiny_id_and_mask) == 2:
                        break
                    else:
                        print('You must enter the id and the mask.')
                        print('Try something like this: 172.16.0.0 255.255.0.0')
                except:
                    print('Something went wrong, try again.')

        elif i == '10':
            while True:
                try:
                    print('>>> Subinterface configuration <<<')
                    subinterface_chose = input('Enter the subinterface (example: g0/0.10): ').strip()
                    subinterface_vlan_chose = input('Which VLAN will this interface use?(example: 10): ').strip()
                    while True:
                        subinterface_ip_chose = input('Enter the subinterface IP and mask (example: 192.168.0.1 255.255.255.0): ').strip().split(' ')
                        if len(subinterface_ip_chose) == 2:
                            break
                        else:
                            print('You need to inform IP Address and Subnet Mask')
                    break
                except:
                    print('Something went wrong, try again.')
        else:
            print(f'The number {i} could not be reached.')
    break

##############################
#        OUTPUT AREA         #
##############################

print('''
Your script is:
''')
init_script()
for i in commands1_input:
    if i == '1':
        hostname(hostname_chose)

    elif i == '2':
        password(password_chose)

    elif i == '3':
        secret(secret_chose)

    elif i == '4':
        banner(banner_chose)

    elif i == '5':
        createVlans(vlanNumbers_chose, vlanNames_chose)

    elif i == '6':
        
        if commands_int_input != 0:
            for i in commands_int_input:
                if i == '11':
                    ip_interface(interface_selected, ip_selected)
                elif i == '12':
                    if interface_vlan_mode == '15':
                        vlan_access_interface(interface_selected,access_interface)
                    elif interface_vlan_mode == '16':
                        vlan_trunk_interface(interface_selected, trunk_native_interface, trunk_allowed_interface)
                elif i == '13':
                    shutdown_interface(interface_selected)
                elif i == '14':
                    no_shutdown_interface(interface_selected)

    elif i == '7':
        
        if commands_int_range_input != 0:
            for i in commands_int_range_input:
                if i == '11':
                    ip_interface_range(interface_range_selected, ip_range_selected)
                elif i == '12':
                    if interface_range_vlan_mode == '15':
                        vlan_access_interface_range(interface_range_selected, access_interface_range)
                    elif interface_range_vlan_mode == '16':
                        vlan_trunk_interface_range(interface_range_selected, trunk_native_interface_range, trunk_allowed_interface_range)
                elif i == '13':
                    shutdown_interface_range(interface_range_selected)
                elif i == '14':
                    no_shutdown_interface_range(interface_range_selected)
    
    elif i == '8':
        
        ssh_lineVty(ip_domain_name_chose, encryptionModulusSSH, lineVTY_chose, username_priv_secret)

    elif i == '9':
        
        for i in commands_ipRouting_input:
            if i == '17':
                static_routing(destiny_id_and_mask, who_knows_the_net)
            elif i == '18':
                default_routing(default_who_knows_the_net)

    elif i == '10':
        subinterface_config(subinterface_chose,subinterface_vlan_chose,subinterface_ip_chose)

finish_script()
print()
