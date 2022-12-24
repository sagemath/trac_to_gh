# Issue 9345: Unhandled SIGFPE is rational_reconstruction if the modulus is zero

archive/issues_009345.json:
```json
{
    "body": "Assignee: AlexGhitza\n\nCC:  jdemeyer\n\nSsage crashes if try to perform a rational_reconstruction with zero modulus and compiled fast algorithm\n\n\n```\nsage: rational_reconstruction(1,0)\n\n\n------------------------------------------------------------\nUnhandled SIGFPE: An unhandled floating point exception occured in Sage.\nThis probably occured because a *compiled* component\nof Sage has a bug in it (typically accessing invalid memory)\nor is not properly wrapped with _sig_on, _sig_off.\nYou might want to run Sage under gdb with 'sage -gdb' to debug this.\nSage will now terminate (sorry).\n------------------------------------------------------------\n\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9345\n\n",
    "created_at": "2010-06-26T10:42:28Z",
    "labels": [
        "algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6.1",
    "title": "Unhandled SIGFPE is rational_reconstruction if the modulus is zero",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9345",
    "user": "lftabera"
}
```
Assignee: AlexGhitza

CC:  jdemeyer

Ssage crashes if try to perform a rational_reconstruction with zero modulus and compiled fast algorithm


```
sage: rational_reconstruction(1,0)


------------------------------------------------------------
Unhandled SIGFPE: An unhandled floating point exception occured in Sage.
This probably occured because a *compiled* component
of Sage has a bug in it (typically accessing invalid memory)
or is not properly wrapped with _sig_on, _sig_off.
You might want to run Sage under gdb with 'sage -gdb' to debug this.
Sage will now terminate (sorry).
------------------------------------------------------------

```


Issue created by migration from https://trac.sagemath.org/ticket/9345





---

archive/issue_comments_088702.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-06-26T10:51:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9345#issuecomment-88702",
    "user": "lftabera"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_088703.json:
```json
{
    "body": "Attachment [trac_9345.patch](tarball://root/attachments/some-uuid/ticket9345/trac_9345.patch) by lftabera created at 2010-06-26 10:51:25",
    "created_at": "2010-06-26T10:51:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9345#issuecomment-88703",
    "user": "lftabera"
}
```

Attachment [trac_9345.patch](tarball://root/attachments/some-uuid/ticket9345/trac_9345.patch) by lftabera created at 2010-06-26 10:51:25



---

archive/issue_comments_088704.json:
```json
{
    "body": "Attachment [trac_9345.2.patch](tarball://root/attachments/some-uuid/ticket9345/trac_9345.2.patch) by mvngu created at 2010-06-26 11:34:23",
    "created_at": "2010-06-26T11:34:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9345#issuecomment-88704",
    "user": "mvngu"
}
```

Attachment [trac_9345.2.patch](tarball://root/attachments/some-uuid/ticket9345/trac_9345.2.patch) by mvngu created at 2010-06-26 11:34:23



---

archive/issue_comments_088705.json:
```json
{
    "body": "Attachment [trac_9345-reviewer.patch](tarball://root/attachments/some-uuid/ticket9345/trac_9345-reviewer.patch) by mvngu created at 2010-06-26 11:40:18\n\nI'm mostly OK with lftabera's patch. Here are some changes that needs to be made:\n\n* Reference the ticket number in the relevant regression test.\n* Use the Python 3.x compliant way of raising exceptions.\n* Add a more general regression test.\n* Credit lftabera in his patch. (We don't accept anonymous patches.) Put a sensible commit message in lftabera's patch. So one now uses [trac_9345.2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/9345/trac_9345.2.patch) instead of [trac_9345.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/9345/trac_9345.patch). \n\nSee the ticket description for instructions on how to apply the relevant patches. Only my proposed changes need review by anyone but me. If they are OK, then the whole ticket receives a positive review.",
    "created_at": "2010-06-26T11:40:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9345#issuecomment-88705",
    "user": "mvngu"
}
```

Attachment [trac_9345-reviewer.patch](tarball://root/attachments/some-uuid/ticket9345/trac_9345-reviewer.patch) by mvngu created at 2010-06-26 11:40:18

I'm mostly OK with lftabera's patch. Here are some changes that needs to be made:

* Reference the ticket number in the relevant regression test.
* Use the Python 3.x compliant way of raising exceptions.
* Add a more general regression test.
* Credit lftabera in his patch. (We don't accept anonymous patches.) Put a sensible commit message in lftabera's patch. So one now uses [trac_9345.2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/9345/trac_9345.2.patch) instead of [trac_9345.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/9345/trac_9345.patch). 

See the ticket description for instructions on how to apply the relevant patches. Only my proposed changes need review by anyone but me. If they are OK, then the whole ticket receives a positive review.



---

archive/issue_comments_088706.json:
```json
{
    "body": "Not quite solved, the problem is not in this method, but in the compiled rational reconstruction\n\n\n```\nsage: ZZ(1).rational_reconstruction(0)\n\n\n------------------------------------------------------------\nUnhandled SIGFPE: An unhandled floating point exception occured in Sage.\nThis probably occured because a *compiled* component\nof Sage has a bug in it (typically accessing invalid memory)\nor is not properly wrapped with _sig_on, _sig_off.\nYou might want to run Sage under gdb with 'sage -gdb' to debug this.\nSage will now terminate (sorry).\n------------------------------------------------------------\n```\n\n\nI will update the patch to the correct function",
    "created_at": "2010-06-26T11:51:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9345#issuecomment-88706",
    "user": "lftabera"
}
```

Not quite solved, the problem is not in this method, but in the compiled rational reconstruction


```
sage: ZZ(1).rational_reconstruction(0)


------------------------------------------------------------
Unhandled SIGFPE: An unhandled floating point exception occured in Sage.
This probably occured because a *compiled* component
of Sage has a bug in it (typically accessing invalid memory)
or is not properly wrapped with _sig_on, _sig_off.
You might want to run Sage under gdb with 'sage -gdb' to debug this.
Sage will now terminate (sorry).
------------------------------------------------------------
```


I will update the patch to the correct function



---

archive/issue_comments_088707.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-06-26T11:51:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9345#issuecomment-88707",
    "user": "lftabera"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_088708.json:
```json
{
    "body": "The following files have a call to rational_reconstruction, computed using\n\n\n```\nsage: search_src('rational_reconstruction',interact=False)\n\n```\n\nand code to make Sage crash\n\n* rings/integer.pyx\n\n\n```\n sage: ZZ(1).rational_reconstruction(0)\n```\n\n  Calls rational.pyrex_rational_reconstruction\n\n* rings/rational.pyx\n\n\n```\n sage: sage.rings.rational.pyrex_rational_reconstruction(1,0)\n```\n\n* rings/arith.py\n\n\n```\n sage: rational_reconstruction(1,0)\n```\n\n  Calls ZZ.rational_reconstruction\n\n* rings/finite_rings/element_ext_pari.py\n\n  Unable to crash, it is an element of a finite field. Anyway, it calls arith.rational_reconstruction\n\n* rings/finite_rings/integer_mod.pyx\n\n  Unable to crash, an element mod 0 is an Integer. Anyway, it calls ZZ.rational_reconstruction\n\n* rings/padics/padic_generic_element.pyx\n\n  Unable to crash, modulus of a p-adic element is not zero. anyway, it calls arith.rational_reconstruction\n\n* matrix/matrix_rational_dense.pyx\n\n1. _lift_crt_rr\n2. _lift_crt_rr_with_lcm\n\n\n   Obsolete functions for crt? They seem not to be used anywhere. By the code, it seems tha mm should be a list of moduli matrices (call of _lift_crt). On the other hand, the product should be an integer \nm= mm.prod(); mpq_rational_reconstruction(Q_row[j], Z_row[j], m.value) So I cannot test whether there is a problem for these functions. I am not able to get crashes or any sensible output from these functions.\n\n* matrix/matrix_integer_sparse.pyx\n\n\n```\n sage: M = random_matrix(ZZ, 3, 3, 'sparse')\n sage: M.rational_reconstruction()\n```\n\n  Calls misc.matrix_integer_sparse_rational_reconstruction\n\n* matrix/misc.pyx\n\n\n```\n sage: M = random_matrix(ZZ, 3, 3, 'sparse')\n sage: sage.matrix.misc.matrix_integer_sparse_rational_reconstruction(M,0)\n```\n\n\n```\n sage: M = random_matrix(ZZ, 3, 3)\n sage: sage.matrix.misc.matrix_integer_dense_rational_reconstruction(M,0)\n```\n\n* matrix/matrix_cyclo_dense.pyx\n\n  Unable to crash. Used in a modular algorithm, calls misc.matrix_integer_dense_rational_reconstruction\n\n* matrix/matrix_integer_dense.pyx\n\n\n```\n sage: M = random_matrix(ZZ,3)\n sage: M.rational_reconstruction(0)\n```\n\n  Calls misc.matrix_integer_dense_rational_reconstruction",
    "created_at": "2010-06-30T13:55:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9345#issuecomment-88708",
    "user": "lftabera"
}
```

The following files have a call to rational_reconstruction, computed using


```
sage: search_src('rational_reconstruction',interact=False)

```

and code to make Sage crash

* rings/integer.pyx


```
 sage: ZZ(1).rational_reconstruction(0)
```

  Calls rational.pyrex_rational_reconstruction

* rings/rational.pyx


```
 sage: sage.rings.rational.pyrex_rational_reconstruction(1,0)
```

* rings/arith.py


```
 sage: rational_reconstruction(1,0)
```

  Calls ZZ.rational_reconstruction

* rings/finite_rings/element_ext_pari.py

  Unable to crash, it is an element of a finite field. Anyway, it calls arith.rational_reconstruction

* rings/finite_rings/integer_mod.pyx

  Unable to crash, an element mod 0 is an Integer. Anyway, it calls ZZ.rational_reconstruction

* rings/padics/padic_generic_element.pyx

  Unable to crash, modulus of a p-adic element is not zero. anyway, it calls arith.rational_reconstruction

* matrix/matrix_rational_dense.pyx

1. _lift_crt_rr
2. _lift_crt_rr_with_lcm


   Obsolete functions for crt? They seem not to be used anywhere. By the code, it seems tha mm should be a list of moduli matrices (call of _lift_crt). On the other hand, the product should be an integer 
m= mm.prod(); mpq_rational_reconstruction(Q_row[j], Z_row[j], m.value) So I cannot test whether there is a problem for these functions. I am not able to get crashes or any sensible output from these functions.

* matrix/matrix_integer_sparse.pyx


```
 sage: M = random_matrix(ZZ, 3, 3, 'sparse')
 sage: M.rational_reconstruction()
```

  Calls misc.matrix_integer_sparse_rational_reconstruction

* matrix/misc.pyx


```
 sage: M = random_matrix(ZZ, 3, 3, 'sparse')
 sage: sage.matrix.misc.matrix_integer_sparse_rational_reconstruction(M,0)
```


```
 sage: M = random_matrix(ZZ, 3, 3)
 sage: sage.matrix.misc.matrix_integer_dense_rational_reconstruction(M,0)
```

* matrix/matrix_cyclo_dense.pyx

  Unable to crash. Used in a modular algorithm, calls misc.matrix_integer_dense_rational_reconstruction

* matrix/matrix_integer_dense.pyx


```
 sage: M = random_matrix(ZZ,3)
 sage: M.rational_reconstruction(0)
```

  Calls misc.matrix_integer_dense_rational_reconstruction



---

archive/issue_comments_088709.json:
```json
{
    "body": "Attachment [trac_9345.3.patch](tarball://root/attachments/some-uuid/ticket9345/trac_9345.3.patch) by lftabera created at 2010-07-02 10:07:18\n\nprevious patches merged",
    "created_at": "2010-07-02T10:07:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9345#issuecomment-88709",
    "user": "lftabera"
}
```

Attachment [trac_9345.3.patch](tarball://root/attachments/some-uuid/ticket9345/trac_9345.3.patch) by lftabera created at 2010-07-02 10:07:18

previous patches merged



---

archive/issue_comments_088710.json:
```json
{
    "body": "New patch with all the modifications. Respecting the code, the patch only changes rings/rational.pyx and matrix/misc.pyx where the offending code is.\n\nHowever, I have added doctests to check all the crashes in the previous post. This might be overkilling though.",
    "created_at": "2010-07-02T10:11:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9345#issuecomment-88710",
    "user": "lftabera"
}
```

New patch with all the modifications. Respecting the code, the patch only changes rings/rational.pyx and matrix/misc.pyx where the offending code is.

However, I have added doctests to check all the crashes in the previous post. This might be overkilling though.



---

archive/issue_comments_088711.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-07-02T10:11:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9345#issuecomment-88711",
    "user": "lftabera"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_088712.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-08-10T06:15:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9345#issuecomment-88712",
    "user": "jdemeyer"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_088713.json:
```json
{
    "body": "I think one should find out which code really causes the crash, because _sig_on/_sig_off should be used there.  See [http://sagemath.org/doc/developer/coding_in_other.html#the-pari-c-library-interface](http://sagemath.org/doc/developer/coding_in_other.html#the-pari-c-library-interface) (the docs are about PARI but apply more generally to all C and Cython code).",
    "created_at": "2010-08-10T06:15:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9345#issuecomment-88713",
    "user": "jdemeyer"
}
```

I think one should find out which code really causes the crash, because _sig_on/_sig_off should be used there.  See [http://sagemath.org/doc/developer/coding_in_other.html#the-pari-c-library-interface](http://sagemath.org/doc/developer/coding_in_other.html#the-pari-c-library-interface) (the docs are about PARI but apply more generally to all C and Cython code).



---

archive/issue_comments_088714.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-09-06T09:03:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9345#issuecomment-88714",
    "user": "lftabera"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_088715.json:
```json
{
    "body": "Attachment [trac-9345-sigs.patch](tarball://root/attachments/some-uuid/ticket9345/trac-9345-sigs.patch) by lftabera created at 2010-09-06 09:03:03\n\nWell, there was a similar problem in #9357 and I got this answer to the question of _sig_onm, _sig_off\n\nhttp://groups.google.com/group/sage-devel/browse_thread/thread/e8317365bfe9e6e8/2a4148024500dfd2\n\nNote that if the exception is controlled by _sig, it will raise a RuntimeError instead of ZeroDivisionError. Moreover, with the patch I provided, all ocurrences of being zero are catched and never reaches the C functions.\n\nAnyway, I have written a second patch that add the _sig_on, _sig_off to the problematic functions, so if they have to be added, apply the following patches (in order):\n\ntrac_9345.3.patch\ntrac-9345-sigs.patch",
    "created_at": "2010-09-06T09:03:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9345#issuecomment-88715",
    "user": "lftabera"
}
```

Attachment [trac-9345-sigs.patch](tarball://root/attachments/some-uuid/ticket9345/trac-9345-sigs.patch) by lftabera created at 2010-09-06 09:03:03

Well, there was a similar problem in #9357 and I got this answer to the question of _sig_onm, _sig_off

http://groups.google.com/group/sage-devel/browse_thread/thread/e8317365bfe9e6e8/2a4148024500dfd2

Note that if the exception is controlled by _sig, it will raise a RuntimeError instead of ZeroDivisionError. Moreover, with the patch I provided, all ocurrences of being zero are catched and never reaches the C functions.

Anyway, I have written a second patch that add the _sig_on, _sig_off to the problematic functions, so if they have to be added, apply the following patches (in order):

trac_9345.3.patch
trac-9345-sigs.patch



---

archive/issue_comments_088716.json:
```json
{
    "body": "Replying to [comment:7 lftabera]:\n> Note that if the exception is controlled by _sig, it will raise a RuntimeError instead of ZeroDivisionError. Moreover, with the patch I provided, all ocurrences of being zero are catched and never reaches the C functions.\nI agree that your patch fixes the problem of division by zero, that wasn't my point.  My point was that, **in addition** you should add _sig_on and _sig_off to make the code more robust (for example, against crtl+C).\n\n> Anyway, I have written a second patch that add the _sig_on, _sig_off to the problematic functions, so if they have to be added, apply the following patches (in order):\n> \n> trac_9345.3.patch\n> trac-9345-sigs.patch\nWell, the _sig_on and _sig_off are in the wrong places (_sig_on should be before any mpz or mpq function is called and _sig_off after). I can have a look at this if you want.",
    "created_at": "2010-09-06T10:33:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9345#issuecomment-88716",
    "user": "jdemeyer"
}
```

Replying to [comment:7 lftabera]:
> Note that if the exception is controlled by _sig, it will raise a RuntimeError instead of ZeroDivisionError. Moreover, with the patch I provided, all ocurrences of being zero are catched and never reaches the C functions.
I agree that your patch fixes the problem of division by zero, that wasn't my point.  My point was that, **in addition** you should add _sig_on and _sig_off to make the code more robust (for example, against crtl+C).

> Anyway, I have written a second patch that add the _sig_on, _sig_off to the problematic functions, so if they have to be added, apply the following patches (in order):
> 
> trac_9345.3.patch
> trac-9345-sigs.patch
Well, the _sig_on and _sig_off are in the wrong places (_sig_on should be before any mpz or mpq function is called and _sig_off after). I can have a look at this if you want.



---

archive/issue_comments_088717.json:
```json
{
    "body": "Attachment [trac-9345-sigs-jd.patch](tarball://root/attachments/some-uuid/ticket9345/trac-9345-sigs-jd.patch) by jdemeyer created at 2010-09-07 20:54:54\n\nBetter alternative to trac-9345-sigs.patch",
    "created_at": "2010-09-07T20:54:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9345#issuecomment-88717",
    "user": "jdemeyer"
}
```

Attachment [trac-9345-sigs-jd.patch](tarball://root/attachments/some-uuid/ticket9345/trac-9345-sigs-jd.patch) by jdemeyer created at 2010-09-07 20:54:54

Better alternative to trac-9345-sigs.patch



---

archive/issue_comments_088718.json:
```json
{
    "body": "Replying to [comment:5 lftabera]:\n> However, I have added doctests to check all the crashes in the previous post. This might be overkilling though.\n\nI agree that it is overkill, but I'm fine with it.  I'm giving positive_review for `trac_9345.3.patch`. Somebody else should review my `trac-9345-sigs-jd.patch`.",
    "created_at": "2010-09-07T21:01:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9345#issuecomment-88718",
    "user": "jdemeyer"
}
```

Replying to [comment:5 lftabera]:
> However, I have added doctests to check all the crashes in the previous post. This might be overkilling though.

I agree that it is overkill, but I'm fine with it.  I'm giving positive_review for `trac_9345.3.patch`. Somebody else should review my `trac-9345-sigs-jd.patch`.



---

archive/issue_comments_088719.json:
```json
{
    "body": "Attachment [trac-9345-sigs-jd-2.patch](tarball://root/attachments/some-uuid/ticket9345/trac-9345-sigs-jd-2.patch) by lftabera created at 2010-09-08 08:13:31\n\nI have corrected jdemeyer patch to also  include the sparse matrix case. The patch to review is trac-9345-sigs-jd-2.patch",
    "created_at": "2010-09-08T08:13:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9345#issuecomment-88719",
    "user": "lftabera"
}
```

Attachment [trac-9345-sigs-jd-2.patch](tarball://root/attachments/some-uuid/ticket9345/trac-9345-sigs-jd-2.patch) by lftabera created at 2010-09-08 08:13:31

I have corrected jdemeyer patch to also  include the sparse matrix case. The patch to review is trac-9345-sigs-jd-2.patch



---

archive/issue_comments_088720.json:
```json
{
    "body": "Replying to [comment:10 lftabera]:\n> I have corrected jdemeyer patch to also  include the sparse matrix case. The patch to review is trac-9345-sigs-jd-2.patch\n\nLooks good to me, but I suppose somebody else should formally review it.",
    "created_at": "2010-09-08T12:02:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9345#issuecomment-88720",
    "user": "jdemeyer"
}
```

Replying to [comment:10 lftabera]:
> I have corrected jdemeyer patch to also  include the sparse matrix case. The patch to review is trac-9345-sigs-jd-2.patch

Looks good to me, but I suppose somebody else should formally review it.



---

archive/issue_comments_088721.json:
```json
{
    "body": "I will move the signals part to #10061, therefore positive review for [attachment:trac_9345.3.patch]",
    "created_at": "2010-11-13T10:43:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9345#issuecomment-88721",
    "user": "jdemeyer"
}
```

I will move the signals part to #10061, therefore positive review for [attachment:trac_9345.3.patch]



---

archive/issue_comments_088722.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-11-13T10:43:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9345#issuecomment-88722",
    "user": "jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_088723.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-11-15T23:26:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9345#issuecomment-88723",
    "user": "jdemeyer"
}
```

Resolution: fixed
