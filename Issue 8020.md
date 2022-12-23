# Issue 8020: python-2.6.4.p4 spkg *totally breaks* itanium support

Issue created by migration from https://trac.sagemath.org/ticket/8020

Original creator: was

Original creation time: 2010-01-21 02:18:07

Assignee: tbd


```
gcc version 4.4.2 (GCC)
****************************************************
Updating readline.c for Linux/Itanium
cp: cannot create regular file `Modules/readline.c': No such file or directory
Error copying patched readline.c

real    0m0.029s
user    0m0.009s
sys     0m0.011s
sage: An error occurred while installing python-2.6.4.p4
Please email sage-devel http://groups.google.com/group/sage-devel
explaining the problem and send the relevant part of
of /home/wstein/screen/cleo/sage-4.3.1/install.log.  Describe your c
```


I missed this doing the release, because our Itaniums weren't accessible.


---

Comment by was created at 2010-01-21 02:25:37

This appears to be trivial to fix.  In spkg-install change:

```
# The following patch for fixing broken readline behavior on Itanium
# Linux definitely does *not* work on anything else.
if [ "`uname -m`" = "ia64" -a "`uname`" = "Linux" ]; then
    echo "Updating readline.c for Linux/Itanium"
    cp patches/readline.c-Itanium-fix Modules/readline.c
}}}   

to

{{{
# The following patch for fixing broken readline behavior on Itanium
# Linux definitely does *not* work on anything else.
if [ "`uname -m`" = "ia64" -a "`uname`" = "Linux" ]; then
    echo "Updating readline.c for Linux/Itanium"
    cp patches/readline.c-Itanium-fix src/Modules/readline.c
}}}


---

Comment by was created at 2010-01-21 02:31:02

Changing status from new to needs_review.


---

Comment by was created at 2010-01-21 02:31:02

Here's the new spkg:

   http://sage.math.washington.edu/home/wstein/patches/python-2.6.4.p5.spkg


---

Comment by craigcitro created at 2010-01-21 03:46:58

Changing status from needs_review to positive_review.


---

Comment by craigcitro created at 2010-01-21 03:46:58

Oops ... yep, that was totally a typo on my part while moving things around in the file. Sorry about that ... fix is obviously the right one.


---

Comment by mvngu created at 2010-01-24 22:29:02

Resolution: fixed


---

Comment by mvngu created at 2010-01-24 22:29:02

William's commit message references ticket #8080, which at present doesn't exist. I've changed the ticket number in his commit message to #8020. For reference, my change (to William's commit message) can be found at

http://sage.math.washington.edu/home/mvngu/spkg/standard/python/python-2.6.4.p5.spkg

Merged [python-2.6.4.p5.spkg](http://sage.math.washington.edu/home/mvngu/spkg/standard/python/python-2.6.4.p5.spkg) in the standard spkg repository.
