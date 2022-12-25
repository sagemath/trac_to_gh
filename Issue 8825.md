# Issue 8825: Improve documentation for function norm

archive/issues_008825.json:
```json
{
    "body": "Assignee: @jasongrout\n\nCC:  nguyenminh2@gmail.com\n\nThe documentation for the function norm currently does not mention that different kinds of norms are used for complex numbers and vectors of complex numbers.\n\nI was very surprised that for a complex number z, \nnorm(z) == norm(vector([z]))<sup>2</sup>, and no hint of this is available from the documentation available through executing \"sage: norm?\".\n\nIssue created by migration from https://trac.sagemath.org/ticket/8825\n\n",
    "created_at": "2010-04-29T19:49:58Z",
    "labels": [
        "component: misc",
        "trivial"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6",
    "title": "Improve documentation for function norm",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8825",
    "user": "https://trac.sagemath.org/admin/accounts/users/johan"
}
```
Assignee: @jasongrout

CC:  nguyenminh2@gmail.com

The documentation for the function norm currently does not mention that different kinds of norms are used for complex numbers and vectors of complex numbers.

I was very surprised that for a complex number z, 
norm(z) == norm(vector([z]))<sup>2</sup>, and no hint of this is available from the documentation available through executing "sage: norm?".

Issue created by migration from https://trac.sagemath.org/ticket/8825





---

archive/issue_comments_080899.json:
```json
{
    "body": "Patch",
    "created_at": "2010-04-29T19:58:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8825",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8825#issuecomment-80899",
    "user": "https://trac.sagemath.org/admin/accounts/users/johan"
}
```

Patch



---

archive/issue_comments_080900.json:
```json
{
    "body": "Changing component from misc to documentation.",
    "created_at": "2010-04-29T20:05:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8825",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8825#issuecomment-80900",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing component from misc to documentation.



---

archive/issue_events_021538.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2010-04-29T20:05:21Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8825",
    "milestone": "sage-4.4.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8825#event-21538"
}
```



---

archive/issue_comments_080901.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-04-29T20:05:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8825",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8825#issuecomment-80901",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_080902.json:
```json
{
    "body": "Attachment [trac_8825_norm_docstring.patch](tarball://root/attachments/some-uuid/ticket8825/trac_8825_norm_docstring.patch) by mvngu created at 2010-04-29 20:05:21",
    "created_at": "2010-04-29T20:05:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8825",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8825#issuecomment-80902",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [trac_8825_norm_docstring.patch](tarball://root/attachments/some-uuid/ticket8825/trac_8825_norm_docstring.patch) by mvngu created at 2010-04-29 20:05:21



---

archive/issue_comments_080903.json:
```json
{
    "body": "I'm happy with the patch [trac_8825_norm_docstring.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8825/trac_8825_norm_docstring.patch). To prevent further confusion regarding how the norm function is defined for various objects, I have added more documentation for various norm functions. The new documentation also cross references between norm functions. So only my patch [trac_8825-more-norm-doc.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8825/trac_8825-more-norm-doc.patch) needs review by anyone but me. If it gets a positive review, the whole ticket is good to go.",
    "created_at": "2010-04-30T20:47:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8825",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8825#issuecomment-80903",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

I'm happy with the patch [trac_8825_norm_docstring.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8825/trac_8825_norm_docstring.patch). To prevent further confusion regarding how the norm function is defined for various objects, I have added more documentation for various norm functions. The new documentation also cross references between norm functions. So only my patch [trac_8825-more-norm-doc.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8825/trac_8825-more-norm-doc.patch) needs review by anyone but me. If it gets a positive review, the whole ticket is good to go.



---

archive/issue_comments_080904.json:
```json
{
    "body": "Attachment [weirddoc.png](tarball://root/attachments/some-uuid/ticket8825/weirddoc.png) by pang created at 2010-05-12 08:36:33",
    "created_at": "2010-05-12T08:36:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8825",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8825#issuecomment-80904",
    "user": "https://trac.sagemath.org/admin/accounts/users/pang"
}
```

Attachment [weirddoc.png](tarball://root/attachments/some-uuid/ticket8825/weirddoc.png) by pang created at 2010-05-12 08:36:33



---

archive/issue_comments_080905.json:
```json
{
    "body": "I've attached a screen capture: the norm reads |*v*| in the notebook (norm?). However, if I read:\n\n$SAGE_ROOT/devel/sage/doc/output/html/en/reference/sage/misc/functional.html\n\nit looks fine.",
    "created_at": "2010-05-12T08:45:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8825",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8825#issuecomment-80905",
    "user": "https://trac.sagemath.org/admin/accounts/users/pang"
}
```

I've attached a screen capture: the norm reads |*v*| in the notebook (norm?). However, if I read:

$SAGE_ROOT/devel/sage/doc/output/html/en/reference/sage/misc/functional.html

it looks fine.



---

archive/issue_comments_080906.json:
```json
{
    "body": "Another comment: when read in the notebook, it says:\n\n```\nSee also\n\n    * norm \u2013 the p -norm of a matrix.\n    * norm \u2013 the p -norm of a vector.\n    * norm \u2013 the norm of a double precision complex number.\n    * norm \u2013 the norm of an arbitrary precision complex number.\n    * norm \u2013 the complex norm of a symbolic expression.\n```\n\nwhich is confusing. Maybe instead of norm it could say sage.matrix.matrix2.Matrix.norm, etcetera. A cool possibility would be to put hyperlinks, but this would probably interfere with the automatic generation of doc, wouldn't it?",
    "created_at": "2010-05-12T08:54:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8825",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8825#issuecomment-80906",
    "user": "https://trac.sagemath.org/admin/accounts/users/pang"
}
```

Another comment: when read in the notebook, it says:

```
See also

    * norm – the p -norm of a matrix.
    * norm – the p -norm of a vector.
    * norm – the norm of a double precision complex number.
    * norm – the norm of an arbitrary precision complex number.
    * norm – the complex norm of a symbolic expression.
```

which is confusing. Maybe instead of norm it could say sage.matrix.matrix2.Matrix.norm, etcetera. A cool possibility would be to put hyperlinks, but this would probably interfere with the automatic generation of doc, wouldn't it?



---

archive/issue_comments_080907.json:
```json
{
    "body": "Nope, you can put in autogenerated hyperlinks.  For example, the markup\n\n```\n:meth:`sage.matrix.matrix2.Matrix.norm`\n```\n\nwould change to a link to that method.",
    "created_at": "2010-06-06T20:20:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8825",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8825#issuecomment-80907",
    "user": "https://github.com/mwhansen"
}
```

Nope, you can put in autogenerated hyperlinks.  For example, the markup

```
:meth:`sage.matrix.matrix2.Matrix.norm`
```

would change to a link to that method.



---

archive/issue_comments_080908.json:
```json
{
    "body": "Attachment [trac_8825-more-norm-doc.patch](tarball://root/attachments/some-uuid/ticket8825/trac_8825-more-norm-doc.patch) by mvngu created at 2010-06-15 04:24:29\n\nReplying to [comment:4 pang]:\n> Maybe instead of norm it could say sage.matrix.matrix2.Matrix.norm, etcetera. \n\nMy updated patch takes care of this. As for the weirdness in the notebook, I don't know how to fix that.",
    "created_at": "2010-06-15T04:24:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8825",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8825#issuecomment-80908",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [trac_8825-more-norm-doc.patch](tarball://root/attachments/some-uuid/ticket8825/trac_8825-more-norm-doc.patch) by mvngu created at 2010-06-15 04:24:29

Replying to [comment:4 pang]:
> Maybe instead of norm it could say sage.matrix.matrix2.Matrix.norm, etcetera. 

My updated patch takes care of this. As for the weirdness in the notebook, I don't know how to fix that.



---

archive/issue_comments_080909.json:
```json
{
    "body": "See my suggestion on [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/2e10a6e35237c87e?hl=en). I personally think it would useful to also add \n\n1) External links to Mathworld and Wikipedia\n\n* http://en.wikipedia.org/wiki/Matrix_norm\n* http://mathworld.wolfram.com/Norm.html\n* http://mathworld.wolfram.com/MatrixNorm.html\n* http://mathworld.wolfram.com/VectorNorm.html \n\nThese would certainly help people like me, who are not mathmaticians and might want to find out a bit more about a topic. \n\n2) Document the nearest Mathematica, Maple, MATLAB and Macsyma commands when possible. \n\nFor Mathematica, it is Norm[] See:\n\nhttp://reference.wolfram.com/mathematica/ref/Norm.html\n\nFor MATLAB it is norm()\n\nhttp://www.mathworks.com/help/techdoc/ref/norm.html\n\nI'm not sure about Maple - but  Norm() might be the right one. \n\nhttp://www.maplesoft.com/support/help/Maple/view.aspx?path=VectorCalculus%2fNorm\n\n(Please check *'all* these - I'm not a mathematician). \n\nHaving a list of the nearest equivalent commands in the commercial packages would be useful if we ever provide any documentation helping people migrate from those packages to Sage. \n\nI'm not saying there's anything wrong with this ticket, and my comments should certainly **not** be interpreted as need_work. But I think the documentation could be made more useful by having links and names of the commands in the external packages. \n\nDave",
    "created_at": "2010-09-21T09:26:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8825",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8825#issuecomment-80909",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

See my suggestion on [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/2e10a6e35237c87e?hl=en). I personally think it would useful to also add 

1) External links to Mathworld and Wikipedia

* http://en.wikipedia.org/wiki/Matrix_norm
* http://mathworld.wolfram.com/Norm.html
* http://mathworld.wolfram.com/MatrixNorm.html
* http://mathworld.wolfram.com/VectorNorm.html 

These would certainly help people like me, who are not mathmaticians and might want to find out a bit more about a topic. 

2) Document the nearest Mathematica, Maple, MATLAB and Macsyma commands when possible. 

For Mathematica, it is Norm[] See:

http://reference.wolfram.com/mathematica/ref/Norm.html

For MATLAB it is norm()

http://www.mathworks.com/help/techdoc/ref/norm.html

I'm not sure about Maple - but  Norm() might be the right one. 

http://www.maplesoft.com/support/help/Maple/view.aspx?path=VectorCalculus%2fNorm

(Please check *'all* these - I'm not a mathematician). 

Having a list of the nearest equivalent commands in the commercial packages would be useful if we ever provide any documentation helping people migrate from those packages to Sage. 

I'm not saying there's anything wrong with this ticket, and my comments should certainly **not** be interpreted as need_work. But I think the documentation could be made more useful by having links and names of the commands in the external packages. 

Dave



---

archive/issue_comments_080910.json:
```json
{
    "body": "Replying to [comment:7 drkirkby]:\n> But I think the documentation could be made more useful by having links and names of the commands in the external packages. \n> \n> Dave \n\n\nOops. I mean the documentation could be made more useful by having the name of the nearest command in the commercial packages. Not necessarily links to them, though that might be worth considering too. Some are non-obvious. For example factor() in Sage can factor an integer:\n\n```\nsage: factor(12)\n2^2 * 3\n```\n\nbut in Mathematica one would use `FactorInteger`\n\n```\nIn[1]:= FactorInteger[12]\n\nOut[1]= {{2, 2}, {3, 1}}\n```",
    "created_at": "2010-09-21T09:38:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8825",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8825#issuecomment-80910",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Replying to [comment:7 drkirkby]:
> But I think the documentation could be made more useful by having links and names of the commands in the external packages. 
> 
> Dave 


Oops. I mean the documentation could be made more useful by having the name of the nearest command in the commercial packages. Not necessarily links to them, though that might be worth considering too. Some are non-obvious. For example factor() in Sage can factor an integer:

```
sage: factor(12)
2^2 * 3
```

but in Mathematica one would use `FactorInteger`

```
In[1]:= FactorInteger[12]

Out[1]= {{2, 2}, {3, 1}}
```



---

archive/issue_comments_080911.json:
```json
{
    "body": "Positive review - these are nice improvements.",
    "created_at": "2010-09-21T13:18:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8825",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8825#issuecomment-80911",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Positive review - these are nice improvements.



---

archive/issue_comments_080912.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-09-21T13:18:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8825",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8825#issuecomment-80912",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_080913.json:
```json
{
    "body": "Note that one has to perhaps change the locale (e.g. `LC_ALL`) to some UTF-8 one before importing the first patch:\n\n```\napplying ../../../patches/trac_8825_norm_docstring.patch\ntransaction abort!\nrollback completed\nabort: decoding near 'Johan Gr\u00f6nqvist <': 'ascii' codec can't decode byte 0xc3 in position 8: ordinal not in range(128)!\n```",
    "created_at": "2010-09-21T13:50:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8825",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8825#issuecomment-80913",
    "user": "https://github.com/nexttime"
}
```

Note that one has to perhaps change the locale (e.g. `LC_ALL`) to some UTF-8 one before importing the first patch:

```
applying ../../../patches/trac_8825_norm_docstring.patch
transaction abort!
rollback completed
abort: decoding near 'Johan Grönqvist <': 'ascii' codec can't decode byte 0xc3 in position 8: ordinal not in range(128)!
```



---

archive/issue_comments_080914.json:
```json
{
    "body": "Replying to [comment:10 leif]:\n\n> Note that one has to perhaps change the locale (e.g. `LC_ALL`) to some UTF-8 one before importing the first patch: abort: decoding near 'Johan Gr\u00f6nqvist <': 'ascii' codec can't decode byte 0xc3 in position 8: ordinal not in range(128)!\n\n\nI do not know what is easiest, but changing my name to Johan Gronqvist (if that is the only problem) is another solution, that may work better. (Those dots are not important to me.)\n\n/ Johan",
    "created_at": "2010-09-22T11:30:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8825",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8825#issuecomment-80914",
    "user": "https://trac.sagemath.org/admin/accounts/users/johan"
}
```

Replying to [comment:10 leif]:

> Note that one has to perhaps change the locale (e.g. `LC_ALL`) to some UTF-8 one before importing the first patch: abort: decoding near 'Johan Grönqvist <': 'ascii' codec can't decode byte 0xc3 in position 8: ordinal not in range(128)!


I do not know what is easiest, but changing my name to Johan Gronqvist (if that is the only problem) is another solution, that may work better. (Those dots are not important to me.)

/ Johan



---

archive/issue_comments_080915.json:
```json
{
    "body": "Replying to [comment:11 johan]:\n> I do not know what is easiest, but changing my name to Johan Gronqvist (if that is the only problem) is another solution, that may work better. (Those dots are not important to me.)\n\n\nNo, that was my (or Mercurial's) mistake. It just happened that I'd changed the locale in the terminal I was trying to apply the patch in; the note was meant to keep others from running into the same.\n\n-Leif",
    "created_at": "2010-09-22T12:42:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8825",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8825#issuecomment-80915",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:11 johan]:
> I do not know what is easiest, but changing my name to Johan Gronqvist (if that is the only problem) is another solution, that may work better. (Those dots are not important to me.)


No, that was my (or Mercurial's) mistake. It just happened that I'd changed the locale in the terminal I was trying to apply the patch in; the note was meant to keep others from running into the same.

-Leif



---

archive/issue_events_021539.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-09-28T09:08:37Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8825",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8825#event-21539"
}
```



---

archive/issue_comments_080916.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-09-28T09:08:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8825",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8825#issuecomment-80916",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed
