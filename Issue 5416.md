# Issue 5416: [with patch, needs review] miscellaneous documentation fixes

Issue created by migration from Trac.

Original creator: cwitty

Original creation time: 2009-03-01 23:53:17

Assignee: cwitty

As I was reviewing sphinxification patches, I noticed a lot of pre-existing issues in the documentation.  Instead of trying to fix these issues as part of sphinxification, I made notes to take care of things later.

This patch covers many of those defects.


---

Attachment

REFEREE REPORT



The patch *misc-doc-fixes.patch* applied OK against 3.4.alpha0 and the documentation built OK with the command:

```
sage -docbuild all html
```

I rebuilt the entire set of documentation because the patch touches files spanning the reference manual, the tutorial, the programming guide, and so on. Although the patch fixes a load of formatting issues and typos, I can still see (in the patch itself) that some typos are not fixed. I'm not saying that the patch introduces any new formatting issues or typos; just that it misses some that I can see in the patch itself. For example,  the patch has the following line to fix `sage/rings/polynomial/pbori.pyx`:

```
`@``@` -1148,7 +1148,7 `@``@`
     def _magma_init_(self, magma):
         r"""
         Return a a string which when evaluated with Magma returns a Magma
-        representaion of this boolean polynomial ring.
+        representation of this boolean polynomial ring.
         
         INPUT:
```

where one should note the line "Return a a string which". Another example concerning the file `sage/rings/real_mpfi.pyx` that the patch touches:

```
`@``@` -3789,7 +3789,7 `@``@`
 #              1.6449340668482264364724151666460251892    # 64-bit
 
 #         Note that the number of bits of precision in the constructor only
-#         effects the internel precision of the pari number, not the number
+#         effects the internal precision of the pari number, not the number
 #         of digits that gets displayed.  To increase that you must
 #         use \code{pari.set_real_precision}.
```

Note the line 

```
+#         effects the internal precision of the pari number, not the number
```

where "effects" should be "affects". I have no time to fix these now, but if anyone does, please open another ticket for that. I can give this patch a positive review for the problems that it fixes.


---

Comment by mabshoff created at 2009-03-02 05:10:15

Unfortunately some of the fixes interact with other documentation fixes, likely due to some of the issues already being fixed via other patches:

```
patching file sage/matrix/matrix_modn_dense.pyx
Hunk #1 FAILED at 1.
1 out of 1 hunk FAILED -- saving rejects to file sage/matrix/matrix_modn_dense.pyx.rej
patching file sage/matrix/matrix_modn_sparse.pyx
Hunk #1 FAILED at 1.
1 out of 1 hunk FAILED -- saving rejects to file sage/matrix/matrix_modn_sparse.pyx.rej
patching file sage/matrix/matrix_real_double_dense.pyx
patching file sage/modules/free_module_element.pyx
patching file sage/rings/arith.py
Hunk #1 succeeded at 197 (offset 1 line).
Hunk #2 FAILED at 963.
Hunk #3 FAILED at 1603.
Hunk #4 succeeded at 1654 (offset 12 lines).
2 out of 4 hunks FAILED -- saving rejects to file sage/rings/arith.py.rej
patching file sage/rings/complex_number.pyx
Hunk #1 succeeded at 305 with fuzz 1.
patching file sage/rings/finite_field.py
patching file sage/rings/finite_field_element.py
patching file sage/rings/ideal.py
Hunk #1 succeeded at 337 (offset 4 lines).
Hunk #2 succeeded at 365 (offset 4 lines).
Hunk #3 FAILED at 579.
Hunk #4 FAILED at 985.
2 out of 4 hunks FAILED -- saving rejects to file sage/rings/ideal.py.rej
patching file sage/rings/integer.pyx
```


Please rebase against 3.4.rc0 out in a couple hours.

Cheers,

Michael


---

Attachment


---

Comment by cwitty created at 2009-03-03 17:16:28

I rebased the patch against 3.4.rc0.  I also took the opportunity to fix one of the issues raised by mvngu (the other had already been fixed in rc0).


---

Comment by mvngu created at 2009-03-04 04:30:39

REFEREE REPORT




The newly rebased patch *misc-doc-fixes-rebased.patch* applied OK against 3.4.rc0. The documentation rebuilds fine and all doctests passed with the options

```
-t -long
```

However, I still see a number of typos in the patch, problems that are NOT introduced by the patch itself. These should be addressed in another ticket, which I plan to do unless someone beats me to it. I can give the rebased patch a positive review for the problems that it fixes.


---

Comment by mabshoff created at 2009-03-04 22:30:04

Resolution: fixed


---

Comment by mabshoff created at 2009-03-04 22:30:04

Merged misc-doc-fixes-rebased.patch in Sage 3.4.rc1.

Cheers,

Michael
