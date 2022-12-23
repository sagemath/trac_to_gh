# Issue 2275: [with patch, needs review] get sloane_functions.py to 100% coverage

Issue created by migration from https://trac.sagemath.org/ticket/2275

Original creator: mhansen

Original creation time: 2008-02-23 04:44:31

Assignee: mhansen

CC:  sage-combinat




---

Attachment

Here is a link:  http://sage.math.washington.edu/home/mhansen/2275.patch


---

Comment by mhansen created at 2008-02-23 05:21:43

Changing status from new to assigned.


---

Comment by jsp created at 2008-02-24 19:12:48

I don't think this is a good idea:

```
All sloane_functions have extensive examples, but from design they are
placed just after the class declaration.
It feels stupid to have "internal" functions
starting with '__' or '_' documented with EXAMPLES!

Let us think at the effect on the reference manual.
I don't think it is a good idea to have internal functions like
__init, _repr and other "hidden" fuctions documented with examples
figuring in the Reference Manual.

If we want users of the OEIS to use Sage, we have to provide them with
adequate examples. Maybe raising the doctest coverage with 2% looks good
but it isn't in this case.

Adding some sloane-functions I was following the 'template'. So there
is, maybe, something wrong with the overall design.


Jaap



```



---

Comment by was created at 2008-02-24 20:35:22

I disagree with Jaap here.  I think getting coverage to 100% is a good idea.


---

Comment by jsp created at 2008-02-24 20:47:42

Replying to [comment:3 was]:
> I disagree with Jaap here.  I think getting coverage to 100% is a good idea. 

Generally spoken yes, but in this case I have my doubts.

Jaap


---

Comment by was created at 2008-03-03 05:28:45

Looks superb to me.


---

Comment by mabshoff created at 2008-03-03 12:33:48

Merged in Sage 2.10.3.rc1


---

Comment by mabshoff created at 2008-03-03 12:33:48

Resolution: fixed
