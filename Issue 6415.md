# Issue 6415: "sage -t foo.pyx" should not by default dynamically build foo.so

Issue created by migration from Trac.

Original creator: GeorgSWeber

Original creation time: 2009-06-25 21:28:29

Assignee: tbd

Recently (during Sage Days 12 ?!) the doctesting code was changed so that "sage -t" on a certain class of *.pyx files now is broken.
Especially, they now get not only copied to some temp directory, but it is attempted to build dynamically the *.so extension out of them, as if they were all files to be loaded/attached.
This almost certainly must fail, if e.g. you have installed a package under $SAGE_ROOT/local/lib/python/site-packages/, with Cython extensions, building which needs certain libraries, additional C sources, special compiler flags, and so on.
(And where one "imports" the functionality, not loads/attaches it.)

Previously, doctesting was very well suited to this situation, but is no more.

So the current (Sage 4.0.2) doctesting code should be enhanced in e.g. one of the following ways:

1) If "dynamically building" of an extension fails, just "try" to import the functionality as a fallback (in other words: use a prebuilt *.so if one exists, and you can't build a fresh one)

2) Change to the old behaviour, and additionally try build dynamically an extension only if it is missing and/or seems to be outdated compared to the *.pyx file

3) Use the old/new behaviour depending on whether ".../site-packages/..." is in the path of the *.pyx-file, or not.

At the core of these problems of course is the fact that there is no standard way to store the build information (not to talk of the "full" dependency information) for a Cython source file.
The Sage project e.g. invented its own custom-made monolithic "module_list.py" on the one hand, its custom-made #clib, #cinclude, ... pragmas on the other hand, but all this does not at all work smoothly together.
Let alone being usable in Sage-related Cython projects which address a broader audience, and are thus placed under .../site-packages/.


---

Comment by Stefan created at 2011-05-24 09:42:43

I ran into this today, but it seems that the -force_lib option solves the issue (it did for me, at least). Am I right?


---

Comment by GeorgSWeber created at 2011-05-25 20:17:36

Changing type from defect to enhancement.


---

Comment by GeorgSWeber created at 2011-05-25 20:17:36

Changing priority from major to minor.


---

Comment by GeorgSWeber created at 2011-05-25 20:17:36

Hi Stefan,
good catch! Yes, I do think the issue of this ticket currently is solvable this way, i.e. alternative 1) of the description is actually (May 2011) implemented halfways.

(No automatism yet, but there's this additional command-line option to forcefully use already existing prebuilt "Python extension" .so-files).

If this ticket bit-rots another two years, it should be closed as "Won't Fix".

Cheers,
Georg


---

Comment by GeorgSWeber created at 2011-05-25 20:17:36

Changing assignee from tbd to GeorgSWeber.


---

Comment by roed created at 2013-03-14 21:59:50

Well, it's been almost another two years.  ;-)

What's the status of this ticket after #12415?  Are the problems still present?


---

Comment by roed created at 2013-03-28 23:18:04

Changing component from doctest to doctest framework.


---

Comment by roed created at 2013-03-28 23:27:00

Changing status from new to needs_review.


---

Comment by roed created at 2013-03-28 23:27:49

Changing status from needs_review to positive_review.


---

Comment by roed created at 2013-03-28 23:27:49

`sage -t foo.pyx` building the module is a feature not a bug.


---

Comment by jdemeyer created at 2013-03-29 19:01:41

Resolution: wontfix
