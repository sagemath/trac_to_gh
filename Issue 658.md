# Issue 658: print the random seed use to initialize the rng, add ability to set seed via command line parameter

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2007-09-15 00:22:37

Assignee: somebody


```
$ magma
Magma V2.13-5     Fri Sep 14 2007 17:16:36 on sage     [Seed = 2401430993]
Type ? for help.  Type <Ctrl>-D to quit.
>
```

Cheers,

Michael


---

Comment by was created at 2007-10-08 14:41:39


```
> > We *really* need a way of specifying a random seed at startup.
> >
>
> When we fixed all the leaks in the random seed code William wrote some
> code to specify the random seed via an environment variable. I grepped
> $SAGE_LOCAL/bin and couldn't find anything, so maybe it wasn't merged.

I removed it because the implementation was way too hack-ish.  It was
mainly for experimenting.

I do encourage David to open a trac ticket about this.  He's right that
seeding the random number generator should be possible via a command
line argument at startup.

One perhaps reasonable way to do this is by setting an environment variable
in local/bin/sage-sage if a certain command line option is set, then in
ext/random.pxi (and anywhere else), somehow using that environment variable
(if set) to seed the random number generator.     The tricky part is one has
to also make sure in all cases that all seeding is done from one place, and
that the random seed is easily available from Sage on startup or in
crash messages.
```



---

Comment by cwitty created at 2008-08-23 20:54:30

The randstate framework essentially fixes this.  It doesn't print the seed on startup, but you can retrieve it with initial_seed(); and it doesn't have a command-line argument for setting the seed, but you can set it with set_random_seed().


---

Comment by cwitty created at 2008-08-23 20:54:30

Resolution: fixed
