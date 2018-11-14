import iperf3, time, threading

def server():
	server = iperf3.Server()
	server.bind_address='192.168.200.20'
	server.port=6969
	#print("starting server")
	#while True:

	print("starting server")
	while True:
		server.run()
		print("transfer done")


s = threading.Thread(target=server)

s.start()

#Function can also be called like normal. Keeping like this so you can thread multiple servers for multiple links at one time