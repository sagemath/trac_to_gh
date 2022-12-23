# Issue 5273: [with patch, needs review] change error message for integer matrices which are too large

Issue created by migration from https://trac.sagemath.org/ticket/5273

Original creator: jhpalmieri

Original creation time: 2009-02-14 16:55:41

Assignee: jhpalmieri

CC:  cwitty

Keywords: 32-bit, 64-bit, matrix

On a 32-bit machine:

```
sage: matrix(ZZ, 100, 2^85)
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
...
ValueError: number of rows and columns must be less than 2^32 (on a 32-bit computer -- use a 64-bit computer for bigger matrices)
```

The attached patch makes this change: if the number of rows or columns is `2^64` or more, it just says the size is too big, it doesn't say anything about a 64-bit computer.  If the number of rows is between `2^32` and `2^64-1` and if the computer is 32-bit, then it gives the above error message.  (The message is also reworded a little bit.)




---

Attachment

Looks good to me.


---

Comment by mabshoff created at 2009-02-15 06:27:53

This ticket fails to import for me:

```
mabshoff@sage:/scratch/mabshoff/sage-3.3.rc1/devel/sage$ patch -p1 --dry-run < trac_5273.patch 
patching file sage/matrix/matrix_space.py
Hunk #1 FAILED at 197.
Hunk #2 FAILED at 215.
2 out of 2 hunks FAILED -- saving rejects to file sage/matrix/matrix_space.py.rej
```

Note that Carl Witty already fixed a bug here recently since signed ints were used:

```
        parent_gens.ParentWithGens.__init__(self, base_ring)
        if not isinstance(base_ring, ring.Ring):
            raise TypeError, "base_ring must be a ring"
        if ncols == None: ncols = nrows
        nrows = int(nrows)
        ncols = int(ncols)
        if nrows < 0:
            raise ArithmeticError, "nrows must be nonnegative"
        if ncols < 0:
            raise ArithmeticError, "ncols must be nonnegative"

        if sage.misc.misc.is_64_bit:
            if nrows >= 2**63 or ncols >= 2**63:
                raise ValueError, "number of rows and columns must be less than 2^63"
        else:
            if nrows >= 2**31 or ncols >= 2**31:
                raise ValueError, "number of rows and columns must be less than 2^31 (on a 32-bit computer -- use a 64-bit computer for bigger matrices)"
```

This patch went into 3.3.alpha6 via #5193, so it looks like the problem has already been fixed.

Thoughts?

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-15 06:40:23


```

[10:28pm] mabs: mhansen: I need to look at John's patch to make 100% sure they 
are both fixing all the same issues (besides John's patch doesn't address the 
signed int problem)
[10:31pm] cwitty: I think the point of #5273 is that the error message on a 
matrix of size 2^80 on a 32-bit computer suggests that it might actually work 
on a 64-bit computer.
[10:31pm] mabs: Yes. That is why I thought something else remains to be done 
[10:32pm] cwitty: But if you're going to worry about that... I'm pretty sure 
there's no computer in the world that can handle a matrix with even 2^50 
entries...
[10:32pm] mabs: cwitty: Can you integrate that change on top of your change.
[10:33pm] mabs: Well, you can create the MatrixSpace 
[10:33pm] cwitty: True.
[10:33pm] mabs: Not that it will not blow up if you do anything serious with 
it, but if things are very sparse it should not appear to work
```



---

Comment by jhpalmieri created at 2009-02-15 16:58:51

Here's a version based off 3.3.rc0.


---

Attachment

To make things 100% sure: the rebased patch applies and doctests fine, so an extra positive review for that patch.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-16 04:07:08

Resolution: fixed


---

Comment by mabshoff created at 2009-02-16 04:07:08

Merged in Sage 3.3.rc1.

Cheers,

Michael
