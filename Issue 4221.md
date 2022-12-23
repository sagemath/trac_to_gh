# Issue 4221: [with package, needs review] pynac package

Issue created by migration from https://trac.sagemath.org/ticket/4221

Original creator: burcin

Original creation time: 2008-09-30 12:34:07

Assignee: burcin

Keywords: symbolics, pynac

To split the task of testing the new pynac package and the interface code from #3872, the new version of the pynac package is moved here.

Latest version of the package can be downloaded from:

http://www.risc.jku.at/people/berocal/sage/pynac-0.1.p0.spkg


---

Comment by mabshoff created at 2008-09-30 12:55:08

Build tested on 

 * OSX 10.4, 10.5
 * Linux x86, x86-64, Itanium 
 * Solaris x86

In total I ran 10 builds including all SkyNet machines. That obviously does not mean it actually works as intended, but the spkg passes the required build tests. Positive review.

Burcin's spkg with some small SPKG.txt cleanups can be found at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.1.3/alpha2/pynac-0.1.p0.spkg


Cheers,

Michael


---

Comment by mabshoff created at 2008-09-30 12:55:08

Resolution: fixed


---

Comment by mabshoff created at 2008-09-30 12:56:44

Merged in Sage 3.1.3.alpha2
