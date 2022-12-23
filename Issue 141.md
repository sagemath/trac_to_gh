# Issue 141: sage -ldist -- needs to be updated

Issue created by migration from https://trac.sagemath.org/ticket/141

Original creator: was

Original creation time: 2006-10-21 01:41:47

Assignee: was

On Fri, 20 Oct 2006 18:06:42 -0700, Mark <mfenner`@`gmail.com> wrote:
> Could someone provide a basic road map of what would need to be done to
> separate the interfaces (i.e., Python code) from the batteries included
> distribution?  Aside from extracting sage-<version> from
> spkg/sage-<version> and doing python setup.py install, that is ...

First, something that might be helpful is to try typing 

    "sage -ldist VER"

which ends up running

    <SAGE_ROOT>/local/bin/sage-libdist

which is supposed to make a "stand alone" version of SAGE without dependencies.
I.e., a tarball that you can "python setup.py install" into a standard Python2.5
install, assuming you have all dependencies.  

It is "slightly" behind, i.e,. I haven't used it in months, so it is not likely
to work.  But it is a first step in the direction of what you want. 

[...]

I just tried "sage -ldist" and it failed because it isn't aware of how
I reorganized where the custom ipython config files go; basically, it fails
in creating an ipython config for SAGE.  But it gets close -- in particular, 
if you run it you'll get a directory
   <SAGE_ROOT>/dist/sage-....
that has a setup.py file in it.  

I haven't kept it up only because the user base until now has not
actually requested it.   I'll list that "sage -ldist" doesn't quite
work as a bug on the tracker, so I can fix it soon.



---

Comment by was created at 2007-01-12 23:27:55

Resolution: wontfix
