# Issue 5001: kernels of integer matrices

Issue created by migration from Trac.

Original creator: jhpalmieri

Original creation time: 2009-01-17 16:36:51

Assignee: was

Keywords: matrix, kernel


```
sage: id = matrix(ZZ, 2, 2, [[1, 0], [0, 1]]) 
sage: id.left_kernel()
Traceback
...
TypeError: Argument K (= Integer Ring) must be a field.
```

On the other hand, `id.right_kernel()` and `id.kernel()` both work, and `id.kernel()` actually computes the left kernel.  Note also that the documentation for both left_kernel and right_kernel says that the answer will be a vector space, not a module over the integers; this should be fixed, too.




---

Attachment


---

Comment by jhpalmieri created at 2009-01-24 17:11:17

Looks good, all tests passed. A few comments: the documentation still says "vector space" when computing the kernel of an integer matrix, but I can live with that.  Perhaps more seriously, if you don't apply patch #5089, then computing the kernel (or left_kernel or right_kernel) of a sparse integer matrix leads to a segmentation fault.  Does this need to be investigated further?


---

Comment by mabshoff created at 2009-01-24 17:58:26

Since #5089 is being merged I am changing this to a positive review. The documentation issue about vector spaces vs. modules should be addressed via a followup ticket. 

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-24 18:05:31

Merged in Sage 3.3.alpha2

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-24 18:05:31

Resolution: fixed
