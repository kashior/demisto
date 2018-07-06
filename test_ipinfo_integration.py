from ipinfo_integration import *


def ip_info_test():
    '''
    took from ipinfo.io 3 big company names after I searched the net for their IP
    This test compare the names with my function output. and also checks if exceptions are raised due to invalid IP
    '''

    IP = ['8.8.8.8', '91.198.174.192', '31.13.77.36']
    COMPANIES = ['AS15169 Google LLC', 'AS14907 Wikimedia Foundation Inc.', 'AS32934 Facebook, Inc.']

    for i in range(len(IP)):
        assert (get_ip_information(IP[i])['org'] == COMPANIES[i])
    try:
        get_ip_information('128.0')
        print("Error: invalid IP was not recognized")
    except Exception:
        pass
    try:
        get_ip_information('google.com')
        print("Error: host recognized as IP")
    except Exception:
        pass

    print('get_ip_information Test completed flawless')
