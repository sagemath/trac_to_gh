# Issue 5271: clean up jmol-11.6.16.spkg from #2873

Issue created by migration from https://trac.sagemath.org/ticket/5271

Original creator: mabshoff

Original creation time: 2009-02-14 14:30:46

Assignee: mabshoff

CC:  jason

jmol-11.6.16.spkg from #2873 was *not* based on the latest upstream jmol.spkg. While taking a closer look I found all kind of other odd things, so I moved the updated spkg to a new ticker. The spkg can be found at 

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.3/rc1/jmol-11.6.16.p0.spkg

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-14 14:30:56

Changing status from new to assigned.


---

Comment by mhansen created at 2009-02-14 15:07:08

Looks good to me.


---

Comment by mabshoff created at 2009-02-14 15:16:14

Resolution: fixed


---

Comment by mabshoff created at 2009-02-14 15:16:14

Merged in Sage 3.3.rc1.

Cheers,

Michael


---

Comment by jason created at 2009-02-15 05:09:09

I based my changes on the jmol spkg that was sitting in my 3.3alpha3 tree, so I'm surprised it wasn't the latest.  Anyways, thanks for noticing this and taking care of it!


---

Comment by mabshoff created at 2009-02-15 06:15:13

Replying to [comment:4 jason]:
> I based my changes on the jmol spkg that was sitting in my 3.3alpha3 tree, so I'm surprised it wasn't the latest.  Anyways, thanks for noticing this and taking care of it!

Well, it was well worth the update of jmol, I was just not happy at that point that I had to resolve what had happened. Note that the faulty .hgignore that lead to many files being ignored by hg was my fault, but I still do not understand how that happened since I assumed that there was just one directory to be ignore. Anyway, this spkg is much cleaner, conforms with the standard packaging rules, i.e. bits in src. Note that I also blame the reviewed for not catching it, too, since I expect reviewers of spkgs to verify in the repo that the history is not partially truncated. But I do it with *every* spkg anyway :)

Cheers,

Michael
