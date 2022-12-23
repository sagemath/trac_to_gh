# Issue 634: Implement "sage -experimental" analog to "sage -optional"

Issue created by migration from https://trac.sagemath.org/ticket/634

Original creator: mabshoff

Original creation time: 2007-09-10 04:06:28

Assignee: mabshoff

Titel says it all.

Cheers,

Michael


---

Comment by mabshoff created at 2007-09-10 04:06:35

Changing status from new to assigned.


---

Comment by was created at 2007-09-10 22:29:04

To do this:

 1. Rename local/bin/sage-list-optional to something like local/bin/sage-list-packages, and change it slightly (change the word "optional" to sys.argv[1])

 2. Make sage-list-optional just be the 2-line program
          sage-list-packages optional

 3. Then sage -experimental and sage -standard are both very easy.  Also implement standard_packages() and experimental_packages() as saag functions, kind of like optional_packages() right now.


---

Comment by mabshoff created at 2007-09-13 03:45:17

Well, I haven't done the above, but at

http://fsmath.mathematik.uni-dortmund.de/~mabshoff/patches/sage-2.8.4.1-add_-experimental_flag.patch

you can find the version that does code duplication for now.

Cheers,

Michael


---

Comment by was created at 2007-09-13 05:02:50

I've merged the above in for sage-2.8.4.2.  For sage-2.9 you could remove the code duplication.


---

Comment by mabshoff created at 2007-09-15 12:30:58

Okay, here is the code merge for the sage scripts:

http://fsmath.mathematik.uni-dortmund.de/~mabshoff/patches/Sage-2.8.4.2-add_-standard-option-to-sage-sage.patch
http://fsmath.mathematik.uni-dortmund.de/~mabshoff/patches/Sage-2.8.4.2-factor-out-package-listing-code.patch

Now 3) is left. I will do that probably later today.

Cheers,

Michael


---

Comment by was created at 2007-09-15 20:24:34

Resolution: fixed


---

Comment by was created at 2007-09-15 20:29:47

Resolution changed from fixed to 


---

Comment by was created at 2007-09-15 20:29:47

Changing status from closed to reopened.


---

Comment by mabshoff created at 2007-09-15 22:31:17

And the python bit of the bugfix:

http://fsmath.mathematik.uni-dortmund.de/~mabshoff/patches/Sage-2.8.4.2-import-experimental-and-standard-in-all.py.patch
http://fsmath.mathematik.uni-dortmund.de/~mabshoff/patches/Sage-2.8.4.2-add-experimental-and-standard-to-package.py.patch

Cheers,

Michael


---

Comment by was created at 2007-09-15 22:44:59

Resolution: fixed
