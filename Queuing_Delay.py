import matplotlib.pylab as plt
import numpy as np

# Suppose you send the packets to the queue in the order they come in.
def queuing_delay1(probability,total_user,import_velocity,process_velocity):
    ## Initialization
    packets = []
    ticket = []
    import_time = 0
    process_time = 0
    # Returns 0 if the process speed cannot be greater than the import speed.
    if process_velocity >= import_velocity:
        return 0
    # The probability of a normal distribution causes the packet to enter the queue.
    # Value in the terminal list is the probability that the packet will enter.
    terminals = np.random.randn(total_user)  # Create a list with a normal distribution.
    # I assume that the probability of entry follows a normal distribution.
    # In other words, I thought I was in Bernoulli RV.

    for i in range(0, total_user):
        if terminals[i] > probability:
            packets.append(np.random.randint(0, 1))  # Generate packets (0 or 1) entering the terminal
        ticket.append(i + 1)  # Generate number tables (in processing order).

    for i in range(len(packets)):  # Obtain processing time, i is the index of the packet.
        # For example, when the throughput rate is 2 (two packets per second),
        # the packet receiving the third ticket takes int(3/2) + 1 = 2 seconds to process.
        if ticket[i] % process_velocity != 0:
            # If the number doesn't fall apart at processing speed,
            processing = int(ticket[i] / process_velocity) + 1
        else:
            processing = int(ticket[i] / process_velocity)
        process_time = process_time + processing

        if ticket[i] % import_velocity != 0:
            importing = int(ticket[i] / import_velocity) + 1
        else:
            importing = int(ticket[i] / import_velocity)
        import_time = import_time + importing
        # When the incoming rate is 4 (4 packets per second),
        # the packet received the third ticket is imported for 4 seconds.
        # The seventh ticket packet takes eight seconds.
        # import_time = import_velocity * (int(ticket[i]/import_velocity)+1) + import_time

    delay_time = process_time + import_time
    return delay_time

# When length of queue is not infinite.
def queuing_delay2(probability, total_user, import_velocity, process_velocity, queue_size):
    packets = []
    ticket = []
    import_time = 0
    process_time = 0
    if process_velocity >= import_velocity:
        return 0
    terminals = np.random.randn(total_user)

    for i in range(0, total_user):
        if terminals[i] > probability:
            packets.append(np.random.randint(0, 1))
        ticket.append(i + 1)

    # Packet Loss
    if len(packets) > queue_size:
        temp = queue_size + 1
        packets[temp:] = []

    for i in range(len(packets)):
        if ticket[i] % process_velocity != 0:
            processing = int(ticket[i] / process_velocity) + 1
        else:
            processing = int(ticket[i] / process_velocity)
        process_time = process_time + processing

        if ticket[i] % import_velocity != 0:
            importing = int(ticket[i] / import_velocity) + 1
        else:
            importing = int(ticket[i] / import_velocity)
        import_time = import_time + importing

    delay_time = process_time + import_time
    return delay_time

def main():
    print('Multiple Cases in Queuing Delay')
    prob = float(input('Enter the probability: '))
    imvel = int(input('Enter the transfer rate from Terminal to Queue (integer only): '))
    prvel = int(input('Enter throughput rate from Queue to System (integer only): '))
    user = int(input('Enter the number of users: '))
    size = int(input('Please enter the size of the queue: '))

    plt.subplot(221)
    x1_label = []
    y1_label = []
    for i in range(0, user, 10):  # Variation in the number of users.
        delaytime = queuing_delay1(probability=prob, total_user=i, import_velocity=imvel, process_velocity=prvel)
        x1_label.append(i)
        y1_label.append(delaytime)
    plt.plot(x1_label, y1_label)
    plt.title("Length of Queue = infinity")
    plt.xlabel("Number of Users(Packets)")
    plt.ylabel("Queuing Delay")

    plt.subplot(222)
    x2_label = []
    y2_label = []
    for i in range(1, prvel, 1):  # Queue process velocity range.
        delaytime = queuing_delay1(probability=prob, total_user=user, import_velocity=imvel, process_velocity=i)
        x2_label.append(i)
        y2_label.append(delaytime)
    plt.plot(x2_label, y2_label)
    plt.title("Length of Queue = infinity")
    plt.xlabel("Velocity of Transmitted Queue")
    plt.ylabel("Queuing Delay")

    plt.subplot(223)
    x3_label = []
    y3_label = []
    for i in range(0, user, 10):  # Users
        delaytime = queuing_delay2(probability=prob, total_user=i, import_velocity=imvel, process_velocity=prvel,
                                   queue_size=size)
        x3_label.append(i)
        y3_label.append(delaytime)
    plt.plot(x3_label, y3_label)
    plt.title("Length of Queue != infinity")
    plt.xlabel("Number of Users")
    plt.ylabel("Queuing Delay")

    plt.subplot(224)
    x4_label = []
    y4_label = []
    for i in range(1, prvel + 100, 1):  # Velocity
        delaytime = queuing_delay2(probability=prob, total_user=user, import_velocity=imvel, process_velocity=i,
                                   queue_size=size)
        x4_label.append(i)
        y4_label.append(delaytime)
    plt.plot(x4_label, y4_label)
    plt.title("Length of Queue != infinity")
    plt.xlabel("Velocity of Transmitted Queue")
    plt.ylabel("Queuing Delay")
    plt.show()

main()