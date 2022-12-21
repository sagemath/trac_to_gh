# Issue 3361: fricas install problem.

Issue created by migration from Trac.

Original creator: wdj

Original creation time: 2008-06-04 16:04:10

Assignee: mabshoff

This was reported first by John Cremona and discussed in the thread
http://groups.google.com/group/sage-devel/browse_thread/thread/85bb061c36c57527
Even though William Stein mentioned someone should create a trac ticket for this issue,
I could not find one, so made this one.

From John C's email:


```
I tried to install fricas (prompted by an earlier thread -- I wonder
which?) but this happened (with 3.0.2 on linux):

 axiom_build_bindir =
/home/jec/sage-3.0.1/spkg/build/fricas-1.0.2/build-dir/build/x86_64-suse-linux/bin
checking for gcl... no
configure: error: GCL and GCL sources missing, see README.wh
***********************************************************
Failed to configure Axiom.
***********************************************************

real    0m0.546s
user    0m0.280s
sys     0m0.268s
sage: An error occurred while installing fricas-1.0.2
...
```

The file 'fricas-1.0.2.spkg' from
http://www.sagemath.org/packages/optional
came from Burcin Erocal on April 1, 2008. 

I can duplicate this problem on amd64 hardy heron (ubuntu 8.04,
on a phenom processor machine), with gcl and binutils-dev installed. 
A similar problem occurs for the older version made by Bill Page at 
http://sage.math.washington.edu/home/page/packages/axiom4sage-0.3.1.spkg

- David Joyner


---

Comment by mabshoff created at 2008-07-31 01:12:39

Waldek Hebish and Bill Page updated the FriCAS.spkg. The new one can be found at

http://sage.math.washington.edu/home/page/packages/fricas-1.0.3.spkg

Cheers,

Michael


---

Comment by mabshoff created at 2008-07-31 02:02:07

An updated spkg with minimal fixes, i.e. I checked in the files into a repo, can be found at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.1/alpha0/fricas-1.0.3.p0.spkg

Positive review from my end. 

Cheers,

Michael


---

Comment by mabshoff created at 2008-07-31 02:10:30

Resolution: fixed


---

Comment by mabshoff created at 2008-07-31 02:10:30

Merged in Sage 3.1.alpha0
