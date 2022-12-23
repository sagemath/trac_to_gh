# Issue 7240: factorization of Cunningham numbers - applications

Issue created by migration from https://trac.sagemath.org/ticket/7240

Original creator: ylchapuy

Original creation time: 2009-10-18 10:35:29

Assignee: tbd

CC:  jpflori rws

Following #7239, use the factorization of Cunningham numbers to speed up polynomial primitivity testing and other finite field stuff (for small characteristic).


---

Comment by ylchapuy created at 2009-10-26 21:59:08

Changing status from new to needs_review.


---

Comment by cremona created at 2009-12-18 17:21:38

The patch applies fine to 4.3.rc0 after installing the optional spkg at #7239 and the patch there, and tests pass.  Good doctests included.

BUT in both places where _cunningham_prime_factors() is called, a run-time error will be raised if the optional database is not installed.  If the database is really going to be optional then these calls must be wrapped with try/except, otherwise people who have not installed the optional package will find lots of their code fails.

Hence: needs work.


---

Comment by cremona created at 2009-12-18 17:21:38

Changing status from needs_review to needs_work.


---

Comment by ylchapuy created at 2009-12-18 18:27:58

In fact if the patch from #7239 is applied, but the database not installed, `_factor_cunningham` will just be the usual factor, with the first time it's called a warning (not an error) saying:

"You might consider installing the optional package for factoring Cunningham numbers with the following command: ``sage -i cunningham_tables-1.0``"

Moreover this warning will only be seen if the characteristic is `p \in {2,3,5,7,11}` and `p^k > 2^100`. I thought it was nice to tell the user that there exists an optional package useful for them, but I can remove it if necessary.


---

Comment by cremona created at 2009-12-18 20:04:38

OK, that is more reasonable.   But why don't we (you!) put a case to sage-devel for including this spkg as standard?  It's only another 492837 bytes, and the cremona database is 78M.


---

Comment by ylchapuy created at 2010-01-20 14:57:54

This ticket is marked as "needs work", but what should be done exactly?


---

Comment by cremona created at 2010-01-20 15:27:36

I set it to "needs work" but then agreed that it was good (but did not change the label).  On the other hand, there has been discussion on sage-devel in favour of including this as standard anyway.   

So I suggest that we give this a positive review.  This will take two steps....


---

Comment by cremona created at 2010-01-20 15:27:36

Changing status from needs_work to needs_review.


---

Comment by cremona created at 2010-01-20 15:27:43

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2010-01-22 17:06:42

After applying the attachment [trac7240_Cunningham_factorization_application.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7240/trac7240_Cunningham_factorization_application.patch), I got the following doctest failures on Sage 4.3.1. In all of these cases, I didn't install the optional Cunningham spkg at #7239

```
[mvngu@sage sage-4.3.1]$ ./sage -t -long devel/sage-main/sage/rings/finite_field_ntl_gf2e.pyx
sage -t -long "devel/sage-main/sage/rings/finite_field_ntl_gf2e.pyx"
**********************************************************************
File "/mnt/usb1/scratch/mvngu/release/sage-4.3.1/devel/sage-main/sage/rings/finite_field_ntl_gf2e.pyx", line 1349:
    sage: b._gap_init_()
Expected:
    'Z(65536)^1'
Got:
    doctest:21: UserWarning: You might consider installing the optional package for factoring Cunningham numbers with the following command: ``sage -i cunningham_tables-1.0``
    'Z(65536)^1'

[mvngu@sage sage-4.3.1]$ ./sage -t -long devel/sage-main/sage/rings/finite_field_element.py
sage -t -long "devel/sage-main/sage/rings/finite_field_element.py"
**********************************************************************
File "/mnt/usb1/scratch/mvngu/release/sage-4.3.1/devel/sage-main/sage/rings/finite_field_element.py", line 375:
    sage: a.multiplicative_order()
Expected:
    124
Got:
    doctest:21: UserWarning: You might consider installing the optional package for factoring Cunningham numbers with the following command: ``sage -i cunningham_tables-1.0``
    124

[mvngu@sage sage-4.3.1]$ ./sage -t -long devel/sage-main/sage/rings/finite_field_ext_pari.py
sage -t -long "devel/sage-main/sage/rings/finite_field_ext_pari.py"
**********************************************************************
File "/mnt/usb1/scratch/mvngu/release/sage-4.3.1/devel/sage-main/sage/rings/finite_field_ext_pari.py", line 103:
    sage: z.multiplicative_order()
Expected:
    15
Got:
    doctest:21: UserWarning: You might consider installing the optional package for factoring Cunningham numbers with the following command: ``sage -i cunningham_tables-1.0``
    15

[mvngu@sage sage-4.3.1]$ ./sage -t -long devel/sage-main/sage/rings/polynomial/polynomial_element.pyx
sage -t -long "devel/sage-main/sage/rings/polynomial/polynomial_element.pyx"
**********************************************************************
File "/mnt/usb1/scratch/mvngu/release/sage-4.3.1/devel/sage-main/sage/rings/polynomial/polynomial_element.pyx", line 2860:
    sage: f.is_irreducible(), f.is_primitive()
Expected:
    (True, False)
Got:
    doctest:21: UserWarning: You might consider installing the optional package for factoring Cunningham numbers with the following command: ``sage -i cunningham_tables-1.0``
    (True, False)

[mvngu@sage sage-4.3.1]$ ./sage -t -long devel/sage-main/sage/groups/generic.py
sage -t -long "devel/sage-main/sage/groups/generic.py"      
**********************************************************************
File "/mnt/usb1/scratch/mvngu/release/sage-4.3.1/devel/sage-main/sage/groups/generic.py", line 774:
    sage: discrete_log(u,g)
Expected:
    123456789
Got:
    doctest:21: UserWarning: You might consider installing the optional package for factoring Cunningham numbers with the following command: ``sage -i cunningham_tables-1.0``
    123456789
```



---

Comment by cremona created at 2010-01-22 17:13:04

I think my positive review was dependent on the vote we had (yes we did!) to include the spkg as standard rather then optional -- it is very small and requires no building.  The spkg is attached to (sorry, linked to) the ticket #7239.  I'm sure I assumed that when that ticket was closed, the right thing would happen to its spkg!


---

Comment by mvngu created at 2010-01-22 18:17:56

Replying to [comment:11 cremona]:
> I think my positive review was dependent on the vote we had (yes we did!) to include the spkg as standard rather then optional

Thank you for the clarification, John. The merging of this ticket can wait until:

 1. the (currently optional) Cunningham package becomes a standard spkg; or
 1. there is some code to test whether that spkg is installed.


---

Attachment


---

Comment by ylchapuy created at 2010-01-25 09:59:23

This is of course all my fault. I stated that the warning wouldn't appear for numbers of less than 100 bits, but it was not the case. I updated the patch, switching two lines and it should be fine now. At least for me the above failures disappear.

The second patch I added is what should be done if the package become standard (and yes we had a vote, what's the next step?). It replaces my warning/advertisment with an error.

Yann


---

Comment by jdemeyer created at 2010-02-11 15:43:08

Dear everyone,

I would like to add a few comments here.  If I understand things correctly, the Cunningham database in SAGE is now just a list of numbers without structure, right?

I have written myself a PARI/GP-2.4 script which

1) tries to determine which b<sup>n</sup>-1 numbers have a non-trivial gcd with a given number.  The algorithm is essentially p-1 factorisation, but with several well-chosen bases instead of one (random) base.

2) uses that information to do Aurifeuillian factorisation and a more clever table lookup.

Step 1) can be skipped if we know exactly that we want to factor 10^555-1 for example.

I could probably manage to port this to some SAGE functions in Python.  Once this has been done, I would like to add a lot more factors to more numbers of the form b^n-1 to the database (larger b and n).


---

Comment by ylchapuy created at 2010-02-11 17:05:38

Replying to [comment:14 jdemeyer]:
> Dear everyone,
> 
> I would like to add a few comments here.  If I understand things correctly, the Cunningham database in SAGE is now just a list of numbers without structure, right?

Yes right, this was just a quick and dirty solution to my problems.

> I have written myself a PARI/GP-2.4 script (snip)
> I could probably manage to port this to some SAGE functions in Python. (snip)

This would be great if you port your work to SAGE. My first thought was to include your script but currently SAGE is still shipping pari 2.3.3.

Yann


---

Comment by was created at 2010-04-29 05:30:44

Changing status from positive_review to needs_work.


---

Comment by ylchapuy created at 2010-04-29 14:51:32

rebased on sage 4.4


---

Attachment

I think it's ok for review now.


---

Comment by ylchapuy created at 2010-04-29 22:03:15

Changing status from needs_work to needs_review.


---

Comment by ylchapuy created at 2010-04-29 22:03:49

(again...) and it should be ok without the spkg.


---

Comment by jdemeyer created at 2010-07-08 14:02:38

Changing component from algebra to factorization.


---

Comment by jdemeyer created at 2010-07-08 14:04:23

I plan to work on this and improve it a lot.  In particular, the database of Cunningham factors should not be just a list, it should know of which numbers the factors are factors of (i.e. factor p divides Phi_a(b))


---

Comment by cremona created at 2010-08-22 13:09:22

This is one of the tickets which the Sage nagbot regularly nags me about.  But anyone seeing Jeroen's last comment will wait rather than review it.  I suggest that *either* this patch gets reviewed as is, and Jeroen's improvements go on another ticket, *or* the "needs review" tag is changed to "needs work".


---

Comment by jdemeyer created at 2010-08-22 13:18:47

It's still in my TODO list.


---

Comment by jdemeyer created at 2010-08-22 13:18:47

Changing status from needs_review to needs_work.


---

Comment by roed created at 2010-09-24 17:53:51

As encouragement for working on this ticket, I'm using `_factor_cunningham` in #7931.  Now that #8334 has a positive review, #7931 is ready to review, but it's getting doctest failures because of the warning generated by _factor_cunningham.


---

Comment by roed created at 2011-06-21 11:11:02

Any progress on this ticket?  I'd like to use it in #8335.


---

Comment by roed created at 2011-12-05 10:55:16

This patch accompanies a new spkg: [http://sage.math.washington.edu/home/roed/cunningham_tables-2.0.spkg](http://sage.math.washington.edu/home/roed/cunningham_tables-2.0.spkg).

Apply 7240.patch only.


---

Comment by roed created at 2011-12-05 10:55:16

Changing status from needs_work to needs_review.


---

Comment by roed created at 2011-12-05 10:57:25

Also, this patch assumes that the Cunningham tables spkg has been made standard.  I'll e-mail sage-devel about that soon.


---

Comment by roed created at 2011-12-05 11:22:42

Changing assignee from tbd to roed.


---

Comment by roed created at 2012-01-04 10:51:22

There's a new version of the spkg at: [Cunningham_Tables-2.1](http://sage.math.washington.edu/home/roed/cunningham_tables-2.1.spkg).  This new version will only work after applying #12133.


---

Comment by ohanar created at 2012-03-18 18:29:11

please make sure that both sobj's use python ints (and longs) and not sage integers. Also remove the trailing whitespace in

 * docstring for FiniteField.factored_order
 * docstring for Polynomial.is_primitive
 * docstring for CunninghamDatabase
 * "x is not a list" line in cunningham_database.py

Finally, it would be great if you would make your error's python 3 compatible, since we should probably start thinking forward to the day we make that transition.


---

Comment by ohanar created at 2012-03-18 18:29:11

Changing status from needs_review to needs_work.


---

Comment by roed created at 2013-03-02 01:11:03

Changing status from needs_work to needs_review.


---

Comment by roed created at 2013-03-02 01:11:03

I've addressed Andrew's comments, and added a new version of the SPKG at http://sage.math.washington.edu/home/roed/cunningham_tables-2.2.spkg


---

Attachment


---

Comment by rws created at 2014-02-13 10:09:56

Changing status from needs_review to needs_work.


---

Comment by rws created at 2014-02-13 10:09:56

Your file `7240.patch` tries to upgrade the `cunningham_table` package to 2.2 which isn't what is advertised with this ticket. Please don't do this, it makes difficult things even more so.

I suppose then that the patch to be reviewed would be the one by `@`ylchapuy named ` trac7240_Cunningham_factorization_application.patch​`. Even with the `-l` option it fails to apply with Sage-6.0.


---

Comment by rws created at 2014-02-13 10:17:41

From the sage developer's guide:

If a function requires an optional package, that function should fail gracefully—*perhaps using a try-except block—when the optional package is not available*, and should give a hint about how to install it. ...


---

Comment by rws created at 2014-02-13 10:20:59

Changing assignee from roed to rws.


---

Comment by jpflori created at 2014-02-13 13:42:57

Replying to [comment:11 cremona]:
> I think my positive review was dependent on the vote we had (yes we did!) to include the spkg as standard rather then optional -- it is very small and requires no building.  The spkg is attached to (sorry, linked to) the ticket #7239.  I'm sure I assumed that when that ticket was closed, the right thing would happen to its spkg!
>  
It was voted that the new cunningham package would become standard.


---

Comment by jpflori created at 2014-02-13 13:43:32

(And note that the data provided should surely be updated.)


---

Comment by rws created at 2014-02-14 08:48:54

Replying to [comment:43 jpflori]:
> (And note that the data provided should surely be updated.)

But don't use $SAGE_DATA anymore, use $SAGE_SHARE or $SAGE_ROOT/share, see #15814


---

Comment by rws created at 2014-02-20 14:49:53

Separated from the SPKG install (#15813) and rebased on 6.2.base2.
----
New commits:


---

Comment by rws created at 2014-02-20 14:49:53

Changing status from needs_work to needs_review.


---

Comment by rws created at 2014-04-04 14:06:08

Changing status from needs_review to needs_work.


---

Comment by rws created at 2014-04-04 14:06:08

patchbot reports failures in `rings/` and `groups/`: among others `ImportError: cannot import name CunninghamDatabase`. Of course the patchbot will test without the package being installed, so it made sense what I wrote in comment:39 about failing gracefully...


---

Comment by rws created at 2014-04-04 16:43:46

Changing status from needs_work to needs_review.


---

Comment by rws created at 2014-04-04 16:43:46

Rebase on 6.2.beta6. Fix failing doctests.
----
New commits:


---

Comment by rws created at 2014-05-07 13:24:14

Changing status from needs_review to needs_work.
