# Issue 490: gcc 4.3: fix gmp.h problem with "using std::FILE"

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2007-08-25 23:13:13

Assignee: was

Hello,

not to be surprised by a new gcc version I have started building gcc 4.3 snapshots (20070824 in this particular case) and compile Sage with them. Here is a problem with gmp.h

Givaro's gmp test fails:

```
g++ -I ../../../../local/include/ -L ../../../../local/lib/ -l gmp  gcc-test.cpp -o gcc-test
In file included from gcc-test.cpp:1:
../../../../local/include/gmp.h:515: error: ‘std::FILE’ has not been declared
```

Uncommenting "std::FILE" fixes the problem.

```
#if defined (__cplusplus)
extern "C" {
//using std::FILE;
#endif
```



---

Comment by mabshoff created at 2007-08-25 23:16:52

Changing assignee from was to mabshoff.


---

Comment by mabshoff created at 2007-08-25 23:17:00

Changing status from new to assigned.


---

Comment by mabshoff created at 2007-08-26 12:49:24

Another suggestion for a fix has been made by Patrick Pelissier:

```
#if defined (__cplusplus)
extern "C" {
#ifdef _GMP_H_HAVE_FILE
using std::FILE;
#endif
#endif
```

I am waiting up what the gmp gods will decide an report back


---

Comment by mabshoff created at 2007-09-06 14:16:18

This fix (in a modified form has been merged in gcc 4.2.2rc3). So rebasing out spkg against the 4.2.2 release will fix the problem.

Cheers,

Michael


---

Comment by mabshoff created at 2007-09-12 14:57:13

Once #542 is done this ticket can be closed, because gmp 4.2.2. has solved the issue.

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-15 10:53:59

Well, I fixed this in some other way via #2929.

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-15 10:53:59

Resolution: fixed


---

Comment by leif created at 2012-07-28 13:35:58

See #12661 for upgrading the optional GMP spkg to a more recent (5.x) version.
