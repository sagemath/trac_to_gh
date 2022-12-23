# Issue 4582: use Singular's capabilities for computing over fraction fields

Issue created by migration from https://trac.sagemath.org/ticket/4582

Original creator: malb

Original creation time: 2008-11-22 12:01:16

Assignee: malb

Guillaume Moroz wrote on [sage-devel]:

"
it seems that the sage interface to singular is not aware that Singular handles multivariate polynomial rings with coefficients in a fraction field.


```
sage: from sage.rings.polynomial.polynomial_singular_interface import
can_convert_to_singular
sage: r=Frac(QQ['a,b'])['x,y']
sage: can_convert_to_singular(r)
False
```


However, it is possible to define it in Singular: in this case, it would be


```
ring R=(0,a,b),(x,y),dp;
```


(following the syntax 2. given at http://www.singular.uni-kl.de/Manual/latest/sing_30.htm#SEC40)

In particular, Gröbner basis can be computed by Singular in these polynomial rings more efficiently than the toy algorithm currently used.
"


I hope this can help!

Best regards,



---

Comment by gmoroz created at 2008-11-26 23:56:32

Patch resolution via pexpect


---

Comment by gmoroz created at 2008-11-27 00:04:54

Resolution: fixed


---

Attachment

The attached patch should satisfy the requierement


---

Comment by mabshoff created at 2008-11-27 00:08:56

Resolution changed from fixed to 


---

Comment by mabshoff created at 2008-11-27 00:08:56

Hi,

please don't close tickets. A ticket is only closed once it has been merged by the release manager. 

Please make sure to read http://wiki.sagemath.org/TracGuidelines since it explains the process.

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-27 00:08:56

Changing status from closed to reopened.


---

Comment by mabshoff created at 2008-11-27 00:14:06

And one more thing: Please make sure to attach the file with the ending ".patch". The current attachment is a plain diff, so in case you use mercurial commit and do an "hg export tip" to create an hg patch. That patch automatically gives credit to you in the hg changelog for example and also has a number of different advantages. If you have trouble using hg we can discuss it either in IRC or on [sage-support].

Cheers,

Michael


---

Comment by gmoroz created at 2008-11-27 00:23:33

Yes sorry, I realized this too late.

It is the first time I use mercurial and just piped the output of 'sage -hg diff' in the text file: I'll check the export mercurial function and send a normal patch in some days.


---

Comment by mabshoff created at 2008-11-27 00:26:28

Replying to [comment:4 gmoroz]:
> Yes sorry, I realized this too late.

No problem, plenty of us have made that mistake :)

> It is the first time I use mercurial and just piped the output of 'sage -hg diff' in the text file: I'll check the export mercurial function and send a normal patch in some days.

Cool. Welcome aboard Sage development.

Cheers,

Michael


---

Comment by gmoroz created at 2008-11-28 22:57:54

Standard mercurial patch


---

Attachment

Patch applies cleanly against 3.2, doctests in `sage.rings` pass, patch contains doctest.


---

Comment by mabshoff created at 2008-11-30 23:12:04

Merged fraction_field.patch in Sage 3.2.1.rc1


---

Comment by mabshoff created at 2008-11-30 23:12:04

Resolution: fixed
