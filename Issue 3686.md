# Issue 3686: trivial problems in extcode.spkg

Issue created by migration from Trac.

Original creator: tabbott

Original creation time: 2008-07-21 05:44:51

Assignee: mabshoff

Below is a list trivial problems in the excode spkg that were found by Debian's automatic package quality checking tools:

# Scripts missing #!/bin/sh lines in extcode-3.0.5.spkg:
mirror
pari/dokchitser/testall
spkg-dist

# Files unnecessarily marked as executable in extcode-3.0.5.spkg
javascript/jsmath/plugins/autoload.js
javascript/jsmath/plugins/CHMmode.js
notebook/javascript/jsmath/plugins/autoload.js
notebook/javascript/jsmath/plugins/CHMmode.js
notebook/javascript/farbtastic/marker.png

# Empty directories in extcode-3.0.5.spkg
# (These look like they might have a purpose, but I'm not sure)
dist/
gap/user/
genus2reduction/
gnuplot/
macaulay2/user/
maple/user/
mathematica/user/
matlab/user/
octave/user/
sage/user/
singular/user/
sobj/



---

Comment by tabbott created at 2008-07-21 05:51:42

Let's display that readably:

# Scripts missing #!/bin/sh lines in extcode-3.0.5.spkg:

```
mirror
pari/dokchitser/testall
spkg-dist
```


# Files unnecessarily marked as executable in extcode-3.0.5.spkg

```
javascript/jsmath/plugins/autoload.js
javascript/jsmath/plugins/CHMmode.js
notebook/javascript/jsmath/plugins/autoload.js
notebook/javascript/jsmath/plugins/CHMmode.js
notebook/javascript/farbtastic/marker.png
```


# Empty directories in extcode-3.0.5.spkg
# (These look like they might have a purpose, but I'm not sure)

```
dist/
gap/user/
genus2reduction/
gnuplot/
macaulay2/user/
maple/user/
mathematica/user/
matlab/user/
octave/user/
sage/user/
singular/user/
sobj/
```



---

Attachment

The Debian people made me fix all these problems myself, so I've attached patches to fix the #! lines to each of these tickets.  You'll have to remove the executable bits yourself, since I seem to recall mercurial doesn't support that.

By the way, the empty directories in the extcode spkg are for the Sage pexpect wrapper, and can't be deleted.  The others can.


---

Comment by tabbott created at 2009-04-26 05:31:34

As well as applying the attached patch, one should run

```
chmod -x notebook/javascript/farbtastic/marker.png javascript/jsmath/plugins/CHMmode.js 
chmod -x javascript/jsmath/plugins/autoload.js notebook/javascript/jsmath/plugins/CHMmode.js 
chmod -x javascript/jsmath/plugins/CHMmode.js
```

from the root of the extcode spkg in order to close this ticket.


---

Comment by awebb created at 2009-07-21 16:26:27

notebook/javascript/jsmath/plugins/CHMmode.js does not seem to exist in extcode-4.1 otherwise the rest seems OK.


---

Comment by awebb created at 2009-07-22 06:00:58

I applied the patch and ran the chmod commands as suggested above. Ignoring the change in one file, everything else worked. 

Note: I applied #3686, #3687, #3688 and #3689 at the same time as my machine is a bit slow (8800 s to run all tests). I changed the packages, did a full build from source and ran 'make testlong'. Everything built and all tests passed. This is with Sage-4.1.


---

Comment by mvngu created at 2009-07-23 09:52:11

Resolution: fixed
