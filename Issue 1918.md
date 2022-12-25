# Issue 1918: Matrices that are printed are not aligned

archive/issues_001918.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @hivert @nthiery\n\nThe rows of matrices in a list right now do not line up when printed, even though carriage returns are inserted as if they should line up.  That means all the matrices look *very* messed up when printing a list of matrices.\n\nIn the command line:\n\n\n```\nsage: list(MatrixSpace(GF(2),2))\n\n[[0 0]\n[0 0],\n [1 0]\n[0 0],\n [0 1]\n[0 0],\n [0 0]\n[1 0],\n [0 0]\n[0 1],\n [1 1]\n[0 0],\n [1 0]\n[1 0],\n [1 0]\n[0 1],\n [0 1]\n[1 0],\n [0 1]\n[0 1],\n [0 0]\n[1 1],\n [1 1]\n[1 0],\n [1 1]\n[0 1],\n [1 0]\n[1 1],\n [0 1]\n[1 1],\n [1 1]\n[1 1]]\n```\n\n\nIn the notebook, it's worse.  Each matrix is chopped in half and continues at the start of the next line.  This gives the appearance of matrices that are not part of the list (one row of one matrix and another row from a different matrix).\n\n\n```\n[[0 0]\n[0 0], [1 0]\n[0 0], [0 1]\n[0 0], [0 0]\n[1 0], [0 0]\n[0 1], [1 1]\n[0 0], [1 0]\n[1 0], [1 0]\n[0 1], [0 1]\n[1 0], [0 1]\n[0 1], [0 0]\n[1 1], [1 1]\n[1 0], [1 1]\n[0 1], [1 0]\n[1 1], [0 1]\n[1 1], [1 1]\n[1 1]]\n```\n\n\nAn example of better output would be:\n\n\n```\nsage: list(MatrixSpace(GF(2),2))\n\n[\n[0 0]\n[0 0],\n\n[1 0]\n[0 0],\n\n[0 1]\n[0 0],\n\n[0 0]\n[1 0],\n\n[0 0]\n[0 1],\n\n[1 1]\n[0 0],\n\n[1 0]\n[1 0],\n\n[1 0]\n[0 1],\n\n[0 1]\n[1 0],\n\n[0 1]\n[0 1],\n\n[0 0]\n[1 1],\n\n[1 1]\n[1 0],\n\n[1 1]\n[0 1],\n\n[1 0]\n[1 1],\n\n[0 1]\n[1 1],\n\n[1 1]\n[1 1]]\n```\n\n\nOr even better:\n\n```\n[\n[0 0]  [1 0]  [0 1]  [0 0]  [0 0]  [1 1]  \n[0 0], [0 0], [0 0], [1 0], [0 1], [0 0], \n\n[1 0]  [1 0]  [0 1]  [0 1]  [0 0]  [1 1]\n[1 0], [0 1], [1 0], [0 1], [1 1], [1 0],\n\n[1 1]  [1 0]  [0 1]  [1 1]\n[0 1], [1 1], [1 1], [1 1]\n]\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1918\n\n",
    "created_at": "2008-01-25T01:27:06Z",
    "labels": [
        "component: linear algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "Matrices that are printed are not aligned",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1918",
    "user": "https://github.com/jasongrout"
}
```
Assignee: @williamstein

CC:  @hivert @nthiery

The rows of matrices in a list right now do not line up when printed, even though carriage returns are inserted as if they should line up.  That means all the matrices look *very* messed up when printing a list of matrices.

In the command line:


```
sage: list(MatrixSpace(GF(2),2))

[[0 0]
[0 0],
 [1 0]
[0 0],
 [0 1]
[0 0],
 [0 0]
[1 0],
 [0 0]
[0 1],
 [1 1]
[0 0],
 [1 0]
[1 0],
 [1 0]
[0 1],
 [0 1]
[1 0],
 [0 1]
[0 1],
 [0 0]
[1 1],
 [1 1]
[1 0],
 [1 1]
[0 1],
 [1 0]
[1 1],
 [0 1]
[1 1],
 [1 1]
[1 1]]
```


In the notebook, it's worse.  Each matrix is chopped in half and continues at the start of the next line.  This gives the appearance of matrices that are not part of the list (one row of one matrix and another row from a different matrix).


```
[[0 0]
[0 0], [1 0]
[0 0], [0 1]
[0 0], [0 0]
[1 0], [0 0]
[0 1], [1 1]
[0 0], [1 0]
[1 0], [1 0]
[0 1], [0 1]
[1 0], [0 1]
[0 1], [0 0]
[1 1], [1 1]
[1 0], [1 1]
[0 1], [1 0]
[1 1], [0 1]
[1 1], [1 1]
[1 1]]
```


An example of better output would be:


```
sage: list(MatrixSpace(GF(2),2))

[
[0 0]
[0 0],

[1 0]
[0 0],

[0 1]
[0 0],

[0 0]
[1 0],

[0 0]
[0 1],

[1 1]
[0 0],

[1 0]
[1 0],

[1 0]
[0 1],

[0 1]
[1 0],

[0 1]
[0 1],

[0 0]
[1 1],

[1 1]
[1 0],

[1 1]
[0 1],

[1 0]
[1 1],

[0 1]
[1 1],

[1 1]
[1 1]]
```


Or even better:

```
[
[0 0]  [1 0]  [0 1]  [0 0]  [0 0]  [1 1]  
[0 0], [0 0], [0 0], [1 0], [0 1], [0 0], 

[1 0]  [1 0]  [0 1]  [0 1]  [0 0]  [1 1]
[1 0], [0 1], [1 0], [0 1], [1 1], [1 0],

[1 1]  [1 0]  [0 1]  [1 1]
[0 1], [1 1], [1 1], [1 1]
]
```



Issue created by migration from https://trac.sagemath.org/ticket/1918





---

archive/issue_comments_012114.json:
```json
{
    "body": "This is another example of something that can probably only ? be addressed\nby changing the Python displayhook thing.  That's completely reasonable.\n\nWilliam",
    "created_at": "2008-01-25T02:05:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1918",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1918#issuecomment-12114",
    "user": "https://github.com/williamstein"
}
```

This is another example of something that can probably only ? be addressed
by changing the Python displayhook thing.  That's completely reasonable.

William



---

archive/issue_comments_012115.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2009-01-22T22:35:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1918",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1918#issuecomment-12115",
    "user": "https://github.com/malb"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_012116.json:
```json
{
    "body": "I did some work to alleviate this issue, including implementing a new displayhook. The displayhook looks at every list, and if any object's repr spans multiple lines it prints the whole list out in a special format. See for yourself:\n\n\n```\nsage: list(MatrixSpace(GF(2),2))\n[\n[0 0]  [1 0]  [0 1]  [0 0]  [0 0]  [1 1]  [1 0]  [1 0]  [0 1]  [0 1]\n[0 0], [0 0], [0 0], [1 0], [0 1], [0 0], [1 0], [0 1], [1 0], [0 1],\n\n[0 0]  [1 1]  [1 1]  [1 0]  [0 1]  [1 1]\n[1 1], [1 0], [0 1], [1 1], [1 1], [1 1]\n]\n```\n\n\nI discovered that IPython has a separate displayhook mechanism -- however, the Sage instance spawned for the notebook does not use IPython. Hence, my code has two separate paths. I tried to ensure that the behavior of the default displayhook would be maintained in any case. I do hope it doesn't break anything :).",
    "created_at": "2009-08-05T01:39:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1918",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1918#issuecomment-12116",
    "user": "https://trac.sagemath.org/admin/accounts/users/wcauchois"
}
```

I did some work to alleviate this issue, including implementing a new displayhook. The displayhook looks at every list, and if any object's repr spans multiple lines it prints the whole list out in a special format. See for yourself:


```
sage: list(MatrixSpace(GF(2),2))
[
[0 0]  [1 0]  [0 1]  [0 0]  [0 0]  [1 1]  [1 0]  [1 0]  [0 1]  [0 1]
[0 0], [0 0], [0 0], [1 0], [0 1], [0 0], [1 0], [0 1], [1 0], [0 1],

[0 0]  [1 1]  [1 1]  [1 0]  [0 1]  [1 1]
[1 1], [1 0], [0 1], [1 1], [1 1], [1 1]
]
```


I discovered that IPython has a separate displayhook mechanism -- however, the Sage instance spawned for the notebook does not use IPython. Hence, my code has two separate paths. I tried to ensure that the behavior of the default displayhook would be maintained in any case. I do hope it doesn't break anything :).



---

archive/issue_comments_012117.json:
```json
{
    "body": "This looks very, *very* nice.  It also leads to huge numbers of failures in doctests in the matrix directory, which would need to be cleaned up by someone in another patch on this ticket.",
    "created_at": "2009-09-17T09:49:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1918",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1918#issuecomment-12117",
    "user": "https://github.com/jasongrout"
}
```

This looks very, *very* nice.  It also leads to huge numbers of failures in doctests in the matrix directory, which would need to be cleaned up by someone in another patch on this ticket.



---

archive/issue_comments_012118.json:
```json
{
    "body": "The patch doesn't just lead to doctest failures in the matrix directory - on my machine it seems to lead to the failure of every single doctest that produces output!  e.g.\n\n```\nFile \"/Applications/sage/devel/sage-1918/sage/algebras/algebra.py\", line 29:\n    sage: is_Algebra(R)\nExpected:\n    True\nGot nothing\n```\n\nWhen running a test manually (i.e. typing it into a sage console), everything works as intended - the output matches the expected doctest result exactly.  So the patch seems to break the doctesting mechanism in some way.  I note that all of the output-producing tests in the new file displayhook.py pass their output through DH.print_obj() or similar.",
    "created_at": "2009-10-06T07:27:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1918",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1918#issuecomment-12118",
    "user": "https://trac.sagemath.org/admin/accounts/users/flawrence"
}
```

The patch doesn't just lead to doctest failures in the matrix directory - on my machine it seems to lead to the failure of every single doctest that produces output!  e.g.

```
File "/Applications/sage/devel/sage-1918/sage/algebras/algebra.py", line 29:
    sage: is_Algebra(R)
Expected:
    True
Got nothing
```

When running a test manually (i.e. typing it into a sage console), everything works as intended - the output matches the expected doctest result exactly.  So the patch seems to break the doctesting mechanism in some way.  I note that all of the output-producing tests in the new file displayhook.py pass their output through DH.print_obj() or similar.



---

archive/issue_comments_012119.json:
```json
{
    "body": "Attachment [trac_1918-displayhook.patch](tarball://root/attachments/some-uuid/ticket1918/trac_1918-displayhook.patch) by wcauchois created at 2009-12-02 08:38:50\n\nbased on sage 4.2.1",
    "created_at": "2009-12-02T08:38:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1918",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1918#issuecomment-12119",
    "user": "https://trac.sagemath.org/admin/accounts/users/wcauchois"
}
```

Attachment [trac_1918-displayhook.patch](tarball://root/attachments/some-uuid/ticket1918/trac_1918-displayhook.patch) by wcauchois created at 2009-12-02 08:38:50

based on sage 4.2.1



---

archive/issue_comments_012120.json:
```json
{
    "body": "Attachment [trac_1918-all.patch](tarball://root/attachments/some-uuid/ticket1918/trac_1918-all.patch) by wcauchois created at 2009-12-02 08:39:22\n\nbased on sage 4.3.alpha0; apply only this patch",
    "created_at": "2009-12-02T08:39:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1918",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1918#issuecomment-12120",
    "user": "https://trac.sagemath.org/admin/accounts/users/wcauchois"
}
```

Attachment [trac_1918-all.patch](tarball://root/attachments/some-uuid/ticket1918/trac_1918-all.patch) by wcauchois created at 2009-12-02 08:39:22

based on sage 4.3.alpha0; apply only this patch



---

archive/issue_comments_012121.json:
```json
{
    "body": "I think this is ready for review! The only doctest failure now is from sage/interfaces/maxima.py, but I'm pretty sure that has nothing to do with this patch (I saw it in the main branch of 4.3.alpha0 as well).",
    "created_at": "2009-12-02T08:46:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1918",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1918#issuecomment-12121",
    "user": "https://trac.sagemath.org/admin/accounts/users/wcauchois"
}
```

I think this is ready for review! The only doctest failure now is from sage/interfaces/maxima.py, but I'm pretty sure that has nothing to do with this patch (I saw it in the main branch of 4.3.alpha0 as well).



---

archive/issue_comments_012122.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-12-02T08:46:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1918",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1918#issuecomment-12122",
    "user": "https://trac.sagemath.org/admin/accounts/users/wcauchois"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_012123.json:
```json
{
    "body": "Replying to [comment:6 wcauchois]:\n> I think this is ready for review! The only doctest failure now is from sage/interfaces/maxima.py, but I'm pretty sure that has nothing to do with this patch (I saw it in the main branch of 4.3.alpha0 as well).\n\nThis is some very good piece of work ! However, I'm soory to say that but I think it is not general enough. In combinatorics, we have a lot of 2d objects (Ferrers diagram, Young tableau). Right now it is hardcoded in the patch that this hook only apply for a list of matrices. should'nt we add some plugin saying that a particular kind of objects are printed by a 2d diagram. Or maybe should we apply the hook allways ? Or for any objects whose __repr__ string contains a newline ? \n\nBut maybe we should keep the for another patch. \n\nBy the way and as a consequence, I don't think this has to do with linear algebra. \n\nCheers,\n\nFlorent",
    "created_at": "2009-12-02T17:26:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1918",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1918#issuecomment-12123",
    "user": "https://github.com/hivert"
}
```

Replying to [comment:6 wcauchois]:
> I think this is ready for review! The only doctest failure now is from sage/interfaces/maxima.py, but I'm pretty sure that has nothing to do with this patch (I saw it in the main branch of 4.3.alpha0 as well).

This is some very good piece of work ! However, I'm soory to say that but I think it is not general enough. In combinatorics, we have a lot of 2d objects (Ferrers diagram, Young tableau). Right now it is hardcoded in the patch that this hook only apply for a list of matrices. should'nt we add some plugin saying that a particular kind of objects are printed by a 2d diagram. Or maybe should we apply the hook allways ? Or for any objects whose __repr__ string contains a newline ? 

But maybe we should keep the for another patch. 

By the way and as a consequence, I don't think this has to do with linear algebra. 

Cheers,

Florent



---

archive/issue_comments_012124.json:
```json
{
    "body": "To be more specific, I'd like to be able to write thing like that\n\n```\nsage: class bla(): \n....:     def __init__(self, str): self.str=str\n....:     def __repr__(self): return self.str\n```\n \nAnd without patching displayhook, to get\n\n```\nsage: sage.misc.displayhook._check_tall_list_and_print(sys.stdout, [a,b])\n[\n       dsf\nwerew  sdf\nsdfd , sf \n]\n```\n\ninstead of...\n\n```\nsage: [bla(\"werew\\nsdfd\"), bla(\"dsf\\nsdf\\nsf\")]\n[werew\nsdfd, dsf\nsdf\nsf]\n```\n\nI'm not sure what is the correct mechanism of plugin. should we add in the class a method called say `_repr_use2d_` ? \n\nFlorent",
    "created_at": "2009-12-02T17:36:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1918",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1918#issuecomment-12124",
    "user": "https://github.com/hivert"
}
```

To be more specific, I'd like to be able to write thing like that

```
sage: class bla(): 
....:     def __init__(self, str): self.str=str
....:     def __repr__(self): return self.str
```
 
And without patching displayhook, to get

```
sage: sage.misc.displayhook._check_tall_list_and_print(sys.stdout, [a,b])
[
       dsf
werew  sdf
sdfd , sf 
]
```

instead of...

```
sage: [bla("werew\nsdfd"), bla("dsf\nsdf\nsf")]
[werew
sdfd, dsf
sdf
sf]
```

I'm not sure what is the correct mechanism of plugin. should we add in the class a method called say `_repr_use2d_` ? 

Florent



---

archive/issue_comments_012125.json:
```json
{
    "body": "Replying to [comment:7 hivert]:\n\n> But maybe we should keep the for another patch. \n\nI agree.  Furthermore, this will let us shake out any unintended consequences or bugs in a narrow case before expanding to lots of combinatorics objects.\n\nThe patch has already waited a long time.  Unless the change you suggest is trivial (but it sounds like already there are questions about the design of your suggestion), I'd say if the patch is ready to go in, let it go in.",
    "created_at": "2009-12-02T17:40:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1918",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1918#issuecomment-12125",
    "user": "https://github.com/jasongrout"
}
```

Replying to [comment:7 hivert]:

> But maybe we should keep the for another patch. 

I agree.  Furthermore, this will let us shake out any unintended consequences or bugs in a narrow case before expanding to lots of combinatorics objects.

The patch has already waited a long time.  Unless the change you suggest is trivial (but it sounds like already there are questions about the design of your suggestion), I'd say if the patch is ready to go in, let it go in.



---

archive/issue_comments_012126.json:
```json
{
    "body": "Replying to [comment:7 hivert]:\n\nI agree that there are many more cases where this type of list formatting could be useful, and indeed the code is general enough to work with any type of object whose repr spans multiple lines. The issue is simply choosing which lists to format specially (in print_obj()).\n\nIn one of my earlier iterations of the displayhook, I applied the special list formatting to every \"tall\" list. But when I ran testall I found that some objects just didn't work well with the formatting. So I think that applying the hook always is a mistake, and besides would introduce many more doctest headaches. Having objects \"opt-in\" by including a special field or method that tells the displayhook to use the special list formatting sounds like a good idea though.\n\nThis kind of work should definitely be done, but in another ticket. We will have to come to an agreement about these design issues. For now, let's get this patch into Sage.",
    "created_at": "2009-12-02T20:21:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1918",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1918#issuecomment-12126",
    "user": "https://trac.sagemath.org/admin/accounts/users/wcauchois"
}
```

Replying to [comment:7 hivert]:

I agree that there are many more cases where this type of list formatting could be useful, and indeed the code is general enough to work with any type of object whose repr spans multiple lines. The issue is simply choosing which lists to format specially (in print_obj()).

In one of my earlier iterations of the displayhook, I applied the special list formatting to every "tall" list. But when I ran testall I found that some objects just didn't work well with the formatting. So I think that applying the hook always is a mistake, and besides would introduce many more doctest headaches. Having objects "opt-in" by including a special field or method that tells the displayhook to use the special list formatting sounds like a good idea though.

This kind of work should definitely be done, but in another ticket. We will have to come to an agreement about these design issues. For now, let's get this patch into Sage.



---

archive/issue_comments_012127.json:
```json
{
    "body": "Replying to [comment:10 wcauchois]:\n> In one of my earlier iterations of the displayhook, I applied the special list formatting to every \"tall\" list. But when I ran testall I found that some objects just didn't work well with the formatting. So I think that applying the hook always is a mistake, and besides would introduce many more doctest headaches. Having objects \"opt-in\" by including a special field or method that tells the displayhook to use the special list formatting sounds like a good idea though.\n\nI even tried to apply it on **all** lists ! I can tell you that there are much more output that looks better with your modification than without. (see e.g. in  `sage/modular/arithgroup/`... I'm not sure doing it systematically is a mistake... But some objects have to adapt their output, and the way you decide to break a line or not is not always optimal (see e.g. the output of ` TabularUnifiedsage/modular/modsym/relation_matrix.py` in your patch.\n\n \n> This kind of work should definitely be done, but in another ticket. We will have to come to an agreement about these design issues. For now, let's get this patch into Sage.\n\nAgreed, this show that they are a lot of possible improvement in sage output routine. Thanks a lot for showing us how to do that. \n\nI'm waiting for the results of the tests to give you a positive review...",
    "created_at": "2009-12-02T20:53:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1918",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1918#issuecomment-12127",
    "user": "https://github.com/hivert"
}
```

Replying to [comment:10 wcauchois]:
> In one of my earlier iterations of the displayhook, I applied the special list formatting to every "tall" list. But when I ran testall I found that some objects just didn't work well with the formatting. So I think that applying the hook always is a mistake, and besides would introduce many more doctest headaches. Having objects "opt-in" by including a special field or method that tells the displayhook to use the special list formatting sounds like a good idea though.

I even tried to apply it on **all** lists ! I can tell you that there are much more output that looks better with your modification than without. (see e.g. in  `sage/modular/arithgroup/`... I'm not sure doing it systematically is a mistake... But some objects have to adapt their output, and the way you decide to break a line or not is not always optimal (see e.g. the output of ` TabularUnifiedsage/modular/modsym/relation_matrix.py` in your patch.

 
> This kind of work should definitely be done, but in another ticket. We will have to come to an agreement about these design issues. For now, let's get this patch into Sage.

Agreed, this show that they are a lot of possible improvement in sage output routine. Thanks a lot for showing us how to do that. 

I'm waiting for the results of the tests to give you a positive review...



---

archive/issue_comments_012128.json:
```json
{
    "body": "Everything is ok ! Positive review. (This is my 11th review for 4.3 :-)",
    "created_at": "2009-12-02T20:56:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1918",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1918#issuecomment-12128",
    "user": "https://github.com/hivert"
}
```

Everything is ok ! Positive review. (This is my 11th review for 4.3 :-)



---

archive/issue_comments_012129.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-02T20:58:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1918",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1918#issuecomment-12129",
    "user": "https://github.com/hivert"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_012130.json:
```json
{
    "body": "I've a request concerning this ticket: You manage to hijack ipython's printer but not python's one.\n\n```\nsage: [matrix(2,2)] * 3\n[\n[0 0]  [0 0]  [0 0]\n[0 0], [0 0], [0 0]\n]\nsage: print([matrix(2,2)] * 3)\n[[0 0]\n[0 0], [0 0]\n[0 0], [0 0]\n[0 0]]\n```\n\nIs it trivial to solve this ? Or should I open a new ticket ?\n\nCheers,\n\nFlorent",
    "created_at": "2009-12-03T21:19:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1918",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1918#issuecomment-12130",
    "user": "https://github.com/hivert"
}
```

I've a request concerning this ticket: You manage to hijack ipython's printer but not python's one.

```
sage: [matrix(2,2)] * 3
[
[0 0]  [0 0]  [0 0]
[0 0], [0 0], [0 0]
]
sage: print([matrix(2,2)] * 3)
[[0 0]
[0 0], [0 0]
[0 0], [0 0]
[0 0]]
```

Is it trivial to solve this ? Or should I open a new ticket ?

Cheers,

Florent



---

archive/issue_comments_012131.json:
```json
{
    "body": "Replying to [comment:14 hivert]:\n> I've a request concerning this ticket: You manage to hijack ipython's printer but not python's one.\n> {{{\n> sage: [matrix(2,2)] * 3\n> [\n> [0 0]  [0 0]  [0 0]\n> [0 0], [0 0], [0 0]\n> ]\n> sage: print([matrix(2,2)] * 3)\n> [[0 0]\n> [0 0], [0 0]\n> [0 0], [0 0]\n> [0 0]]\n> }}}\n> Is it trivial to solve this ? Or should I open a new ticket ?\n\nYou raise an interesting point Florent. The problem here is that Python's displayhook mechanism only affects the output from the interpreter, not the behavior of the print statement. In fact, the displayhook uses the print statement to output values, so if the print statement used the displayhook it would be bad.\n\nAFAIK, there is no way to hook into the print statement. All it does is write the object's repr to sys.stdout. And now we run into the limitation that drove us to use a displayhook in the first place: you can't change the way repr behaves for lists.\n\nThe only thing I can suggest is to add a function, say, `format_list_of_matrices()` to the matrix library so that your code becomes:\n\n```\nsage: print format_list_of_matrices([matrix(2,2) * 3])\n```\n\nBut I feel like such a facility would be not at all obvious for end-users. Unless they notice how crappy a list of matrices looks when its `print`ed and root around the documentation for answers.",
    "created_at": "2009-12-04T03:07:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1918",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1918#issuecomment-12131",
    "user": "https://trac.sagemath.org/admin/accounts/users/wcauchois"
}
```

Replying to [comment:14 hivert]:
> I've a request concerning this ticket: You manage to hijack ipython's printer but not python's one.
> {{{
> sage: [matrix(2,2)] * 3
> [
> [0 0]  [0 0]  [0 0]
> [0 0], [0 0], [0 0]
> ]
> sage: print([matrix(2,2)] * 3)
> [[0 0]
> [0 0], [0 0]
> [0 0], [0 0]
> [0 0]]
> }}}
> Is it trivial to solve this ? Or should I open a new ticket ?

You raise an interesting point Florent. The problem here is that Python's displayhook mechanism only affects the output from the interpreter, not the behavior of the print statement. In fact, the displayhook uses the print statement to output values, so if the print statement used the displayhook it would be bad.

AFAIK, there is no way to hook into the print statement. All it does is write the object's repr to sys.stdout. And now we run into the limitation that drove us to use a displayhook in the first place: you can't change the way repr behaves for lists.

The only thing I can suggest is to add a function, say, `format_list_of_matrices()` to the matrix library so that your code becomes:

```
sage: print format_list_of_matrices([matrix(2,2) * 3])
```

But I feel like such a facility would be not at all obvious for end-users. Unless they notice how crappy a list of matrices looks when its `print`ed and root around the documentation for answers.



---

archive/issue_comments_012132.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-12-06T09:20:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1918",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1918#issuecomment-12132",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_events_002074.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-12-06T09:20:03Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1918",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1918#event-2074"
}
```
