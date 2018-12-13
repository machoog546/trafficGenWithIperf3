#!/bin/bash

#change ports and addresses as needed
echo "Starting iPerf3 Servers"
echo ""

# -p port, -s for server side, and -B to bind to server address.
sudo iperf3 -p 6969 -s -B 192.168.201.20 -D
echo "Port 6969 on 192.168.201.20 running in background"
echo

sudo iperf3 -p 6970 -s -B 192.168.202.20 -D
echo "Port 6970 on 192.168.202.20 running in background"
echo

sudo iperf3 -p 6971 -s -B 192.168.203.20 -D
echo "Port 6971 on 192.168.203.20 running in background"
echo

sudo iperf3 -p 6971 -s -B 192.168.201.20 -D
echo "Port 6971 on 192.168.204.20 running in background"
echo
#I don't know bash well. I'll add checks later (Might assign servers to process numbers?)