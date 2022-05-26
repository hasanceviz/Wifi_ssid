import subprocess
from pathlib import Path

data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors="backslashreplace").split('\n')
profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
root_dir = Path("~").expanduser()
target_path = root_dir / "Desktop\ssid_ve_sifreler.txt"
ssid = open(target_path, 'w')
ssid.write("{:<30}| {:<}\n".format("Wi-Fi SSID", "Şifreler"))
ssid.write("----------------------------------------------\n")
for i in profiles:
    try:
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8', errors="backslashreplace").split('\n')
        results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
        try:
            print ("{:<30}|  {:<}".format(i, results[0]))
            ssid.write("{:<30}|  {:<}\n".format(i, results[0]))
        except IndexError:
            print ("{:<30}|  {:<}".format(i, ""))
            ssid.write("{:<30}|  {:<}\n".format(i, ""))
    except subprocess.CalledProcessError:
        print ("{:<30}|  {:<}".format(i, "ENCODING ERROR"))
        ssid.write("{:<30}|  {:<}\n".format(i, "ENCODING ERROR"))