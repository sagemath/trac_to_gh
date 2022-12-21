# Issue 3424: jordan_form gives incorrect results due to imprecise roots

Issue created by migration from Trac.

Original creator: johnwilmes

Original creation time: 2008-06-14 20:17:47

Assignee: was

mat.jordan_form(CDF) gives the wrong Jordan form for some matrices because mat.charpoly().roots() sometimes gives separate roots when it should give a single root. Attached is a patch that adds a new parameter to jordan_form so that users can specify a number of digits of rounding to the roots of the characteristic polynomial.


```
sage: m                            

[1 1]
[0 1]
sage: m.jordan_form()              

[1 1]
[0 1]
sage: m.jordan_form(CDF)

[1.0|  0]
[---+---]
[  0|1.0]
sage: m.jordan_form(CDF, digits=2)

[1.0 1.0]
[  0 1.0]
```



---

Attachment


---

Comment by cwitty created at 2008-06-15 06:32:25

I think that rounding is a bad way to do this... this would not merge roots 1.44999999 and 1.450000001, but would merge 1.45000001 and 1.549999999.  It would be better to specify some sort of relative error.


---

Comment by johnwilmes created at 2008-06-15 07:08:08

I'm not sure I follow you. Using the rounding method from the patch:

```
sage: def do_round(eval, digits):
....:     eval = CDF(eval) 
....:     r = CDF(round(eval.real(), digits), round(eval.imag(), digits))
....:     return r
....: 
sage: do_round(1.44999999, 3)
1.45
sage: do_round(1.45000001, 3)
1.45
sage: do_round(1.54999999, 3)
1.55
```


This seems to be the desired behavior.


---

Comment by cwitty created at 2008-06-15 07:43:29

It depends on how many digits you round to.

```
sage: do_round(1.44999999, 1)
1.4
sage: do_round(1.45000001, 1)
1.5
sage: do_round(1.54999999, 1)
1.5
sage: 1.45000001 - 1.44999999
1.99999998784506e-8
sage: 1.54999999 - 1.45000001
0.0999999800000002
```


Here the first and second numbers round differently, even though they differ by about 2e-8; and the second and third numbers round the same, even though they differ by about 0.1.  Similar examples could be found for rounding to any number of digits.


---

Comment by johnwilmes created at 2008-06-20 00:36:38

Replying to [comment:4 cwitty]:
> It depends on how many digits you round to.

I see what you mean now, and that does seem like a significant problem. However, I can't see a way of using the distance between roots without using a more complicated clustering algorithm that introduces its own problems. So for example, suppose we start with the roots 1.45, 1.50, and 1.55, and the user specifies an error tolerance of 0.05. It's not clear to be what the correct way to group the roots would be. Do we treat them all as the same root? Do we arbitrarily put them into two different categories, or leave them all separate?


---

Comment by jason created at 2008-11-14 05:14:01

Or we can just throw a numerical precision warning that says that the jordan form is pretty much nonsense when computing with imprecise numbers.  I don't know if there is an easy way to get around the issue you are point out.

Maybe one way to do it would be to surround each root with an interval with radius = your tolerance.  If two roots intersect, then consider them the same.  This might lead to problems, but in the end, I think it will be more helpful than hurtful.  I'd also put out the warning that the results probably are nonsense because of numerical issues.


---

Comment by jason created at 2008-11-14 05:15:34

in other words, in the extreme case you point out, group all the roots as the same.  In practice, people should not be specifying intervals that large.  In practice, I don't think you will see a huge chain of roots that are all within some tolerance of their neighbors (for reasonable tolerances).


---

Comment by johnwilmes created at 2016-06-08 15:10:54

Changing status from needs_work to needs_review.


---

Comment by johnwilmes created at 2016-06-08 15:10:54

I thought I should finally take care of this, but now (8 years later) sage very sensibly refuses to compute Jordan forms over inexact fields. So the "defect" is no longer present, and I guess this can be closed? (Or if anyone actually wants this over inexact fields, I can submit a new patch...)


---

Comment by rws created at 2016-08-22 13:23:59

Changing status from needs_review to needs_info.


---

Comment by rws created at 2016-08-22 13:23:59

Setting to needs_info because no code is to be reviewed.
