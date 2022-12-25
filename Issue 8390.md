# Issue 8390: Find all roots of a trigonometric equation

archive/issues_008390.json:
```json
{
    "body": "Assignee: olazo\n\nCC:  @robert-marik @kcrisman @mwhansen\n\nKeywords: trigonometric, roots\n\nWhen using\n\n\n```\nx,y=var('x,y')\nsolve([sin(2*x-pi/6)==1/2],x)\n```\n\n\nsage returns [x == 1/6*pi]. Which is correct, but we would wish to have all roots. This can be done with:\n\n\n```\nsolve([sin(2*x-pi/6)==y,y==1/2],[x,y])\n```\n\n\nwhich returns [[x == 1/2*pi + pi*z5, y == (1/2)], [x == 1/6*pi + pi*z7, y == (1/2)]]\n\nBut this is a very weird way to do things. Surely solve([sin(2*x-pi/6)==y,y==1/2],[x,y]) should also give all roots.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8390\n\n",
    "created_at": "2010-02-27T19:07:36Z",
    "labels": [
        "component: algebra",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4",
    "title": "Find all roots of a trigonometric equation",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8390",
    "user": "https://trac.sagemath.org/admin/accounts/users/olazo"
}
```
Assignee: olazo

CC:  @robert-marik @kcrisman @mwhansen

Keywords: trigonometric, roots

When using


```
x,y=var('x,y')
solve([sin(2*x-pi/6)==1/2],x)
```


sage returns [x == 1/6*pi]. Which is correct, but we would wish to have all roots. This can be done with:


```
solve([sin(2*x-pi/6)==y,y==1/2],[x,y])
```


which returns [[x == 1/2*pi + pi*z5, y == (1/2)], [x == 1/6*pi + pi*z7, y == (1/2)]]

But this is a very weird way to do things. Surely solve([sin(2*x-pi/6)==y,y==1/2],[x,y]) should also give all roots.

Issue created by migration from https://trac.sagemath.org/ticket/8390





---

archive/issue_comments_075005.json:
```json
{
    "body": "CCing our maxima experts--this looks like it might be a problem with maxima.",
    "created_at": "2010-02-27T19:33:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8390",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8390#issuecomment-75005",
    "user": "https://github.com/jasongrout"
}
```

CCing our maxima experts--this looks like it might be a problem with maxima.



---

archive/issue_comments_075006.json:
```json
{
    "body": "Sage interface for Maxima's solver works like this:\n\nWe try Maxima's solve function first. It we get empty answer, we try the to_poly_solve for the same equation.\n\nIf the answer is not empty, we pass the answer of solve command to Maxima's to_poly_solve.\n\nFor our equation, solve command in Maxima gives only one solution pi/6 (and probably writes something like \"SOLVE is using arc-trig functions to get a solution. Some solutions will be lost.\" on terminal).\n\n\n```\n[marik@um-bc107 /opt/sage]$ ./sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: eq = sin(2*x-pi/6) == 1/2\nsage: eq._maxima_().solve(x)\n[x=%pi/6]\nsage: eq._maxima_().to_poly_solve(x)\n%union([x=-(-2*%pi*%z6-%pi)/2],[x=-(-2*%pi*%z8-%pi/3)/2])\nsage:\n```\n\n| Sage Version 4.3.2, Release Date: 2010-02-06                       |\n| Type notebook() for the GUI, and license() for information.        |\nI hope this is an explanation. I do not have enough experiences with to_poly_solve, so my questions are: Is it good idea to skip solve and use to_poly_solve immediatelly when to_poly_sole = True? Or is it posssible to check from within Sage, that the warning about arc-trig functions has been printed? Or introduce to_poly_solve = 'force' to omit solve command?\n\nNow you can use \n\n```\nsage: eq._maxima_().to_poly_solve(x).sage()\n[[x == 1/2*pi + pi*z16], [x == 1/6*pi + pi*z18]]\n```\n",
    "created_at": "2010-02-27T21:08:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8390",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8390#issuecomment-75006",
    "user": "https://github.com/robert-marik"
}
```

Sage interface for Maxima's solver works like this:

We try Maxima's solve function first. It we get empty answer, we try the to_poly_solve for the same equation.

If the answer is not empty, we pass the answer of solve command to Maxima's to_poly_solve.

For our equation, solve command in Maxima gives only one solution pi/6 (and probably writes something like "SOLVE is using arc-trig functions to get a solution. Some solutions will be lost." on terminal).


```
[marik@um-bc107 /opt/sage]$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: eq = sin(2*x-pi/6) == 1/2
sage: eq._maxima_().solve(x)
[x=%pi/6]
sage: eq._maxima_().to_poly_solve(x)
%union([x=-(-2*%pi*%z6-%pi)/2],[x=-(-2*%pi*%z8-%pi/3)/2])
sage:
```

| Sage Version 4.3.2, Release Date: 2010-02-06                       |
| Type notebook() for the GUI, and license() for information.        |
I hope this is an explanation. I do not have enough experiences with to_poly_solve, so my questions are: Is it good idea to skip solve and use to_poly_solve immediatelly when to_poly_sole = True? Or is it posssible to check from within Sage, that the warning about arc-trig functions has been printed? Or introduce to_poly_solve = 'force' to omit solve command?

Now you can use 

```
sage: eq._maxima_().to_poly_solve(x).sage()
[[x == 1/2*pi + pi*z16], [x == 1/6*pi + pi*z18]]
```




---

archive/issue_comments_075007.json:
```json
{
    "body": "temporary patch:\n\n```\ndiff -r 799f70320d89 sage/symbolic/expression.pyx\n--- a/sage/symbolic/expression.pyx      Thu Feb 11 09:03:17 2010 -0800\n+++ b/sage/symbolic/expression.pyx      Sun Feb 28 16:16:33 2010 +0100\n@@ -6501,7 +6501,7 @@\n         # solutions being returned.                            #\n         ########################################################\n         if to_poly_solve and not multiplicities:\n-            if len(X)==0: # if Maxima's solve gave no solutions, only try it\n+            if len(X)==0 or to_poly_solve == 'force': # if Maxima's solve gave no solutions, only try it\n                 try:\n                     s = m.to_poly_solve(x)\n                     T = string_to_list_of_solutions(repr(s))\n```\n\n\nallows this\n\n```\n[marik@taxus ../sage-4.3.3.alpha0]$ ./sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n**********************************************************************\n*                                                                    *\n* Warning: this is a prerelease version, and it may be unstable.     *\n*                                                                    *\n**********************************************************************\nsage: solve(sin(x)==1/2,x)\n[x == 1/6*pi]\nsage: solve(sin(x)==1/2,x,to_poly_solve = 'force')\n[x == 5/6*pi + 2*pi*z8, x == 1/6*pi + 2*pi*z6]\nsage:\n```\n",
    "created_at": "2010-02-28T15:17:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8390",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8390#issuecomment-75007",
    "user": "https://github.com/robert-marik"
}
```

temporary patch:

```
diff -r 799f70320d89 sage/symbolic/expression.pyx
--- a/sage/symbolic/expression.pyx      Thu Feb 11 09:03:17 2010 -0800
+++ b/sage/symbolic/expression.pyx      Sun Feb 28 16:16:33 2010 +0100
@@ -6501,7 +6501,7 @@
         # solutions being returned.                            #
         ########################################################
         if to_poly_solve and not multiplicities:
-            if len(X)==0: # if Maxima's solve gave no solutions, only try it
+            if len(X)==0 or to_poly_solve == 'force': # if Maxima's solve gave no solutions, only try it
                 try:
                     s = m.to_poly_solve(x)
                     T = string_to_list_of_solutions(repr(s))
```


allows this

```
[marik@taxus ../sage-4.3.3.alpha0]$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
**********************************************************************
*                                                                    *
* Warning: this is a prerelease version, and it may be unstable.     *
*                                                                    *
**********************************************************************
sage: solve(sin(x)==1/2,x)
[x == 1/6*pi]
sage: solve(sin(x)==1/2,x,to_poly_solve = 'force')
[x == 5/6*pi + 2*pi*z8, x == 1/6*pi + 2*pi*z6]
sage:
```




---

archive/issue_comments_075008.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-28T23:42:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8390",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8390#issuecomment-75008",
    "user": "https://github.com/robert-marik"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_075009.json:
```json
{
    "body": "The patch is attached. Code starts at line 6564. The rest is from reindent.py (I got memory error when testing).\n\nThe patch introduces option to_poly_solve='force'. Perhaps, could be done automatically in future when invcerse trigonometric functions appear. Needs some coding in Lisp and changes in Maxima, see [Maxima forum](http://thread.gmane.org/gmane.comp.mathematics.maxima.general/29966/focus=29974).",
    "created_at": "2010-02-28T23:42:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8390",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8390#issuecomment-75009",
    "user": "https://github.com/robert-marik"
}
```

The patch is attached. Code starts at line 6564. The rest is from reindent.py (I got memory error when testing).

The patch introduces option to_poly_solve='force'. Perhaps, could be done automatically in future when invcerse trigonometric functions appear. Needs some coding in Lisp and changes in Maxima, see [Maxima forum](http://thread.gmane.org/gmane.comp.mathematics.maxima.general/29966/focus=29974).



---

archive/issue_comments_075010.json:
```json
{
    "body": "Attachment [trac-8390.patch](tarball://root/attachments/some-uuid/ticket8390/trac-8390.patch) by @robert-marik created at 2010-04-06 20:51:20\n\nrebased for Sage 4.3.5",
    "created_at": "2010-04-06T20:51:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8390",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8390#issuecomment-75010",
    "user": "https://github.com/robert-marik"
}
```

Attachment [trac-8390.patch](tarball://root/attachments/some-uuid/ticket8390/trac-8390.patch) by @robert-marik created at 2010-04-06 20:51:20

rebased for Sage 4.3.5



---

archive/issue_comments_075011.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-04-07T14:07:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8390",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8390#issuecomment-75011",
    "user": "https://github.com/williamstein"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_075012.json:
```json
{
    "body": "The code looks fine to me. I agree that the interface is not so elegant, since it's somewhat tied to Maxima, and it's uncomfortable to have an input (to_poly_solve) be either bool or string.  However, I can't really think of anything better given the design decisions we've already made. \n\nAll tests pass.",
    "created_at": "2010-04-07T14:07:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8390",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8390#issuecomment-75012",
    "user": "https://github.com/williamstein"
}
```

The code looks fine to me. I agree that the interface is not so elegant, since it's somewhat tied to Maxima, and it's uncomfortable to have an input (to_poly_solve) be either bool or string.  However, I can't really think of anything better given the design decisions we've already made. 

All tests pass.



---

archive/issue_comments_075013.json:
```json
{
    "body": "Merged trac-8390.patch in 4.4.alpha0",
    "created_at": "2010-04-15T20:11:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8390",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8390#issuecomment-75013",
    "user": "https://github.com/jhpalmieri"
}
```

Merged trac-8390.patch in 4.4.alpha0



---

archive/issue_events_008575.json:
```json
{
    "actor": "https://github.com/jhpalmieri",
    "created_at": "2010-04-15T20:11:34Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8390",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8390#event-8575"
}
```



---

archive/issue_comments_075014.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-15T20:11:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8390",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8390#issuecomment-75014",
    "user": "https://github.com/jhpalmieri"
}
```

Resolution: fixed
