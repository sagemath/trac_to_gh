# Issue 6109: Bring documentation for QQbar up to 100% and add to reference manual

archive/issues_006109.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  cwitty\n\nKeywords: QQbar documentation\n\nThis is not good:\n\nsage/rings/qqbar.py\nSCORE sage/rings/qqbar.py: 40% (110 of 272)\n\nand we also need to put this into the reference manual.  It is not totally clear which section, so I'll start out by putting it into number_fields.rst.\n\nI discovered this while trying to actually use the class, of course...so I will have a go but might need to consult Carl.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6109\n\n",
    "created_at": "2009-05-21T08:29:20Z",
    "labels": [
        "algebra",
        "major",
        "bug"
    ],
    "title": "Bring documentation for QQbar up to 100% and add to reference manual",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6109",
    "user": "cremona"
}
```
Assignee: tbd

CC:  cwitty

Keywords: QQbar documentation

This is not good:

sage/rings/qqbar.py
SCORE sage/rings/qqbar.py: 40% (110 of 272)

and we also need to put this into the reference manual.  It is not totally clear which section, so I'll start out by putting it into number_fields.rst.

I discovered this while trying to actually use the class, of course...so I will have a go but might need to consult Carl.

Issue created by migration from https://trac.sagemath.org/ticket/6109





---

archive/issue_comments_048802.json:
```json
{
    "body": "I should have said:  there is an excellent block of nearly 500 lines at the beginning of qqbar.py, -- all the more reason to get that into the manual!",
    "created_at": "2009-05-21T08:43:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6109",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6109#issuecomment-48802",
    "user": "cremona"
}
```

I should have said:  there is an excellent block of nearly 500 lines at the beginning of qqbar.py, -- all the more reason to get that into the manual!



---

archive/issue_comments_048803.json:
```json
{
    "body": "Attachment [trac_6109_1.patch](tarball://root/attachments/some-uuid/ticket6109/trac_6109_1.patch) by cremona created at 2009-05-21 11:32:38\n\nPart 1: applies to 4.0.alpha0",
    "created_at": "2009-05-21T11:32:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6109",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6109#issuecomment-48803",
    "user": "cremona"
}
```

Attachment [trac_6109_1.patch](tarball://root/attachments/some-uuid/ticket6109/trac_6109_1.patch) by cremona created at 2009-05-21 11:32:38

Part 1: applies to 4.0.alpha0



---

archive/issue_comments_048804.json:
```json
{
    "body": "The first patch converts the docstrings to ReST and put the file into the reference manual, so it looks ok. Still to do:\n1. Reformat the docstrongs which do exist into standard layout (with INPUT/OUTPUT blocks etc)\n2. Add docstrings for 162 functions which do not yet have them (!)\n3. Add doctests to those and the few function which have docstrings but no doctests.\n\nI have taken the liberty of adding \"needs review\" already despite not having increased the coverage at all yet, since I do actually believe that this should go in already.  there is a huge amount of very useful code here which deserves better publicity (as I think having it in the reference manual will do) and there is already plenty of documentation.  Having been through this file, I can see that I should be using QQbar much more than I have done up to now.\n\nI am not promising to work on tasks 1-3 above i nthe near future, so if anyone else wants to make a start they should go ahead.",
    "created_at": "2009-05-21T11:38:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6109",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6109#issuecomment-48804",
    "user": "cremona"
}
```

The first patch converts the docstrings to ReST and put the file into the reference manual, so it looks ok. Still to do:
1. Reformat the docstrongs which do exist into standard layout (with INPUT/OUTPUT blocks etc)
2. Add docstrings for 162 functions which do not yet have them (!)
3. Add doctests to those and the few function which have docstrings but no doctests.

I have taken the liberty of adding "needs review" already despite not having increased the coverage at all yet, since I do actually believe that this should go in already.  there is a huge amount of very useful code here which deserves better publicity (as I think having it in the reference manual will do) and there is already plenty of documentation.  Having been through this file, I can see that I should be using QQbar much more than I have done up to now.

I am not promising to work on tasks 1-3 above i nthe near future, so if anyone else wants to make a start they should go ahead.



---

archive/issue_comments_048805.json:
```json
{
    "body": "Suggestion for Carl:  I think that the functions norm() and conjugate() on QQbar are not very useful.  I would change the name of conjugate() to complex_conjugate().\n\nI would like to see new functions conjugates(), norm(), trace():\n\n* a.conjugates()  returns a.minpoly().roots(QQbar,multiplicities=False)\n* a.norm()  returns a.minpoly().constant_coefficient()  (* correct sign)\n* a.trace() returns -a.minpoly().coeffs()[a.degree()-1]\n\nThe more I look at qqbar.py the more impressed I am!\n\nJohn",
    "created_at": "2009-05-22T08:36:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6109",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6109#issuecomment-48805",
    "user": "cremona"
}
```

Suggestion for Carl:  I think that the functions norm() and conjugate() on QQbar are not very useful.  I would change the name of conjugate() to complex_conjugate().

I would like to see new functions conjugates(), norm(), trace():

* a.conjugates()  returns a.minpoly().roots(QQbar,multiplicities=False)
* a.norm()  returns a.minpoly().constant_coefficient()  (* correct sign)
* a.trace() returns -a.minpoly().coeffs()[a.degree()-1]

The more I look at qqbar.py the more impressed I am!

John



---

archive/issue_comments_048806.json:
```json
{
    "body": "The patch applies fine to 4.0.rc1, and qqbar.py passes doctests (unsurprisingly, since the patch doesn't actually change any tests). The key thing is the documentation, which complies fine except for one small glitch:\n\n\n```\nreading sources... sage/rings/qqbar\nWARNING: /home/david/sage-4.0.rc1/local/lib/python2.5/site-packages/sage/rings/qqbar.py:docstring of sage.rings.qqbar:81: (ERROR/3) Unexpected indentation.\n```\n\n\nI can't remotely pin down what it is that's upsetting the Sphinx parser. If you delete the entire offending docstring -- the big one at the top of the file -- you get the same \"unexpected indentation\" error message again, but purporting to be coming from the docstring of some other random function, and if you go through several iterations of deleting docstrings it starts claiming that there is an unexpected indentation at line 0. This sounds rather like a Sphinx bug to me, especially as the finished documentation looks absolutely fine.\n\nI agree with John that the benefits of getting QQbar into the reference manual make it worth merging this patch now -- let's have a new ticket for adding the missing doctests.\n\nDavid",
    "created_at": "2009-05-28T10:37:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6109",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6109#issuecomment-48806",
    "user": "davidloeffler"
}
```

The patch applies fine to 4.0.rc1, and qqbar.py passes doctests (unsurprisingly, since the patch doesn't actually change any tests). The key thing is the documentation, which complies fine except for one small glitch:


```
reading sources... sage/rings/qqbar
WARNING: /home/david/sage-4.0.rc1/local/lib/python2.5/site-packages/sage/rings/qqbar.py:docstring of sage.rings.qqbar:81: (ERROR/3) Unexpected indentation.
```


I can't remotely pin down what it is that's upsetting the Sphinx parser. If you delete the entire offending docstring -- the big one at the top of the file -- you get the same "unexpected indentation" error message again, but purporting to be coming from the docstring of some other random function, and if you go through several iterations of deleting docstrings it starts claiming that there is an unexpected indentation at line 0. This sounds rather like a Sphinx bug to me, especially as the finished documentation looks absolutely fine.

I agree with John that the benefits of getting QQbar into the reference manual make it worth merging this patch now -- let's have a new ticket for adding the missing doctests.

David



---

archive/issue_comments_048807.json:
```json
{
    "body": "Thanks, David -- I spent ages trying to track down that error but without success.  I should have mentioned that when I posted the patch.",
    "created_at": "2009-05-28T11:05:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6109",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6109#issuecomment-48807",
    "user": "cremona"
}
```

Thanks, David -- I spent ages trying to track down that error but without success.  I should have mentioned that when I posted the patch.



---

archive/issue_comments_048808.json:
```json
{
    "body": "Attachment [6109_fix.patch](tarball://root/attachments/some-uuid/ticket6109/6109_fix.patch) by davidloeffler created at 2009-05-28 12:43:57\n\none-line ReST fix",
    "created_at": "2009-05-28T12:43:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6109",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6109#issuecomment-48808",
    "user": "davidloeffler"
}
```

Attachment [6109_fix.patch](tarball://root/attachments/some-uuid/ticket6109/6109_fix.patch) by davidloeffler created at 2009-05-28 12:43:57

one-line ReST fix



---

archive/issue_comments_048809.json:
```json
{
    "body": "Found it: here's a one-line patch that adds a missing blank line before a doctest block. (I have found several other similar glitches in the reference manual, which I'm about to open a ticket for.)",
    "created_at": "2009-05-28T13:01:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6109",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6109#issuecomment-48809",
    "user": "davidloeffler"
}
```

Found it: here's a one-line patch that adds a missing blank line before a doctest block. (I have found several other similar glitches in the reference manual, which I'm about to open a ticket for.)



---

archive/issue_comments_048810.json:
```json
{
    "body": "That is amazing -- the line given in the error message is miles away from the actual error.\n\nWe can now definitely give thie a +1 and it can rather safely be merged!",
    "created_at": "2009-05-28T17:32:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6109",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6109#issuecomment-48810",
    "user": "cremona"
}
```

That is amazing -- the line given in the error message is miles away from the actual error.

We can now definitely give thie a +1 and it can rather safely be merged!



---

archive/issue_comments_048811.json:
```json
{
    "body": "Merged both patches in 4.0.1.alpha0.",
    "created_at": "2009-06-01T00:00:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6109",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6109#issuecomment-48811",
    "user": "mhansen"
}
```

Merged both patches in 4.0.1.alpha0.



---

archive/issue_comments_048812.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-01T00:00:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6109",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6109#issuecomment-48812",
    "user": "mhansen"
}
```

Resolution: fixed
