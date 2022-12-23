# Issue 2530: interact bug -- drop down menu default doesn't show default value

Issue created by migration from https://trac.sagemath.org/ticket/2530

Original creator: was

Original creation time: 2008-03-15 06:28:46

Assignee: boothby


```
@interact
def _(f = (33,[1..100])):
    pass
```


The drop down should be set to 33 but isn't. 



---

Attachment

The attached patch fixes some minor issues with selectors with interact:

 1. the default for a drop-down menu is now correct,

 2. buttons with strings are no longer have quotes,

 3. the default value for selectors is the actual value rather than the index into the list of values, which is much much more natural.


---

Comment by TimothyClemans created at 2008-03-16 00:15:37

I tested this, and it looks good to me.


---

Comment by mabshoff created at 2008-03-16 00:55:37

Resolution: fixed


---

Comment by mabshoff created at 2008-03-16 00:55:37

Merged in Sage 2.10.4.rc0


---

Comment by mabshoff created at 2008-03-16 02:41:50

Replying to [comment:2 TimothyClemans]:
> I tested this, and it looks good to me.

Timothy,

for the record: Please doctest patches you review and clearly indicate what you doctested, i.e. all of Sage, some subdirectory and so on. Applying this patch causes a doctest failure, see #2538.

Cheers,

Michael
