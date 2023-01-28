import webbrowser
import time

# Open the proxies file
with open("proxies.txt", "r") as file:
    proxies = file.readlines()

# Remove newline characters from the proxies
proxies = [proxy.strip() for proxy in proxies]

# Set the target URL
target_url = "https://www.example.com"

# Set the number of windows to open
num_windows = 3

# Set the number of seconds to wait between opening each window
wait_time = 2

# Counter for the proxies list
proxy_counter = 0

# Open the target URL in a new window for each proxy
for i in range(num_windows):
    if proxy_counter == len(proxies):
        proxy_counter = 0
    webbrowser.get(using='windows-default').open_new(target_url + '?proxy=' + proxies[proxy_counter])
    time.sleep(wait_time)
    proxy_counter += 1
