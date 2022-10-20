def bandwidth(link):
    dict = {"(1,2)":"10Mbps", "(2,3)":"5Mbps", "(3,4)":"10Mbps"}
    l1 = link.split(',')[0]
    l2 = link.split(',')[1]
    if link in dict:
        print(f'Bandwidth for link between h{l1[1]} and h{l2[0]} is {dict[link]}')
    else:
        print(f'Bandwidth for link not present')

if __name__ == "__main__":
    input_link = input("Enter the link:")
    bandwidth(input_link)
