# Issue 4238: option to create local .so file for .spyx modules

Issue created by migration from https://trac.sagemath.org/ticket/4238

Original creator: robertwb

Original creation time: 2008-10-02 19:33:58

Assignee: was

Loading an .spyx file requires a recompile for each new startup of Sage. There should be a way to save the .so file locally and load it like a module. 


---

Comment by robertwb created at 2008-10-02 19:38:41

Original patch from David Fu


---

Attachment

get doctests passing


---

Comment by robertwb created at 2008-10-02 19:40:43

The one question I have is if we should have a new global function for this behavior, or just provide it as an option to the cython function.


---

Comment by mabshoff created at 2008-10-03 00:01:19

This is a duplicate of #909, which I am closing.

Cheers,

Michael


---

Comment by robertwb created at 2008-10-03 09:01:31

I searched for a similar ticket, but I guess I didn't throw in the right keywords. Crazy how I think 3-digit trac tickets are "low" now...


---

Comment by GeorgSWeber created at 2008-10-05 19:49:04

First and foremost: I do give this patch a positive review, get this code in!

But the only reason is that it is the first new code in the spyx/load/attach for quite some time. This area is in a sorrow state, several tickets are open addressing different symptoms of the same cause:
It's all still nothing but a quick and dirty hack.

We will have problems with this new patch, consider the following scenario:
Two files foo.spyx and bar.sage, where bar.sage imports sth from foo.spyx.
1. User creates local foo.so
2. User is happy, until he needs in bar.sage a change in sth
3. User attaches foo.spyx and develops the needed change
4. User exits Sage
5. User reenters Sage
6. User loads bar.sage and wonders why the hell sth displays the old behaviour ...

Of course "User" forgot" to re-create the local foo.so, so the old one was taken.
But it is counter-intuitive that anyone should have to remember to do that manually, since the Sage had all information it needed to update the local foo.so itself!

In spite of this patch being so error-prone, without doing small steps in at least some patches, it seems that nothing would move here. So again, positive review.

At last for the question of a "new global function":
Well, the Right Thing (TM) to do here would be to introduce proper dependency handling in the load/attach code, probably best done with the help of a tool like Scons. Then, using attach/load just like one does right now, "behind the scenes" there would happen a bit more magic. To the end that whenever the sourcecode of some .spyx and anything else didn't change, a respective .so would already exist and be used (which is quick, as desired); and whenever the sourcecode --- or some other dependency of the .spyx, like e.g. a C library! --- did change, everything needed would happen automatically.

So, in an ideal world, the question about "global function or not" should be utterly superfluous. This problem "always long starting times due to recompilation done every time" just wouldn't exist!
But we live in a real world, with limited resources ...
So let's add just another hack that at least relieves some of the pain for some of us.


---

Comment by mabshoff created at 2008-10-07 22:40:42

local_so_doctests.patch will likely break on Cygwin, but I guess it will be easy enough to fix.

Cheers,

Michael


---

Comment by mabshoff created at 2008-10-07 23:25:25

Merged both patches in Sage 3.1.3.alpha3


---

Comment by mabshoff created at 2008-10-07 23:25:25

Resolution: fixed
