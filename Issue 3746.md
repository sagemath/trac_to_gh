# Issue 3746: segfault in dist_factor.py on itanium

Issue created by migration from https://trac.sagemath.org/ticket/3746

Original creator: was

Original creation time: 2008-07-30 13:36:06

Assignee: yi




```
wstein@iras:~/iras/build/sage-3.0.6.final>         ./sage -t -long devel/sage/sage/dsage/dist_functions/dist_factor.py
sage -t -long devel/sage/sage/dsage/dist_functions/dist_factor.pysh: line 1: 17221 Segmentation fault      /home/wstein/iras/build/sage-3.0.6.final/local/bin/python /home/wstein/iras/build/sage-3.0.6.final/tmp/.doctest_dist_factor.py >/tmp/tmpKoKDAX 2>/tmp/tmpz35sr7
[DSage] Closed connection to localhost

A mysterious error (perphaps a memory error?) occurred, which may have crashed doctest.
         [25.0 s]
exit code: 768

----------------------------------------------------------------------
The following tests failed:


        sage -t -long devel/sage/sage/dsage/dist_functions/dist_factor.py
Total time for all tests: 25.0 seconds
wstein@iras:~/iras/build/sage-3.0.6.final> 
```



```
wstein@iras:~/iras/build/sage-3.0.6.final> uname -a
Linux iras 2.6.16.46-0.12-default #1 SMP Thu May 17 14:00:09 UTC 2007 ia64 ia64 ia64 GNU/Linux

cpuinfo:
...
processor  : 3
vendor     : GenuineIntel
arch       : IA-64
family     : 32
model      : 0
revision   : 7
archrev    : 0
features   : branchlong, 16-byte atomic ops
cpu number : 0
cpu regs   : 4
cpu MHz    : 1594.000675
itc MHz    : 399.167296
BogoMIPS   : 3186.68
siblings   : 2
physical id: 3
core id    : 1
thread id  : 0
```



---

Comment by was created at 2008-08-02 18:54:07

Changing priority from major to blocker.


---

Comment by was created at 2008-08-02 18:54:07

This also happens on sage.math (opteron debian):

```
sage -t -long devel/sage/sage/dsage/dist_functions/dist_factor.pysh: line 1: 19413 Segmentation fault      /home/was/build/sage-3.1.alpha0/local/bin/python /home/was/build/sage-3.1.alpha0/tmp/.doctest_dist_factor.py >/tmp/tmpPwlp8k 2>/tmp/tmpRTHU_D
[DSage] Closed connection to localhost

A mysterious error (perphaps a memory error?) occurred, which may have crashed doctest.
	 [25.5 s]
```



---

Comment by gfurnish created at 2008-12-10 02:34:35

Changing assignee from yi to gfurnish.


---

Comment by gfurnish created at 2008-12-10 02:34:35

Changing status from new to assigned.


---

Comment by gfurnish created at 2008-12-10 02:34:35

I mentioned in #4745 that the second of the three patches might fix this -- here is what I think happened to cause this.  The race condition in question caused dsage to read in a pickled object from a file before it was done being written to the file.  This caused mysterious failures at best and segfaults at worse.  With #4745 applied I ran these doctests for 10200 iterations (~7 hours) without a single doctest failure.  I think that #4745 kills this heisenbug.


---

Comment by gfurnish created at 2008-12-10 14:35:01

Apparently the last time I tested this I forgot to use long mode, so I reran it after night.  After testing for 24722.3 seconds dist_factor failed a test case (looks like a time-out), but it did not segfault.  I will continue to stress test this, but I think my earlier assessment is still correct.


---

Comment by mabshoff created at 2008-12-11 15:27:31

Fixed by merging #4745 in Sage 3.2.2.alpha2.

Cheers,

Michael


---

Comment by mabshoff created at 2008-12-11 15:27:31

Resolution: fixed
