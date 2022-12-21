# Issue 3112: [with patch, needs review] Generate self-orthogonal binary codes

Issue created by migration from Trac.

Original creator: rlm

Original creation time: 2008-05-06 18:57:03

Assignee: rlm

CC:  wdj mhansen


```
sage: for B in self_orthogonal_binary_codes(8,3):
....:     print B.gen_mat()
....:     print
....:     
[1 1]

[1 1 0 0]
[0 0 1 1]

[1 0 1 0 0 0]
[0 1 0 1 0 0]
[0 0 0 0 1 1]

[1 1 1 1]

[1 1 1 1 0 0]
[0 0 0 0 1 1]

[1 0 1 1 1 0 0 0]
[0 1 0 0 0 1 0 0]
[0 0 0 0 0 0 1 1]

[1 0 1 1 1 0 0 0]
[0 1 0 0 0 1 0 0]
[0 0 1 0 1 0 1 1]

[1 1 1 1 0 0]
[0 1 0 1 1 1]

[1 0 1 1 0 1 0]
[0 1 0 1 1 1 0]
[0 0 1 0 1 1 1]

[1 0 1 1 0 1 0 0]
[0 1 0 1 1 1 0 0]
[0 0 0 1 0 1 1 1]

[1 1 1 1 0 0 0 0]
[0 0 0 0 1 1 1 1]

[1 1 1 1 1 1]

[1 1 1 1 1 1 0 0]
[0 0 0 0 0 0 1 1]

[1 1 1 1 1 1 0 0]
[0 1 0 0 0 1 1 1]

[1 1 1 1 1 1 1 1]
```



---

Comment by mabshoff created at 2008-05-06 20:03:48

Hi rlm,

I didn't look at the patch too closely, but I noticed that you added a lot of code with sparse documentation and also some [internal] function that are not doctested. Is there more coming?

Cheers,

Michael


---

Comment by rlm created at 2008-05-06 20:45:06

The only new external function is `self_orthogonal_binary_codes`, which does have doctests. Most of the internal functions are cdef, and they are only there for the self orthogonal code generator.

Perhaps you'd like more doctests for `self_orthogonal_binary_codes`?


---

Comment by wdj created at 2008-05-07 18:12:03

This passes sage -testall.

Some questions.

1. Does the command 
 	517	    def matrix(self): 
return a generator matrix or the so-called syndrome table or ...? 
Does the name matrix seem too ambiguous to you?

2. Should the docstring for self_orthogonal_binary_codes
explain that you are actually computing a complete set of representatives
of equivalence clasees of such codes up to a given length and dim? 

3. When you run self_orthogonal_binary_codes, are you actually
computing all the (equiv classes of) [n,k]-codes, then adding up those
to get the codes up to a given length and dim? Or, are you somehow
getting all of them at once? In either case, it would obviously be
useful to have a function which only returns those of a given 
length. It would be easy enough to simply simply filter out the 
"bad" ones from the output of self_orthogonal_binary_codes. However, 
I wonder if there was a slicker way to do this using Cython?

4. I'm not competent enough to review the cython code. Mike Hansen,
can you do this?


---

Comment by rlm created at 2008-05-07 18:39:06

Regarding 1, 2, and 4, there is a second patch on the way.

Regarding 3, the codes are built up recursively, so the program is naturally computing up to some n and k, but I guess I could put in an option for the filtering so you didn't have to do it each time.


---

Comment by wdj created at 2008-05-07 18:58:14

1. This seems to be a bug:


```
sage: B = self_orthogonal_binary_codes(8,4,4)
sage: for C in B: print C.gen_mat()
....:
[1 1 1 1]
[1 1 1 1 0 0]
[0 1 0 1 1 1]
[1 0 1 1 0 1 0]
[0 1 0 1 1 1 0]
[0 0 1 0 1 1 1]
[1 0 0 1 1 0 1 0]
[0 1 0 1 1 1 0 0]
[0 0 1 0 1 1 1 0]
[0 0 0 1 0 1 1 1]
[1 0 1 1 0 1 0 0]
[0 1 0 1 1 1 0 0]
[0 0 0 1 0 1 1 1]
[1 1 1 1 0 0 0 0]
[0 0 0 0 1 1 1 1]
[1 1 1 1 1 1 1 1]
sage: for C in B: print C.gen_mat()
....:
sage:                          
```

It appears B cannot be re-used!??

2. Can the docstring for this command explain what kind of object the output is?
A natural thing for a user to try is to pick off the first element:


```
sage: B = self_orthogonal_binary_codes(8,4,4)
sage: B[0]
---------------------------------------------------------------------------
<type 'exceptions.TypeError'>             Traceback (most recent call last)

/mnt/drive_hda1/sagefiles/sage-3.0.1/<ipython console> in <module>()

<type 'exceptions.TypeError'>: 'generator' object is unsubscriptable
```

But as you see, a type error is raised.

3. Check this out:


```
sage: C = QuasiQuadraticResidueCode(11)
sage: G = C.automorphism_group_binary_code()
sage: G.order()/MathieuGroup(22).order()
2
```

This is very interesting!


---

Comment by rlm created at 2008-05-07 22:00:51

David,

Both 1 and 2 are generally properties of iterators. What you want might be `list(self_orthogonal_binary_codes(8,4,4))`.


---

Comment by wdj created at 2008-05-08 01:45:50

Okay, thanks. Could you toss in an example to that effect in the docstring?


---

Comment by rlm created at 2008-05-10 22:05:43

What this patch provides is a Python iterator. If someone wants to make a nicer interface, that's great, but that should be the subject of a separate ticket.


---

Comment by wdj created at 2008-05-11 16:21:49

The 2 patches apply cleanly to 3.0.1 and pass sage -testall.

1. This segfault is a problem:

sage: len(list(self_orthogonal_binary_codes(8, 4, d=1, equal=True)))


------------------------------------------------------------
Unhandled SIGSEGV: A segmentation fault occured in SAGE.
This probably occured because a *compiled* component
of SAGE has a bug in it (typically accessing invalid memory)
or is not properly wrapped with _sig_on, _sig_off.
You might want to run SAGE under gdb with 'sage -gdb' to debug this.
SAGE will now terminate (sorry).
------------------------------------------------------------

This is a rather nasty segfault which does not return the command line
in the terminal window....

Once this is fixed, it would be useful for doctesting (and user's understanding) 
to include something like this in the docstring.

2. Minor issue: instead of 


```
    Generates all (permutation equivalence classes of) self-orthogonal binary
    linear codes of length in [1..n] and dimension in [1..k].
    
    NOTE:
    Technically, what is returned is a set of representatives of these classes.
```

I would say something like


```
    Returns a Python iterator which generates a complete set of representatives of 
    all permutation equivalence classes of self-orthogonal binary linear codes of 
    length in [1..n] and dimension in [1..k].
```


3. Other than these, looks good to me.


---

Comment by wdj created at 2008-05-11 16:25:00

One more (minor notational) thing: I think the use of the parameter d in the function


```
self_orthogonal_binary_codes(8, 4, d=2,...
```

goes against standard notation. Usually, d represents the minimum distance and either b or c represent the divisibility factor. Probably b is preferable here since c is somethings used for codewords.


---

Comment by rlm created at 2008-05-11 18:00:58

David,

That's a nasty segfault there. Also, I agree with all your comments. Expect a new patch soon.


---

Comment by rlm created at 2008-05-11 20:20:03

The new patch fixes both your problems. Thanks!


---

Comment by wdj created at 2008-05-12 00:42:57

These three patches apply cleanly to 3.0.1 and pass sage -testall. I think this is a very significant contribution and hope it can be applied before 3.0.2 comes out.


---

Attachment

This is a flat version of the previous three.


---

Comment by mabshoff created at 2008-05-22 02:22:07

Hi rlm.

assuming 100% doctest coverage this patch will be merged in 3.0.2.rc0.

Cheers,

Michael


---

Attachment

That should do it.


---

Comment by mabshoff created at 2008-05-22 20:36:09

Oops, the patch no longer applies cleanly:

```
mabshoff`@`sage:/scratch/mabshoff/release-cycle/sage-3.0.2.rc0/devel/sage$ patch -p1 < trac_3112-socodes.patch
patching file sage/coding/all.py
patching file sage/coding/binary_code.pxd
patching file sage/coding/binary_code.pyx
Hunk #2 FAILED at 34.
Hunk #3 succeeded at 72 (offset 2 lines).
Hunk #4 succeeded at 534 (offset 2 lines).
Hunk #5 succeeded at 549 (offset 2 lines).
Hunk #6 succeeded at 570 (offset 2 lines).
Hunk #7 succeeded at 588 (offset 2 lines).
Hunk #8 succeeded at 615 (offset 2 lines).
Hunk #9 succeeded at 833 (offset 2 lines).
Hunk #10 succeeded at 847 (offset 2 lines).
Hunk #11 succeeded at 940 (offset 2 lines).
Hunk #12 succeeded at 954 (offset 2 lines).
Hunk #13 succeeded at 1202 (offset 2 lines).
Hunk #14 succeeded at 1249 (offset 2 lines).
Hunk #15 succeeded at 1275 (offset 2 lines).
Hunk #16 succeeded at 1810 (offset 2 lines).
Hunk #17 succeeded at 1818 (offset 2 lines).
Hunk #18 succeeded at 1838 (offset 2 lines).
Hunk #19 succeeded at 1848 (offset 2 lines).
Hunk #20 succeeded at 2110 (offset 2 lines).
Hunk #21 succeeded at 2347 (offset 2 lines).
Hunk #22 succeeded at 2377 (offset 2 lines).
Hunk #23 succeeded at 2397 (offset 2 lines).
Hunk #24 succeeded at 2414 (offset 2 lines).
Hunk #25 succeeded at 2434 (offset 2 lines).
Hunk #26 succeeded at 2445 (offset 2 lines).
Hunk #27 succeeded at 2533 (offset 2 lines).
Hunk #28 succeeded at 2603 (offset 2 lines).
Hunk #29 succeeded at 2621 (offset 2 lines).
Hunk #30 succeeded at 2665 (offset 2 lines).
Hunk #31 succeeded at 2691 (offset 2 lines).
Hunk #32 succeeded at 2706 (offset 2 lines).
Hunk #33 succeeded at 2774 (offset 2 lines).
Hunk #34 succeeded at 2795 (offset 2 lines).
Hunk #35 succeeded at 2809 (offset 2 lines).
Hunk #36 succeeded at 2827 (offset 2 lines).
Hunk #37 succeeded at 2848 (offset 2 lines).
Hunk #38 succeeded at 2858 (offset 2 lines).
Hunk #39 succeeded at 2920 (offset 2 lines).
Hunk #40 succeeded at 2992 (offset 2 lines).
Hunk #41 succeeded at 3093 (offset 2 lines).
Hunk #42 succeeded at 3168 (offset 2 lines).
Hunk #43 succeeded at 3195 (offset 2 lines).
Hunk #44 succeeded at 3221 (offset 2 lines).
Hunk #45 succeeded at 3303 (offset 2 lines).
Hunk #46 succeeded at 3499 (offset 2 lines).
Hunk #47 succeeded at 3518 (offset 2 lines).
1 out of 47 hunks FAILED -- saving rejects to file sage/coding/binary_code.pyx.rej
patching file sage/coding/linear_code.py
Hunk #5 succeeded at 1491 (offset 9 lines).
```

Feel free to rebase it against my tree on sage.math with the above path. There are still some doctests missing, but let's get this merged and open a follow up ticket.

Cheers,

Michael


---

Comment by rlm created at 2008-05-22 22:42:12

This should replace the previous two.


---

Attachment

The new patch applies cleanly. In the process of rebasing rlm also found an issue in #3269's docstring.

Cheers,

Michael


---

Comment by mabshoff created at 2008-05-22 23:12:40

Resolution: fixed


---

Comment by mabshoff created at 2008-05-22 23:12:40

Merged in Sage 3.0.2.rc0
