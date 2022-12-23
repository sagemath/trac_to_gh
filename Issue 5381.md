# Issue 5381: Refactor matrix kernels

Issue created by migration from https://trac.sagemath.org/ticket/5381

Original creator: rbeezer

Original creation time: 2009-02-26 03:24:43

Assignee: rbeezer

CC:  burcin

Keywords: matrix kernel refactor

From proposal on sage-devel:

Place the guts of kernel computations for each (specialized) class into a right_kernel() method, where it would seem to naturally belong.  Mostly these would replace kernel() methods that are computing left kernels.  A call to kernel() or left_kernel() should arrive at the top of the hierarchy where it would take a transpose and call the (specialized) right_kernel().  So there wouldn't be a change in behavior in routines currently calling kernel () or left_kernel(), and we would retain Sage's preference for the left by having the vanilla kernel() give back a left kernel.  The changes would be more efficient computationally and also make the code more expressive of what is really happening when and where.


---

Attachment


---

Comment by jason created at 2009-04-03 21:04:44

This patch conflicts with #5408; I get a reject for that part.  Can you rebase this patch?  I'll look at it quickly before it bitrots this time!


---

Comment by rbeezer created at 2009-04-06 04:26:49

Replying to [comment:3 jason]:

Hi Jason,

Thanks for looking at this.  I think the reject was my fault.  Partway through doing this I fixed a bug with #5408 and I don't think I got everything put back together right on this patch.  Apply just the new patch (version 2), and test matrices over ZZ with `algorithm='pari'` since that is where I had to reconstruct the mix-up.  I have tested this against all of the sage/matrix directory.

Thanks again - this will let me get to #5135.

Rob


---

Attachment


---

Comment by jason created at 2009-04-15 05:34:33

Thanks for rebasing.  This is great work!  Positive review pending taking care of the following comments.

 * In matrix2.pyx, the exact same code is repeated for kernel() and for left_kernel().  I think it would be cleaner to just have kernel call left_kernel(), rather than repeating the code to compute and cache the left kernel.

 * In matrix_integer_dense.pyx, you add a note to kernel_matrix() that tells the user that the preferred method is to call an underscore function.  It seems odd to direct a user away from an API function to a function that is not an officially supported function.  This is especially odd because the reason is a speculative "in case this function is deprecated in the future".  To fix this, I would just delete the note about the deprecation.  If a user wants the left kernel matrix, then that's what they want; they'd rather have the function do the work of the transpose and the right kernel matrix.

 * A couple of the functions (I believe in matrix_integer_dense.pyx, for example) that are modified are left without doctests.  These should have at least minimal doctests, and preferably should have doctests for the corner cases (e.g., 0 rows or 0 columns in a matrix).

Doctests pass in matrix/*.pyx.  They should be run on all of Sage for this one, though, since kernels are probably used in lots of places of Sage.


---

Comment by rbeezer created at 2009-04-27 03:47:55

New patch ("_3") addresses all reviewer comments above, though I could only find one function that needed to have doctests added (`_kernel_matrix_using_pari`).

Passed the following tests:

sage -testall

sage -t --randorder sage/matrix/*

sage -docbuild reference pdf


Apply just this new (third) patch, which was built on 3.4.2.alpha0

Minh - timings are getting a bit dated, but are probably still accurate, though most of the speedup came from improvments discovered in transposes while working through this.  You could say "a 16% improvement in right kernels by eliminating paired transposes."


---

Attachment

The latest patch addresses Jason's comments; it applies cleanly and passes testlong.


---

Comment by mabshoff created at 2009-05-11 13:50:02

Merged trac_5381_matrix_kernels_3.patch in Sage 4.0.alpha0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-05-11 13:50:02

Resolution: fixed
