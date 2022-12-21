# Issue 9103: ATLAS  has modifications to upstream source

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2010-05-31 11:22:31

Assignee: AlexGhitza

I believe the ATLAS package has modifications to the upstream source code, as some files in the 'patches' subdirectory are identical to those in the original source code directory. 

Furthermore, ATLAS was apparently updated to the latest upstream source code on February 20th, 2009 (that's what SPKG.txt says), but some of the files in the 'src' directory have modification dates of June 22nd 2009 - some 4 months later. 

I don't know for sure who is guilty here, but I've suspicion it might be me, as 'hg log' shows:


```
changeset:   53:41de1efe8559
user:        Robert Miller <rlm`@`rlmiller.org>
date:        Thu Jul 02 14:13:54 2009 -0700
summary:     Checked in drkirkby's changes

changeset:   52:3acaaff52099
user:        William Stein <wstein`@`gmail.com>
date:        Tue Jun 02 14:30:03 2009 -0700
summary:     fix FAT binary building so only impacts x86 boxes (e.g. not itanium!)
```


So it looks like I probably screwed up, and Robert did not notice and checked in my changes.  


---

Comment by AlexGhitza created at 2010-09-02 11:00:34

Changing assignee from AlexGhitza to tbd.


---

Comment by AlexGhitza created at 2010-09-02 11:00:34

Changing component from algebra to packages.


---

Comment by jdemeyer created at 2013-05-24 12:20:38

Should be fixed by #10508.


---

Comment by jdemeyer created at 2013-05-24 12:20:38

Resolution: invalid
