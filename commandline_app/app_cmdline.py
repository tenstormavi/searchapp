import os
import sys
import requests
import json 
import time 
import pdb
import collections

def json_log ():
   pathname = os.path.dirname(sys.argv[0])
   fullpath = os.path.abspath(pathname)
   listof_files = []
   location_list = []
   big_list = collections.defaultdict(list)
   start_time = time.time()
   i=0
   fout = open("test.json",'w')
   for dirname, dirnames, filenames in os.walk('.'):
      for subdirname in dirnames:
         os.path.join(dirname,subdirname)
      for filename in filenames:
         location = os.path.join(dirname,filename)
         location_list.append (location)
         #file_detail = {'filename':filename,'location':location}
         #listof_files.append ({'file':file_detail})
         file_name = filename
         s = tuple(file_name)
         r = []
         for size in range(1, len(s)+1):
            for index in range(len(s)+1-size):
               x= file_name[index:index+size]
               big_list[x].append(i)
         i=i+1
   #print big_list.items()
   k=1
   while k!=0:
      g =  raw_input ("enter the name of the file ") 
      if g=="0":
         k=0 
      if g in big_list:
         n = big_list[g]
         #print n
         l=0
         for v in n:
             l=location_list[v]
             l = l[1:]
             print fullpath + l
             
   #print location_list
         #fout = open("test.json",'w')
   #print listof_files
   #pdb.set_trace()
   #fout.write (json.dumps(listof_files,indent=4,ensure_ascii=False))
   #fout.close()
   #print("--- %s seconds ---" % time.time() - start_time)
         


if __name__ == "__main__":
     json_log ()
     #fin = open("test.json",'r')
     #s = fin.read ()
     #print s
     #fin.close ()
     

