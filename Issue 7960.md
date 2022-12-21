# Issue 7960: QQbar should accept number field elements with embeddings

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2010-01-17 00:26:12

Assignee: was

CC:  vdelecroix

One should be able to do 


```
sage: K.<a> = NumberField(x^3-x+1, embedding=-1.32)
sage: QQBar(a)
-1.324717957244746?
```


Followup to #4621


---

Comment by vdelecroix created at 2015-02-26 10:06:24

cc'ing me.

The function `sage.rings.number_field.number_field_morphisms.create_embedding_from_approx` should really be smarter. This is related to what I am currently doing in #17830.


---

Comment by mmezzarobba created at 2018-09-22 14:31:45

Fixed in #13041.


---

Comment by mkoeppe created at 2018-10-02 00:59:14

Changing status from new to needs_review.


---

Comment by pbruin created at 2018-11-09 13:41:06

The requested example now works.  It would be even nicer to also have a coercion map from `K` to `QQbar`, but currently we do not have this:

```
sage: K.<a> = NumberField(x^3 - x + 1, embedding=-1.32)
sage: QQbar(a)
-1.324717957244746?
sage: QQbar.coerce_map_from(K) is None
True
```



---

Comment by pbruin created at 2018-11-09 13:44:31

Replying to [comment:8 pbruin]:
> It would be even nicer to also have a coercion map from `K` to `QQbar`
OK, there is already a ticket for this: #5355.  Positive review for this one.


---

Comment by pbruin created at 2018-11-09 13:44:31

Changing status from needs_review to positive_review.


---

Comment by embray created at 2019-02-26 13:58:00

Presuming these are all correctly reviewed as either duplicate, invalid, or wontfix.


---

Comment by embray created at 2019-02-26 13:58:00

Resolution: invalid


---

Comment by slelievre created at 2019-02-26 14:23:01

Just fixing the example in the ticket description so anyone can check this now works.
