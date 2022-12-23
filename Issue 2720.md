# Issue 2720: Sage 2.11.alpha2: fix documentation build issues

Issue created by migration from https://trac.sagemath.org/ticket/2720

Original creator: mabshoff

Original creation time: 2008-03-29 17:12:34

Assignee: tba

I got a patch for this. Coming up shortly.

Cheers,

Michael


---

Comment by mabshoff created at 2008-03-29 17:12:41

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-03-29 17:12:41

Changing assignee from tba to mabshoff.


---

Attachment

There is one hunk in the patch I am unhappy with:

```
295	 	            sage: pf._str_() 
296	 	            '_application PolyhedralFan\n_version 2.2\n_type PolyhedralFan\n
\nAMBIENT_DIM\n3\n\nDIM\n3\n\nLINEALITY_DIM\n0\n\nRAYS\n1 0 0\t# 0\n0 1 0\t# 1\n0 0 1\t# 
2\n\nN_RAYS\n3\n\nLINEALITY_SPACE\n\nORTH_LINEALITY_SPACE\n0 0 1\n0 1 0\n1 0 0\n\nF_VECTOR\n1 
3 1\n\nCONES\n{}\t# Dimension 0\n{0}\t# Dimension 1\n{1}\n{2}\n{0 1}\t# Dimension 2\n{0 2}\n{1 
2}\n{0 1 2}\t# Dimension 3\n\nMAXIMAL_CONES\n{0 1 2}\t# Dimension 3\n\nPURE\n1\n' 
 	295	            sage: len(pf._str_()) 
 	296	            369 
```

The output from `pf._str_()` doesn't play nice with TeX at all due to the `#` characters. I see no other elegant workaround for this issue but to just test the lenght of the output. 

Thoughts?

Cheers,

Michael


---

Attachment


---

Comment by mabshoff created at 2008-03-29 17:55:38

Replying to [comment:2 mabshoff]:
> There is one hunk in the patch I am unhappy with:
> {{{
> 295	 	            sage: pf._str_() 
> 296	 	            '_application PolyhedralFan\n_version 2.2\n_type PolyhedralFan\n
> \nAMBIENT_DIM\n3\n\nDIM\n3\n\nLINEALITY_DIM\n0\n\nRAYS\n1 0 0\t# 0\n0 1 0\t# 1\n0 0 1\t# 
> 2\n\nN_RAYS\n3\n\nLINEALITY_SPACE\n\nORTH_LINEALITY_SPACE\n0 0 1\n0 1 0\n1 0 0\n\nF_VECTOR\n1 
> 3 1\n\nCONES\n{}\t# Dimension 0\n{0}\t# Dimension 1\n{1}\n{2}\n{0 1}\t# Dimension 2\n{0 2}\n{1 
> 2}\n{0 1 2}\t# Dimension 3\n\nMAXIMAL_CONES\n{0 1 2}\t# Dimension 3\n\nPURE\n1\n' 
>  	295	            sage: len(pf._str_()) 
>  	296	            369 
> }}}
> The output from `pf._str_()` doesn't play nice with TeX at all due to the `#` characters. I see no other elegant workaround for this issue but to just test the lenght of the output. 

Thanks to some input from cwitty I fixed the issue.

Cheers,

Michael


---

Comment by cwitty created at 2008-03-29 18:03:14

Based only on reading the patches, these two patches look good.


---

Comment by mabshoff created at 2008-03-29 18:06:10

Resolution: fixed


---

Comment by mabshoff created at 2008-03-29 18:06:10

Merged in Sage 2.11.rc0
