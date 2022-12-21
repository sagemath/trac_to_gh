# Issue 5967: ElementWrapper: A class for wrapping Sage or Python objects as Sage elements

Issue created by migration from Trac.

Original creator: nthiery

Original creation time: 2009-05-03 01:26:19

Assignee: nthiery

CC:  sage-combinat

This patch implements a simple class ElementWrapper for wrapping Sage
or Python objects as Sage elements, with reasonable default
implementations of repr, cmp, hash, etc. The typical use case is for
trivially constructing new element classes from preexisting Sage or
Python classes, with a containment relation.

This class is used extensively in the examples of the upcoming category framework patch #5891.



---

Comment by mabshoff created at 2009-05-03 01:55:31

This is broken:

```
 	129	            sage: cmp(l11, l12), cmp(l12, l11)   # values differ 
 	130	            (-1, 1) 
 	131	            sage: cmp(l11, l21), cmp(l21, l11)   # parents differ 
 	132	            (-1, 1) 
```

*Never* check the return value of `cmp` to be -1 or 1, but always write

```
sage: cmp(l11, l21) in [-1,1]
True
```

since the value depends on memory location. I have had to fix this literally dozens of times in doctests.

Cheers,

Michael


---

Comment by mabshoff created at 2009-05-03 01:57:46

This ticket also needs to be properly market with a marker so it is picked up for review.

Another thing to fix is to get this file into the documentation. Unless it is in the documentation the vast majority of people will never know of its existence. Current policy is that every file that is well documented and 100% doctested belongs in the documentation. 

Cheers,

Michael


---

Comment by nthiery created at 2009-05-03 02:25:04

Replying to [comment:1 mabshoff]:
> This is broken:
> {{{
>  	129	            sage: cmp(l11, l12), cmp(l12, l11)   # values differ 
>  	130	            (-1, 1) 
>  	131	            sage: cmp(l11, l21), cmp(l21, l11)   # parents differ 
>  	132	            (-1, 1) 
> }}}
> *Never* check the return value of `cmp` to be -1 or 1, but always write
> {{{
> sage: cmp(l11, l21) in [-1,1]
> True
> }}}
> since the value depends on memory location. I have had to fix this literally dozens of times in doctests.

Ok, will do.


---

Comment by nthiery created at 2009-05-03 02:25:56

Replying to [comment:2 mabshoff]:
> This ticket also needs to be properly market with a marker so it is picked up for review.

Any suggestion for that marker?

> Another thing to fix is to get this file into the documentation. Unless it is in the documentation the vast majority of people will never know of its existence. Current policy is that every file that is well documented and 100% doctested belongs in the documentation. 

Ok, will do.


---

Comment by mabshoff created at 2009-05-03 02:29:15

Replying to [comment:4 nthiery]:
> Replying to [comment:2 mabshoff]:
> > This ticket also needs to be properly market with a marker so it is picked up for review.
> 
> Any suggestion for that marker?

I meant the standard "[with patch, needs review]" :)

Cheers,

Michael


---

Comment by nthiery created at 2009-05-03 02:33:04

Replying to [comment:5 mabshoff]:
> I meant the standard "[with patch, needs review]" :)

Oops, I was sure I had done this!


---

Comment by nthiery created at 2009-05-03 03:02:37

Done, and patch updated. Thanks Michael for your suggestions.


---

Comment by aschilling created at 2009-05-07 03:50:26

The tests of the patch pass when applied to sage-3.4.2.

Besides the application to the category framework #5891,
this patch will be useful for crystals. For example the
class Letter(Element):
in /combinat/crystals/letters.py
can be shortened by inheriting from ElementWrapper.

I give this patch a positive review!


---

Comment by nthiery created at 2009-05-19 06:25:19

Changing status from new to assigned.


---

Comment by mabshoff created at 2009-05-22 14:20:14

Has anybody non-combinat signed off on this? Not that I don't trust Anne, but ... ;)

Cheers,

Michael


---

Comment by nthiery created at 2009-05-23 07:41:28

The uploaded patch adds a warning about the probable little change of interface in the near future (but after integration of the category patch).
Robert promised to have a look at this shortly.


---

Comment by robertwb created at 2009-05-23 08:55:48

I agree this looks good. The only caveat is that the docstring reads 


```
Therefore, ``o`` does inherit the string
```


where it probably should be "does not."


---

Attachment


---

Comment by nthiery created at 2009-05-23 15:49:44

Replying to [comment:12 robertwb]:
> I agree this looks good. The only caveat is that the docstring reads 
> 
> {{{
> Therefore, ``o`` does inherit the string
> }}}
> 
> where it probably should be "does not."

Oops, indeed! Thanks. Patch updated.


---

Comment by mhansen created at 2009-05-31 23:40:42

Merged in 4.0.1.alpha0.


---

Comment by mhansen created at 2009-05-31 23:40:42

Resolution: fixed
