# Issue 2928: another p-adic extension segfault

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2008-04-15 05:49:17

Assignee: roed


```
K.<b> = Qp(13).extension(x^2+x-1)
fatal error:
   internal error: can't grow this _ntl_gbigint
exit...
/Users/robert/sage/current/local/bin/sage-sage: line 357: 18024 Abort
trap              python "$`@`"
```


Applying the patches from #2843 didn't fix this. 


---

Comment by mabshoff created at 2008-04-15 05:56:27

Hi Robert, 

my alpha5 merge tree doesn't experience the problem:

```
mabshoff`@`sage:/scratch/mabshoff/release-cycle/sage-3.0.alpha5$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 3.0.alpha4, Release Date: 2008-04-12                  |
| Type notebook() for the GUI, and license() for information.        |
sage: K.<b> = Qp(13).extension(x^2+x-1)
sage:
```

I would suggest you wait for alpha5 [out once I merge #2927, #2929 and the LinBox.spkg update not yet in trac] and then verify that it works for you, too.

Cheers,

Michael


---

Comment by kedlaya created at 2008-04-15 11:14:25

This is fixed in my alpha4 tree (which also has #2903 and #2928 applied):

```
sage: K.<b> = Qp(13).extension(x^2+x-1)
sage: print K
Unramified Extension of 13-adic Field with capped relative precision 20 in b defined by (1 + O(13^20))*x^2 + (1 + O(13^20))*x + (12 + 12*13 + 12*13^2 + 12*13^3 + 12*13^4 + 12*13^5 + 12*13^6 + 12*13^7 + 12*13^8 + 12*13^9 + 12*13^10 + 12*13^11 + 12*13^12 + 12*13^13 + 12*13^14 + 12*13^15 + 12*13^16 + 12*13^17 + 12*13^18 + 12*13^19 + O(13^20))
```

so this ticket is being closed.


---

Comment by kedlaya created at 2008-04-15 11:14:25

Resolution: fixed


---

Comment by kedlaya created at 2008-04-16 11:27:27

This is apparently not fixed for robertwb, and it's not fixed for me either on 32-bit Ubuntu, so this ticket is being reopened. (In my previous comment, #2928 should of course have been #2843.)


---

Comment by kedlaya created at 2008-04-16 11:27:27

Resolution changed from fixed to 


---

Comment by kedlaya created at 2008-04-16 11:27:27

Changing status from closed to reopened.


---

Comment by wjp created at 2008-04-20 00:54:58

`PowComputer_ZZ_pX_small.__new__` has a `ZZ_pX_c tmp` that gets used a number of times. It seems that the `ZZ_p`'s that are allocated for the coefficients of `tmp` the first time it is used have non-resizable storage. On a 32-bit machine this fixed size turns out to be too small for one of the later uses of `tmp`, causing the reported error message.

It's too late at night for me to write a patch for this now, but I'll probably take a shot at it tomorrow unless somebody else wants to.


---

Comment by wjp created at 2008-04-20 01:06:43

To expand on this a little bit, I think that the right way to fix it is making `ZZ_pX_conv_modulus` re-allocate its `fout` argument if necessary.


---

Attachment


---

Attachment


---

Comment by wjp created at 2008-04-20 13:42:47

Following the suggestion from Roed on IRC, the attached patch allocates `ZZ_pX tmp` with large enough coefficient size to handle all moduli.

Done for both `PowComputer_ZZ_pX_small` and `PowComputer_ZZ_pX_big`.

(Please ignore the first patch (it broke `_big`), and only apply/review the second.)


---

Comment by kedlaya created at 2008-04-20 22:07:01

Applied against 3.0.rc0, this fixes the problem on my 32-bit machine (where I was able to replicate the problem before). It seems like a pretty clean way to do it without imposing a serious performance hit. Positive review.


---

Comment by mabshoff created at 2008-04-21 00:37:10

Resolution: fixed


---

Comment by mabshoff created at 2008-04-21 00:37:10

Merged padics_tmp_coeff_size.2.patch in Sage 3.0.rc1
