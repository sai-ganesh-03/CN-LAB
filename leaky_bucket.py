filled=0
bucket_size=400
left=bucket_size
while left >=0:
    print("Enter the input size and output size of packet")
    input_size=int(input())
    output_size=int(input())
    filled+=input_size
    filled-=output_size
    left=bucket_size-filled
    if left>=0:
        print("Packet put into bucket")
print("bucket is full")
