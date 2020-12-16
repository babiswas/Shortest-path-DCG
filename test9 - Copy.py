import argparse

if __name__=="__main__":
   parser=argparse.ArgumentParser()
   parser.add_argument("--number1",help="Enter number1")
   parser.add_argument("--number2",help="Enter number2")
   parser.add_argument("--operation",help="Enter operation")
   args=parser.parse_args()
   number1=int(args.number1)
   number2=int(args.number2)
   if args.operation=="add":
      print(number1+number2)
   elif args.operation=="sub":
      print(number2-number1)
   else:
      print("Unsupported operation")
