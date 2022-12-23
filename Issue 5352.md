# Issue 5352: the valgrind log files in sage-doctest are written to $HOME/.sage instead of $DOT_SAGE

Issue created by migration from https://trac.sagemath.org/ticket/5352

Original creator: mabshoff

Original creation time: 2009-02-23 22:37:41

Assignee: cwitty

CC:  mjo

Fix it so that the logs end up in DOT_SAGE since that does not have to be $HOME/.sage as hard coded for the log files.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-23 22:37:48

Changing status from new to assigned.


---

Comment by mabshoff created at 2009-02-23 22:37:48

Changing assignee from cwitty to mabshoff.


---

Comment by mabshoff created at 2009-03-01 02:27:36

Better luck in 3.4.1.

Cheers,

Michael


---

Comment by aapitzsch created at 2011-01-05 17:03:00

Changing status from new to needs_review.


---

Comment by rochelol2 created at 2011-02-08 10:33:42

Patch tested successfully on 4.6.1, however (beginner question) what is the correct procedure
for reviewing such an out of sage-library/ issue ?


---

Comment by burcin created at 2011-05-31 13:43:52

Replying to [comment:4 rochelol2]:
> Patch tested successfully on 4.6.1, however (beginner question) what is the correct procedure
> for reviewing such an out of sage-library/ issue ?

There is a repository, referred to as the script repository, in `$SAGE_LOCAL/bin`. The patch should apply cleanly to this repo, have proper mercurial headers, etc.

Attached patch does not fix all the problem places. The script `sage-valgrind` still refers to `$HOME/.sage`. Could you fix that and use "hg export" to create the patch?


---

Comment by burcin created at 2011-05-31 13:43:52

Changing status from needs_review to needs_work.


---

Attachment


---

Comment by aapitzsch created at 2011-06-02 15:36:15

Changing status from needs_work to needs_review.


---

Comment by mjo created at 2011-12-04 03:25:31

I think all of the affected scripts need to source sage-env for the default value of `$DOT_SAGE`. As is,


```
$ ./local/bin/sage-valgrind 
/local/bin/sage-ipython
mkdir: cannot create directory `/valgrind': Permission denied
```



---

Comment by mjo created at 2011-12-04 03:25:31

Changing status from needs_review to needs_work.


---

Comment by mjo created at 2011-12-04 17:47:55

Changing status from needs_work to needs_review.


---

Comment by mjo created at 2011-12-04 17:47:55

Replying to [comment:7 mjo]:
> I think all of the affected scripts need to source sage-env for the default value of `$DOT_SAGE`.

After RTFMing, I see that I shouldn't be running the script from bash anyway, so this criticism is invalid.


---

Comment by mjo created at 2011-12-05 04:58:49

I think this looks good. Here's how I tested:

 1. Install valgrind.
 2. Rebuild sage with SAGE_VALGRIND="yes".
 3. Create an empty suppressions file (Trac #11918)
 4. Remove my ~/.sage/valgrind
 5. Create and export DOT_SAGE=~/grind
 6. Execute,
  * sage -valgrind
  * sage -cachegrind
  * sage -callgrind
  * sage -massif
  * sage -tp 4 -long -valgrind devel/sage/sage (Killed this one prematurely since it was going to take a month)
 7. Tried to run sage -omega, but the exp-omega tool has been removed from recent versions of valgrind.
 8. Checked my ~/.sage and ~/grind directories to make sure all of the log files wound up in the right places.
 9. make ptestlong, no failures
 10. Grep for leftover '$HOME/.sage' instances in local/bin


---

Comment by mjo created at 2011-12-05 04:58:49

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2011-12-09 10:21:45

Resolution: fixed
