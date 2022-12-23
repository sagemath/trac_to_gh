# Issue 3758: crypto --   sage -t -long devel/sage/sage/crypto/mq/sr.py  fails on many machines

Issue created by migration from https://trac.sagemath.org/ticket/3758

Original creator: was

Original creation time: 2008-08-02 18:59:13

Assignee: tbd


```

=====================================================

[was@localhost ~]$ cat /etc/issue
RHEL5 -- StartCom Enterprise Linux AS release 5.0.0 (Kishuf)
Kernel \r on an \m

        sage -t -long devel/sage/sage/crypto/mq/sr.py
Total time for all tests: 4047.3 seconds

Because of lack of RAM:

[was@localhost ~]$ free
             total       used       free     shared    buffers     cached
Mem:        255704     223072      32632          0      35608     140592
Swap:       524280      41776     482504

I still am very unhappy about this doctest failure.  Shouldn't Sage should work and
pass its test suite  with 768MB memory?

=====================================================

On the Ubuntu LTS 64-bit Sage install with 1GB RAM exactly one failure:


        sage -t -long devel/sage/sage/crypto/mq/sr.py

was@SAGE64VPC:~$ free
             total       used       free     shared    buffers     cached
Mem:       1028380     576408     451972          0     101512     196976

=====================================================
```



---

Comment by was created at 2008-08-05 05:34:23

Here's what it looks like:

```
[was@localhost sage-3.1.alpha0]$ ./sage -t --long devel/sage/sage/crypto/mq/sr.py
sage -t --long devel/sage/sage/crypto/mq/sr.py              sh: line 1: 28053 Killed                  /home/was/build/sage-3.1.alpha0/local/bin/python /home/was/build/sage-3.1.alpha0/tmp/.doctest_sr.py >/tmp/tmp6Q-Tzr 2>/tmp/tmpNd2IJH

A mysterious error (perphaps a memory error?) occurred, which may have crashed doctest.
	 [134.8 s]
exit code: 768
 
----------------------------------------------------------------------
The following tests failed:


	sage -t --long devel/sage/sage/crypto/mq/sr.py
Total time for all tests: 134.8 seconds
[was@localhost sage-3.1.alpha0]$ 
```



---

Comment by malb created at 2008-08-18 19:38:38

This is related to/the same as #1046.


---

Comment by mabshoff created at 2008-10-29 12:46:49

Hmm, #4380 seems to make the situation better, but on a 10.4 box with plenty of RAM and a 32 bit build of Sage we still get

```
varro:~/sage-3.2.alpha1 mabshoff$ ./sage -t -long devel/sage/sage/crypto/mq/sr.py
sage -t -long devel/sage/sage/crypto/mq/sr.py                
halt 14

error: no more memory
System 324568k:356856k Appl 319751k/4816k Malloc 3654k/401k Valloc 320512k/4415k Pages 80090/38 Regions 626:685

A mysterious error (perphaps a memory error?) occurred, which may have crashed doctest.
	 [812.5 s]
exit code: 768
```

But overall with #4380 applied we see big improvements already.

Cheers,

Michael


---

Attachment

The problem here is that the doctest for sage.crypto.mq.sr.test_consistency uses too much memory.

There are two options to fix this:

1)  Just take the doc test out.
<or>
2)  Change the doctest to call test_consistency w/ max_n=1 instead of max_n=2.  This leads to a more than 5 fold improvement of memory usage / time.

This patch implements 2, because (1) would make test coverage numbers decrease.


---

Comment by malb created at 2009-01-24 08:04:22

looks good.


---

Comment by mabshoff created at 2009-01-24 13:15:47

Resolution: fixed


---

Comment by mabshoff created at 2009-01-24 13:15:47

Merged in Sage 3.3.alpha2
