# Issue 5334: libgcrypt.spkg: Disable padlock again unconditionally

Issue created by migration from https://trac.sagemath.org/ticket/5334

Original creator: mabshoff

Original creation time: 2009-02-22 10:43:25

Assignee: mabshoff

This was reported in IRC:

```

[02:28am] tringlarido: I had a problem with compiling the sage3-3 sources.
[02:29am] mabs: hi
[02:29am] mabs: What platform are you on?
[02:29am] tringlarido: The install exit exactly at the same step than 
http://groups.google.fr/group/sage-devel/browse_thread/thread/9d4b39e961c24e4f/89bfb1cd2822ffd2?lnk=gst&q=rijndael#89bfb1cd2822ffd2
[02:29am] tringlarido: Linux iml88 2.6.11-6mdk #1 Tue Mar 22 16:04:32 CET 2005 i686 Intel(R) Pentium(R) 4 CPU 2.80GHz unknown GNU/Linux
[02:30am] mabs: Ok, I see what the problem is.
```

I reenabled padlock support in 3.3 since the libgcrypt people claimed that it had been fixed. The spkg at 

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.4/alpha0/libgcrypt-1.4.3.p0.spkg

disables it again and also adds Solaris 64 bit build support while I am in there :)

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-22 10:46:01

And it seems to work:

```

[02:44am] tringlarido: I restart the build, but I don't know where it 
starts from (the beginning ?). I well tell you if it works. Thanks.
[02:45am] mabs: It will restart from where it left of.
[02:45am] mabs: I.e it will build libgrcypt first.
[02:45am] tringlarido: OK. I saw the libcrypt build just pass.
[02:45am] mabs: The log should be scrolling by, so you should see 
then the next one is done.
[02:45am] mabs: Ok great.
```


We still do need a formal review of the spkg, but that shouldn't be too much work.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-22 11:03:53

Changing status from new to assigned.


---

Comment by mhansen created at 2009-02-24 18:01:01

Looks good to me.


---

Comment by mabshoff created at 2009-02-24 19:34:52

Resolution: fixed


---

Comment by mabshoff created at 2009-02-24 19:34:52

Merged in Sage 3.4.alpha0.

Cheers,

Michael
