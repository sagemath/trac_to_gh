# Issue 4040: Update biopython optional package to 1.47

Issue created by migration from Trac.

Original creator: mhampton

Original creation time: 2008-09-02 20:32:45

Assignee: mabshoff

Keywords: biopython, optional packages

Just keeping this package up to date.  Actually 1.48 will be out pretty soon.


---

Comment by mhampton created at 2008-09-02 20:34:50

First attempt is up at:

http://www.d.umn.edu/~mhampton/biopython-1.47.spkg


---

Comment by mabshoff created at 2008-09-04 02:45:54

I fixed a bunch of issues: 

 * put the repo back in. *Never* remove the hg repo in an spkg.
 * put back "exit 1" in case either one of the python modules fails to build
 * moved setup.py into patches where it belongs
 * checked in all the changes
 * removed OSX crap files, i.e. `._*`

With those changes I give this spkg at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.1.2/rc0/biopython-1.47.spkg

a positive review. Please base future spkgs on this one since I did not increment the patch level.

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-04 02:48:07

Resolution: fixed


---

Comment by mabshoff created at 2008-09-04 02:48:07

Merged into the optional repo in Sage 3.1.2.rc0.
