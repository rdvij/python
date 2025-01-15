import argparse

def multiply(a):
    for i in range(1, len(a)):
        a[0] *= a[i]
    return a[0]

def main():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--integers', metavar='N', type=int, nargs='+',
                        help='an integer for the accumulator')
    parser.add_argument('--sum', dest='accumulate', action='store_const',
                        const=sum, default=max,
                        help='sum the integers (default: find the max)')
    parser.add_argument('--multiply', dest='accumulate', action='store_const',
                        help='multiply the integers (default: find the max', const=multiply)

    args = parser.parse_args()
    print(args.accumulate(args.integers))

if __name__ == "__main__":
    main()