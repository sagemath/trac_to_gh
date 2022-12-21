# Issue 7108: Sage 4.1.2.rc0 doctest failures on 32-bit Fedora 9

Issue created by migration from Trac.

Original creator: mvngu

Original creation time: 2009-10-04 06:17:06

Assignee: tbd

As the subject says. This was reported to [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/c8b23afa63990d0f).


---

Comment by was created at 2009-10-04 17:24:42

I just tried a clean build of sage-4.1.2.rc0 + a bit and get *only* one failure in twist.py:


```
----------------------------------------------------------------------
The following tests failed:


        sage -t -long "devel/sage/sage/server/simple/twist.py"
```


The failure is:

```
sage -t -long "devel/sage/sage/server/simple/twist.py"      
**********************************************************************
File "/home/wstein/screen/cicero/build/sage-4.1.2.rc1.alpha1/devel/sage/sage/server/simple/twist.py", line 51:
    sage: print get_url('http://localhost:%s/simple/compute?session=%s&code=2*2' % (port, session))
Expected:
    {
    "status": "done",
    "files": [],
    "cell_id": 1
    }
    ___S_A_G_E___
    4
Got:
    {
    "status": "computing",
    "files": [],
    "cell_id": 1
    }
    ___S_A_G_E___
    <BLANKLINE>
**********************************************************************
1 items had failures:
   1 of  24 in __main__.example_0
***Test Failed*** 1 failures.
For whitespace errors, see the file /home/wstein/.sage//tmp/.doctest_twist.py
         [17.8 s]
```


This is somwhat expected since cicero is slow and the difference between the above two is that one didn't finish and the other did.  Hmm.


---

Comment by was created at 2009-10-04 17:47:17

I also see exactly the same twist.py failure on opensuse 64-bit.  I think this is likely just a poorly written doctest. 

Yes, in fact, looking at the doctest it is:

```
Run a command::

    sage: sleep(0.5)
    sage: print get_url('http://localhost:%s/simple/compute?session=%s&code=2*2' % (port, session))
    {
    "status": "done",
    "files": [],
    "cell_id": 1
    }
    ___S_A_G_E___
    4
```


To be frank, it is utterly ridiculous to think that a doctest like this is going to work all the time.  Often computers get heavily loaded during testing, or are slow because of DNS configuration, virtualization, etc.   The above test needs to be rewritten.  Two options:
    
    * try repeatedly until status is done.

    * put some ...'s in the output.


---

Comment by robertwb created at 2009-10-05 16:46:38

I had figured that 2*2 would be nearly instantaneous to compute, even on a heavily loaded machine, but here we're also waiting for the sage session to start up. 

We should add a "timeout=-1" to that url so it waits for the computation to finish no matter what (and then can delete the "sleep(0.5)."


---

Comment by was created at 2009-10-07 12:47:15

The same testing issue comes up with OS X 10.5 and is fixed there in #7112.  I'm thus closing this as a dupe.


---

Comment by was created at 2009-10-07 12:47:15

Resolution: duplicate
