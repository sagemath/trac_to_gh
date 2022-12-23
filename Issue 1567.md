# Issue 1567: zn_poly spkg

Issue created by migration from https://trac.sagemath.org/ticket/1567

Original creator: dmharvey

Original creation time: 2007-12-19 15:18:45

Assignee: was

spkg for the `zn_poly` library:

http://math.harvard.edu/~dmharvey/zn_poly/releases/zn_poly-0.4.1.spkg

I've tested it on some platforms, but it needs to be tested on more.

See also

http://groups.google.com/group/sage-devel/browse_thread/thread/9844ce77400e7ed4



---

Comment by mhansen created at 2007-12-22 22:37:57

Spkg builds and installs fine for me on 64-bit Ubuntu 7.10.


---

Comment by mabshoff created at 2007-12-23 02:31:29

I would suggest to make this optional first and get some more build reports from a whole bunch of different compilers and build envs. Since a build failure of this spkg will cause problems for many people the reward doesn't outweigh the risk for 2.9.1 and maybe even 2.9.2. 

Cheers,

Michael


---

Comment by mabshoff created at 2007-12-23 02:52:25


```
[03:27] <dmharvey> i strongly recommend NOT putting zn_poly.spkg into 2.9.1
[03:28] <mabshoff> :)
[03:28] <dmharvey> agree with mabshoff it's too early
```



---

Comment by mabshoff created at 2007-12-23 02:57:25

I have added zn_poly-0.4.1.spkg to the experimental spkg repo.

Cheers,

Michael


---

Comment by boothby created at 2008-03-16 06:59:47

Compiled fine on my server (debian / xeon).


---

Comment by malb created at 2008-03-17 23:26:58

As the author of the spkg explicitly warns us not to put the spkg in Sage, shouldn't it be moved to another milestone like sage-feature?


---

Comment by dmharvey created at 2008-03-17 23:47:26

I should clarify. This spkg contains some gcc assembly macros. These are borrowed from GMP and NTL, so I think they should be fine, but I haven't personally tested them on all the platforms that they are supposed to support. This is the only reason I want to hold back. If we get positive build reports on all target platforms, then I have no further objections, unless any reviewer is unhappy with the code for some other reason.

I'd like to point out that `zn_poly` has grown substantially since this release. There have been several releases (see http://math.harvard.edu/~dmharvey/zn_poly), all of which have been used in 'real life' by both myself and Andrew Sutherland on a variety of systems. As soon as this spkg is regularly shipped with Sage, I'll be providing constant updated spkgs for each new release. I'm going slow at the moment with the spkgs since this is the first spkg I have made.


---

Comment by jbmohler created at 2008-03-18 15:44:58

Builds, tunes, and installs fine for me with Gentoo on Intel P4 and Intel T2060.


---

Comment by mabshoff created at 2008-03-18 20:37:35

Hi David, 

it looks like the time is right now to include this spkg in Sage. My understanding is that we also need this for #1568. So I can you start a thread on sage-devel that requests a vote for inclusion? You should do that by describing what the spkg does, how large it is and what the benefits are. I am sure it will be included, but that is the process we decided upon and I am sure you saw the SQLAlchemy vote a couple days ago.

I will test this spkg and review its layout for conformance later today.

Cheers,

Michael


---

Comment by mabshoff created at 2008-03-20 02:22:26

The vote to get this spkg in is at

https://groups.google.com/group/sage-devel/t/7a1b4a6979555524

Since everybody voted to get it in and about 24 hours have elapsed I am considering this spkg voted in.

Cheers,

Michael


---

Comment by mabshoff created at 2008-03-20 02:51:22

I posted a slightly updated spkg at

http://sage.math.washington.edu/home/mabshoff/release-cycles-2.11/alpha0/zn_poly-0.4.1.p0.spkg

Cheers,

Michael


---

Comment by mabshoff created at 2008-03-20 02:52:10

Resolution: fixed


---

Comment by mabshoff created at 2008-03-20 02:52:10

Merged in Sage 2.11.alpha0


---

Comment by mabshoff created at 2008-03-20 04:25:15

Oh yeah, positive review obviously :)

Cheers,

Michael
