from argparse import ArgumentParser

def build_parser():
    parser = ArgumentParser()
    parser.add_argument('--input',
            dest='input'
            )
    return parser


parser = build_parser()
options = parser.parse_args()


def main():

 Name = options.input
 Name1 = float(Name) + 10
 print(Name1)



if __name__ == '__main__':
    main()
    
    
    
