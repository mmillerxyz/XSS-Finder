# *************************************************************************************** #
# ---------------------------------- EULA NOTICE ---------------------------------------- #
#                     Agreement between "Haroon Awan" and "You"(user).                    #
# ---------------------------------- EULA NOTICE ---------------------------------------- #
#  1. By using this piece of software your bound to these point.                          #
#  2. This an End User License Agreement (EULA) is a legal between a software application #
#     author "Haroon Awan" and (YOU) user of this software.                               #
#  3. This software application grants users rights to use for any purpose or modify and  #
#     redistribute creative works.                                                        #
#  4. This software comes in "is-as" warranty, author "Haroon Awan" take no responsbility #
#     what you do with by/this software as your free to use this software.                #
#  5. Any other purpose(s) that it suites as long as it is not related to any kind of     #
#     crime or using it in un-authorized environment.                                     #
#  6. You can use this software to protect and secure your data information in any        #
#     environment.                                                                        #
#  7. It can also be used in state of being protection against the unauthorized use of    #
#     information.                                                                        #
#  8. It can be used to take measures achieve protection.                                 #
# *************************************************************************************** #

#!/usr/bin/env python

# Imports
import sys, httplib2, re, requests, urllib2, urlparse, json, time, httplib, cookielib, urllib, httplib, urllib, socket, urlparse, os, sys, time, mechanize 
from threadpool import *

os.system('clear')

print("""      
                                   _                         _               
                                  (_)                       | |              
 ___  ___ _ __ ___  __ _ _ __ ___  _ _ __   __ _    ___ ___ | |__  _ __ __ _ 
/ __|/ __| '__/ _ \/ _` | '_ ` _ \| | '_ \ / _` |  / __/ _ \| '_ \| '__/ _` |
\__ \ (__| | |  __/ (_| | | | | | | | | | | (_| | | (_| (_) | |_) | | | (_| |
|___/\___|_|  \___|\__,_|_| |_| |_|_|_| |_|\__, |  \___\___/|_.__/|_|  \__,_|
                                            __/ |                            
                                           |___/                             
	 			swiss knife for XSS fuzzing 	                                       

[+] Programmer : Shadab Siddiqui
[+] Coder      : Haroon Awan
[+] Version    : Linux
""")

# Config
DEBUG = True
MAX_THREAD_COUNT = 10
#SITES_FILENAME = 'sites'
PAYLOADS_FILENAME = 'payloads'
SCHEME_DELIMITER = '://'
#XSS_RESPONSE = "alert('XSS')"

cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

intt=0
# -------------------------------------
def attack(url, payload):
# -------------------------------------

    t_start = time.time()
    return_dict = dict()
    return_dict['url'] = url
#    return_dict['url_data'] = data
    return_dict['vulnerability'] = False
    try:
        return_dict['method'] = 'GET'
        XSS_RESPONSE=payload
        #print "payload--->", payload
        attack= urllib2.urlopen(url).read()
        #print "\nURL being hit :", url
        index = attack.find(XSS_RESPONSE)
        buffer = 20
        print_url=url.replace("<","&lt")
        attack = attack.split("\n");
        len(attack)
        #print "\nurl->\n",url
        if index != -1:
            return_dict[' vulnerability'] = True
            return_dict['vulnerability_data'] = line.strip()
            print "[+] Reflection Found, manually confirm", attack[index-buffer:index+len(XSS_RESPONSE)+buffer]
            print " [!] URL: ",print_url
            intt=intt+1
            print intt
    #        break

            #print "here"
        t_end = time.time()
        return_dict['time'] = round((t_end - t_start), 2)

    except KeyboardInterrupt, ke:
        sys.exit(0)
    except Exception, e:
        return_dict['exception'] = str(e)


# -------------------------------------
if __name__ == '__main__':
# -------------------------------------

    # Init
    t_global_start = time.time()

#    sites_file = open(SITES_FILENAME)
    payloads_file = open(PAYLOADS_FILENAME)
    threadpool = ThreadPool(MAX_THREAD_COUNT)

    # Load SITES and PAYLOADS files
#    sites = []
#    input = str(raw_input("[+] Enter Absolute URL: "))
    sites = str(raw_input("[+] Enter Absolute URI: "))
#    sites = input
#    input = sites
    print "[+] Loaded Parallel Engine"
    print "[+] Loaded Payloads"
    print "[+] Performing tests"
    payloads = []
    for payload in payloads_file:
        payloads.append(payload[:-1])

        # Loop through sites

        # Extract Base URL and Parameters from site
    parse_url = urlparse.urlparse(sites)
    base_url = '%s%s%s%s' % (parse_url.scheme, SCHEME_DELIMITER, parse_url.netloc, parse_url.path)
#print base_url
    param_parse_list = urlparse.urlparse(sites)[4].split('&')
    param_dict = dict()
    for param_parse_entry in param_parse_list:
#        tmp = param_parse_entry.split('=')
        tmp = param_parse_entry.split(" ")
        param_dict[tmp[0]] = tmp[0]
        # Loop through payloads
    for payload in payloads:
            # Loop through parameters
        #print payload
        for k1, v1 in iter(sorted(param_dict.iteritems())):
                # Build GET param string and POST param dict
            get_params = ''
            post_params = dict()

            for k2, v2 in iter(sorted(param_dict.iteritems())):
                if k1 == k2:
                    get_params += '%s%s&' % (k2, payload)
#                    get_params += '%s=%s&' % (k2, payload)
                    post_params[k2] = payload
                else:
#                    get_params += '%s=%s&' % (k2, v2)
                    get_params += '%s%s&' % (k2, v2)
                    post_params[k2] = v2

            get_params = get_params[:-1]
            #print get_params
                # Enqueue GET attack
            get_attack_url = '%s?%s' % (base_url, get_params)
            threadpool.enqueue(attack, get_attack_url, payload)

            #attack(get_attack_url, payload)



    # Wait for threadpool
    threadpool.wait()

    # Exit
    t_global_end = time.time()
    #if DEBUG:
    #print "int->",int
    if(intt == 0):
        print "[!] Specified URI is not vulernable "
    print '[!] Time taken for parallel scan : %.2f seconds' % (t_global_end - t_global_start)

