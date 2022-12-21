# Issue 5311: Update to ATLAS 3.8.3 (latest upstream release)

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2009-02-19 05:16:09

Assignee: mabshoff

Clint writes:

```
I have released 3.8.3.  This is, of course, mainly a bugfix release.
However, I have also backported some assembly kernels from the 3.9 series
for the Core2 and AMD64K10h architectures.  We have architectural defaults
for these systems, as well as the new Corei7 (64 bit only).  For Core2-based
systems, the speedup is substantial (K10h speedup is modest).

You should also be aware of one error, *which has not been fixed in 3.8.3*
  http://math-atlas.sourceforge.net/errata.html#scal0

Cheers,
Clint
```



---

Comment by mabshoff created at 2009-02-20 20:22:45

The spkg at

 http://sage.math.washington.edu/home/mabshoff/release-cycles-3.3/rc3/atlas-3.8.3.spkg

updates to ATLAS 3.8.3. The following patches were rebased/changed:

 * archinfo_linux.c - only the Itanium hunk is needed
 * archinfo_x86.c - only case 6 PIV hunk is needed
 * Make.top - identical 
 * probe_comp.c - needs to be rebased to account for SiCortex fix

Other than that the Core i7 support works, it identifies the Itanium2 boxen on SkyNet correctly (vanilla ATLAS doesn't) and this spkg also fixes #1641.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-20 20:22:45

Changing status from new to assigned.


---

Comment by ghtdak created at 2009-02-20 20:56:06

Happily installs and runs on 3.3.alpha4 (what I had laying around on the i7 box).  

Other comments recommended by mabshoff: 

(12:51:46 PM) mabs: Well, it is a very clean spkg with 3 beautiful commits.

(12:52:06 PM) mabs: This is the best spkg ever. Michael needs to get a gold star :)

(12:52:41 PM) mabs: I tested it widely, so it will work :)

seems about right


---

Comment by mabshoff created at 2009-02-20 20:58:55

Resolution: fixed


---

Comment by mabshoff created at 2009-02-20 20:58:55

Merged in Sage 3.3.rc3.

Cheers,

Michael
