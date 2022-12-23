# Issue 4810: qepcad-1.50 fails to build without tcsh

Issue created by migration from https://trac.sagemath.org/ticket/4810

Original creator: mabshoff

Original creation time: 2008-12-16 06:37:59

Assignee: cwitty

CC:  jondo

Martin Rubey reported in http://groups.google.com/group/sage-devel/browse_thread/thread/d48a4139afd07da8

```
just for the record: installing tcsh makes the problem go away.  This hint was 
buried in a longer mail on this list, so I repeat it here... 
```

He also reported an interface problem which could also be split off to another ticket:

```
Another hint:  qepcad does not like fractions, not even of integers, and the 
sage interface doesn't deal with this.  So you have to reduce them yourself, 
i.e., instead of 
a < b/2 
write 
2*a < b 
Otherwise qepcad will appear to do nothing. 
```


Cheers,

Michael


---

Comment by rws created at 2015-10-22 08:02:27

See also #19450


---

Comment by jdemeyer created at 2015-10-22 08:24:12

Any reason to think that these two tickets are related?


---

Comment by jdemeyer created at 2017-03-14 16:25:48

Probably obsolete


---

Comment by jdemeyer created at 2017-03-14 16:25:48

Resolution: invalid


---

Comment by tmonteil created at 2017-03-15 07:21:41

Indeed, it has been fixed in #10224, with a patch to remove that dependency to tcsh : https://git.sagemath.org/sage.git/diff/build/pkgs/qepcad/patches/makefile_no_csh.patch?id=9b43535c1221c86b6e4f17cd36951d88a2c350fb
