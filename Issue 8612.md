# Issue 8612: potentially horrible multimodular matrix echelon bug

Issue created by migration from Trac.

Original creator: was

Original creation time: 2010-03-26 05:46:26

Assignee: was

I was browsing the code in matrix/misc.pyx, and noticed:

```
These lines are in misc.pyx:

        if not proof:
            verbose("Not checking validity of result (since proof=False).", level=2, caller_name="multimod echelon")
            break
        d   = E.denominator()
        hdE = long(E.height())
        if True or hdE * self.ncols() * height < prod:
            break
        M = prod * p*p*p

```


Notice the "if True" -- that disables proof checking no matter what!!  This must be removed.  This could get hit in rare cased by, e.g., the modular symbols code, and it would lead to weird inconsistencies later on.... which is something we've seen on big examples.

I'm guessing this was the result of disabling proof checking while developing the code, then never switching it back.


---

Comment by was created at 2010-03-26 05:51:05

Changing status from new to needs_review.


---

Attachment


---

Comment by rbeezer created at 2010-03-28 23:17:38

In 


```
d   = E.denominator()
hdE = long(E.height())
if True or hdE * self.ncols() * height < prod:
    break
```


does  d  need to multiply  E.height()  at some point in the computation of hdE?  

It seems so in the algorithm as outlined in step (5) in the docstring.  And if not, does  d  then not need to be computed?  Hopefully, there's something mildly amiss here, but I've not studied the whole routine carefully.

Rob


---

Comment by was created at 2010-03-29 04:29:42

Yes, you're right, it needs to be 

```
hdE = long((d*E).height())
```


The algorithm is described with proof here: http://wstein.org/books/modform/modform/linear_algebra.html#echelon-forms-over

I've posted a part2 patch that fixes the issue you've pointed out.


---

Attachment


---

Comment by rbeezer created at 2010-03-29 04:35:04

OK, looks good then.  Wasn't sure just where to stuff the d.  ;-)

I'm going to run tests, but it may be morning before I have a report.


---

Comment by rbeezer created at 2010-03-29 05:38:11

Passed all tests.  Positive review.  

I'll post a consolidated patch.


---

Comment by rbeezer created at 2010-03-29 05:38:11

Changing status from needs_review to positive_review.


---

Comment by rbeezer created at 2010-03-29 05:39:12

Release manager: Apply just this patch.


---

Comment by was created at 2010-03-29 22:06:58

Resolution: fixed


---

Attachment

Merged into sage-4.3.5
