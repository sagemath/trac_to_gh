# Issue 8898: some files in sage-4.4.{0,1} have dos line ending instead of a unix line ending

Issue created by migration from https://trac.sagemath.org/ticket/8898

Original creator: fbissey

Original creation time: 2010-05-05 23:01:42

Assignee: AlexGhitza

CC:  fredrik.johansson

the following 4 files in the sage spkg have dos line ending rather than unix ones:
sage/libs/mpmath/ext_impl.pxd
sage/libs/mpmath/ext_main.pyx
sage/libs/mpmath/ext_main.pxd
sage/libs/mpmath/ext_libmp.pyx

I found about this while trying to build sage with python-2.6.5
which absolutely refused to parse these files as is.
Not sure how to submit a patch for line endings.


---

Comment by mvngu created at 2010-05-05 23:13:15

Some files under `sage/logic/` also have DOS line ending.


---

Comment by fbissey created at 2010-05-05 23:20:05

just checked sage/logic/booleval.py is actually in "mac format" in sage-4.4
I will check sage-4.4.1 later.
But those are pure python files, they may be ok but cython with
python-2.6.5 refused to deal with the other 4.


---

Comment by AlexGhitza created at 2010-09-02 09:31:16

Changing assignee from AlexGhitza to jason.


---

Comment by AlexGhitza created at 2010-09-02 09:31:16

Changing component from algebra to misc.


---

Comment by mvngu created at 2010-09-07 11:35:41

The attached patch converts the following files to use Unix line endings:

 * `sage/libs/mpmath/ext_impl.pxd`
 * `sage/libs/mpmath/ext_main.pyx`
 * `sage/libs/mpmath/ext_main.pxd`
 * `sage/libs/mpmath/ext_libmp.pyx`
 * `sage/logic/booleval.py`

I used the Perl script at

http://www.obviously.com/tech_tips/dos2unix.html

to convert to Unix end lines. Fredrik Johansson is a main developer of mpmath. I have CC'd him so he is aware of this Unix line endings issue.


---

Comment by mvngu created at 2010-09-07 11:35:41

Changing priority from minor to trivial.


---

Comment by mvngu created at 2010-09-07 11:35:41

Changing status from new to needs_review.


---

Comment by fbissey created at 2010-11-11 09:34:33

Changing status from needs_review to needs_work.


---

Comment by fbissey created at 2010-11-11 09:34:33

sage/libs/mpmath/ext_impl.pxd at least as been changed since this patch has been posted. It may need rebasing for all 4 files.


---

Attachment

update of the patch based on sage-4.6


---

Comment by fbissey created at 2010-11-11 09:50:32

Changing status from needs_work to needs_review.


---

Comment by fbissey created at 2010-11-11 09:50:32

OK - so I updated the patch (but could not delete the old one, I don't have the
right to do it).

This fairly trivial patch now needs a review.


---

Comment by cschwan created at 2010-11-11 10:38:05

I have tested the patch with python-2.6.6 and sage-on-gentoo - everything fine here.


---

Attachment

Here are some problems with [attachment:trac_8898-unix-endlines.2.patch]:

 * It fails to apply on Sage 4.6.1.alpha0; I got the following failure:
 {{{
[mvngu`@`sage sage-main]$ pwd
/dev/shm/mvngu/sage-4.6.1.alpha0/devel/sage-main
[mvngu`@`sage sage-main]$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/8898/trac_8898-unix-endlines.2.patch && hg qpush 
adding trac_8898-unix-endlines.2.patch to series file
applying trac_8898-unix-endlines.2.patch
patching file sage/libs/mpmath/ext_main.pyx
Hunk #1 FAILED at 0
1 out of 1 hunks FAILED -- saving rejects to file sage/libs/mpmath/ext_main.pyx.rej
patch failed, unable to continue (try -v)
patch failed, rejects left in working dir
errors during apply, please fix and refresh trac_8898-unix-endlines.2.patch
 }}}

 * The attachment [attachment:trac_8898-unix-endlines.2.patch] doesn't convert the file `sage/logic/booleval.py` to use Unix line ending.

My rebased patch should take care of the above issues for Sage 4.6.1.alpha0. See the ticket description for which patch to apply.


---

Comment by fbissey created at 2010-11-12 08:29:58

Sorry I missed sage/logic/booleval.py somehow. In any case this one is no bother
and is only included for consistency. It doesn't prevent building the way the other
do and it is usable. I also didn't see there was a change affecting this in 4.6.1.alpha0. I will test it shortly and report.


---

Comment by fbissey created at 2010-11-12 22:46:44

Changing status from needs_review to positive_review.


---

Comment by fbissey created at 2010-11-12 22:46:44

4.6.1.alpha0 took me for a little ride.
Anyway, Minh's new patch applies cleanly to 4.6.1.alpha0 and it compiles
cleanly with a python-2.6.5 install as expected. sage starts without problems.
For safety I also did a run of sage -t --long in the sage/libs/mpmath/ and
sage/logic/ and everything ran ok.

I am putting this back to positive review, hopefully no one messed up with those
files in alpha1 so it will apply cleanly there as well.


---

Comment by jdemeyer created at 2010-11-13 16:22:55

Script to do the changes (to be executed in SAGE_ROOT/devel/sage)


---

Comment by jdemeyer created at 2010-11-13 16:23:16

Changing status from positive_review to needs_work.


---

Attachment


---

Comment by jdemeyer created at 2010-11-13 16:24:50

Any complaints if I execute the script [attachment:8898.sh] instead of applying the patch?  The script also fixes some more files.


---

Comment by jdemeyer created at 2010-11-13 16:24:50

Changing status from needs_work to needs_review.


---

Comment by fbissey created at 2010-11-13 17:45:01

Replying to [comment:12 jdemeyer]:
> Any complaints if I execute the script [attachment:8898.sh] instead of applying the patch?  The script also fixes some more files.

No complaints here. As I initially said my main concern are the cython files.
I'll be happy if a fix goes in script or patch.


---

Comment by fbissey created at 2010-11-14 09:24:21

I am building 4.6.1.alpha2 which includes the fix. cython parsed everything
without trouble using python-2.6.5 and compilation is now underway.
So it looks good to me.


---

Comment by jdemeyer created at 2010-11-14 15:54:59

François, I am interpreting your post as a positive review, okay?


---

Comment by jdemeyer created at 2010-11-14 15:54:59

Changing status from needs_review to positive_review.


---

Comment by fbissey created at 2010-11-14 18:04:22

Replying to [comment:15 jdemeyer]:
> François, I am interpreting your post as a positive review, okay?

OK, the build finished successfully, so yes positive review.


---

Comment by jdemeyer created at 2010-11-15 23:24:39

Resolution: fixed
