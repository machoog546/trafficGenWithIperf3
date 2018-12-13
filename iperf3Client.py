import iperf3, time
import multiprocessing as mp

def client_side(cli, serv, port, YesNo):

	if YesNo: #if you only want some of the processes, this will skip log creation
		f = open("port_" + str(port) + ".txt", "w+")
	
	traffic=iperf3.Client()
	traffic.duration=90
	traffic.bind_address=cli
	traffic.server_hostname = serv
	traffic.port=port
	traffic.bandwidth = 180000000 #180Mbps-ish
	result = traffic.run()
	time.sleep(2)
		
	if YesNo:
		result = str(result)
		time.sleep(1)
		
		f.write(result)
		f.close() #Not needed but i want to make sure it saves

clients = [6969, 6970,6971,6971] #not needed. can be put in the args space of the MP call

threads =[]
print("starting")
c1 = mp.Process(target=client_side, args=("192.168.201.10", "192.168.201.20", clients[0], True,))#, daemon  = True) #not sure if needed. 
threads.append(c1)
c2 = mp.Process(target=client_side, args=("192.168.202.10", "192.168.202.20", clients[1], True,))#, daemon  = True) #need faster hardware
threads.append(c2)
c3 = mp.Process(target=client_side, args=("192.168.203.10", "192.168.203.20", clients[2], True,))#, daemon  = True)
threads.append(c3)
c4 = mp.Process(target=client_side, args=("192.168.204.10", "192.168.204.20", clients[3], True,))#, daemon  = True)
threads.append(c4)

print(threads)  #checking if appended correctly
for thread in threads:
	print("Starting " + str(thread))
	thread.start()
	time.sleep(2)
	

for thread in threads:

	thread.join()
	time.sleep(1)

print("Complete")