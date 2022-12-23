# Issue 1523: rewrite the mathematica/maple <---> sage interfaces for osx to be much easier to use for the "lay person"

Issue created by migration from https://trac.sagemath.org/ticket/1523

Original creator: was

Original creation time: 2007-12-15 07:28:23

Assignee: was

This illustrates the unnecessary confusion:


```
> are working fine.  I'll try "math"....I have a currently executing (long
> running) mathemataica simulation going, and it's fine.
>
> Bill
>
> "math" is not found on OSX terminal! neither is mathematica; sage brings up
> a new SAGE notebook, and all of it "runs" except the calls to Maple (which I
> don't have installed on this MAC) and Mathematica 6.0,which I do....so some
> like we were getting (via airport????) is now missing....or something else.

I probably didn't put the math script that I made somewhere in your PATH.
I can't remember where I put it now, but that would be the problem.
I really need to make Sage automatically do this (with no user intervention).
Can you type

 locate math

and send me the output, which will contain a script named "math"?
Then you just have to move that script to /usr/bin/ so it is in you PATH.
```



---

Comment by was created at 2007-12-17 16:50:13


```
Justin (cc: sage-devel),

There are now a lot of people using Sage on OSX who don't know
(much) about the command line, but who are maple/mathematica
users.  When they try:

  sage: mathematica('2+2')

they get a big error message about creating a "math" script, etc.,
and similarly for Maple.

It seems to me that instead of that big error, we could *automatically*
track down Maple/Mathematica on their system and
create the script and put it in SAGE_ROOT/local/bin/.

Thoughts?

It seems like OSX mojo is relevant to this problem.

```



---

Comment by kcrisman created at 2013-02-13 02:34:07

I'm not sure we should be fixing this... or at least, sage-wishlist.


---

Comment by jdemeyer created at 2015-06-23 13:49:26

Changing component from interfaces to interfaces: optional.
