# Issue 1159: Bug in python range

Issue created by migration from https://trac.sagemath.org/ticket/1159

Original creator: robertwb

Original creation time: 2007-11-12 22:12:49

Assignee: was

%python
class MyInt:
    def __init__(self, n):
        self.n = int(n)
    def __int__(self):
        return self.n

print range(MyInt(2**3), MyInt(2**3+10))
print "here"
print range(MyInt(2**34), MyInt(2**34+10))


---

Comment by robertwb created at 2007-11-12 22:13:10


```
%python
class MyInt:
    def __init__(self, n):
        self.n = int(n)
    def __int__(self):
        return self.n

print range(MyInt(2**3), MyInt(2**3+10))
print "here"
print range(MyInt(2**34), MyInt(2**34+10))
```



---

Comment by mhansen created at 2007-11-20 00:16:19

I can't find any issue with this.  It works correctly for me in both the Python and Sage environments.


---

Comment by robertwb created at 2007-12-01 00:30:14

I get 


```
Traceback (most recent call last):    print range(MyInt(2**34), MyInt(2**34+10))
  File "/Users/robert/sage/current/local/lib/python2.5/site-packages/sage/server/support.py", line 260, in syseval
    return system.eval(cmd)
  File "/Users/robert/sage/current/local/lib/python2.5/site-packages/sage/misc/python.py", line 21, in eval
    eval(z, globals, locals)
  File "/Users/robert/sage/sage-2.8.11/data/extcode/sage/", line 1, in <module>
    
TypeError: range() integer start argument expected, got instance.
```


On a 64-bit machine, try 

```
print range(2**64, 2**64+10)
print range(MyInt(2**64), MyInt(2**64+10))
```


I believe this is a bug in Python, and have reported it here: http://bugs.python.org/issue1533


---

Comment by jason created at 2009-10-06 19:25:38

Changing status from new to needs_info_new.


---

Comment by Koen created at 2010-12-10 14:30:00

Fixed in upstream Python 2.6.6 / Python 2.7 (see issue 1533 linked to above) and fix will also be in Python 3 releases. This needs an upgrade of the Sage Python from 2.6.4 to 2.6.6.


---

Comment by Koen created at 2010-12-10 14:30:00

Changing status from needs_info to needs_work.


---

Comment by Koen created at 2010-12-10 14:34:06

Alternative fix to upgrade to Python 2.6.6 would be the upgrade to Python 2.7 from ticket http://trac.sagemath.org/sage_trac/ticket/9958


---

Comment by jason created at 2011-12-14 03:26:41

Fixed by #9958, when it gets merged (upgrade to python 2.7)


---

Comment by jdemeyer created at 2012-01-06 08:47:31

Changing status from needs_work to positive_review.


---

Comment by jdemeyer created at 2012-01-13 08:58:35

Resolution: duplicate
