# Issue 3040: [with patch; needs review] make it so magma(A) works for matrices over cyclotomic number fields

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-04-27 03:21:07

Assignee: was

CC:  ncalexan




---

Attachment

Whoever reviews this also ought to review #2171

Cheers,

Michael


---

Comment by ncalexan created at 2008-05-05 18:39:40

As written, this does not work.  Was it the wrong version of the patch?

Here's a potential doctest, it fails because magma(K) does not work.


```
        We coerce a matrix over a cyclotomic field, where the
        generator must be named during the coercion.
            sage: K.<z> = CyclotomicField(12)
            sage: A = matrix(K, 2, 3, [z, 1+z, z^7 - z + 10/3, 1, 0, z^2 + z + 9*z^11])
            sage: B = magma(A); B                       # optional
            sage: B.Type()                              # optional
            ModMatFldElt
            sage: B.Parent()                            # optional
            Full KMatrixSpace of 2 by 3 matrices over XXX
```



---

Comment by craigcitro created at 2008-05-10 10:44:45

This works fine -- assuming you have the first patch from #3042 applied. Once that's in place, this is awesome.


---

Comment by craigcitro created at 2008-05-10 11:00:44

Oh, and I noticed that this patch didn't have a doctest. I mistakenly let it through -- so I'm adding one, and attaching a patch.


---

Attachment

sage-3040.patch no longer applies cleanly. Please rebase.

Cheers,

Michael


---

Attachment


---

Comment by mabshoff created at 2008-06-09 07:42:19

Merged sage-3040-rebase.patch and sage-3040-doctest-rebase.patch in Sage 3.0.3.alpha2


---

Comment by mabshoff created at 2008-06-09 07:42:19

Resolution: fixed


---

Comment by mabshoff created at 2008-06-09 07:47:16

The patches have been rebased, so correct the "Summary".

Cheers,

Michael
