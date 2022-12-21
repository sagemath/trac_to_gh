# Issue 5797: raise coverage in matrix1.pyx to 100%

Issue created by migration from Trac.

Original creator: ddrake

Original creation time: 2009-04-16 03:22:05

Assignee: mabshoff

CC:  jason

In 3.4.1.rc2, matrix1.pyx is missing doctests and documentation. I'll attach a patch that covers all but two functions:

`new_matrix` is just a wrapper around `matrix_space` and `MatrixSpace`. The documentation for `MatrixSpace` isn't complete enough for me to say exactly what all the parameters of `new_matrix` do. Can someone who knows more about this make a suggestion?

The function `_singular_` has no doctests (and the current docstring is deeply confusing) and -- surprise, surprise -- is broken. I'll open a separate ticket for that.


---

Attachment


---

Comment by ddrake created at 2009-04-16 04:11:49

The attached patch adds doctests, documentation, and also fixes up a lot of the ReST formatting.

I'm ignoring `_singular_` for now, since it's broken and I don't know enough to fix it. I do need advice on what to do for `new_matrix`.


---

Comment by ddrake created at 2009-04-16 04:19:27

The `_singular_` ticket is #5798.


---

Attachment

replaces previous


---

Comment by cremona created at 2009-04-18 15:02:41

The patch applies fine (to 3.4.1.rc3) and the docs build and look ok.

It seems a pity not to have any doctest for new_matrix(), so I have added one.  I also added "indirect doctest" where necessary and a load(dumps) test, so that we now have

```
sage/matrix/matrix1.pyx
SCORE sage/matrix/matrix1.pyx: 97% (36 of 37)

Missing doctests:
	 * _singular_(self, singular=None):
```


I put "positive review" despite adding a little.

The new patch replaces the first one.


---

Comment by mabshoff created at 2009-04-18 17:36:29

Well, the coverage is 97%, so let's adjust the summary ;)

Cheers,

Michael


---

Comment by ddrake created at 2009-04-18 22:22:13

Replying to [comment:4 cremona]:
> I put "positive review" despite adding a little.

I'm not sure if I can/should review your changes, but they are fine and I approve. :)

I didn't know about the "indirect doctest", nor really how to write a load/dumps test. Thanks for adding those.

Thank you also for writing the new_matrix doctest. Perhaps I should open another ticket for improving the MatrixSpace documentation.


---

Comment by mabshoff created at 2009-04-22 07:00:07

Oops?

```
Building modified file sage/matrix/matrix1.pyx.
Execute 1 commands (using 1 threads)
python2.5 `which cython` --embed-positions --incref-local-binop -I/scratch/mabshoff/sage-3.4.2.alpha0/devel/sage-main -o sage/matrix/matrix1.c sage/matrix/matrix1.pyx

Error converting Pyrex file to C:
------------------------------------------------------------
...
include "../ext/stdsage.pxi"
include "../ext/python.pxi"

import sage.modules.free_module

TESTS::
    ^
------------------------------------------------------------
```

Adding appropriate `"""` fixes it.

Cheers,

Michael


---

Attachment

I moved John's misplaced TESTS block inside the file's header docstring. Coverage is now 97%, with only the missing Singular doctest.


---

Comment by cremona created at 2009-04-22 09:02:55

Sorry about that -- very mysterious as I certainly did test my own patch.  Thanks for fixing it.  john


---

Comment by mabshoff created at 2009-04-23 06:18:43

Merged trac_5797-review-fixed.patch in Sage 3.4.2.alpha0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-23 06:18:43

Resolution: fixed
