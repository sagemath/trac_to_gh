# Issue 1279: LLL on "tall" matrices immediately crashes sage

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-11-26 08:38:20

Assignee: was

If you create an n x m matrix over ZZ in sage with n > m, then 
run the LLL algorithm on it (fplll), Sage completely terminates.


```
sage: A = random_matrix(ZZ, 15, 10)
sage: A.LLL()
Ill-formed matrix  : d>n
bsd:~ was$ 
```


Possible Solutions:
  1. trap bad conditions somewhere and raise an exception.

  2. Just immediately give an error in the A.LLL function if A is nonsquare (instead of letting fplll do this
 
  3. Put an error in the fplll wrapper code in libs/fplll


---

Comment by malb created at 2007-11-26 09:59:53

Changing assignee from was to malb.


---

Comment by malb created at 2007-11-26 09:59:53

Changing status from new to assigned.


---

Comment by malb created at 2007-11-27 18:08:30

A new spkg is available at which replaces the `exit(1)` call with an `abort()` call which we can and do trap.

http://sage.math.washington.edu/home/malb/pkgs/libfplll-2.1.4-20071127.spkg

Still, we should check for nr>nc ourselves to present a more userfriendly exception rather than a RuntimeError


---

Attachment


---

Comment by was created at 2007-11-27 22:50:26

Looks good ready to include.


---

Comment by malb created at 2007-11-28 10:11:04

Do not apply this patch as is:

Damien Stehle wrote via e-mail:


```
I did not apply your patch for d>n, which is not invalid
(though it was said to be in proved.cpp). If there are linear
dependencies, LLL will just find them and output zero vectors before a
LLL-reduced basis of the input lattice.
```


the new fplll is available at

http://sage.math.washington.edu/home/malb/pkgs/fplll-2.1.5.tgz


---

Comment by malb created at 2007-11-28 12:48:45

Damien replaced all `exit` calls with `quit` calls. However, neither I nor `man` knows about any `quit` system call and thus 2.1.5 doesn't build at least on my machine.


---

Comment by malb created at 2007-11-29 10:19:01

A new spkg is available at 

http://sage.math.washington.edu/home/malb/pkgs/libfplll-2.1.6-20071129.spkg

which fixes this issue for me. Don't forget to touch `fplll.pyx` and `sage -b` after installing that package.


---

Comment by cwitty created at 2007-12-01 02:47:31

I installed the new spkg (on 32-bit x86 Linux).  The test in the bug report no longer crashes, and doctests in fplll.pyx and matrix_integer_dense.pyx still pass.

I did not apply the attached patch, and I don't think we should apply it... as Damien points out, that case is not actually invalid.

In short, the spkg looks good to me.


---

Comment by mabshoff created at 2007-12-01 18:12:00

Merged in 2.8.15.alpha1.


---

Comment by mabshoff created at 2007-12-01 18:12:00

Resolution: fixed


---

Comment by mabshoff created at 2007-12-01 19:49:13

To make it crystal clear: The spkg was merged, the patch was backed out after Carl reminded me :)

Michael
