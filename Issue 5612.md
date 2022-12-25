# Issue 5612: docs for solving a system of linear equations symbolically using symbolic matrices

archive/issues_005612.json:
```json
{
    "body": "Assignee: @williamstein\n\nThis should go into some docs somewhere.  Maybe under solve_right or in a primer?\n\nIt's to solve the linear system a*x+b*y=3, c*x+d*y=5.\n\n\n```\nsage: var('a,b,c,d,x,y')\n(a, b, c, d, x, y)\nsage: A=matrix(2,[a,b,c,d]); A\n[a b]\n[c d]\nsage: result=vector([3,5]); result\n(3, 5)\nsage: soln=A.solve_right(result) # you could also do soln=A\\result\nsage: soln\n(3/a - b*(5 - 3*c/a)/(a*(d - b*c/a)), (5 - 3*c/a)/(d - b*c/a))\n\n\nNow, checking our answers:\n\n\nsage: (a*x+b*y).subs(x=soln[0],y=soln[1]).simplify_full()\n3\nsage: (c*x+d*y).subs(x=soln[0],y=soln[1]).simplify_full()\n5\n\n\nOr just checking it with matrix multiplication:\n\nsage: A*soln\n(a*(3/a - b*(5 - 3*c/a)/(a*(d - b*c/a))) + b*(5 - 3*c/a)/(d - b*c/a), \nc*(3/a - b*(5 - 3*c/a)/(a*(d - b*c/a))) + (5 - 3*c/a)*d/(d - b*c/a))\n\nLet's simplify each entry by applying the \"simplify_full\" function to \neach entry:\n\nsage: (A*soln).apply_map(lambda x: x.simplify_full())\n(3, 5)\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5612\n\n",
    "created_at": "2009-03-25T23:42:55Z",
    "labels": [
        "component: linear algebra",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-5.3",
    "title": "docs for solving a system of linear equations symbolically using symbolic matrices",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5612",
    "user": "https://github.com/jasongrout"
}
```
Assignee: @williamstein

This should go into some docs somewhere.  Maybe under solve_right or in a primer?

It's to solve the linear system a*x+b*y=3, c*x+d*y=5.


```
sage: var('a,b,c,d,x,y')
(a, b, c, d, x, y)
sage: A=matrix(2,[a,b,c,d]); A
[a b]
[c d]
sage: result=vector([3,5]); result
(3, 5)
sage: soln=A.solve_right(result) # you could also do soln=A\result
sage: soln
(3/a - b*(5 - 3*c/a)/(a*(d - b*c/a)), (5 - 3*c/a)/(d - b*c/a))


Now, checking our answers:


sage: (a*x+b*y).subs(x=soln[0],y=soln[1]).simplify_full()
3
sage: (c*x+d*y).subs(x=soln[0],y=soln[1]).simplify_full()
5


Or just checking it with matrix multiplication:

sage: A*soln
(a*(3/a - b*(5 - 3*c/a)/(a*(d - b*c/a))) + b*(5 - 3*c/a)/(d - b*c/a), 
c*(3/a - b*(5 - 3*c/a)/(a*(d - b*c/a))) + (5 - 3*c/a)*d/(d - b*c/a))

Let's simplify each entry by applying the "simplify_full" function to 
each entry:

sage: (A*soln).apply_map(lambda x: x.simplify_full())
(3, 5)
```



Issue created by migration from https://trac.sagemath.org/ticket/5612





---

archive/issue_comments_043745.json:
```json
{
    "body": "Make sure to change \n\n```\nmatrix(2,[a,b,c,d])\nvector([3,5])\n```\n\n\nto\n\n\n```\nmatrix(SR,2,[a,b,c,d])\nvector(SR,[3,5])\n```\n\n\nsince otherwise people get really confused when slight changes lead to breakage (e.g., see sage-support).\n\nAlso, I'm concerned about the large number of wishlist-style trac tickets you've been creating lately, like this one.  If everybody made tickets like you're doing it about similar things, trac would soon become unusable.",
    "created_at": "2009-03-26T15:22:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5612",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5612#issuecomment-43745",
    "user": "https://github.com/williamstein"
}
```

Make sure to change 

```
matrix(2,[a,b,c,d])
vector([3,5])
```


to


```
matrix(SR,2,[a,b,c,d])
vector(SR,[3,5])
```


since otherwise people get really confused when slight changes lead to breakage (e.g., see sage-support).

Also, I'm concerned about the large number of wishlist-style trac tickets you've been creating lately, like this one.  If everybody made tickets like you're doing it about similar things, trac would soon become unusable.



---

archive/issue_comments_043746.json:
```json
{
    "body": "Well, we're told to make a trac ticket for every item, so I'm also using it as a to-do list for when I have a few minutes.  In reality, I just made this a trac ticket because of the specific request on the sage lists; I wasn't planning on making it a trac ticket originally.  When I have a few minutes, I can just go to tickets that I've created, pick one that fits into the time I have, and make a patch.\n\nI can make them all attached to the wishlist milestone, if that's better.\n\nI was going to make all the color items a single ticket, but then I remembered the rebukes I've received about lumping too much together on a ticket...",
    "created_at": "2009-03-26T17:43:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5612",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5612#issuecomment-43746",
    "user": "https://github.com/jasongrout"
}
```

Well, we're told to make a trac ticket for every item, so I'm also using it as a to-do list for when I have a few minutes.  In reality, I just made this a trac ticket because of the specific request on the sage lists; I wasn't planning on making it a trac ticket originally.  When I have a few minutes, I can just go to tickets that I've created, pick one that fits into the time I have, and make a patch.

I can make them all attached to the wishlist milestone, if that's better.

I was going to make all the color items a single ticket, but then I remembered the rebukes I've received about lumping too much together on a ticket...



---

archive/issue_comments_043747.json:
```json
{
    "body": "Changing keywords from \"\" to \"beginner\".",
    "created_at": "2010-09-03T21:24:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5612",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5612#issuecomment-43747",
    "user": "https://github.com/jasongrout"
}
```

Changing keywords from "" to "beginner".



---

archive/issue_comments_043748.json:
```json
{
    "body": "Guys, when I try this out, I get to the following line and get the following error (both ways):\n\n\n\n```\nsoln=A.solve_right(result) # you could also do soln=A\\result\n```\n\n\n\n```\nTraceback (most recent call last):\n  File \"<stdin>\", line 1, in <module>\n  File \"_sage_input_15.py\", line 10, in <module>\n    exec compile(u'open(\"___code___.py\",\"w\").write(\"# -*- coding: utf-8 -*-\\\\n\" + _support_.preparse_worksheet_cell(base64.b64decode(\"c29sbj1BLnNvbHZlX3JpZ2h0KHJlc3VsdCkgIyB5b3UgY291bGQgYWxzbyBkbyBzb2xuPUFccmVzdWx0\"),globals())+\"\\\\n\"); execfile(os.path.abspath(\"___code___.py\"))\n  File \"\", line 1, in <module>\n    \n  File \"/tmp/tmpJ1xbYN/___code___.py\", line 2, in <module>\n    exec compile(u'soln=A.solve_right(result) # you could also do soln=A\\\\result\n  File \"\", line 1, in <module>\n    \n  File \"matrix2.pyx\", line 281, in sage.matrix.matrix2.Matrix.solve_right (sage/matrix/matrix2.c:3796)\n  File \"ring.pyx\", line 835, in sage.rings.ring.Ring.is_integral_domain (sage/rings/ring.c:6410)\nNotImplementedError\n```\n\n\nThis is in 4.8.\n\nJoal Heagney",
    "created_at": "2012-04-12T13:24:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5612",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5612#issuecomment-43748",
    "user": "https://trac.sagemath.org/admin/accounts/users/JoalHeagney"
}
```

Guys, when I try this out, I get to the following line and get the following error (both ways):



```
soln=A.solve_right(result) # you could also do soln=A\result
```



```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "_sage_input_15.py", line 10, in <module>
    exec compile(u'open("___code___.py","w").write("# -*- coding: utf-8 -*-\\n" + _support_.preparse_worksheet_cell(base64.b64decode("c29sbj1BLnNvbHZlX3JpZ2h0KHJlc3VsdCkgIyB5b3UgY291bGQgYWxzbyBkbyBzb2xuPUFccmVzdWx0"),globals())+"\\n"); execfile(os.path.abspath("___code___.py"))
  File "", line 1, in <module>
    
  File "/tmp/tmpJ1xbYN/___code___.py", line 2, in <module>
    exec compile(u'soln=A.solve_right(result) # you could also do soln=A\\result
  File "", line 1, in <module>
    
  File "matrix2.pyx", line 281, in sage.matrix.matrix2.Matrix.solve_right (sage/matrix/matrix2.c:3796)
  File "ring.pyx", line 835, in sage.rings.ring.Ring.is_integral_domain (sage/rings/ring.c:6410)
NotImplementedError
```


This is in 4.8.

Joal Heagney



---

archive/issue_comments_043749.json:
```json
{
    "body": "Attachment [trac_5612_solve_symbolic_matrix.patch](tarball://root/attachments/some-uuid/ticket5612/trac_5612_solve_symbolic_matrix.patch) by @abrochard created at 2012-06-02 23:42:16\n\nI added the example of symbolic matrix to the doc and fixed the bug reported by Joal Heagney. The error came from is_integral_domain() function in ring.pyx. Since a field is a specific type of integral domain, I just added a if clause.",
    "created_at": "2012-06-02T23:42:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5612",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5612#issuecomment-43749",
    "user": "https://github.com/abrochard"
}
```

Attachment [trac_5612_solve_symbolic_matrix.patch](tarball://root/attachments/some-uuid/ticket5612/trac_5612_solve_symbolic_matrix.patch) by @abrochard created at 2012-06-02 23:42:16

I added the example of symbolic matrix to the doc and fixed the bug reported by Joal Heagney. The error came from is_integral_domain() function in ring.pyx. Since a field is a specific type of integral domain, I just added a if clause.



---

archive/issue_comments_043750.json:
```json
{
    "body": "Changing assignee from @williamstein to @mmasdeu.",
    "created_at": "2012-06-08T16:00:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5612",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5612#issuecomment-43750",
    "user": "https://github.com/mmasdeu"
}
```

Changing assignee from @williamstein to @mmasdeu.



---

archive/issue_comments_043751.json:
```json
{
    "body": "Looks good to me. It does what the ticked asked and fixed a bug with SR.",
    "created_at": "2012-06-08T16:00:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5612",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5612#issuecomment-43751",
    "user": "https://github.com/mmasdeu"
}
```

Looks good to me. It does what the ticked asked and fixed a bug with SR.



---

archive/issue_comments_043752.json:
```json
{
    "body": "Well the patch works fine on the example problems in sage 5.0. Haven't checked to see if it has other consequences elsewhere though.",
    "created_at": "2012-06-09T04:37:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5612",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5612#issuecomment-43752",
    "user": "https://trac.sagemath.org/admin/accounts/users/JoalHeagney"
}
```

Well the patch works fine on the example problems in sage 5.0. Haven't checked to see if it has other consequences elsewhere though.



---

archive/issue_comments_043753.json:
```json
{
    "body": "I just ran into the error reported by JoalHeagney while going through some Sage demo worksheets from past talks. This bug must have been introduced sometime after the talk was given because I remember solving symbolic matrix equations just fine. It would be great if this got doctested and into Sage ASAP.",
    "created_at": "2012-07-23T16:32:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5612",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5612#issuecomment-43753",
    "user": "https://github.com/benjaminfjones"
}
```

I just ran into the error reported by JoalHeagney while going through some Sage demo worksheets from past talks. This bug must have been introduced sometime after the talk was given because I remember solving symbolic matrix equations just fine. It would be great if this got doctested and into Sage ASAP.



---

archive/issue_comments_043754.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2012-07-23T16:32:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5612",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5612#issuecomment-43754",
    "user": "https://github.com/benjaminfjones"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_043755.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2012-07-23T16:32:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5612",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5612#issuecomment-43755",
    "user": "https://github.com/benjaminfjones"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_043756.json:
```json
{
    "body": "Oops, sorry. I saw the doctests in the patch and then promptly forgot about them. The patch looks very good to me. I'll do some more extensive testing and if all looks good, positive review.",
    "created_at": "2012-07-23T16:33:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5612",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5612#issuecomment-43756",
    "user": "https://github.com/benjaminfjones"
}
```

Oops, sorry. I saw the doctests in the patch and then promptly forgot about them. The patch looks very good to me. I'll do some more extensive testing and if all looks good, positive review.



---

archive/issue_comments_043757.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2012-07-23T16:33:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5612",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5612#issuecomment-43757",
    "user": "https://github.com/benjaminfjones"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_043758.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-07-23T22:13:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5612",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5612#issuecomment-43758",
    "user": "https://github.com/benjaminfjones"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_043759.json:
```json
{
    "body": "Changing type from enhancement to defect.",
    "created_at": "2012-07-23T22:13:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5612",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5612#issuecomment-43759",
    "user": "https://github.com/benjaminfjones"
}
```

Changing type from enhancement to defect.



---

archive/issue_comments_043760.json:
```json
{
    "body": "The patch applies cleanly to 5.2.rc0 and passes all tests. It looks good to go. Thanks for the contribution (and the bug report, Joel).",
    "created_at": "2012-07-23T22:13:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5612",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5612#issuecomment-43760",
    "user": "https://github.com/benjaminfjones"
}
```

The patch applies cleanly to 5.2.rc0 and passes all tests. It looks good to go. Thanks for the contribution (and the bug report, Joel).



---

archive/issue_comments_043761.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2012-08-01T12:09:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5612",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5612#issuecomment-43761",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed
