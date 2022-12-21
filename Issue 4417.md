# Issue 4417: [with patch, needs review] fix steenrod algebra 'optional' doctest

Issue created by migration from Trac.

Original creator: jhpalmieri

Original creation time: 2008-11-01 02:39:53

Assignee: jhpalmieri

Keywords: steenrod algebra

In [response to mabshoff](http://groups.google.com/group/sage-devel/browse_frm/thread/be920ff2cef4a376), here is a patch to fix the failed 'optional' doctest in steenrod_algebra.py.  I don't actually know why this was only caught with optional; perhaps because the words 'package', 'long', and 'optional' appear somewhere in the file (although they're nowhere near each other or this test)?  Anyway, I fixed the doctest to be what it should be (i.e., what Sage was computing, which is also what I get by hand), and I changed 'package' to 'module' everywhere so that sage -t will test the same things as sage -t -optional.

  John




---

Attachment

Hi John,

this one was a really strange doctest failure and I am glad you fixed it.

One thing I noticed while looking at the file was that you use constructs like

```
sage: B = SteenrodAlgebra(2, 'adem')
```

which seem very un-Sagish, i.e. one would use some (optional) keyword in the constructor like

```
sage: B = SteenrodAlgebra(2, foo=adem)
```

This certainly should not addressed via this ticket, but might be something that should be discussed on [sage-devel].

Cheers,

Michael

PS: I will test and review this patch shortly.


---

Comment by jhpalmieri created at 2008-11-01 03:22:41


```
SteenrodAlgebra(5, 'adem')
```

could be changed to

```
SteenrodAlgebra(5, basis='adem')
```

(These both work right now; it would just be a matter of changing the documentation to reflect the preferred choice, if the second choice is better.)  I don't know how to implement something like

```
SteenrodAlgebra(5, basis=adem)
```

though, without importing `adem` into the global name space.

  John


---

Comment by mabshoff created at 2008-11-01 21:02:53

Replying to [comment:2 jhpalmieri]:
> {{{
> SteenrodAlgebra(5, 'adem')
> }}}
> could be changed to
> {{{
> SteenrodAlgebra(5, basis='adem')
> }}}
> (These both work right now; it would just be a matter of changing the documentation to reflect the preferred choice, if the second choice is better.)  

That sounds good to me. I would also prefer "foo" and not 'foo' for strings, but that is probably personal preference.

> I don't know how to implement something like
> {{{
> SteenrodAlgebra(5, basis=adem)
> }}}
> though, without importing `adem` into the global name space.
> 
>   John
> 

Ok.

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-01 21:05:47

Positive review, the patch fixes the issue.

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-01 21:06:07

Merged in Sage 3.2.alpha3


---

Comment by mabshoff created at 2008-11-01 21:06:07

Resolution: fixed
