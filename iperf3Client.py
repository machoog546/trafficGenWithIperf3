import iperf3, time, threading

def client():
	
	print("starting client")
	client = iperf3.Client()
	client.Duration = 4
	client.bind_address="192.168.200.10"
	client.server_hostname='192.168.200.20'
	client.port=6969
	#client.json_output=False
	time.sleep(2) #used to make sure server is up and ready
	result=client.run()
	

	print(result)
	

c = threading.Thread(target=client)

c.start()

#assuming we will thread multiple clinets or this should be running while other checks are be going.