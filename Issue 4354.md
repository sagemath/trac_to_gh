# Issue 4354: loading a file with spaces in the filename doesn't work

Issue created by migration from https://trac.sagemath.org/ticket/4354

Original creator: anakha

Original creation time: 2008-10-24 00:41:49

Assignee: tbd

try it at home:


```
$ echo 'print "ok"' > 'test file.sage'
$ sage "test file.sage"
```



---

Comment by anakha created at 2008-10-24 00:42:54

Changing assignee from tbd to anakha.


---

Comment by anakha created at 2008-10-24 00:42:54

Crap, I need to relax on the submit button


---

Comment by anakha created at 2008-10-24 00:42:54

Changing component from algebra to misc.


---

Attachment

With the above patch and replacement sage script the example given should work and print 'ok'.

Be aware that if you copied the sage script somewhere (like /usr/local/bin) for convenience you need to modify that copy too.  The line near the end that reads 

```
"$SAGE_ROOT/local/bin/sage-sage" $*
```

needs to be replaced by

```
"$SAGE_ROOT/local/bin/sage-sage" "$@"
```



---

Comment by mvngu created at 2008-10-27 12:35:07

For the patch *sage*, below are some possible fixes to the documentation. Please also refer to #1389.



1.

```
-echo "You must compile SAGE first using 'make' in the SAGE root directory." >&2
+echo "You must compile Sage first using 'make' in the Sage root directory." >&2
```



2.

```
-echo "(If you have already compiled SAGE, you must set the SAGE_ROOT variable in "
+echo "(If you have already compiled Sage, you must set the SAGE_ROOT variable in "
```



3.

```
-# whenver SAGE exists.
+# whenever Sage exits.
```



---

Comment by was created at 2008-11-29 02:54:32

REFEREE:

Can you please rebase this against 3.2.1.alpha*?  I tried applying and got some many failed hunks I can't go further.

```
sage: hg_scripts.apply('http://trac.sagemath.org/sage_trac/attachment/ticket/4354/trac_4354.patch')
Attempting to load remote file: http://trac.sagemath.org/sage_trac/attachment/ticket/4354/trac_4354.patch?format=raw
Loading: [..]
cd "/Users/wstein/sage/local/bin" && hg status
cd "/Users/wstein/sage/local/bin" && hg status
cd "/Users/wstein/sage/local/bin" && hg import   "/Users/wstein/.sage/temp/teragon_2.local/1537/tmp_0.patch"
applying /Users/wstein/.sage/temp/teragon_2.local/1537/tmp_0.patch
patching file sage-sage
Hunk #5 succeeded at 227 with fuzz 1 (offset 4 lines).
Hunk #6 succeeded at 246 with fuzz 1 (offset 4 lines).
Hunk #7 FAILED at 332
Hunk #8 FAILED at 376
Hunk #10 succeeded at 474 with fuzz 1 (offset 41 lines).
Hunk #12 succeeded at 507 with fuzz 1 (offset 41 lines).
Hunk #18 succeeded at 603 with fuzz 1 (offset 41 lines).
Hunk #20 succeeded at 647 with fuzz 1 (offset 41 lines).
Hunk #27 FAILED at 768
Hunk #28 FAILED at 794
4 out of 28 hunks FAILED -- saving rejects to file sage-sage.rej
abort: patch failed to apply
```


Note -- I did *read* the patch and I think it's very good.  Also, I'm very glad for Mvngu's observations about all those typos, especially line -2 of SAGE_ROOT/sage.  Can you fix those typos in sage too?


---

Comment by was created at 2008-11-29 07:16:58

From patch author:

```
I'm kind of overloaded with work from school now, so it will have to
wait about 2 or 3 weeks.  If nobody does it before then, I'll do it.
```



---

Attachment


---

Comment by abergeron created at 2008-12-24 04:40:33

Changing assignee from anakha to abergeron.


---

Comment by abergeron created at 2008-12-24 04:40:33

I'm back in buisness!

trac_4354.2.patch is a rebase against 3.2.2

sage.2 is the sage startup script with the doc changes proposed by mvngu.


---

Comment by GeorgSWeber created at 2008-12-29 21:16:21

Target time for the review: January 13th


---

Comment by GeorgSWeber created at 2009-01-15 21:41:29

Rescheduled for January 18th


---

Comment by GeorgSWeber created at 2009-01-19 00:15:50

Unfortunately, this patch no longer applies cleanly against Sage 3.2.3.
It is obvious how to rebase it, though (sigh).


---

Attachment

Rebase against 3.3.alpha1


---

Comment by abergeron created at 2009-01-24 02:48:37

Changing status from new to assigned.


---

Attachment

rebase against 3.3.rc0 (you'll need also to put "sage.2" as "sage" into $SAGE_ROOT )


---

Comment by GeorgSWeber created at 2009-02-14 21:53:01

Well, this time "sage-run" had changed in between 3.3.alpha0 and 3.3.rc0.

I carefully hand-edited the 3.3.alpha0 patch (which did apply to 3.3.rc0 "sage-sage" only, but no longer to "sage-run") to reflect these changes, so the HG changeset header with the credit stayed the same.

The resulting patch now applies cleanly against 3.3.rc0.


---

Comment by GeorgSWeber created at 2009-02-14 22:07:05

Hello Michael,

this should go in 3.3 now. Of the handful files above, you'll need two:

A) The third one "sage.2" to go directly (no repo!!) right under $SAGE_ROOT as "sage" to replace the older script of the same name there. Mind the usual file executable flag issues ;-)

B) The last one "trac_4354_rebase_3.3.rc0.patch" applies as a HG patch to /local/bin (Sage scripts) repo.

Then test (as the original ticket comment says) from the bash command line (say after "your_favourite_path_to/sage -sh"):

```
$ echo 'print "ok"' > 'test file.sage'
$ sage "test file.sage"
```


(This can hardly be a doctest, it's just outside scope --- and IMHO the issue of testing this kind of environmental stuff should not burden this ticket here, although it is a valid question.)


---

Comment by mabshoff created at 2009-02-15 14:05:16

Resolution: fixed


---

Comment by mabshoff created at 2009-02-15 14:05:16

Merged sage.2 and trac_4354_rebase_3.3.rc0.patch in Sage 3.3.rc1.

I double checked both patches and I am confident they do the right thing.

Cheers,

Michael
