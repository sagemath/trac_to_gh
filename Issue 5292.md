# Issue 5292: Error in FractionField conversion

Issue created by migration from https://trac.sagemath.org/ticket/5292

Original creator: robertwb

Original creation time: 2009-02-17 08:01:35

Assignee: tbd

On Feb 16, 2009, at 4:01 PM, Jason Bandlow wrote:


```
sage: R.<x> = QQ[]; S.<q,t> = QQ[]; F = FractionField(S);
sage: x in S   # this is ok
False
sage: x in F   # this is not

ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (857, 0))

ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (862, 0))

---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
...
/home/jason/<string> in <module>()

NameError: name 'x' is not defined
```



---

Comment by robertwb created at 2009-02-17 08:07:19

This is because eval is being used in lines 585+ of multi_polynomial_libsingular.pyx .


---

Comment by robertwb created at 2009-02-17 08:14:54

It's probably bad that it's even using strings here, but this fixes things a bit...

Now, the use of eval() here is bad... for example

sage: sage: R.<x> = QQ[]; S.<q,t> = R[]; F = FractionField(S);
sage: x in S
False

is still wrong. There are better ways of going about this but at least it doesn't crash. And I'm more OK with a False negative, but if this is accepted a new ticket should be created to follow up.


---

Attachment


---

Comment by mabshoff created at 2009-02-17 20:03:16

With the patch applied to my 3.3.rc2 merge tree all doctests pass.

Cheers,

Michael


---

Comment by was created at 2009-02-17 23:42:36

BAD

```
15:38 < wstein2> Ouch.
15:38 < wstein2> It has:
15:38 < wstein2> " except SyntaxError, NameError:"
15:38 < wstein2> As a new addition.
15:38 < wstein2> That is a major annoying python gotcha.
15:38 < wstein2> That assigns the exception to NameError.
15:38 < wstein2> It should be
15:38 < wstein2> except (SyntaxError, NameError):
15:38 < wstein2> Ooops!
15:39 < mabs> mk
15:39 < wstein2> I don't know why that would do any good either...
15:40 < wstein2> also, the patch should have a doctest
15:40 < mabs> Hmm, that might be difficult to do.
15:41 < wstein2> in fac the patch does *not* fix the problem.
15:41 < wstein2> You only wrote "all tests pass".
15:41 < wstein2> But that is because there are no new tests.
15:41 < wstein2> That ticket is a mess.
15:41 < mhansen> Patch up for #5298.
15:41 < wstein2> So you wrote: "With the patch applied to my 3.3.rc2 merge tree all doctests pass. "
15:41 < mabs> I did not write that about #5291.
15:41 < wstein2> But there was nothing to test that the problem was fixed.
15:42 < mabs> I wrote that about #5287
15:42 < wstein2> I'm talking about #5292.
15:42 < wstein2> Sorry.
15:42 -!- You're now known as wstein-5292
15:42 < mabs> Yes.
```



---

Comment by was created at 2009-02-17 23:46:12

fixed the previous very broken patch.


---

Attachment

I've attached a patch addressing all my remarks.  Somebody review this.  Mabshoff -- apply both patches in order.


---

Comment by mhansen created at 2009-02-17 23:56:26

Looks good to me.


---

Comment by robertwb created at 2009-02-18 00:02:39

Ouch, sorry. Yeah, that's one "wart" that I'm glad is being moved: http://www.python.org/dev/peps/pep-3110/

I should have added a test, but as I mentioned I don't think this resolves the real issue here (and since I found exactly where the problem was I wanted to make note of it).


---

Comment by mabshoff created at 2009-02-18 00:26:48

Merged both patches in Sage 3.3.rc2.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-18 00:26:48

Resolution: fixed
