# Issue 2041: [with doc patch, needs review] tutorial: long lines in verbatim environments get cut off in pdf file

Issue created by migration from https://trac.sagemath.org/ticket/2041

Original creator: AlexGhitza

Original creation time: 2008-02-03 23:38:23

Assignee: AlexGhitza

See the discussion at
http://groups.google.com/group/sage-devel/browse_thread/thread/99ef95ceff366175/8e44f7219c7394d9

Lines longer than about 74 characters in verbatim environments are longer than the text width in the pdf files.  Worse, if they're longer than about 80 characters they just fall off the page and the rest gets cut off.

The attached doc patch does the following:
1. Ignore the "slightly long, but still completely visible" lines (i.e left them the way they were).  They're not that pretty, but wrapping them only makes things nicer by a marginal amount.
2. Manually wrapped the really long lines where stuff was lost: when these lines corresponded to sage: input commands, I broke them up in a place that looked ok to me with a backslash and continued on the next line.  I added warnings to the reader not to type in the ....: that appear on subsequent lines then.  If the lines correspond to long sage output, I just broke them after 72 characters, the exact same way that sage would behave if the terminal were 72 characters wide.  




---

Comment by mabshoff created at 2008-02-04 05:09:06

Hi Alex, 

you seem to have used some kind of hard wrapping to correct the issue. And the result some times cases line breaks inside words like

```
2480 Eisenstein subspace of dimension 1 of Modular Forms space of dimension 2 f 
2481 or Congruence Subgroup Gamma0(11) of weight 2 over Rational Field 
```


Cheers,

Michael


---

Comment by AlexGhitza created at 2008-02-04 15:02:46

Yes, that was on purpose (as I said above).  That's precisely how Sage's output is printed, I don't see why it should be beautified for documentation purposes.  The point of the tutorial is to get people used to the system, not to some idealized notion of the system.

Anyway, that was just my train of thought when working on this, and I'm willing to change my mind if there are arguments against it.


---

Comment by AlexGhitza created at 2008-02-12 04:16:49

I have fixed the problem Michael pointed out, and did some more beautification work on the tutorial: some typos, some changes in formulation.  I've replaced the old patch with the new and improved one.


---

Comment by mabshoff created at 2008-02-16 00:33:02

Except for the hunk

```
995	998	\SAGE makes some use of Singular \cite{Si}, e.g.,  
996	 	for computation of gcd's and Gr\"obner basis 
 	999	for computation of gcd's and Gr\"obner bases 
997	1000	of ideals. 
```

the patch looks good. We use `Gr\"obner basis` all over the place in the document and it seems to be the standard name even in English. I am giving the patch a positive review and will remove the hunk above before applying.

Cheers,

Michael


---

Comment by mabshoff created at 2008-02-16 00:55:02

I had to resolve some rejects since some of the fixes already made it in. The final version of the patch that I applied can be found at

http://sage.math.washington.edu/home/mabshoff/release-cycles-2.10.2/alpha1/trac_2041-tut_long_lines.patch

To get the full picture look at the commit prior to this patch.

Cheers,

Michael


---

Comment by mabshoff created at 2008-02-16 00:55:16

Resolution: fixed


---

Comment by mabshoff created at 2008-02-16 00:55:16

Merged in Sage 2.10.2.alpha1


---

Comment by mabshoff created at 2008-02-17 04:42:30

The patch actually causes various doctest failures in `tut.tex`. I am not sure how to balance this issue with readability.

Cheers,

Michael


---

Attachment


---

Comment by AlexGhitza created at 2008-02-17 20:13:35

OK, I've redone this patch to fix the doctest failures.  Right now there are no doctest failures, at the price of three lines being too long.  I say we put this patch in as it is, and deal with these three lines when we get a chance.


---

Comment by AlexGhitza created at 2008-02-17 20:14:03

Changing status from closed to reopened.


---

Comment by AlexGhitza created at 2008-02-17 20:14:03

Resolution changed from fixed to 


---

Comment by mabshoff created at 2008-02-17 20:22:22

Since the patch has already been replied I need a patch that reverts the three problematic issues. I will look into this or once 2.10.1.alpha1 is out you could give me a relative patch ;)

Cheers,

Michael


---

Comment by AlexGhitza created at 2008-02-17 20:58:35

I'm getting rather confused with what I have now versus what's merged versus what's on trac, so I'll just wait until 2.10.2.alpha1 and submit a relative patch (unless of course mabshoff will already have worked his magic :)


---

Comment by AlexGhitza created at 2008-02-20 13:43:56

I have uploaded a patch that is based on 2.10.2.alpha1 and passes all the tests in sage -t tut.tex.


---

Attachment

The new patch `tut_verbatim.patch` looks good to me except

```
999	 	for computation of gcd's and Gr\"obner basis 
 	999	for computation of gcd's and Gr\"obner bases 
```


Applying with that hunk removed. Great work Alex.

Cheers,

Michael


---

Comment by mabshoff created at 2008-02-20 14:04:14

Merged `tut_verbatim.patch` in Sage 2.10.2.alpha2


---

Comment by mabshoff created at 2008-02-20 14:04:14

Resolution: fixed
