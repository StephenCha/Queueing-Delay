# Queuing Delay

If a data packet is sent to the lighter and is fast, the router temporarily queues the packets that it did not process on time before sending them. This is called queuing delay. If the number of packets increases, it can be seen that queuing delay increases naturally. This repository is a simple simulation of queuing delay.

## Simple Explanation

### Terminology

 Packet loss : a packet that is thrown away when data continues to come in even though the queue is full. 
 
### Requirements

Python 3

Matplotlib and numpy for Python version

## Case I

Details can be found through the queuing delay 1 function annotation. When queuing is infinite in length, I simulate and visualize the queuing delay values according to the number of packets (users) and the rate of transmission of queuing.

## Case II

I looked into the relationship between queuing delay and size when queuing is not infinite.

## Results

![Result](https://user-images.githubusercontent.com/17807597/117294099-35caf200-aead-11eb-8a96-f1b69f705589.png)

I was able to get the above results through the following parameter settings.
* Probability = 0.7
* Import Velocity = 40 [Packets / Seconds]
* Process Velocity = 23 [Packets / Second]
* Number of Users = 2500
* Size of Queue = 155

### Commit

**Length of queue = ∞, x = Users(Packets), y = Queuing Delay**

As the number of packets increases, it can be seen that queuing delay increases exponentially. This queuing delay can also be seen as average response time. The reason is that when a delay occurs in communication between the system (server) and terminal (packet), the response time is the same as delay time. The size limit of queue does not exist, indicating that it continues to increase. A large number of users constantly enter queue, but the process velocity in the system is always constant, so it has to increase.

**Length of queue = ∞, x = Process Velocity, y = Queuing Delay**

The queuing delay value according to the queue's transmission rate indicates that it is an exponentially decay. The faster queue's transmission speed (processing time), the less packets stay in queue, and the less time it stays at the same time. As a result, I observe that the graph is representative.

**Length of queue ≠ ∞, x = Users(Packets), y = Queuing Delay**

The queue size was set to 155 packets, which allowed number of users to measure upper bound on approximately 664 packets. From the time the terminal (packet) exceeds 664 people, the value of queueing delay remains constant at 986 packets/second, resulting in packet loss from terminal to queue due to an excess of queue size. The number of users < 664 shows that queueing delay is exponentially increased, similar to the earlier graph modification. Until the number of users reaches 2,500, it can be seen that queueing delay continues to incubate extensively, but steeply before the 664 packet.

**Length of queue ≠ ∞, x = Process Velocity, y = Queuing Delay**

The difference from the previous graph is found in velocity of transmitted queue (process velocity) at 38. If this speed is exceeded, the queuing delay is fixed at zero and no delay occurs in queuing. When the processing speed is fast enough, the existence of queue is overshadowed and this point is velocity = 38 for this simulation.

## Reference

From Books, Probability, Statistics, and Random Processes for Electrical Engineering, Alberto Leon-Garcia, Chapter 12 Introduction to Queueing Theory p.713
