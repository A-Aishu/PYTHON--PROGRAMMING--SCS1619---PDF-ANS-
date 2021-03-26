f1 = None
for i in range (5):
    with open ("data.txt",  "w" ) as f1:
               if  i  >  2:
                     break
print (f1.closed)                 
