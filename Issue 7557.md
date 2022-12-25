# Issue 7557: conversion of complex numbers in symbolic expressions to maxima broken

archive/issues_007557.json:
```json
{
    "body": "Assignee: @burcin\n\nCC:  @kcrisman\n\nReported on sage-support:\n\n\n```\nvar('y', domain='real')\nassume(y, 'real')\n\nabs(exp(y*I)).simplify()\n    1\n\nabs(exp(1.1*y*I)).simplify()\n    e^(1.1*I*y)\n\nThe last result is incorrect. It seems simplify() doesn't like\nfloating point?\n```\n\n\nIn this thread:\n\nhttp://groups.google.com/group/sage-support/browse_thread/thread/c6d4c757cef8cc4a\n\n\nMore evidence:\n\n\n```\nsage: t = abs(exp(y*I)); t\nabs(e^(I*y))\nsage: t._maxima_init_()\n'abs(exp((y)*(0+%i*1)))'\n\nsage: u = abs(exp(1.1*y*I)); u\nabs(e^(1.10000000000000*I*y))\nsage: u._maxima_init_()\n'abs(exp((y)*(1.1000000000000001*I)))'\n```\n\n\nThis might be the reason:\n\n\n```\nsage: t.operands()[0].operands()[0].operands()[1].pyobject()\nI\nsage: type(t.operands()[0].operands()[0].operands()[1].pyobject())\n<type 'sage.rings.number_field.number_field_element_quadratic.NumberFieldElement_quadratic'>\n\nsage: u.operands()[0].operands()[0].operands()[1].pyobject()\n1.10000000000000*I\nsage: type(u.operands()[0].operands()[0].operands()[1].pyobject())\n<type 'sage.rings.complex_number.ComplexNumber'>\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7557\n\n",
    "created_at": "2009-11-30T09:58:16Z",
    "labels": [
        "component: symbolics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-5.7",
    "title": "conversion of complex numbers in symbolic expressions to maxima broken",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7557",
    "user": "https://github.com/burcin"
}
```
Assignee: @burcin

CC:  @kcrisman

Reported on sage-support:


```
var('y', domain='real')
assume(y, 'real')

abs(exp(y*I)).simplify()
    1

abs(exp(1.1*y*I)).simplify()
    e^(1.1*I*y)

The last result is incorrect. It seems simplify() doesn't like
floating point?
```


In this thread:

http://groups.google.com/group/sage-support/browse_thread/thread/c6d4c757cef8cc4a


More evidence:


```
sage: t = abs(exp(y*I)); t
abs(e^(I*y))
sage: t._maxima_init_()
'abs(exp((y)*(0+%i*1)))'

sage: u = abs(exp(1.1*y*I)); u
abs(e^(1.10000000000000*I*y))
sage: u._maxima_init_()
'abs(exp((y)*(1.1000000000000001*I)))'
```


This might be the reason:


```
sage: t.operands()[0].operands()[0].operands()[1].pyobject()
I
sage: type(t.operands()[0].operands()[0].operands()[1].pyobject())
<type 'sage.rings.number_field.number_field_element_quadratic.NumberFieldElement_quadratic'>

sage: u.operands()[0].operands()[0].operands()[1].pyobject()
1.10000000000000*I
sage: type(u.operands()[0].operands()[0].operands()[1].pyobject())
<type 'sage.rings.complex_number.ComplexNumber'>
```


Issue created by migration from https://trac.sagemath.org/ticket/7557





---

archive/issue_comments_064151.json:
```json
{
    "body": "The thread [here](http://groups.google.com/group/sage-support/browse_thread/thread/28bbd04a78dadb57/a6cbc2743ca47948) suggests perhaps this is fixed in Maxima 5.23.",
    "created_at": "2011-02-08T17:28:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7557",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7557#issuecomment-64151",
    "user": "https://github.com/kcrisman"
}
```

The thread [here](http://groups.google.com/group/sage-support/browse_thread/thread/28bbd04a78dadb57/a6cbc2743ca47948) suggests perhaps this is fixed in Maxima 5.23.



---

archive/issue_comments_064152.json:
```json
{
    "body": "Robert Dodier of Maxima suggests in [this sage-support thread](http://groups.google.com/group/sage-support/browse_thread/thread/28bbd04a78dadb57/d8db720220ee3508?show_docid=d8db720220ee3508#) that this should now be fixed.",
    "created_at": "2012-02-27T13:56:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7557",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7557#issuecomment-64152",
    "user": "https://github.com/kcrisman"
}
```

Robert Dodier of Maxima suggests in [this sage-support thread](http://groups.google.com/group/sage-support/browse_thread/thread/28bbd04a78dadb57/d8db720220ee3508?show_docid=d8db720220ee3508#) that this should now be fixed.



---

archive/issue_comments_064153.json:
```json
{
    "body": "Oops, those were the same thread!",
    "created_at": "2012-02-27T15:46:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7557",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7557#issuecomment-64153",
    "user": "https://github.com/kcrisman"
}
```

Oops, those were the same thread!



---

archive/issue_comments_064154.json:
```json
{
    "body": "Changing keywords from \"\" to \"interfaces\".",
    "created_at": "2012-11-20T09:53:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7557",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7557#issuecomment-64154",
    "user": "https://github.com/burcin"
}
```

Changing keywords from "" to "interfaces".



---

archive/issue_comments_064155.json:
```json
{
    "body": "[This sage-support thread](https://groups.google.com/d/topic/sage-support/mua3IYmrAWc/discussion) is also about the same problem. Patch coming up.",
    "created_at": "2012-11-20T09:53:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7557",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7557#issuecomment-64155",
    "user": "https://github.com/burcin"
}
```

[This sage-support thread](https://groups.google.com/d/topic/sage-support/mua3IYmrAWc/discussion) is also about the same problem. Patch coming up.



---

archive/issue_comments_064156.json:
```json
{
    "body": "Patch up. Please review.",
    "created_at": "2012-11-20T10:27:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7557",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7557#issuecomment-64156",
    "user": "https://github.com/burcin"
}
```

Patch up. Please review.



---

archive/issue_comments_064157.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2012-11-20T10:27:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7557",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7557#issuecomment-64157",
    "user": "https://github.com/burcin"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_064158.json:
```json
{
    "body": "I updated the patch with a minor doctest correction in `expression.pyx`.",
    "created_at": "2012-11-20T10:45:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7557",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7557#issuecomment-64158",
    "user": "https://github.com/burcin"
}
```

I updated the patch with a minor doctest correction in `expression.pyx`.



---

archive/issue_comments_064159.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-11-20T13:21:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7557",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7557#issuecomment-64159",
    "user": "https://github.com/vbraun"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_064160.json:
```json
{
    "body": "Looks good to me!",
    "created_at": "2012-11-20T13:21:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7557",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7557#issuecomment-64160",
    "user": "https://github.com/vbraun"
}
```

Looks good to me!



---

archive/issue_comments_064161.json:
```json
{
    "body": "Am I testing this correctly? I don't see any change:\n\n\n```\n0 jan@osprey:~/sage/sage-5.4/devel$hg qpush \napplying trac_7557-maxima_complex_number_conversion.patch\nnow at: trac_7557-maxima_complex_number_conversion.patch\n0 jan@osprey:~/sage/sage-5.4/devel$hg qapplied\ntrac_7557-maxima_complex_number_conversion.patch\n0 jan@osprey:~/sage/sage-5.4/devel$mysage -b complexbug\n\n----------------------------------------------------------\nsage: Building and installing modified Sage library files.\n\n\nInstalling c_lib\nscons: `install' is up to date.\nUpdating Cython code....\nExecuting 0 commands (using 1 thread)\nTime to execute 0 commands: 0.0179660320282 seconds\nFinished compiling Cython code (time = 0.490197181702 seconds)\nrunning install\nrunning build\nrunning build_py\nrunning build_ext\nExecuting 0 commands (using 1 thread)\nTime to execute 0 commands: 0.00303983688354 seconds\nTotal time spent compiling C/C++ extensions:  0.0404081344604 seconds.\nrunning install_lib\nrunning install_egg_info\nRemoving /home/jan/sage/sage-5.4/local/lib/python2.7/site-packages/sage-0.0.0-py2.7.egg-info\nWriting /home/jan/sage/sage-5.4/local/lib/python2.7/site-packages/sage-0.0.0-py2.7.egg-info\n\nreal\t0m1.531s\nuser\t0m1.112s\nsys\t0m0.240s\n0 jan@osprey:~/sage/sage-5.4/devel$mysage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n^[[ALoading Sage library. Current Mercurial branch is: complexbug\nsage: u=1.2; m=0.5; jacobi('sn',u,m)          \n0.887715488619\nsage: jacobi('sn',u+2*I*elliptic_kc(1-m),m)   \njacobi_sn(1.2 + 3.7081493546*I, 0.500000000000000)\nsage: n(jacobi('sn',u+2*I*elliptic_kc(1-m),m))\n| Sage Version 5.4, Release Date: 2012-11-09                         |\n| Type \"notebook()\" for the browser-based notebook interface.        |\n| Type \"help()\" for help.                                            |\n```\n\n\n(Hangs, I interrupted it after 30 seconds. Running this calculation directly in maxima takes one second)",
    "created_at": "2012-11-20T15:47:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7557",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7557#issuecomment-64161",
    "user": "https://github.com/pipedream"
}
```

Am I testing this correctly? I don't see any change:


```
0 jan@osprey:~/sage/sage-5.4/devel$hg qpush 
applying trac_7557-maxima_complex_number_conversion.patch
now at: trac_7557-maxima_complex_number_conversion.patch
0 jan@osprey:~/sage/sage-5.4/devel$hg qapplied
trac_7557-maxima_complex_number_conversion.patch
0 jan@osprey:~/sage/sage-5.4/devel$mysage -b complexbug

----------------------------------------------------------
sage: Building and installing modified Sage library files.


Installing c_lib
scons: `install' is up to date.
Updating Cython code....
Executing 0 commands (using 1 thread)
Time to execute 0 commands: 0.0179660320282 seconds
Finished compiling Cython code (time = 0.490197181702 seconds)
running install
running build
running build_py
running build_ext
Executing 0 commands (using 1 thread)
Time to execute 0 commands: 0.00303983688354 seconds
Total time spent compiling C/C++ extensions:  0.0404081344604 seconds.
running install_lib
running install_egg_info
Removing /home/jan/sage/sage-5.4/local/lib/python2.7/site-packages/sage-0.0.0-py2.7.egg-info
Writing /home/jan/sage/sage-5.4/local/lib/python2.7/site-packages/sage-0.0.0-py2.7.egg-info

real	0m1.531s
user	0m1.112s
sys	0m0.240s
0 jan@osprey:~/sage/sage-5.4/devel$mysage
----------------------------------------------------------------------
----------------------------------------------------------------------
^[[ALoading Sage library. Current Mercurial branch is: complexbug
sage: u=1.2; m=0.5; jacobi('sn',u,m)          
0.887715488619
sage: jacobi('sn',u+2*I*elliptic_kc(1-m),m)   
jacobi_sn(1.2 + 3.7081493546*I, 0.500000000000000)
sage: n(jacobi('sn',u+2*I*elliptic_kc(1-m),m))
| Sage Version 5.4, Release Date: 2012-11-09                         |
| Type "notebook()" for the browser-based notebook interface.        |
| Type "help()" for help.                                            |
```


(Hangs, I interrupted it after 30 seconds. Running this calculation directly in maxima takes one second)



---

archive/issue_comments_064162.json:
```json
{
    "body": "You need the latest Sage version. On Sage-5.5.rc0 + the patch from this ticket I get the following:\n\n```\nsage: u=1.2; m=0.5; jacobi('sn',u,m)\n0.887715488619\nsage: jacobi('sn',u+2*I*elliptic_kc(1-m),m)   \n0.887715488619 - 1.79195288805e-15*I\nsage: n(jacobi('sn',u+2*I*elliptic_kc(1-m),m))\n0.887715488619280 - 1.79195288804672e-15*I\n```\n\nso it works as it should.",
    "created_at": "2012-11-20T21:00:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7557",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7557#issuecomment-64162",
    "user": "https://github.com/vbraun"
}
```

You need the latest Sage version. On Sage-5.5.rc0 + the patch from this ticket I get the following:

```
sage: u=1.2; m=0.5; jacobi('sn',u,m)
0.887715488619
sage: jacobi('sn',u+2*I*elliptic_kc(1-m),m)   
0.887715488619 - 1.79195288805e-15*I
sage: n(jacobi('sn',u+2*I*elliptic_kc(1-m),m))
0.887715488619280 - 1.79195288804672e-15*I
```

so it works as it should.



---

archive/issue_comments_064163.json:
```json
{
    "body": "Great work, Burcin!",
    "created_at": "2012-11-20T21:30:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7557",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7557#issuecomment-64163",
    "user": "https://github.com/kcrisman"
}
```

Great work, Burcin!



---

archive/issue_comments_064164.json:
```json
{
    "body": "The documentation isn't properly formatted:\n\n```\ndocstring of sage.symbolic.expression.Expression.abs:24: WARNING: Literal block expected; none found.\n```\n",
    "created_at": "2012-12-18T14:56:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7557",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7557#issuecomment-64164",
    "user": "https://github.com/jdemeyer"
}
```

The documentation isn't properly formatted:

```
docstring of sage.symbolic.expression.Expression.abs:24: WARNING: Literal block expected; none found.
```




---

archive/issue_comments_064165.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2012-12-18T14:56:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7557",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7557#issuecomment-64165",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_064166.json:
```json
{
    "body": "Attachment [trac_7557-maxima_complex_number_conversion.2.patch](tarball://root/attachments/some-uuid/ticket7557/trac_7557-maxima_complex_number_conversion.2.patch) by @kcrisman created at 2012-12-18 15:02:37\n\nUse this patch",
    "created_at": "2012-12-18T15:02:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7557",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7557#issuecomment-64166",
    "user": "https://github.com/kcrisman"
}
```

Attachment [trac_7557-maxima_complex_number_conversion.2.patch](tarball://root/attachments/some-uuid/ticket7557/trac_7557-maxima_complex_number_conversion.2.patch) by @kcrisman created at 2012-12-18 15:02:37

Use this patch



---

archive/issue_comments_064167.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2012-12-18T15:03:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7557",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7557#issuecomment-64167",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_064168.json:
```json
{
    "body": "I think this one should work?\n\nPatchbot, apply trac_7557-maxima_complex_number_conversion.2.patch",
    "created_at": "2012-12-18T15:03:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7557",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7557#issuecomment-64168",
    "user": "https://github.com/kcrisman"
}
```

I think this one should work?

Patchbot, apply trac_7557-maxima_complex_number_conversion.2.patch



---

archive/issue_comments_064169.json:
```json
{
    "body": "On arando (32-bit Linux i686) and possibly all 32-bit systems:\n\n```\nsage -t  --long -force_lib devel/sage/sage/functions/special.py\n**********************************************************************\nFile \"/var/lib/buildbot/build/sage/arando-1/arando_full/build/sage-5.6.beta1/devel/sage-main/sage/functions/special.py\", line 481:\n    sage: t._maxima_init_(maxima)\nExpected:\n    '0.88771548861927996 - 1.7919528880467190e-15*%i'\nGot:\n    '0.88771548861927740 - 4.3254035228713778e-16*%i'\n**********************************************************************\nFile \"/var/lib/buildbot/build/sage/arando-1/arando_full/build/sage-5.6.beta1/devel/sage-main/sage/functions/special.py\", line 483:\n    sage: t.n()\nExpected:\n    0.887715488619280 - 1.79195288804672e-15*I\nGot:\n    0.887715488619277 - 4.32540352287138e-16*I\n**********************************************************************\n```\n",
    "created_at": "2012-12-19T21:12:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7557",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7557#issuecomment-64169",
    "user": "https://github.com/jdemeyer"
}
```

On arando (32-bit Linux i686) and possibly all 32-bit systems:

```
sage -t  --long -force_lib devel/sage/sage/functions/special.py
**********************************************************************
File "/var/lib/buildbot/build/sage/arando-1/arando_full/build/sage-5.6.beta1/devel/sage-main/sage/functions/special.py", line 481:
    sage: t._maxima_init_(maxima)
Expected:
    '0.88771548861927996 - 1.7919528880467190e-15*%i'
Got:
    '0.88771548861927740 - 4.3254035228713778e-16*%i'
**********************************************************************
File "/var/lib/buildbot/build/sage/arando-1/arando_full/build/sage-5.6.beta1/devel/sage-main/sage/functions/special.py", line 483:
    sage: t.n()
Expected:
    0.887715488619280 - 1.79195288804672e-15*I
Got:
    0.887715488619277 - 4.32540352287138e-16*I
**********************************************************************
```




---

archive/issue_comments_064170.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2012-12-19T21:12:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7557",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7557#issuecomment-64170",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_064171.json:
```json
{
    "body": "*** ping ***\n\nUsing `# abs tol` should fix these.",
    "created_at": "2013-01-10T15:38:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7557",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7557#issuecomment-64171",
    "user": "https://github.com/jdemeyer"
}
```

*** ping ***

Using `# abs tol` should fix these.



---

archive/issue_comments_064172.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2013-01-10T16:06:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7557",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7557#issuecomment-64172",
    "user": "https://github.com/burcin"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_064173.json:
```json
{
    "body": "Thanks for the reminder Jeroen.",
    "created_at": "2013-01-10T16:06:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7557",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7557#issuecomment-64173",
    "user": "https://github.com/burcin"
}
```

Thanks for the reminder Jeroen.



---

archive/issue_comments_064174.json:
```json
{
    "body": "I get \n\n```\n\nsage -t  \"devel/sage-main/sage/functions/special.py\"        \n    ... ''', res, 1e-13, 'ab\n    ^\nSyntaxError: invalid syntax\n\n\t [0.2 s]\n \n----------------------------------------------------------------------\nThe following tests failed:\n\n\n\tsage -t  \"devel/sage-main/sage/functions/special.py\"\nTotal time for all tests: 0.2 seconds\n```\n\nNot sure what happened here.  This is on 64-bit, apparently - I get the old answer.",
    "created_at": "2013-01-10T16:49:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7557",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7557#issuecomment-64174",
    "user": "https://github.com/kcrisman"
}
```

I get 

```

sage -t  "devel/sage-main/sage/functions/special.py"        
    ... ''', res, 1e-13, 'ab
    ^
SyntaxError: invalid syntax

	 [0.2 s]
 
----------------------------------------------------------------------
The following tests failed:


	sage -t  "devel/sage-main/sage/functions/special.py"
Total time for all tests: 0.2 seconds
```

Not sure what happened here.  This is on 64-bit, apparently - I get the old answer.



---

archive/issue_comments_064175.json:
```json
{
    "body": "Here's the relevant part from the tmp file.\n\n```\n\n        TESTS:\n\n        Check if complex numbers in the arguments are converted to maxima\n        correctly :trac:`7557`::\n\n            >>> t = jacobi('sn',RealNumber('1.2')+Integer(2)*I*elliptic_kc(Integer(1)-RealNumber('.5')),RealNumber('.5'))###line 480:_sage_    >>> t = jacobi($\n            >>> t._maxima_init_(maxima)###line 481:_sage_    >>> t._maxima_init_(maxima)\n            '0.88771548861927...*%i'\n>>> res = Exception\n>>> res =  t.n() # abs tol 1e-13###line 483:_sage_    >>> t.n() # abs tol 1e-13\n>>> check_with_tolerance('''\n...             0.887715488619280 - 1.79195288804672e-15*I\n...         \"\"\"\n... ''', res, 1e-13, 'ab\n>>> sig_on_count()\n0\n\"\"\"\n```\n\nSo this might be something that only works with a working abs tol, which I may not yet have - is this based on beta3 or beta2?  I haven't compiled beta3 yet since I can't upgrade it ;-)",
    "created_at": "2013-01-10T16:52:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7557",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7557#issuecomment-64175",
    "user": "https://github.com/kcrisman"
}
```

Here's the relevant part from the tmp file.

```

        TESTS:

        Check if complex numbers in the arguments are converted to maxima
        correctly :trac:`7557`::

            >>> t = jacobi('sn',RealNumber('1.2')+Integer(2)*I*elliptic_kc(Integer(1)-RealNumber('.5')),RealNumber('.5'))###line 480:_sage_    >>> t = jacobi($
            >>> t._maxima_init_(maxima)###line 481:_sage_    >>> t._maxima_init_(maxima)
            '0.88771548861927...*%i'
>>> res = Exception
>>> res =  t.n() # abs tol 1e-13###line 483:_sage_    >>> t.n() # abs tol 1e-13
>>> check_with_tolerance('''
...             0.887715488619280 - 1.79195288804672e-15*I
...         """
... ''', res, 1e-13, 'ab
>>> sig_on_count()
0
"""
```

So this might be something that only works with a working abs tol, which I may not yet have - is this based on beta3 or beta2?  I haven't compiled beta3 yet since I can't upgrade it ;-)



---

archive/issue_comments_064176.json:
```json
{
    "body": "Attachment [trac_7557-fix_doctest_precision.patch](tarball://root/attachments/some-uuid/ticket7557/trac_7557-fix_doctest_precision.patch) by @burcin created at 2013-01-11 13:17:31",
    "created_at": "2013-01-11T13:17:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7557",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7557#issuecomment-64176",
    "user": "https://github.com/burcin"
}
```

Attachment [trac_7557-fix_doctest_precision.patch](tarball://root/attachments/some-uuid/ticket7557/trac_7557-fix_doctest_precision.patch) by @burcin created at 2013-01-11 13:17:31



---

archive/issue_comments_064177.json:
```json
{
    "body": "Replying to [comment:16 kcrisman]:\n> {{{\n> \n> sage -t  \"devel/sage-main/sage/functions/special.py\"        \n>     ... ''', res, 1e-13, 'ab\n>     ^\n> SyntaxError: invalid syntax\n> }}}\n\nThis seems to be a problem with the `sage-doctest` script. If the triple-quotes immediately follow the doctest result, it generates a temporary file with a syntax error. I cleaned up the patch before submitting, but didn't realize deleting empty lines could cause doctest failures.\n\nI uploaded a new patch with the same name. It should work now.\n\nI don't have time to open a ticket for the `sage-doctest` bug right now.",
    "created_at": "2013-01-11T13:23:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7557",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7557#issuecomment-64177",
    "user": "https://github.com/burcin"
}
```

Replying to [comment:16 kcrisman]:
> {{{
> 
> sage -t  "devel/sage-main/sage/functions/special.py"        
>     ... ''', res, 1e-13, 'ab
>     ^
> SyntaxError: invalid syntax
> }}}

This seems to be a problem with the `sage-doctest` script. If the triple-quotes immediately follow the doctest result, it generates a temporary file with a syntax error. I cleaned up the patch before submitting, but didn't realize deleting empty lines could cause doctest failures.

I uploaded a new patch with the same name. It should work now.

I don't have time to open a ticket for the `sage-doctest` bug right now.



---

archive/issue_comments_064178.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-01-11T17:11:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7557",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7557#issuecomment-64178",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_064179.json:
```json
{
    "body": "Seems fine now, thanks.  I don't have a 32-bit system to test this on, though.\n\nPatchbot, apply trac_7557-maxima_complex_number_conversion.2.patch and trac_7557-fix_doctest_precision.patch",
    "created_at": "2013-01-11T17:11:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7557",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7557#issuecomment-64179",
    "user": "https://github.com/kcrisman"
}
```

Seems fine now, thanks.  I don't have a 32-bit system to test this on, though.

Patchbot, apply trac_7557-maxima_complex_number_conversion.2.patch and trac_7557-fix_doctest_precision.patch



---

archive/issue_comments_064180.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2013-01-21T21:07:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7557",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7557#issuecomment-64180",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed
