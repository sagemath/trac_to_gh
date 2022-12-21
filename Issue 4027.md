# Issue 4027: Sage 3.1.2.alpha3: matrix_mod2_dense.pyx doctest failure on 32 bits

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-09-01 00:59:27

Assignee: malb


```
bash-3.2$ ./sage -t devel/sage/sage/matrix/matrix_mod2_dense.pyx
sage -t  devel/sage/sage/matrix/matrix_mod2_dense.pyx       sh: line 1: 19961 Abort trap              /Users/mabshoff/sage-3.1.2.alpha3/local/bin/python /Users/mabshoff/sage-3.1.2.alpha3/tmp/.doct
est_matrix_mod2_dense.py > /var/folders/uO/uOBV9ZyXHvWiSlU9K+3AE++++UE/-Tmp-/tmpqHbQOr 2> /var/folders/uO/uOBV9ZyXHvWiSlU9K+3AE++++UE/-Tmp-/tmpBMZa3v
**********************************************************************
File "/Users/mabshoff/sage-3.1.2.alpha3/tmp/matrix_mod2_dense.py", line 1496:
    sage: print A.str()
Expected:
    [1 1 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
    [0 1 1 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
    [1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0]
    [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
Got:
    [1 1 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
    [0 1 1 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
    [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0]
    [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
**********************************************************************
File "/Users/mabshoff/sage-3.1.2.alpha3/tmp/matrix_mod2_dense.py", line 1501:
    sage: ZZ(sage.matrix.matrix_mod2_dense._read_bits(A,2,0,64))
Expected:
    13835058055282163713
Got:
    1
**********************************************************************
File "/Users/mabshoff/sage-3.1.2.alpha3/tmp/matrix_mod2_dense.py", line 1505:
    sage: print A.str()
Expected:
    [1 1 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
    [0 1 1 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
    [1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0]
    [0 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0]
Got:
    [1 1 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
    [0 1 1 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
    [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0]
    [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0]
**********************************************************************
File "/Users/mabshoff/sage-3.1.2.alpha3/tmp/matrix_mod2_dense.py", line 1510:
    sage: ZZ(sage.matrix.matrix_mod2_dense._read_bits(A,3,1,64))
Expected:
    13835058055282163713
Got:
    1
For whitespace errors, see the file /Users/mabshoff/sage-3.1.2.alpha3/tmp/.doctest_matrix_mod2_dense.pym4ri_mm_calloc: calloc returned NULL

A mysterious error (perphaps a memory error?) occurred, which may have crashed doctest.
  [10.2 s]
exit code: 768
```



---

Attachment


---

Comment by malb created at 2008-09-01 10:17:42

The doctest failures can easily be fixed by disabling the respective code (it is just there for testing purposes and that code isn't used by anything in production use yet)

I'll have to come up with a second patch for the CALLOC issue.


---

Comment by mabshoff created at 2008-09-01 10:24:39

Patch looks good to me. The calloc issue might or might not be solved by the new upstream spkg. If it is still a problem I will open a new ticket for it.

Cheers,

Michael


---

Comment by malb created at 2008-09-01 11:23:17

A new SPKG is up at:

  http://sage.math.washington.edu/home/malb/spkgs/libm4ri-20080901.spkg

With that SPKG and a touch on `matrix_mod2_dense.pxd` + `sage -b` all tests pass on BSD:


```
Sage subshell$ sage -t ~/sage-3.1.2.alpha3/devel/sage/sage/matrix/matrix_mod2_dense.pyx
sage -t  devel/sage/sage/matrix/matrix_mod2_dense.pyx
         [4.4 s]

----------------------------------------------------------------------
All tests passed!
Total time for all tests: 4.4 seconds
```



---

Comment by mabshoff created at 2008-09-01 12:15:42

The spkg has been reviewed at #4024, so I am giving the patch a positive review since it makes the doctest work on OSX 32 bit again.

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-01 12:17:12

Resolution: fixed


---

Comment by mabshoff created at 2008-09-01 12:17:12

Merged in Sage 3.1.2.alpha4
