import argparse


if __name__=="__main__":
   parser=argparse.ArgumentParser()
   parser.add_argument("num",help="Enter number",type=int)
   args=parser.parse_args()
   print(args.num)
