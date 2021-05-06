# Queuing Delay

If a data packet is sent to the lighter and is fast, the router temporarily queues the packets that it did not process on time before sending them. This is called queuing delay. If the number of packets increases, it can be seen that queuing delay increases naturally. This repository is a simple simulation of queuing delay.

## Terminology

 Packet loss : a packet that is thrown away when data continues to come in even though the queue is full. 
 
 ## Requirements

Python 3

Matplotlib and numpy for Python version

## Case I

Details can be found through the queuing delay 1 function annotation. When queuing is infinite in length, I simulate and visualize the queuing delay values according to the number of packets (users) and the rate of transmission of queuing.

## Case II

I looked into the relationship between queuing delay and size when queuing is not infinite.
