# Multiprocess Traffic Gen with iPerf3
This script in its current form will allow you to set up 4 processes of traffic gen using the Python 3 wrapper for Iperf3, and the bash script will start the server side of the traffic as daemon.

When tests are complete a text file is saved as a JSON formatted text file called port_*port#*.txt 

## Prerequisites
Instructions/Requirements needed to run this chunk of code.

All testing for this script was done on Debian related distros between loopbacks on the same machine and several rounds going to a RaspberryPi. More testing to be done in the following weeks.

### Hardware
The following items will be needed
'''
 Two servers/PC running a Linux OS
 '''

 ### Software
 Server bash script copied to one, and iperf3Client.py on the other
 >If needed you can copy both to both devices and run traffic in either direction.
 iPerf3 Wrapper for python
 iPerf3 software installed to Linux
 Python 3.5+
 '''

 ## Instalation

- Ubuntu:

.. code:: bash

    sudo apt-get install iperf3

- CenOS/RedHat

.. code:: bash

    sudo yum install iperf3

Once the iperf3 utility is installed the simplest way to install the python wrapper is through
`PyPi <https://pypi.python.org/pypi/iperf3>`__

.. code:: bash

    pip install iperf3

You can also install directly from the github repository:

## Notes

Wraper repo found at <https://github.com/thiezn/iperf3-python>

