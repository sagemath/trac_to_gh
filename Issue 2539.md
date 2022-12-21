# Issue 2539: Sage 2.10.4.rc0: dsage/dist_functions/dist_factor.py timeout issue with -long

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-03-16 01:30:30

Assignee: yi


```
sage -t -long devel/sage/sage/dsage/dist_functions/dist_factor.py
**********************************************************************
File "dist_factor.py", line 29:
    sage: f.wait(timeout=60) # long time
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-2.10.4.rc0/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[5]>", line 1, in <module>
        f.wait(timeout=Integer(60)) # long time###line 29:
    sage: f.wait(timeout=60) # long time
      File "/scratch/mabshoff/release-cycle/sage-2.10.4.rc0/local/lib/python2.5/site-packages/sage/dsage/dist_functions/dist_function.py", line 183, in wait
        time.sleep(0.5)
      File "/scratch/mabshoff/release-cycle/sage-2.10.4.rc0/local/lib/python2.5/site-packages/sage/dsage/dist_functions/dist_function.py", line 179, in handler
        raise RuntimeError('Maximum wait time exceeded.')
    RuntimeError: Maximum wait time exceeded.
**********************************************************************
File "dist_factor.py", line 30:
    sage: f.done # long time
Expected:
    True
Got:
    False
**********************************************************************
File "dist_factor.py", line 32:
    sage: print f # long time
Expected:
    Factoring "42535295865117307932921825928971026431"
    Prime factors found so far: [31, 601, 1801, 269089806001, 4710883168879506001]
Got:
    Factoring "42535295865117307932921825928971026431"
    Prime factors found so far: [31, 601, 1801]
**********************************************************************
1 items had failures:
   3 of   8 in __main__.example_0
***Test Failed*** 3 failures.
For whitespace errors, see the file .doctest_dist_factor.py
```


While the above doctest usually only takes about 25 seconds wall time when I do parallel testing it times out every couple doctests. Raising the limit for this long doctest to something larger might be a solution.

Cheers,

Michael


---

Comment by yi created at 2008-03-16 21:59:19

Interesting. 
How do I turn parallel testing on to try and reproduce locally? 
It would be better to see why it's taking more than 60 seconds than to simply raise the timeout. doctests that take 60 seconds (even for long time) are probably pretty bad.


---

Comment by yi created at 2008-03-21 20:58:47

Pinging Michael...

Is this still an issue? I still don't understand what you mean by "parallel testing" or how to go about reproducing this.


---

Comment by mabshoff created at 2008-04-09 04:12:03

Replying to [comment:2 yi]:
> Pinging Michael...
> 
> Is this still an issue? I still don't understand what you mean by "parallel testing" or how to go about reproducing this. 

Yes, it still regularly happens. Run "sage -tp 10 devel/sage/sage" on sage.math to trigger this. I am seeing it regularly with 3.0.alpha[0-3].

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-26 02:54:31

Resolution: fixed


---

Comment by mabshoff created at 2008-04-26 02:54:31

I have not seen this for several dozen "-tp 8 -long" on sage.math. Since I was the one who was able to trigger this reliably I am considering this fixed. 

Cheers,

Michael
