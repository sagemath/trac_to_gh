# Issue 1789: standalone Sage scripts don't work on Linux -- they work fine on OS X

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-01-15 23:42:31

Assignee: was


```
Hi Robert,

    1. Is this a clean, from-source build of sage-2.9.3?


Yes, i tried it out on two different systems now, Athlon XP, and Core Duo, both running on Debian Etch, and both show the same behaviour

    2. What is the output of /usr/bin/env for you? Mine (Intel OS X
    10.5.1) doesn't mention sage at all, although mysteriously things are
    working for me.


the  SAGE_ROOT directory is included in my path, i even defined a global variable with this name, i.e.  SAGE_ROOT.
 

    > #!/usr/bin/env sage -python
    > import sys

    For me, I get
    $ ./BMV.sage
    $


you response encouraged me to try out some more things, and if i change the first line to

#!/usr/bin/env sage-python
instead of

#!/usr/bin/env sage -python
(note that there is no space anymore) things work as excepted (at least import sys and print "Hello World"), seems like my /usr/bin/env does not like the space between (#!/usr/bin/env "sage -python" does not work either)

but however, using

#!/path/to/sage_root/sage-python
import sys

still does not work and shows the same strange "mouse behaviour" as described in my original posting, on both systems!!
no idea why the second one does not work on my systems!!


    However, when I run the sage itself, it looks like it's pointing at
    some weird version:
    $ /usr/bin/env sage
    ----------------------------------------------------------------------
    | SAGE Version 2.9.2, Release Date: 2008-01-05                       |
    | Type notebook() for the GUI, and license() for information.        |
    ----------------------------------------------------------------------
    Loading SAGE library. Current Mercurial branch is: demo


$/usr/bin/env sage

brings me to the sage prompt as expected

    Hopefully this helps, although I have a feeling this thread isn't
    over... 


Anyway, at least i found a partial solution to carry on with, but it seems as there are still some things to clarify, especially the mouse thing concerning the import sys

Thank you very much,
Georg
```





---

Comment by was created at 2008-01-19 13:57:02

fixes the examples and docs in the examples/programming/scripts to avoid a lot of confusion, e.g., so they work on both os x and linux instead of just os x.


---

Attachment

I've posted a patch that gets applied in the SAGE_ROOT/examples directory.


---

Comment by ncalexan created at 2008-01-19 19:12:38

This seems like a reasonable change to make.  The situation is tricky and it appears that the best thing to be done is to document how it can be made to work.


---

Comment by mabshoff created at 2008-01-19 20:02:56

Resolution: fixed


---

Comment by mabshoff created at 2008-01-19 20:02:56

Merged in Sage 2.10.1.alpha0
