# Issue 4304: [with patch, needs review] split up NTL's decl.pxi

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2008-10-15 17:44:13

Assignee: cwitty

CC:  robertwb




---

Attachment

I could not apply the patch:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 3.1.3, Release Date: 2008-10-14                       |
| Type notebook() for the GUI, and license() for information.        |
sage: hg_scripts.import_patch("/tmp/ntl_decl_refactor.patch")
cd "/usr/local/sage-3.1.3/sage/local/bin" && hg status
cd "/usr/local/sage-3.1.3/sage/local/bin" && hg status
cd "/usr/local/sage-3.1.3/sage/local/bin" && hg import   "/tmp/ntl_decl_refactor
.patch"
applying /tmp/ntl_decl_refactor.patch
unable to find 'sage/libs/ntl/decl.pxi' for patching
1 out of 1 hunk FAILED -- saving rejects to file sage/libs/ntl/decl.pxi.rej
unable to find 'sage/libs/ntl/ntl_ZZX.pyx' for patching
1 out of 1 hunk FAILED -- saving rejects to file sage/libs/ntl/ntl_ZZX.pyx.rej
unable to find 'sage/libs/ntl/ntl_ZZ_pX.pxd' for patching
2 out of 2 hunks FAILED -- saving rejects to file sage/libs/ntl/ntl_ZZ_pX.pxd.rej
unable to find 'sage/libs/ntl/ntl_lzz_p.pxd' for patching
1 out of 1 hunk FAILED -- saving rejects to file sage/libs/ntl/ntl_lzz_p.pxd.rej
unable to find 'sage/libs/ntl/ntl_lzz_pX.pxd' for patching
1 out of 1 hunk FAILED -- saving rejects to file sage/libs/ntl/ntl_lzz_pX.pxd.rej
unable to find 'sage/rings/padics/pow_computer_ext.pxd' for patching
1 out of 1 hunk FAILED -- saving rejects to file sage/rings/padics/pow_computer_ext.pxd.rej
unable to find 'sage/rings/polynomial/polynomial_integer_dense_flint.pyx' for patching
1 out of 1 hunk FAILED -- saving rejects to file sage/rings/polynomial/polynomial_integer_dense_flint.pyx.rej
unable to find 'sage/rings/polynomial/polynomial_integer_dense_ntl.pyx' for patching
1 out of 1 hunk FAILED -- saving rejects to file sage/rings/polynomial/polynomial_integer_dense_ntl.pyx.rej
unable to find 'sage/rings/polynomial/polynomial_modn_dense_ntl.pxd' for patching
1 out of 1 hunk FAILED -- saving rejects to file sage/rings/polynomial/polynomial_modn_dense_ntl.pxd.rej
unable to find 'sage/rings/polynomial/polynomial_modn_dense_ntl.pyx' for patching
5 out of 5 hunks FAILED -- saving rejects to file sage/rings/polynomial/polynomial_modn_dense_ntl.pyx.rej
abort: patch failed to apply
```



---

Comment by mabshoff created at 2008-10-15 19:39:13

Hi Paul,

you did apply the patch to the scripts repo, but you need to apply the patch to the hg_sage repo. I just tested and the patch applies fine against 3.1.3 as well as 3.1.4.

Cheers,

Michael


---

Comment by robertwb created at 2008-10-15 20:22:10

Merges fine, building right now, but the code looks good and should help speed up build time and make things much cleaner.


---

Comment by mabshoff created at 2008-10-17 23:17:56

Doctests pass, positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-10-18 00:02:26

Resolution: fixed


---

Comment by mabshoff created at 2008-10-18 00:02:26

Merged in Sage 3.2.alpha0
