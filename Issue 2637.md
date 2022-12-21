# Issue 2637: Patch so that a user can choose encodings in sage scripts.

Issue created by migration from Trac.

Original creator: lars.fischer

Original creation time: 2008-03-21 21:43:30

Assignee: was

Keywords: encoding utf-8

This ticket is related to my question on sage-support:
http://groups.google.com/group/sage-support/browse_thread/thread/dab6a0880fa8b942
and Martin Albrecht's patch.

With Martin's patch, sage scripts default to utf-8 encoding, which is a good default as ascii is a subset of utf-8, it is compatible with existing sage-scripts.

But I think that a user should be able to select a coding, if utf-8 is not suitable for him. For example a user with an editor not supporting unicode or a user needing utf-16. So sage should support python encoding hints.  
 
Please see the attached patch to sage/misc/interpreter.py, which tries to find out if the first line contains an encoding hint. If true, use the line from the file, else print the utf-8 encoding hint.

With best regards,
Lars Fischer


---

Comment by lars.fischer created at 2008-03-21 21:46:00

Find an use encoding hints in the first line of a sage script.


---

Attachment

I do not see a patch attached. Where is it?

Cheers,

Michael


---

Comment by mabshoff created at 2008-03-21 21:51:07

Ok, the bundle showed up, i.e. it was a race condition. We do prefer patches over bundles, especially for single commit changesets.

I am not sure this is a good feature since UTF-8 is ubiquitous out there these days. We build Python with ucs4 anyway, so I see no point to this patch. This  will only cause trouble if people start exchanging Sage files with different encodings. The code isn't doctested either, so if it were accepted that needs to be added, too.

Cheers,

Michael


---

Comment by lars.fischer created at 2008-03-22 12:19:16

Replying to [comment:2 mabshoff]:
> Ok, the bundle showed up, i.e. it was a race condition. We do prefer patches over bundles, especially for single commit changesets.

I followed the advise in 
http://www.sagemath.org/doc/html/prog/node72.html
 * "For the occasional contributor:"
 
> I am not sure this is a good feature since UTF-8 is ubiquitous out there these days. We build Python with ucs4 anyway, so I see no point to this patch. This  will only cause trouble if people start exchanging Sage files with different encodings. The code isn't doctested either, so if it were accepted that needs to be added, too.

I was thinking exactly the same after I saw the Martin's patch: 
_"That will only cause trouble if someone wants to use something different than UTF-8. With sage being compatible with Python, sage should also support encoding selection."_ 
So I think it is the other way around: you get in trouble if people start using sage e.g. in Asia, using their their local encoding and there is no way to tell sage that the file is something different than UTF-8.

Perhaps I am a bit too sensitive, because I have a long and frustrating history with computersystems making assumptions about encodings. 

If there is interest, I can add doctests. What hg_sage. .... function would I use to get a file, I can attach? export() with the last but one entry from the log, and then replacing the attachment above?

With best regards,
Lars Fischer


---

Comment by lars.fischer created at 2008-03-31 14:31:00

I created a new patch file with hg_sage.export() . I hope this is a patch file. At least the first line in the file says so. 

Now the function contains some doctest. But I cannot sage -t interpreter.py, there is a nodoctest in the first line and if I temporarily  delete it, there are errors. 

I attached interpreter.py and after that I was able to record the tests.

With best regards,
Lars Fischer


---

Comment by lars.fischer created at 2008-03-31 14:58:49

Find and use encoding hints in the first line of a sage script. Replace the previous attachment.


---

Attachment

Hi Lars,

after thinking about the issue some more I changed my mind and now believe that this is a good idea. Patch looks good to me. Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-13 18:13:04

But there are a bunch of issues with the doctests:

 * devel/sage/sage/misc/interpreter.py has doctests disabled in general
 * you need to add "from sage.misc.interpreter import handle_encoding_declaration" to make the doctests work
 * Even then I get the following failure:

```
File "/scratch/mabshoff/release-cycle/sage-3.0.alpha5/tmp/interpreter.py", line 355:
    sage: c4='import os, sys\n...'
Expected:
    handle_encoding_declaration(c1, sys.stdout)
    # -*- coding: latin-1 -*-
    'import os, sys\n..'
Got nothing
```

There are other, unrelated doctest failure issues in that file, I fixed most of them and will hopefully post a patch shortly.

Cheers,

Michael


---

Comment by craigcitro created at 2008-06-20 04:31:25

Changing keywords from "encoding utf-8" to "encoding utf-8, editor_malb".


---

Comment by malb created at 2008-06-23 23:54:16

Lars are you planing to address Michael's concern? I took over making sure that the patch gets in (I'm the editor for it now) and thus I wonder.


---

Comment by malb created at 2008-06-24 08:10:44

Apply `encoding.hg.patch` first then `trac2637_fixes.patch` which still needs a review. With my fixes I'd give Lars' patch a positive review. Mabshoff can you review my patch?


---

Comment by lars.fischer created at 2008-06-24 12:08:22

Replying to [comment:8 malb]:

Hello,

I am very busy at the moment. Because of that I was so quiet. Additionally the last upgrade  to sage 3.0 (sage -b main; sage -upgrade;) left my testing branch with the modified version of handle_encoding_declaration unusable:


```
sage -br test

----------------------------------------------------------
sage: Building and installing modified SAGE library files.
.....
----------------------------------------------------------------------
----------------------------------------------------------------------
Setting permissions of DOT_SAGE directory so only you can read and write it.
Loading SAGE library. Current Mercurial branch is: test
---------------------------------------------------------------------------
<type 'exceptions.ImportError'>           Traceback (most recent call last)
....
/usr/local/sage/local/lib/python2.5/site-packages/sage/rings/polynomial/all.py in <module>()
     35
     36 # Boolean Polynomial Rings
---> 37 from sage.rings.polynomial.pbori import BooleanPolynomialRing
     38
     39 from sage.rings.polynomial.multi_polynomial_ideal import is_MPolynomialIdeal
| SAGE Version 3.0, Release Date: 2008-04-23                         |
| Type notebook() for the GUI, and license() for information.        |
<type 'exceptions.ImportError'>: libpolybori.so: cannot open shared object file: No such file or directory
sage:                    
```


I did not know how to deal with it, today I just rm-rf my sage-test branch, cloned a new one from the 3.0 version, sage -br test, hg_sage.applied encoding.hg.patch and trac2637_fixes.patch.

After that sage -b  and then sage -t interpreter.py was successful.

> Lars are you planing to address Michael's concern? I took over making sure that the patch gets in (I'm the editor for it now) and thus I wonder.

What concern do you mean, after testing works?


With best regards,

Lars Fischer


---

Comment by malb created at 2008-06-24 12:38:59

Replying to [comment:10 lars.fischer]:
> After that sage -b  and then sage -t interpreter.py was successful.
> 
> > Lars are you planing to address Michael's concern? I took over making sure that the patch gets in (I'm the editor for it now) and thus I wonder.
> 
> What concern do you mean, after testing works?

I addressed the Michael's review in my patch so all that is needed from my perspective is a review of my patch. This can be either done by you or by Michael or by somebody else. Cheers, Martin


---

Comment by mabshoff created at 2008-06-24 13:08:57

Two suggestions for Martin's patch: I would remove the doctest:

```
78	 	    sage: V = VectorSp 
 	78	 
 	79	    sage: V = VectorSp # not tested 
79	80	    VectorSpace                      VectorSpace_subspace 
80	81	    VectorSpace_ambient              VectorSpace_subspace_with_basis 
81	82	    VectorSpace_generic
```

since it does not work any more as is and open a ticket for

```
513	 	        sage: preparser(False) 
514	 	        sage: 2/3 
 	519	 
 	520	        sage: preparser(False)  
 	521	        sage: 2/3 # not tested since the doctest framework preparses anyway 
515	522	        0 
 	523	 
```

unless the preparser is unfixable. When I attempted to fix all the doctests in the file I ran into the same problem and gave up after I ran into the same problem.

Cheers,

Michael


---

Attachment

addresses mabshoff's review, sort of


---

Comment by malb created at 2008-06-24 13:42:37

* Yes, the file is old and a mess.
 * The doctests double as documentation so I vote against removing them.
 * I updated the VectorSpa<tab> docs to the current behaviour.
 * Cleaning up interpreter.py should be a different ticket and no hold-back for this one IMHO.


---

Comment by mabshoff created at 2008-06-24 14:10:57

I agree with malb and I will review malb's new patch today.

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-23 05:47:12

Positive review. Sorry for the *loooonnnng* delay - my bad.

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-30 06:37:08

I am too paranoid to put this into 3.2.1 at this late stage, but it will be one of the first patches in 3.2.2.alpha0 early next week.

Cheers,

Michael


---

Comment by mabshoff created at 2008-12-10 12:36:04

Merged encoding.hg.patch and two hunks from trac2637_fixes.patch in Sage 3.2.2.alpha1. 

The other four hunks from trac2637_fixes.patch were already in the tree.

Finally :)

Cheers,

Michael


---

Comment by mabshoff created at 2008-12-10 12:36:04

Resolution: fixed
