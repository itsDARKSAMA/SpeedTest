import speedtest

speed_test = speedtest.Speedtest()

# a.almajayda : get servers list
print("[+] Loading Servers List ...")
speed_test.get_servers()
print("[+] Choosing Best Server ...")
# a.almajyda : Choosing the Best Server 
best_server = speed_test.get_best_server()
print(f"[+] Found Best Server is : {best_server['host']} located in : {best_server['country']}")
print("[+] Performing Download Test ...")
# a.almajayda : downloading test 
download_test = speed_test.download()
download_test = download_test /1024 /1024
print("[+] Performing Upload Test ...")
# a.almajayda : uploading test 
upload_test = speed_test.upload()
upload_test = upload_test /1024 /1024
# a.almajayda : get the ping result
ping_result = speed_test.results.ping

# a.almajayda : print the results
print(f"[+] Download] Speed : {download_test:.2f} Mbit/s")
print(f"[+] Upload Speed : {upload_test:.2f} Mbit/s")
print(f"[+] Ping Reslut : {ping_result:.2f} ms")


