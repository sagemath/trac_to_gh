# Issue 8410: Improve robustness of @parallel

Issue created by migration from https://trac.sagemath.org/ticket/8410

Original creator: boothby

Original creation time: 2010-03-01 17:30:52

Assignee: tbd

CC:  wstein

Run the following:


```

@parallel(4)
def sleeper(x):
    sleep(x)

for _ in sleeper([10]*100):
    pass

```


and interrupt it with ctrl-c (or esc in the notebook).   We get


```
Killing any remaining workers...
[Errno 3] No such process
---------------------------------------------------------------------------
KeyboardInterrupt                         Traceback (most recent call last)

/home/boothby/<ipython console> in <module>()

/usr/local/sage/local/lib/python2.6/site-packages/sage/parallel/use_fork.pyc in __call__(self, f, inputs)
     98                         signal.alarm(int(walltime() - oldest)+1)
     99                     try:
--> 100                         pid = os.wait()[0]
    101                         signal.signal(signal.SIGALRM, signal.SIG_IGN)
    102                     except RuntimeError:

/usr/local/sage/local/lib/python2.6/site-packages/sage/interfaces/get_sigs.pyc in my_sigint(x, n)
      7 
      8 def my_sigint(x, n):
----> 9     raise KeyboardInterrupt
     10 
     11 def my_sigfpe(x, n):

KeyboardInterrupt: 
}}} 

and then, let's restart the computation:

{{{
sage: for _ in sleeper([10]*100):
    print "hello"
    pass
....: 
15775
[Errno 39] Directory not empty: '/home/boothby/.sage/temp/sage.math.washington.edu/15401/dir_0'
Killing any remaining workers...
}}}

All I can do here is restart Sage.



---

Comment by was created at 2010-06-24 05:02:31

First remark: This fails *exactly* the same on the command line.  Also the error is now:

```
sage: for _ in sleeper([10]*100):
....:         pass
....: 
91260
Killing any remaining workers...
```



---

Attachment


---

Comment by was created at 2010-06-24 05:43:53

Changing status from new to needs_review.


---

Comment by boothby created at 2010-06-24 05:52:09

Changing status from needs_review to positive_review.


---

Comment by boothby created at 2010-06-24 05:52:09

works for me


---

Comment by mpatel created at 2010-07-20 10:02:01

Resolution: fixed
