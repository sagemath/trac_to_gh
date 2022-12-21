# Issue 2155: [with patch; needs review] greatly speed up matrix inversion for 1x1 and 2x2 matrices over QQ by a factor of 20!

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-02-14 02:10:20

Assignee: was

Before:


```
sage: a = matrix(QQ, 2, [1, 5, 17, 3]); a
[ 1  5]
[17  3]
sage: time for _ in xrange(10^4): b = a.invert()
CPU times: user 5.74 s, sys: 0.13 s, total: 5.87 s
Wall time: 5.94
```


After:


```
sage: time for _ in xrange(10^4): b = a.invert()
CPU times: user 0.22 s, sys: 0.04 s, total: 0.26 s
Wall time: 0.29
```


This also does not leak memory:

```
sage: get_memory_usage()
'122M+'
sage: time for _ in xrange(10^5): b = a.invert()
CPU times: user 2.33 s, sys: 0.36 s, total: 2.69 s
Wall time: 2.70
sage: get_memory_usage()
'122M+'
```




---

Attachment

Works great for me. The doctest for invert() has some spurious code at the top of the examples block though. 

Since you're going to have to be in there anyway, it might be a bit more readable if "t0" was renamed to "det."


---

Attachment

I have addressed the referee's (Robert's) two complaints.  I also added an architecture for fast change of base ring and computation of the Hadamard bound.  This second thing is technically unrelated but it was too difficult to separate out safely. 

This is now vastly faster than before

```
sage: a = random_matrix(ZZ,500)
sage: time a.change_ring(RDF)
CPU times: user 0.01 s, sys: 0.00 s, total: 0.02 s
Wall time: 0.02
```



---

Comment by was created at 2008-02-16 04:06:41

By the way, apply both patches, in order.


---

Comment by robertwb created at 2008-02-16 18:16:29

The code looks good to me, but I just tried to pull these two, in order, on a clean 2.10.1, and it's giving me errors: 

robert$ sage -hg import ~/Desktop/patches/trac-2155-part2.patch 
applying /Users/robert/Desktop/patches/trac-2155-part2.patch
patching file sage/matrix/matrix_integer_dense.pyx
Hunk #2 FAILED at 1017
Hunk #3 FAILED at 2823
2 out of 3 hunks FAILED -- saving rejects to file sage/matrix/matrix_integer_dense.pyx.rej
abort: patch failed to apply

You have a warning on the `hadamard_bound` function if the entries are too large--does it raise an error or give erroneous results?


---

Comment by mabshoff created at 2008-03-05 00:46:12

Resolution: fixed


---

Comment by mabshoff created at 2008-03-05 00:46:12

Merged in Sage 2.10.3.rc1 (or earlier via #2053). It would be great if somebody could revisit this ticket.
