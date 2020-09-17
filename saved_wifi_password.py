import subprocess

data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode(
    'utf-8', errors="backslashreplace").split('\n')
profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]

allwifi = {}
total = len(profiles)
current = 1
for i in profiles:
    try:
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode(
            'utf-8', errors="backslashreplace").split('\n')
        results = [b.split(":")[1][1:-1]
                   for b in results if "Key Content" in b]
        try:
            # print("{:<30}|  {:<}".format(i, results[0]))
            allwifi[i] = results[0]
            print(current * 100 / total, end="%\n")
            current += 1
        except IndexError:
            # print("{:<30}|  {:<}".format(i, ""))
            allwifi[i] = ""
            print(current * 100 / total, end="%\n")
            current += 1
    except subprocess.CalledProcessError:
        # print("{:<30}|  {:<}".format(i, "ENCODING ERROR"))
        allwifi[i] = "ENCODING ERROR"
        print(current * 100 / total, end="%\n")
        current += 1

ssid = str(input("Enter the wifi name : "))
password = allwifi[ssid]
print(password)
