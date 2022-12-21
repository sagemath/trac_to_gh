# Issue 48: spkg-install for singular

Issue created by migration from Trac.

Original creator: anonymous

Original creation time: 2006-09-13 09:28:23

Assignee: somebody

On Tue, 12 Sep 2006 17:32:37 -0700, Rob Gross <gross`@`bc.edu> wrote:
 
I finally found my error, by deleting every alias and environment
variable in turn and seeing if I could then build sage successfully
from scratch.  I'm still not sure why defining the environment
variable TMPDIR as /tmp caused a problem, but it did.  TMPDIR defaults
to /tmp anyway, according to "man ar" which is why I'm a bit confused
why it caused a problem.
 
I can't remember why I had bothered to define TMPDIR in the first
place, but there must have been some other build at some other time
that needed it to be defined.
 
Thanks for all of your help.  I suppose that adding a check to make
sure that no one else commits this particular act of stupidity might
be a good idea, but it's impossible to guess at all of the potential
things that could go wrong.--Rob
 
I can put "unset TMPDIR" in the spkg-install file for singular.  I'm
really glad you tracked this down precisely!
 
William


---

Comment by was created at 2007-01-13 02:10:56

put into singular-3-0-2-20070105 (version on 0112)


---

Comment by was created at 2007-01-13 02:10:56

Resolution: fixed


---

Comment by jdemeyer created at 2012-07-25 17:04:15

Changing component from basic arithmetic to packages.
