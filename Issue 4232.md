# Issue 4232: #249 causes bug in importing large lists

Issue created by migration from https://trac.sagemath.org/ticket/4232

Original creator: jason

Original creation time: 2008-10-01 20:02:22

Assignee: somebody

CC:  robertwb alexghitza

Try the following in a sage that contains the patch at #249


```
a=[(i,randint(0,100)) for i in range(3000)]                  
f=open("mytest.sage",'w')                  
f.write("a=[\n")                           
f.writelines(["%s,\n"%str(i) for i in a])  
f.write("(0,0)]")                          
f.close()
load mytest.sage            
```


Without the patch at #249, the load completes in about a second.  With the patch, I get recursion errors, ending in:


```
/home/jason/download/sage-3.1.3.alpha1/local/lib/python2.5/site-packages/sage/misc/preparser.py in preparse(line, reset, do_time, ignore_prompts)
    811 
    812 
--> 813 
    814 
    815 

/home/jason/download/sage-3.1.3.alpha1/local/lib/python2.5/site-packages/sage/misc/preparser.py in preparse(line, reset, do_time, ignore_prompts)
    811 
    812 
--> 813 
    814 
    815 

/home/jason/download/sage-3.1.3.alpha1/local/lib/python2.5/site-packages/sage/misc/preparser.py in preparse(line, reset, do_time, ignore_prompts)
    811 
    812 
--> 813 
    814 
    815 

/home/jason/download/sage-3.1.3.alpha1/local/lib/python2.5/site-packages/sage/misc/preparser.py in preparse(line, reset, do_time, ignore_prompts)
    678 
    679 
--> 680 
    681 
    682 

/home/jason/download/sage-3.1.3.alpha1/local/lib/python2.5/site-packages/sage/misc/preparser.py in strip_string_literals(code)
    267 
    268 
--> 269 
    270 
    271 

RuntimeError: maximum recursion depth exceeded in cmp
```


One solution is to revert the patch at #249.  Of course, the better is to find the bug and fix it :).



---

Comment by jason created at 2008-10-01 20:08:02

This affects sage 3.1.3alpha1 and later.


---

Attachment


---

Comment by jason created at 2008-10-01 23:56:08

This patch fixes the bug for me.


---

Comment by mabshoff created at 2008-10-02 01:42:02

Resolution: fixed


---

Comment by mabshoff created at 2008-10-02 01:42:02

Merged in Sage 3.1.3.alpha3
