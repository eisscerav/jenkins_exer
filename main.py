import argparse


def demo():
    print("demo python")


def demo_argparse():
    parser = argparse.ArgumentParser(description='name')
    parser.add_argument('--family', type=str, help='first name')
    parser.add_argument('--name', type=str, dest='ffan_name', metavar='meta', help='last name')
    args = parser.parse_args()

                        print(f"args.family={args.family}, args.ffan_name={args.ffan_name}")
if __name__ == '__main__':
#    demo()
    demo_argparse()
