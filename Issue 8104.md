# Issue 8104: developer's guide for making spkgs should specify that patches need to be version controlled

Issue created by migration from Trac.

Original creator: ddrake

Original creation time: 2010-01-28 03:57:55

Assignee: mvngu

CC:  mvngu

When working on a spkg and adding or modifying patches, the developers' guide (http://www.sagemath.org/doc/developer/producing_spkgs.html) should remind developers to version-control the patches.


```
19:38 < gsmcwhirter> if some or all of the existing patches no
  longer apply, should they be left there or deleted? (on networkx, 
  there was an edit to a file to switch from numerix to numpy, but 
  the latest upstream source uses numpy by default)
19:39 < ddrake> I'd delete obsolete patches, and mention that you 
  did so in SPKG.txt.
19:48 < ddrake> also note that the patches/ directory is version 
  controlled, so make sure you 'hg add' new patches and 'hg rm' 
  unneeded ones.
19:51 < mvngu> ddrake: That looks like a sensible thing to do. But 
  it's not documented at http://www.sagemath.org/doc/developer
  /producing_spkgs.html. 
19:51 < mvngu> ddrake: Could you open a ticket for this and CC me 
  on it?
19:51 < ddrake> sure. 
19:52 < ddrake> the documentation you just linked to does say "Make 
  sure that the hg repo contains every file outside the src 
  directory, and that these are all up-to-date and commited into 
  the repo."
19:52 < ddrake> but perhaps patches bear a special mention, just to 
  make it clear. I'll open the ticket.
```



---

Comment by mvngu created at 2010-02-09 12:12:36

A patch addressing this issue is up at #8079.


---

Comment by mvngu created at 2010-02-14 14:38:33

Resolution: fixed


---

Comment by mvngu created at 2010-02-14 14:38:33

Close as fixed by #8079.
