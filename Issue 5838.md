# Issue 5838: crash in Singular's polynomial gcd

archive/issues_005838.json:
```json
{
    "body": "Assignee: malb\n\nCC:  malb\n\nHere's what I type to provoke the crash:\n\n```\nstd = os.environ['SAGE_DATA'] + '/extcode/pickle_jar/pickle_jar.tar.bz2'\nsage.structure.sage_object.unpickle_all(std)\nsage.structure.sage_object.unpickle_all(std)\n```\n\n(this is the doctest of unpickle_all, plus an extra repetition of the second line)\n\nHere's the output:\n\n\n```\nsage: std = os.environ['SAGE_DATA'] + '/extcode/pickle_jar/pickle_jar.tar.bz2'\nsage: sage.structure.sage_object.unpickle_all(std)\n/home/cwitty/sage-3.4.1.rc3/local/lib/python2.5/site-packages/IPython/iplib.py:2073: DeprecationWarning: RQDF is deprecated; use RealField(212) instead.\n  exec code_obj in self.user_global_ns, self.user_ns\nSuccessfully unpickled 483 objects.\nFailed to unpickle 0 objects.\nsage: sage.structure.sage_object.unpickle_all(std)\n/home/cwitty/sage-3.4.1.rc3/local/bin/sage-sage: line 198: 22270 Aborted                 sage-ipython \"$@\" -i\n```\n\n\nThe first section of the backtrace is:\n\n\n```\n#0  0x00007fc7c14c2105 in raise () from /lib/libc.so.6\n#1  0x00007fc7c14c3623 in abort () from /lib/libc.so.6\n#2  0x00007fc7bcedd6d8 in global_NTL_error_callback ()\n   from /home/cwitty/sage-3.4.1.rc3/local/lib/libcsage.so\n#3  0x00007fc7bc9451ef in NTL::Error (\n    s=0x7fc7bc97def1 \"InvMod: inverse undefined\") at tools.c:38\n#4  0x00007fc7bc88ebd9 in NTL::InvMod (a=<value optimized out>, n=244)\n    at ZZ.c:351\n#5  0x00007fc7bc90545f in NTL::PlainRem (r=@0x7fffca29e230, a=@0x7fffca29e230, \n    b=@0x6) at ../include/NTL/lzz_p.h:278\n#6  0x00007fc7bc9140bb in NTL::GCD (d=@0x7fffca29e360, \n    u=<value optimized out>, v=@0x7fffca29e390) at lzz_pX1.c:558\n#7  0x00007fc7a963206a in gcd_poly_p (f=@0x7fffca29e9e0, g=@0x7fffca29e9d0)\n    at /home/cwitty/sage-3.4.1.rc3/local/include/NTL/lzz_pX.h:696\n#8  0x00007fc7a9633835 in gcd_poly (f=<value optimized out>, g=@0x7fffca29ee50)\n    at cf_gcd.cc:538\n#9  0x00007fc7a963401e in gcd (f=@0x7fffca29ee60, g=@0x7fffca29ee50)\n    at cf_gcd.cc:776\n#10 0x00007fc7a9634601 in gcd_test_one (f=@0x7fffca29f3b0, g=@0x7fffca29f3c0, \n    swap=true) at cf_gcd.cc:76\n#11 0x00007fc7a9631b70 in gcd_poly_p (f=@0x7fffca29f7b0, g=@0x7fffca29f7a0)\n    at cf_gcd.cc:353\n#12 0x00007fc7a963373d in gcd_poly (f=<value optimized out>, g=@0x7fffca29fbb0)\n    at cf_gcd.cc:543\n#13 0x00007fc7a9635d89 in chinrem_gcd (FF=<value optimized out>, \n    GG=<value optimized out>) at cf_gcd.cc:1088\n#14 0x00007fc7a96337e1 in gcd_poly (f=<value optimized out>, g=@0x7fffca2a0560)\n    at cf_gcd.cc:601\n#15 0x00007fc7a963401e in gcd (f=@0x7fffca2a0550, g=@0x7fffca2a0560)\n    at cf_gcd.cc:776\n#16 0x00007fc7a94a69f8 in singclap_gcd (f=0x7fc7a930b198, g=0x7fc7a930b058)\n    at clapsing.cc:230\n#17 0x00007fc7a992d2f9 in __pyx_pf_4sage_5rings_10polynomial_28multi_polynomial_libsingular_23MPolynomial_libsingular_gcd (__pyx_v_self=0x5e60830, \n    __pyx_args=<value optimized out>, __pyx_kwds=<value optimized out>)\n    at sage/rings/polynomial/multi_polynomial_libsingular.cpp:31063\n#18 0x00000000004187e3 in PyObject_Call (func=0x58ad, arg=0x58ad, kw=0x6)\n    at Objects/abstract.c:1861\n#19 0x00007fc7b3aaf02f in __pyx_pf_4sage_5rings_22fraction_field_element_20FractionFieldElement_reduce (__pyx_v_self=0x5e5e2d0, unused=<value optimized out>)\n    at sage/rings/fraction_field_element.c:2288\n#20 0x00000000004187e3 in PyObject_Call (func=0x58ad, arg=0x58ad, kw=0x6)\n    at Objects/abstract.c:1861\n#21 0x00007fc7b3aa3b2b in __pyx_pf_4sage_5rings_22fraction_field_element_20FractionFieldElement___init__ (__pyx_v_self=0x5e5e2d0, \n    __pyx_args=<value optimized out>, __pyx_kwds=<value optimized out>)\n    at sage/rings/fraction_field_element.c:1905\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5838\n\n",
    "created_at": "2009-04-20T21:07:49Z",
    "labels": [
        "commutative algebra",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "crash in Singular's polynomial gcd",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5838",
    "user": "cwitty"
}
```
Assignee: malb

CC:  malb

Here's what I type to provoke the crash:

```
std = os.environ['SAGE_DATA'] + '/extcode/pickle_jar/pickle_jar.tar.bz2'
sage.structure.sage_object.unpickle_all(std)
sage.structure.sage_object.unpickle_all(std)
```

(this is the doctest of unpickle_all, plus an extra repetition of the second line)

Here's the output:


```
sage: std = os.environ['SAGE_DATA'] + '/extcode/pickle_jar/pickle_jar.tar.bz2'
sage: sage.structure.sage_object.unpickle_all(std)
/home/cwitty/sage-3.4.1.rc3/local/lib/python2.5/site-packages/IPython/iplib.py:2073: DeprecationWarning: RQDF is deprecated; use RealField(212) instead.
  exec code_obj in self.user_global_ns, self.user_ns
Successfully unpickled 483 objects.
Failed to unpickle 0 objects.
sage: sage.structure.sage_object.unpickle_all(std)
/home/cwitty/sage-3.4.1.rc3/local/bin/sage-sage: line 198: 22270 Aborted                 sage-ipython "$@" -i
```


The first section of the backtrace is:


```
#0  0x00007fc7c14c2105 in raise () from /lib/libc.so.6
#1  0x00007fc7c14c3623 in abort () from /lib/libc.so.6
#2  0x00007fc7bcedd6d8 in global_NTL_error_callback ()
   from /home/cwitty/sage-3.4.1.rc3/local/lib/libcsage.so
#3  0x00007fc7bc9451ef in NTL::Error (
    s=0x7fc7bc97def1 "InvMod: inverse undefined") at tools.c:38
#4  0x00007fc7bc88ebd9 in NTL::InvMod (a=<value optimized out>, n=244)
    at ZZ.c:351
#5  0x00007fc7bc90545f in NTL::PlainRem (r=@0x7fffca29e230, a=@0x7fffca29e230, 
    b=@0x6) at ../include/NTL/lzz_p.h:278
#6  0x00007fc7bc9140bb in NTL::GCD (d=@0x7fffca29e360, 
    u=<value optimized out>, v=@0x7fffca29e390) at lzz_pX1.c:558
#7  0x00007fc7a963206a in gcd_poly_p (f=@0x7fffca29e9e0, g=@0x7fffca29e9d0)
    at /home/cwitty/sage-3.4.1.rc3/local/include/NTL/lzz_pX.h:696
#8  0x00007fc7a9633835 in gcd_poly (f=<value optimized out>, g=@0x7fffca29ee50)
    at cf_gcd.cc:538
#9  0x00007fc7a963401e in gcd (f=@0x7fffca29ee60, g=@0x7fffca29ee50)
    at cf_gcd.cc:776
#10 0x00007fc7a9634601 in gcd_test_one (f=@0x7fffca29f3b0, g=@0x7fffca29f3c0, 
    swap=true) at cf_gcd.cc:76
#11 0x00007fc7a9631b70 in gcd_poly_p (f=@0x7fffca29f7b0, g=@0x7fffca29f7a0)
    at cf_gcd.cc:353
#12 0x00007fc7a963373d in gcd_poly (f=<value optimized out>, g=@0x7fffca29fbb0)
    at cf_gcd.cc:543
#13 0x00007fc7a9635d89 in chinrem_gcd (FF=<value optimized out>, 
    GG=<value optimized out>) at cf_gcd.cc:1088
#14 0x00007fc7a96337e1 in gcd_poly (f=<value optimized out>, g=@0x7fffca2a0560)
    at cf_gcd.cc:601
#15 0x00007fc7a963401e in gcd (f=@0x7fffca2a0550, g=@0x7fffca2a0560)
    at cf_gcd.cc:776
#16 0x00007fc7a94a69f8 in singclap_gcd (f=0x7fc7a930b198, g=0x7fc7a930b058)
    at clapsing.cc:230
#17 0x00007fc7a992d2f9 in __pyx_pf_4sage_5rings_10polynomial_28multi_polynomial_libsingular_23MPolynomial_libsingular_gcd (__pyx_v_self=0x5e60830, 
    __pyx_args=<value optimized out>, __pyx_kwds=<value optimized out>)
    at sage/rings/polynomial/multi_polynomial_libsingular.cpp:31063
#18 0x00000000004187e3 in PyObject_Call (func=0x58ad, arg=0x58ad, kw=0x6)
    at Objects/abstract.c:1861
#19 0x00007fc7b3aaf02f in __pyx_pf_4sage_5rings_22fraction_field_element_20FractionFieldElement_reduce (__pyx_v_self=0x5e5e2d0, unused=<value optimized out>)
    at sage/rings/fraction_field_element.c:2288
#20 0x00000000004187e3 in PyObject_Call (func=0x58ad, arg=0x58ad, kw=0x6)
    at Objects/abstract.c:1861
#21 0x00007fc7b3aa3b2b in __pyx_pf_4sage_5rings_22fraction_field_element_20FractionFieldElement___init__ (__pyx_v_self=0x5e5e2d0, 
    __pyx_args=<value optimized out>, __pyx_kwds=<value optimized out>)
    at sage/rings/fraction_field_element.c:1905
```



Issue created by migration from https://trac.sagemath.org/ticket/5838





---

archive/issue_comments_045874.json:
```json
{
    "body": "Looking a bit further into it, the actual pickles that trigger the problem are those in `sage.combinat.sf.macdonald`. Namely, if these ones are removed from the pickle jar, then the problem disappears...",
    "created_at": "2013-01-27T08:07:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5838",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5838#issuecomment-45874",
    "user": "Bouillaguet"
}
```

Looking a bit further into it, the actual pickles that trigger the problem are those in `sage.combinat.sf.macdonald`. Namely, if these ones are removed from the pickle jar, then the problem disappears...



---

archive/issue_comments_045875.json:
```json
{
    "body": "As an update, because the system changed since, the commands to trigger this are:\n\n```\nsage: import os\nsage: std = os.environ['SAGE_SHARE'] + '/sage/ext/pickle_jar/pickle_jar.tar.bz2'\nsage: sage.structure.sage_object.unpickle_all(std)\nsage: sage.structure.sage_object.unpickle_all(std)\n```\n",
    "created_at": "2014-04-14T13:52:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5838",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5838#issuecomment-45875",
    "user": "rws"
}
```

As an update, because the system changed since, the commands to trigger this are:

```
sage: import os
sage: std = os.environ['SAGE_SHARE'] + '/sage/ext/pickle_jar/pickle_jar.tar.bz2'
sage: sage.structure.sage_object.unpickle_all(std)
sage: sage.structure.sage_object.unpickle_all(std)
```




---

archive/issue_comments_045876.json:
```json
{
    "body": "The output of the code in comment:4 is now\n\n```\nSuccessfully unpickled 586 objects.\nFailed to unpickle 0 objects.\n```\n\nwhich I guess is OK.",
    "created_at": "2014-08-11T06:07:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5838",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5838#issuecomment-45876",
    "user": "rws"
}
```

The output of the code in comment:4 is now

```
Successfully unpickled 586 objects.
Failed to unpickle 0 objects.
```

which I guess is OK.



---

archive/issue_comments_045877.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2014-08-11T06:07:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5838",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5838#issuecomment-45877",
    "user": "rws"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_045878.json:
```json
{
    "body": "Wouldn't it make sense to add a doctest for this, to make sure that it stays fixed?",
    "created_at": "2014-08-11T11:45:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5838",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5838#issuecomment-45878",
    "user": "pbruin"
}
```

Wouldn't it make sense to add a doctest for this, to make sure that it stays fixed?



---

archive/issue_comments_045879.json:
```json
{
    "body": "Changing priority from critical to major.",
    "created_at": "2014-08-11T15:26:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5838",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5838#issuecomment-45879",
    "user": "rws"
}
```

Changing priority from critical to major.



---

archive/issue_comments_045880.json:
```json
{
    "body": "Replying to [comment:8 pbruin]:\n> Wouldn't it make sense to add a doctest for this, to make sure that it stays fixed?\nOf course, thanks for the hint.\n----\nNew commits:",
    "created_at": "2014-08-11T15:26:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5838",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5838#issuecomment-45880",
    "user": "rws"
}
```

Replying to [comment:8 pbruin]:
> Wouldn't it make sense to add a doctest for this, to make sure that it stays fixed?
Of course, thanks for the hint.
----
New commits:



---

archive/issue_comments_045881.json:
```json
{
    "body": "Question: \n\nwhy there was a crash in Singular's polynomial gcd and how it got fixed?\n\nIt is not obvious for me...( I'm new to sage and do not yet understand everything)",
    "created_at": "2014-08-11T15:38:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5838",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5838#issuecomment-45881",
    "user": "jakobkroeker"
}
```

Question: 

why there was a crash in Singular's polynomial gcd and how it got fixed?

It is not obvious for me...( I'm new to sage and do not yet understand everything)



---

archive/issue_comments_045882.json:
```json
{
    "body": "Replying to [comment:11 jakobkroeker]:\n> Question: \n> \n> why there was a crash in Singular's polynomial gcd and how it got fixed?\n> \n> It is not obvious for me...( I'm new to sage and do not yet understand everything)\n\nThe crash was quite old (5 years ago) and presumably happened because of an old Singular version. This triggered an unpickling crash. Pickling is the Python name for serialization, see https://en.wikipedia.org/wiki/Serialization\n\nI admit the doctest tests the unpickling issue, i.e., the symptom not the cause. OTOH it has the potential to catch a lot of other bugs. The bug itself was probably fixed by a newer Singular version.",
    "created_at": "2014-08-11T15:45:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5838",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5838#issuecomment-45882",
    "user": "rws"
}
```

Replying to [comment:11 jakobkroeker]:
> Question: 
> 
> why there was a crash in Singular's polynomial gcd and how it got fixed?
> 
> It is not obvious for me...( I'm new to sage and do not yet understand everything)

The crash was quite old (5 years ago) and presumably happened because of an old Singular version. This triggered an unpickling crash. Pickling is the Python name for serialization, see https://en.wikipedia.org/wiki/Serialization

I admit the doctest tests the unpickling issue, i.e., the symptom not the cause. OTOH it has the potential to catch a lot of other bugs. The bug itself was probably fixed by a newer Singular version.



---

archive/issue_comments_045883.json:
```json
{
    "body": "Q: should the tag 'long time' be added to the test?",
    "created_at": "2014-08-11T17:49:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5838",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5838#issuecomment-45883",
    "user": "jakobkroeker"
}
```

Q: should the tag 'long time' be added to the test?



---

archive/issue_comments_045884.json:
```json
{
    "body": "You must certainly remove the ` # not tested`, otherwise you are just testing once, not twice...",
    "created_at": "2014-08-11T18:48:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5838",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5838#issuecomment-45884",
    "user": "jdemeyer"
}
```

You must certainly remove the ` # not tested`, otherwise you are just testing once, not twice...



---

archive/issue_comments_045885.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2014-08-11T18:49:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5838",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5838#issuecomment-45885",
    "user": "jdemeyer"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_045886.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-08-12T07:18:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5838",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5838#issuecomment-45886",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_045887.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2014-08-12T07:19:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5838",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5838#issuecomment-45887",
    "user": "rws"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_045888.json:
```json
{
    "body": "Done, thanks.",
    "created_at": "2014-08-12T07:19:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5838",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5838#issuecomment-45888",
    "user": "rws"
}
```

Done, thanks.



---

archive/issue_comments_045889.json:
```json
{
    "body": "The new commit moves the new doctest after the existing one testing the plain `unpickle_all()` command, for clarity and to save one run of `unpickle_all()`.  Setting the location of the pickle jar (`std`) probably had to be done by hand in earlier versions, but now one can just omit the `dir` argument.  I also made the explanation slightly more explicit.  If you agree with the changes, you can set it to positive review; if not, you can just put back your branch.",
    "created_at": "2014-08-12T17:11:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5838",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5838#issuecomment-45889",
    "user": "pbruin"
}
```

The new commit moves the new doctest after the existing one testing the plain `unpickle_all()` command, for clarity and to save one run of `unpickle_all()`.  Setting the location of the pickle jar (`std`) probably had to be done by hand in earlier versions, but now one can just omit the `dir` argument.  I also made the explanation slightly more explicit.  If you agree with the changes, you can set it to positive review; if not, you can just put back your branch.



---

archive/issue_comments_045890.json:
```json
{
    "body": "Yes, much clearer, thanks.",
    "created_at": "2014-08-13T07:01:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5838",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5838#issuecomment-45890",
    "user": "rws"
}
```

Yes, much clearer, thanks.



---

archive/issue_comments_045891.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-08-13T07:01:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5838",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5838#issuecomment-45891",
    "user": "rws"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_045892.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2014-08-13T17:06:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5838",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5838#issuecomment-45892",
    "user": "vbraun"
}
```

Resolution: fixed



---

archive/issue_comments_045893.json:
```json
{
    "body": "Assuming, I understand everything correctly..\n\n `@`pbruin\n\n The commit\n http://git.sagemath.org/sage.git/commit/?id=87d608a0d1cb1dc78186e89e46c3c651b6711090\n\n does not what Ralph Stephan intended,\n namely unpickle the 'pickle_jar.tar.bz2'\n\n `@`rws did you not notice that?",
    "created_at": "2014-08-14T09:17:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5838",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5838#issuecomment-45893",
    "user": "jakobkroeker"
}
```

Assuming, I understand everything correctly..

 `@`pbruin

 The commit
 http://git.sagemath.org/sage.git/commit/?id=87d608a0d1cb1dc78186e89e46c3c651b6711090

 does not what Ralph Stephan intended,
 namely unpickle the 'pickle_jar.tar.bz2'

 `@`rws did you not notice that?



---

archive/issue_comments_045894.json:
```json
{
    "body": "Hm, I thought the double unpickling was the issue tested but now I'm not sure anymore...",
    "created_at": "2014-08-14T09:25:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5838",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5838#issuecomment-45894",
    "user": "rws"
}
```

Hm, I thought the double unpickling was the issue tested but now I'm not sure anymore...



---

archive/issue_comments_045895.json:
```json
{
    "body": "I didn't understand everything correctly. \nUnpickling of pickle_jar.tar.bz2 _is_ checked by the doctest\nand everyhing is fine.",
    "created_at": "2014-08-14T09:30:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5838",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5838#issuecomment-45895",
    "user": "jakobkroeker"
}
```

I didn't understand everything correctly. 
Unpickling of pickle_jar.tar.bz2 _is_ checked by the doctest
and everyhing is fine.



---

archive/issue_comments_045896.json:
```json
{
    "body": "Hello,\n\nthis test fails on a dated gentoo(?) install\nwith error\n\n```\n**********************************************************************\nFile \"src/sage/structure/sage_object.pyx\", line 1411, in sage.structure.sage_object.unpickle_all\nFailed example:\n    sage.structure.sage_object.unpickle_all()  # (4s on sage.math, 2011)\nExpected:\n    doctest:... DeprecationWarning: This class is replaced by Matrix_modn_dense_float/Matrix_modn_dense_double.\n    See http://trac.sagemath.org/4260 for details.\n    Successfully unpickled ... objects.\n    Failed to unpickle 0 objects.\nGot:\n    *** The old options style (`tar fx ...`) is highly discouraged, please use the modern form (leading dash before options).\n    *** The standard way (with expanded options; you can still bundle options) for your command would be: tar -f - -x\n    doctest:1: DeprecationWarning: OrderedAlphabet is deprecated; use Alphabet instead.\n    See http://trac.sagemath.org/8920 for details.\n    doctest:843: DeprecationWarning: This class is replaced by Matrix_modn_dense_float/Matrix_modn_dense_double.\n    See http://trac.sagemath.org/4260 for details.\n    Successfully unpickled 586 objects.\n    Failed to unpickle 0 objects.\n```\n\nany idea how to fix it ?",
    "created_at": "2014-08-25T20:44:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5838",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5838#issuecomment-45896",
    "user": "jakobkroeker"
}
```

Hello,

this test fails on a dated gentoo(?) install
with error

```
**********************************************************************
File "src/sage/structure/sage_object.pyx", line 1411, in sage.structure.sage_object.unpickle_all
Failed example:
    sage.structure.sage_object.unpickle_all()  # (4s on sage.math, 2011)
Expected:
    doctest:... DeprecationWarning: This class is replaced by Matrix_modn_dense_float/Matrix_modn_dense_double.
    See http://trac.sagemath.org/4260 for details.
    Successfully unpickled ... objects.
    Failed to unpickle 0 objects.
Got:
    *** The old options style (`tar fx ...`) is highly discouraged, please use the modern form (leading dash before options).
    *** The standard way (with expanded options; you can still bundle options) for your command would be: tar -f - -x
    doctest:1: DeprecationWarning: OrderedAlphabet is deprecated; use Alphabet instead.
    See http://trac.sagemath.org/8920 for details.
    doctest:843: DeprecationWarning: This class is replaced by Matrix_modn_dense_float/Matrix_modn_dense_double.
    See http://trac.sagemath.org/4260 for details.
    Successfully unpickled 586 objects.
    Failed to unpickle 0 objects.
```

any idea how to fix it ?



---

archive/issue_comments_045897.json:
```json
{
    "body": "The second attempt to unpickle all crashes with both GMP 5.1.3, the current version in Sage, and GMP 6.1.1, in exactly the same manner as in the ticket description, with GCC 5.4.0, 6.1.0, and also Sage's GCC 4.9.3 (on Linux x86_64 at least).\n\nSage version 7.3.rc0 (NTL meanwhile at 9.8.1.p1, Singular still 3.1.7p1.p1).\n\n(Presumably just incidentally) doesn't happen with Sage's MPIR, currently 2.7.2.",
    "created_at": "2016-07-31T21:18:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5838",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5838#issuecomment-45897",
    "user": "leif"
}
```

The second attempt to unpickle all crashes with both GMP 5.1.3, the current version in Sage, and GMP 6.1.1, in exactly the same manner as in the ticket description, with GCC 5.4.0, 6.1.0, and also Sage's GCC 4.9.3 (on Linux x86_64 at least).

Sage version 7.3.rc0 (NTL meanwhile at 9.8.1.p1, Singular still 3.1.7p1.p1).

(Presumably just incidentally) doesn't happen with Sage's MPIR, currently 2.7.2.



---

archive/issue_comments_045898.json:
```json
{
    "body": "Replying to [comment:25 leif]:\n> The second attempt to unpickle all crashes with both GMP 5.1.3, the current version in Sage, and GMP 6.1.1, in exactly the same manner as in the ticket description, with GCC 5.4.0, 6.1.0, and also Sage's GCC 4.9.3 (on Linux x86_64 at least).\n> \n> Sage version 7.3.rc0 (NTL meanwhile at 9.8.1.p1, Singular still 3.1.7p1.p1).\n> \n> (Presumably just incidentally) doesn't happen with Sage's MPIR, currently 2.7.2.\n\\\\\n\nAnd the winners (apparently) are:\n\n  `_class__sage_combinat_sf_macdonald_MacdonaldPolynomials_*.sobj`\n\n(When I skip these six, I can successfully `unpickle_all()` as often as I want in a row.)",
    "created_at": "2016-08-01T04:46:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5838",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5838#issuecomment-45898",
    "user": "leif"
}
```

Replying to [comment:25 leif]:
> The second attempt to unpickle all crashes with both GMP 5.1.3, the current version in Sage, and GMP 6.1.1, in exactly the same manner as in the ticket description, with GCC 5.4.0, 6.1.0, and also Sage's GCC 4.9.3 (on Linux x86_64 at least).
> 
> Sage version 7.3.rc0 (NTL meanwhile at 9.8.1.p1, Singular still 3.1.7p1.p1).
> 
> (Presumably just incidentally) doesn't happen with Sage's MPIR, currently 2.7.2.
\\

And the winners (apparently) are:

  `_class__sage_combinat_sf_macdonald_MacdonaldPolynomials_*.sobj`

(When I skip these six, I can successfully `unpickle_all()` as often as I want in a row.)



---

archive/issue_comments_045899.json:
```json
{
    "body": "Don't know yet who's to blame (on Sage's side, perhaps Singular's), but I can pretty well imagine what's happening here; the only difference between MPIR and GMP here being that the latter reuses user-freed memory regions earlier than the former does.\n\nWill investigate later, haven't looked at the code yet.",
    "created_at": "2016-08-01T05:45:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5838",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5838#issuecomment-45899",
    "user": "leif"
}
```

Don't know yet who's to blame (on Sage's side, perhaps Singular's), but I can pretty well imagine what's happening here; the only difference between MPIR and GMP here being that the latter reuses user-freed memory regions earlier than the former does.

Will investigate later, haven't looked at the code yet.



---

archive/issue_comments_045900.json:
```json
{
    "body": "Replying to [comment:26 leif]:\n> And the winners (apparently) are:\n> \n>   `_class__sage_combinat_sf_macdonald_MacdonaldPolynomials_*.sobj`\n> \n> (When I skip these six, I can successfully `unpickle_all()` as often as I want in a row.)\n\nTo no surprise, these objects / classes have been added shortly before Carl Witty reported the issue (for Sage 3.4.1.rc3):\n\n```\ntype(obj) = <class 'sage.combinat.sf.macdonald.MacdonaldPolynomials_ht'>\nversion = 3.4.rc1\nobj =\n'Macdonald polynomials in the Ht basis over Fraction Field of Multivariate Polynomial Ring in q, t over Rational Field'\n\ntype(obj) = <class 'sage.combinat.sf.macdonald.MacdonaldPolynomials_h'>\nversion = 3.4.rc1\nobj =\n'Macdonald polynomials in the H basis over Fraction Field of Multivariate Polynomial Ring in q, t over Rational Field'\n\ntype(obj) = <class 'sage.combinat.sf.macdonald.MacdonaldPolynomials_j'>\nversion = 3.4.rc1\nobj =\n'Macdonald polynomials in the J basis over Fraction Field of Multivariate Polynomial Ring in q, t over Rational Field'\n\ntype(obj) = <class 'sage.combinat.sf.macdonald.MacdonaldPolynomials_p'>\nversion = 3.4.rc1\nobj =\n'Macdonald polynomials in the P basis over Fraction Field of Multivariate Polynomial Ring in q, t over Rational Field'\n\ntype(obj) = <class 'sage.combinat.sf.macdonald.MacdonaldPolynomials_q'>\nversion = 3.4.rc1\nobj =\n'Macdonald polynomials in the Q basis over Fraction Field of Multivariate Polynomial Ring in q, t over Rational Field'\n\ntype(obj) = <class 'sage.combinat.sf.macdonald.MacdonaldPolynomials_s'>\nversion = 3.4.rc1\nobj =\n'Macdonald polynomials in the S basis over Fraction Field of Multivariate Polynomial Ring in q, t over Rational Field'\n```\n",
    "created_at": "2016-08-01T06:18:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5838",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5838#issuecomment-45900",
    "user": "leif"
}
```

Replying to [comment:26 leif]:
> And the winners (apparently) are:
> 
>   `_class__sage_combinat_sf_macdonald_MacdonaldPolynomials_*.sobj`
> 
> (When I skip these six, I can successfully `unpickle_all()` as often as I want in a row.)

To no surprise, these objects / classes have been added shortly before Carl Witty reported the issue (for Sage 3.4.1.rc3):

```
type(obj) = <class 'sage.combinat.sf.macdonald.MacdonaldPolynomials_ht'>
version = 3.4.rc1
obj =
'Macdonald polynomials in the Ht basis over Fraction Field of Multivariate Polynomial Ring in q, t over Rational Field'

type(obj) = <class 'sage.combinat.sf.macdonald.MacdonaldPolynomials_h'>
version = 3.4.rc1
obj =
'Macdonald polynomials in the H basis over Fraction Field of Multivariate Polynomial Ring in q, t over Rational Field'

type(obj) = <class 'sage.combinat.sf.macdonald.MacdonaldPolynomials_j'>
version = 3.4.rc1
obj =
'Macdonald polynomials in the J basis over Fraction Field of Multivariate Polynomial Ring in q, t over Rational Field'

type(obj) = <class 'sage.combinat.sf.macdonald.MacdonaldPolynomials_p'>
version = 3.4.rc1
obj =
'Macdonald polynomials in the P basis over Fraction Field of Multivariate Polynomial Ring in q, t over Rational Field'

type(obj) = <class 'sage.combinat.sf.macdonald.MacdonaldPolynomials_q'>
version = 3.4.rc1
obj =
'Macdonald polynomials in the Q basis over Fraction Field of Multivariate Polynomial Ring in q, t over Rational Field'

type(obj) = <class 'sage.combinat.sf.macdonald.MacdonaldPolynomials_s'>
version = 3.4.rc1
obj =
'Macdonald polynomials in the S basis over Fraction Field of Multivariate Polynomial Ring in q, t over Rational Field'
```




---

archive/issue_comments_045901.json:
```json
{
    "body": "Replying to [comment:25 leif]:\n> The second attempt to unpickle all crashes with both GMP 5.1.3, the current version in Sage, and GMP 6.1.1, in exactly the same manner as in the ticket description, with GCC 5.4.0, 6.1.0, and also Sage's GCC 4.9.3 (on Linux x86_64 at least).\n> \n> Sage version 7.3.rc0 (NTL meanwhile at 9.8.1.p1, Singular still 3.1.7p1.p1).\n> \n> (Presumably just incidentally) doesn't happen with Sage's MPIR, currently 2.7.2.\n\nIndeed, since the above failure incidentally vanishes with #21188. (So far only tried with GMP 5.1.3 and GCC 4.9.3 though.)\n\nI.e., when building Sage / Singular with GMP, a `configure` test for FLINT in Singular failed because it used `-lmpir`, such that Singular and libsingular \"silently\" got built without using FLINT.",
    "created_at": "2016-08-09T15:37:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5838",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5838#issuecomment-45901",
    "user": "leif"
}
```

Replying to [comment:25 leif]:
> The second attempt to unpickle all crashes with both GMP 5.1.3, the current version in Sage, and GMP 6.1.1, in exactly the same manner as in the ticket description, with GCC 5.4.0, 6.1.0, and also Sage's GCC 4.9.3 (on Linux x86_64 at least).
> 
> Sage version 7.3.rc0 (NTL meanwhile at 9.8.1.p1, Singular still 3.1.7p1.p1).
> 
> (Presumably just incidentally) doesn't happen with Sage's MPIR, currently 2.7.2.

Indeed, since the above failure incidentally vanishes with #21188. (So far only tried with GMP 5.1.3 and GCC 4.9.3 though.)

I.e., when building Sage / Singular with GMP, a `configure` test for FLINT in Singular failed because it used `-lmpir`, such that Singular and libsingular "silently" got built without using FLINT.



---

archive/issue_comments_045902.json:
```json
{
    "body": "Changing keywords from \"\" to \"sage_object unpickle_all() NTL::InvMod abort inverse undefined\".",
    "created_at": "2016-08-09T15:55:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5838",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5838#issuecomment-45902",
    "user": "leif"
}
```

Changing keywords from "" to "sage_object unpickle_all() NTL::InvMod abort inverse undefined".



---

archive/issue_comments_045903.json:
```json
{
    "body": "I am seeing this doctest (2nd unpickling) failing on FreeBSD (see #22679).\n\nThis might be due to some toolchain issues I have there ATM (I see mysterious errors in sympow, depending upon unrecognised compiler options passed, or not...).",
    "created_at": "2017-04-14T16:22:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5838",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5838#issuecomment-45903",
    "user": "dimpase"
}
```

I am seeing this doctest (2nd unpickling) failing on FreeBSD (see #22679).

This might be due to some toolchain issues I have there ATM (I see mysterious errors in sympow, depending upon unrecognised compiler options passed, or not...).
