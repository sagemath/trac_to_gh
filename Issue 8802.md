# Issue 8802: sqrt() for QQbar and AA should have a parameter "all"

Issue created by migration from https://trac.sagemath.org/ticket/8802

Original creator: cremona

Original creation time: 2010-04-28 14:41:11

Assignee: AlexGhitza

CC:  robertwb davidloeffler cremona

This is inconsistent with other versions of sqrt():

```
sage: QQbar(2).sqrt()
1.414213562373095?
sage: QQbar(2).sqrt(all=True)
```


In addition, there should be a parameter "extend" to handle this:

```
sage: AA(2).sqrt()
1.414213562373095?
sage: AA(-2).sqrt()
1.414213562373095?*I
```

In the second example, we should not return a root in QQbar unless extend=True.


---

Attachment

Add all and extend parameters to sqrt for QQbar and AA


---

Comment by barinder created at 2010-06-07 15:21:19

Changing status from new to needs_review.


---

Comment by barinder created at 2010-06-07 15:35:21

Patch based on 4.4.2 and works fine on 4.4.3. The two problems identified by cremona have been resolved:


```
sage: QQbar(2).sqrt()
1.414213562373095?
sage: QQbar(2).sqrt(all=True)
[1.414213562373095?, -1.414213562373095?]
```


The following command 


```
sage: AA(-2).sqrt(extend=False)
}}} 

returns an error, like it should.


---

Comment by robertwb created at 2010-06-07 16:22:23

Mostly looks good. Some minor comments: 

 * There's a lot of redundancy between the AA and QQbar cases, perhaps it could be consolidated (this isn't that big of a deal though)
 * You normalize the root order in the all=True case, which I think is good, but the same normalization would probably be worth doing for the all=False case too (I'd be happy if it might negate twice to simplify the logic, as that will be relatively cheap).


---

Attachment

As before, but addresses the ordering issue raised by robertwb


---

Comment by cremona created at 2010-06-09 13:17:04

Changing status from needs_review to needs_work.


---

Attachment

Fixed docstring format issues and simplified: applies to 4.4.4.alpha0


---

Comment by cremona created at 2010-06-09 14:52:57

Version 3 of the patch (jointly written by Barinder and John) simplifies the code more and fixes docstring issues.  We removed the sign normalisation code, since the pow function already delivers a normalised result.


---

Comment by cremona created at 2010-06-09 14:52:57

Changing status from needs_work to needs_review.


---

Comment by davidloeffler created at 2010-06-10 10:45:40

Changing status from needs_review to positive_review.


---

Comment by robertwb created at 2010-06-10 15:12:33

Looks good to me too.


---

Comment by mhansen created at 2010-06-11 19:16:28

Resolution: fixed
