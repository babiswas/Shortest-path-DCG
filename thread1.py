from threading import Thread
import time


def task(str1):
   print(f"Obtained task {str1}")
   time.sleep(2)
   print("Executing task")
   print(f"Completed task {str1}")


if __name__=="__main__":
   tasklist=["task "+str(i) for i in range(10)]
   threadlist=[Thread(target=task,args=(tasks,)) for tasks in tasklist]
   for th in threadlist:
      th.start()
   for th in threadlist:
      th.join()

   