# Issue 5413: [with patch, needs review] deprecate substitution via __call__ w/ unnamed arguments

archive/issues_005413.json:
```json
{
    "body": "Assignee: burcin\n\nCC:  jason\n\nAs discussed on sage-devel here: http://groups.google.com/group/sage-devel/browse_thread/thread/b1a03f8fc8ae8fcd/553773d7ba600ae7#553773d7ba600ae7\n\nI added deprecation warnings to the four affected __call__ functions (two for symbolic values, one for equations, one for matrices), and fixed almost all the warnings in all the doctests other than the doctests specifically for those __call__ methods.\n\nThere's one set of warnings that I didn't figure out how to fix (in piecewise.py), so I just added the warning to the expected output for now.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5413\n\n",
    "created_at": "2009-03-01T18:00:29Z",
    "labels": [
        "calculus",
        "major",
        "bug"
    ],
    "title": "[with patch, needs review] deprecate substitution via __call__ w/ unnamed arguments",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5413",
    "user": "cwitty"
}
```
Assignee: burcin

CC:  jason

As discussed on sage-devel here: http://groups.google.com/group/sage-devel/browse_thread/thread/b1a03f8fc8ae8fcd/553773d7ba600ae7#553773d7ba600ae7

I added deprecation warnings to the four affected __call__ functions (two for symbolic values, one for equations, one for matrices), and fixed almost all the warnings in all the doctests other than the doctests specifically for those __call__ methods.

There's one set of warnings that I didn't figure out how to fix (in piecewise.py), so I just added the warning to the expected output for now.

Issue created by migration from https://trac.sagemath.org/ticket/5413





---

archive/issue_comments_041851.json:
```json
{
    "body": "Two trivial doctest failures:\n\n```\nsage -t -long devel/sage/doc/en/constructions/calculus.rst # 1 doctests failed\nsage -t -long devel/sage/doc/fr/tutorial/tour_algebra.rst # 1 doctests failed\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2009-03-02T06:51:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5413",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5413#issuecomment-41851",
    "user": "mabshoff"
}
```

Two trivial doctest failures:

```
sage -t -long devel/sage/doc/en/constructions/calculus.rst # 1 doctests failed
sage -t -long devel/sage/doc/fr/tutorial/tour_algebra.rst # 1 doctests failed
```


Cheers,

Michael



---

archive/issue_comments_041852.json:
```json
{
    "body": "Attachment [deprecate-symbolic-unnamed-call.patch](tarball://root/attachments/some-uuid/ticket5413/deprecate-symbolic-unnamed-call.patch) by cwitty created at 2009-03-03 02:40:26\n\nOops, forgot to doctest the documentation.  I've replaced my original patch with a new one that also fixes these two doctest failures.",
    "created_at": "2009-03-03T02:40:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5413",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5413#issuecomment-41852",
    "user": "cwitty"
}
```

Attachment [deprecate-symbolic-unnamed-call.patch](tarball://root/attachments/some-uuid/ticket5413/deprecate-symbolic-unnamed-call.patch) by cwitty created at 2009-03-03 02:40:26

Oops, forgot to doctest the documentation.  I've replaced my original patch with a new one that also fixes these two doctest failures.



---

archive/issue_comments_041853.json:
```json
{
    "body": "This is an (email) reminder to myself to review this to get it in.",
    "created_at": "2009-03-13T19:17:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5413",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5413#issuecomment-41853",
    "user": "jason"
}
```

This is an (email) reminder to myself to review this to get it in.



---

archive/issue_comments_041854.json:
```json
{
    "body": "This ticket probably also affects #5093.",
    "created_at": "2009-03-13T19:29:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5413",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5413#issuecomment-41854",
    "user": "jason"
}
```

This ticket probably also affects #5093.



---

archive/issue_comments_041855.json:
```json
{
    "body": "Thanks for working on this Carl.\n\nI only read the patch, didn't test it yet. Explicitly having to use .function() in two places bothers me:\n\n* for each component of Piecewise\n* in the call to generate_plot_points\n\nPerhaps we should modify these to handle non function arguments more gracefully after this change. \n\nI understand that this might require a new syntax to construct Piecewise objects. One option is to add a new parameter, which includes an ordered list of variables. E.g.,\n\n\n```\n    sage: Piecewise([[(0,1),x^2],[(1,2),5-x^2]] ,[x])\n```\n\nor\n\n```\n    sage: f = Piecewise([[(-1,1),1/2+x-x^3 + y]],[x,y])\n```\n\n\nComments?",
    "created_at": "2009-03-14T12:08:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5413",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5413#issuecomment-41855",
    "user": "burcin"
}
```

Thanks for working on this Carl.

I only read the patch, didn't test it yet. Explicitly having to use .function() in two places bothers me:

* for each component of Piecewise
* in the call to generate_plot_points

Perhaps we should modify these to handle non function arguments more gracefully after this change. 

I understand that this might require a new syntax to construct Piecewise objects. One option is to add a new parameter, which includes an ordered list of variables. E.g.,


```
    sage: Piecewise([[(0,1),x^2],[(1,2),5-x^2]] ,[x])
```

or

```
    sage: f = Piecewise([[(-1,1),1/2+x-x^3 + y]],[x,y])
```


Comments?



---

archive/issue_comments_041856.json:
```json
{
    "body": "The above comment for Piecewise would probably also apply to symbolic matrices and vectors, right? (well, at least, as soon as symbolic vectors are callable, anyway).  I think that Burcin's proposal is okay, but doesn't extend very well to matrices and vectors, since I'd hate to mess up the standard matrix/vector constructors.  I'm don't know a better way to extend this to matrices and vectors, though.  Maybe we ought to just deprecate calling a symbolic matrix without keyword arguments, and just implement the callable symbolic vector with the same restrictions.",
    "created_at": "2009-03-14T12:21:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5413",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5413#issuecomment-41856",
    "user": "jason"
}
```

The above comment for Piecewise would probably also apply to symbolic matrices and vectors, right? (well, at least, as soon as symbolic vectors are callable, anyway).  I think that Burcin's proposal is okay, but doesn't extend very well to matrices and vectors, since I'd hate to mess up the standard matrix/vector constructors.  I'm don't know a better way to extend this to matrices and vectors, though.  Maybe we ought to just deprecate calling a symbolic matrix without keyword arguments, and just implement the callable symbolic vector with the same restrictions.



---

archive/issue_comments_041857.json:
```json
{
    "body": "The patch already does deprecate calling a symbolic matrix without keyword arguments.",
    "created_at": "2009-03-14T13:22:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5413",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5413#issuecomment-41857",
    "user": "cwitty"
}
```

The patch already does deprecate calling a symbolic matrix without keyword arguments.



---

archive/issue_comments_041858.json:
```json
{
    "body": "Yes.  I thought Burcin's comment was about a syntax to avoid the .function() call.  That's what I was commenting on.",
    "created_at": "2009-03-14T13:38:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5413",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5413#issuecomment-41858",
    "user": "jason"
}
```

Yes.  I thought Burcin's comment was about a syntax to avoid the .function() call.  That's what I was commenting on.



---

archive/issue_comments_041859.json:
```json
{
    "body": "After discussions on IRC and sage-devel (http://groups.google.com/group/sage-devel/browse_thread/thread/97cdf80edb089481/73e8e6659c09e1d9#73e8e6659c09e1d9) we've decided on a much more extensive deprecation scheme.  So it's not worth reviewing the current patch.  (I should have a new patch within a few days.)",
    "created_at": "2009-03-16T21:22:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5413",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5413#issuecomment-41859",
    "user": "cwitty"
}
```

After discussions on IRC and sage-devel (http://groups.google.com/group/sage-devel/browse_thread/thread/97cdf80edb089481/73e8e6659c09e1d9#73e8e6659c09e1d9) we've decided on a much more extensive deprecation scheme.  So it's not worth reviewing the current patch.  (I should have a new patch within a few days.)



---

archive/issue_comments_041860.json:
```json
{
    "body": "Attachment [trac5413-deprecate-symbolic-unnamed-call.patch](tarball://root/attachments/some-uuid/ticket5413/trac5413-deprecate-symbolic-unnamed-call.patch) by cwitty created at 2009-03-20 03:06:10\n\nI've posted a patch that implements the more extensive deprecation described here: http://groups.google.com/group/sage-devel/browse_thread/thread/97cdf80edb089481#\n\nThe patch now depends on #5093.\n\nApply only the second patch.",
    "created_at": "2009-03-20T03:06:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5413",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5413#issuecomment-41860",
    "user": "cwitty"
}
```

Attachment [trac5413-deprecate-symbolic-unnamed-call.patch](tarball://root/attachments/some-uuid/ticket5413/trac5413-deprecate-symbolic-unnamed-call.patch) by cwitty created at 2009-03-20 03:06:10

I've posted a patch that implements the more extensive deprecation described here: http://groups.google.com/group/sage-devel/browse_thread/thread/97cdf80edb089481#

The patch now depends on #5093.

Apply only the second patch.



---

archive/issue_comments_041861.json:
```json
{
    "body": "This is really odd:\n\n\n```\n[19:53] <jason> sage: g(x)=sin\n[19:53] <jason> sage: g(3)\n[19:53] <jason> sin(3)\n[19:53] <jason> sage: g(x)=sin+x\n[19:53] <jason> sage: g(3)\n[19:53] <jason> sin + 3\n[19:54] <jason> but\n[19:54] <jason> sage: g(x)=sin+cos; g(3)\n[19:54] <jason> sin + cos\n```\n",
    "created_at": "2009-03-25T01:15:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5413",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5413#issuecomment-41861",
    "user": "jason"
}
```

This is really odd:


```
[19:53] <jason> sage: g(x)=sin
[19:53] <jason> sage: g(3)
[19:53] <jason> sin(3)
[19:53] <jason> sage: g(x)=sin+x
[19:53] <jason> sage: g(3)
[19:53] <jason> sin + 3
[19:54] <jason> but
[19:54] <jason> sage: g(x)=sin+cos; g(3)
[19:54] <jason> sin + cos
```




---

archive/issue_comments_041862.json:
```json
{
    "body": "Jason, I get the same behavior without Carl's patch on Sage-3.4. I suggest moving that to a separate ticket. We could also argue if that is valid syntax there.\n\nI give a positive review to this. It would be good to get this in an alpha and let more people play with it. Thanks again Carl.\n\nCheers,\nBurcin",
    "created_at": "2009-03-25T10:35:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5413",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5413#issuecomment-41862",
    "user": "burcin"
}
```

Jason, I get the same behavior without Carl's patch on Sage-3.4. I suggest moving that to a separate ticket. We could also argue if that is valid syntax there.

I give a positive review to this. It would be good to get this in an alpha and let more people play with it. Thanks again Carl.

Cheers,
Burcin



---

archive/issue_comments_041863.json:
```json
{
    "body": "comment:12 is now #5607.",
    "created_at": "2009-03-25T10:58:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5413",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5413#issuecomment-41863",
    "user": "burcin"
}
```

comment:12 is now #5607.



---

archive/issue_comments_041864.json:
```json
{
    "body": "I agree that we should get this into the alpha so it gets wider exposure.  (providing doctests pass) positive review from me too.",
    "created_at": "2009-03-25T14:37:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5413",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5413#issuecomment-41864",
    "user": "jason"
}
```

I agree that we should get this into the alpha so it gets wider exposure.  (providing doctests pass) positive review from me too.



---

archive/issue_comments_041865.json:
```json
{
    "body": "There is one tiny doctest issue left - at least in my merge tree :)\n\n```\nsage -t -long \"devel/sage/doc/en/constructions/calculus.rst\"\n**********************************************************************\nFile \"/scratch/mabshoff/sage-3.4.1.alpha0/devel/sage/doc/en/constructions/calculus.rst\", line 222:\n    sage: f.integral()\nExpected:\n    Piecewise defined function with 2 parts, [[(0, 1), x^3/3], [(1, 2), (15*x - x^3)/3 - 13/3]]\nGot:\n    Piecewise defined function with 2 parts, [[(0, 1), x |--> x^3/3], [(1, 2), x |--> (15*x - x^3)/3 - 13/3]]\n**********************************************************************\n1 items had failures:\n   1 of   9 in __main__.example_8\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /scratch/mabshoff/sage-3.4.1.alpha0/tmp/.doctest_calculus.py\n\t [4.3 s]\nexit code: 1024\n```\n\n\nI am fixing this with a reviewer patch.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-25T23:12:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5413",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5413#issuecomment-41865",
    "user": "mabshoff"
}
```

There is one tiny doctest issue left - at least in my merge tree :)

```
sage -t -long "devel/sage/doc/en/constructions/calculus.rst"
**********************************************************************
File "/scratch/mabshoff/sage-3.4.1.alpha0/devel/sage/doc/en/constructions/calculus.rst", line 222:
    sage: f.integral()
Expected:
    Piecewise defined function with 2 parts, [[(0, 1), x^3/3], [(1, 2), (15*x - x^3)/3 - 13/3]]
Got:
    Piecewise defined function with 2 parts, [[(0, 1), x |--> x^3/3], [(1, 2), x |--> (15*x - x^3)/3 - 13/3]]
**********************************************************************
1 items had failures:
   1 of   9 in __main__.example_8
***Test Failed*** 1 failures.
For whitespace errors, see the file /scratch/mabshoff/sage-3.4.1.alpha0/tmp/.doctest_calculus.py
	 [4.3 s]
exit code: 1024
```


I am fixing this with a reviewer patch.

Cheers,

Michael



---

archive/issue_comments_041866.json:
```json
{
    "body": "Attachment [trac_5413-reviewer.patch](tarball://root/attachments/some-uuid/ticket5413/trac_5413-reviewer.patch) by mabshoff created at 2009-03-25 23:30:42",
    "created_at": "2009-03-25T23:30:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5413",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5413#issuecomment-41866",
    "user": "mabshoff"
}
```

Attachment [trac_5413-reviewer.patch](tarball://root/attachments/some-uuid/ticket5413/trac_5413-reviewer.patch) by mabshoff created at 2009-03-25 23:30:42



---

archive/issue_comments_041867.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-03-25T23:31:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5413",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5413#issuecomment-41867",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_041868.json:
```json
{
    "body": "Merged trac5413-deprecate-symbolic-unnamed-call.patch and trac_5413-reviewer.patch in Sage 3.4.1.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-25T23:31:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5413",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5413#issuecomment-41868",
    "user": "mabshoff"
}
```

Merged trac5413-deprecate-symbolic-unnamed-call.patch and trac_5413-reviewer.patch in Sage 3.4.1.alpha0.

Cheers,

Michael
