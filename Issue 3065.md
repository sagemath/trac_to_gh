# Issue 3065: empty matrices: frobenius() throws  RuntimeError

Issue created by migration from Trac.

Original creator: dfdeshom

Original creation time: 2008-04-30 15:16:35

Assignee: was

This happens for frobenius(0) and frobenius(2) only. 

```
sage: m = matrix([])
sage: m.frobenius(0)
<type 'exceptions.OverflowError'>: range() result has too many items

sage: m.frobenius(2)
<type 'exceptions.RuntimeError'>:

sage: m.frobenius(2,'x')
<type 'exceptions.RuntimeError'>:

```



---

Comment by dfdeshom created at 2008-04-30 21:33:14

Changing keywords from "" to "pari".


---

Comment by dfdeshom created at 2008-04-30 21:33:14

PARI might be to blame here. The code below should return 0 everytime: 

```
sage: pari('matrix(0,0)').ncols()
 0

sage: pari('matrix(0,0)').nrows()
 47961608997888

sage: pari('matrix(0,0)').nrows()
 47961608997888
```



---

Comment by dfdeshom created at 2008-05-01 15:45:13

Patch attached. I suspect the problem I pointed above is due to `<GEN>self.g[1]` not being initialized.


---

Comment by mabshoff created at 2008-05-02 17:22:02

Opps, in case of `if self.ncols() == 0:` you never call `_sig_off`:

```
5391	5391	        _sig_on 
 	5392	        # if this matrix has no columns 
 	5393	        # then it has no rows.  
 	5394	        if self.ncols() == 0: 
 	5395	            return 0 
```

Other than that the patch looks fine to me.

Cheers,

Michael


---

Comment by was created at 2008-05-02 17:31:34


```
10:23 < dfdeshom-away> mabshoff: re: #3065: self>ncols() itself includes sig_on/sig_off calls, does 
                       that matter?
10:23 < jason|log> How would it make things worse?
10:23 < mabshoff> dfdeshom-away: Yes. I think it does.
10:23 < wstein> I don't know.  I'm just paranaoid about async calls, javascript, and putting in delays 
                that could lock the browser.
10:24 < mabshoff> wstein knows more about the code, but I think the fix is easy enough.
10:24 < wstein> Basically "putting in a delay" never quite works right robustly when
10:24 < wstein> doing async programming, in my experience.
10:24 < mabshoff> And since we are playing with the interrupt handler here I would consider the fix 
                  simple enough to actually do it.
10:24 < wstein> dfdeshom-away -- that code is very very bad.
10:24 < wstein> You will break things horribly by doing tat.
10:25 < mabshoff> :)
10:25 < wstein> It breaks two rules of _sig_*:
10:25 < mabshoff> +1 for code review.
10:25 < dfdeshom-away> feel free. I'll get to it this afternoon, but I don't know what your timeline is
10:25 < wstein> (1) never put any Python code in there.
10:25 < wstein> (2) always balance _sig_on with _sig_off.
10:25 < wstein> The fix is easy.
10:25 < wstein> Just put _sig_on *after* the if self.ncols() == 0: line
10:25 < wstein> Very easy fix.
```



---

Attachment


---

Comment by mabshoff created at 2008-05-05 15:51:34

Patch looks good to me. My concerns have been addressed. Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-05-05 20:36:23

Merged in Sage 3.0.2.alpha0


---

Comment by mabshoff created at 2008-05-05 20:36:23

Resolution: fixed
