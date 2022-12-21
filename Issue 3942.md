# Issue 3942: Sage interfaces vs. pyprocessing

Issue created by migration from Trac.

Original creator: rlm

Original creation time: 2008-08-24 05:16:36

Assignee: was

CC:  cwitty

When using pyprocessing, if you use an interface to some external function, such as GAP, sometimes the separate subprocesses will collide, since they all share the same temporary file.

A temporary fix (due to cwitty) was to add

`sage.interfaces.expect.tmp_expect_interface_local = '/tmp/interface' + str(os.getpid())`

to the beginning of the function succeeding the ``@`parallel` decorator. This way, the temp files are separate. This should probably be part of the `parallel` function itself.


---

Comment by malb created at 2008-08-24 11:40:41

How about replacing tmp_expect_interface_local by a function that returns, 

  `'/tmp/interface' + str(os.getpid())`

this way, it should always just work?


---

Comment by rlm created at 2008-08-24 14:40:03


```
rank4:sage-main rlmill$ ../../sage -tp 2 sage/interfaces/
Global iterations: 1
File iterations: 1
TeX files: 0
 
----------------------------------------------------------------------
sage -t  devel/sage-main/sage/interfaces/tachyon.py
	 [2.0 s]
sage -t  devel/sage-main/sage/interfaces/tests.py
	 [3.5 s]
sage -t  devel/sage-main/sage/interfaces/singular.py
	 [3.5 s]
sage -t  devel/sage-main/sage/interfaces/sage0.py
	 [9.4 s]
sage -t  devel/sage-main/sage/interfaces/r.py
	 [7.0 s]
sage -t  devel/sage-main/sage/interfaces/rubik.py
	 [15.8 s]
sage -t  devel/sage-main/sage/interfaces/qsieve.py
	 [3.4 s]
sage -t  devel/sage-main/sage/interfaces/povray.py
	 [2.2 s]
sage -t  devel/sage-main/sage/interfaces/phc.py
	 [3.2 s]
sage -t  devel/sage-main/sage/interfaces/octave.py
	 [2.9 s]
sage -t  devel/sage-main/sage/interfaces/psage.py
	 [11.8 s]
sage -t  devel/sage-main/sage/interfaces/mwrank.py
	 [2.0 s]
sage -t  devel/sage-main/sage/interfaces/mupad.py
	 [2.1 s]
sage -t  devel/sage-main/sage/interfaces/monitor.py
	 [2.1 s]
sage -t  devel/sage-main/sage/interfaces/matlab.py
	 [2.0 s]
sage -t  devel/sage-main/sage/interfaces/mathematica.py
	 [2.0 s]
sage -t  devel/sage-main/sage/interfaces/maple.py
	 [2.0 s]
sage -t  devel/sage-main/sage/interfaces/magma_sim.py
	 [1.9 s]
sage -t  devel/sage-main/sage/interfaces/magma_free.py
	 [2.0 s]
sage -t  devel/sage-main/sage/interfaces/magma.py
	 [1.9 s]
sage -t  devel/sage-main/sage/interfaces/macaulay2.py
	 [1.9 s]
sage -t  devel/sage-main/sage/interfaces/lie.py
	 [2.1 s]
sage -t  devel/sage-main/sage/interfaces/maxima.py
	 [17.0 s]
sage -t  devel/sage-main/sage/interfaces/kash.py
	 [2.0 s]
sage -t  devel/sage-main/sage/interfaces/gnuplot.py
	 [2.1 s]
sage -t  devel/sage-main/sage/interfaces/gp.py
	 [3.4 s]
sage -t  devel/sage-main/sage/interfaces/gfan.py
	 [2.0 s]
sage -t  devel/sage-main/sage/interfaces/get_sigs.py
	 [2.0 s]
sage -t  devel/sage-main/sage/interfaces/genus2reduction.py
	 [2.7 s]
sage -t  devel/sage-main/sage/interfaces/gap.py
	 [3.4 s]
sage -t  devel/sage-main/sage/interfaces/frobby.py
	 [2.0 s]
sage -t  devel/sage-main/sage/interfaces/expect.py
	 [6.9 s]
sage -t  devel/sage-main/sage/interfaces/axiom.py
	 [1.9 s]
sage -t  devel/sage-main/sage/interfaces/ecm.py
	 [14.5 s]
All tests passed!
Total time for all tests: 76.7 seconds
rank4:sage-main rlmill$ 
```



---

Attachment


---

Comment by rlm created at 2008-08-24 14:41:51

My one concern with this patch is that the temp files should be cleaned up properly. I don't know the mechanisms for this...


---

Comment by was created at 2008-08-24 17:15:59

> My one concern with this patch is that the temp files should be cleaned up properly. 
> I don't know the mechanisms for this... 

That's all taken care of because the files are in SAGE_TMP.  No worries.

I think this is a good patch.


---

Comment by mabshoff created at 2008-08-25 03:52:14

Resolution: fixed


---

Comment by mabshoff created at 2008-08-25 03:52:14

Merged in Sage 3.1.2.alpha1
