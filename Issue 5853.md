# Issue 5853: Restify and include more documentation on elliptic curves

archive/issues_005853.json:
```json
{
    "body": "Assignee: was\n\nCC:  cremona\n\nKeywords: documentation, elliptic curves\n\nThis is a follow-up on ticket #4933 and #5851. I plan to work on following files\n\n* padic_height.py\n* ell_modular_symbols.py\n* ell_tate_curve.py\n* padic_lseries.py\n* sha_tate.py\n\nIssue created by migration from https://trac.sagemath.org/ticket/5853\n\n",
    "created_at": "2009-04-22T13:26:26Z",
    "labels": [
        "number theory",
        "major",
        "bug"
    ],
    "title": "Restify and include more documentation on elliptic curves",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5853",
    "user": "wuthrich"
}
```
Assignee: was

CC:  cremona

Keywords: documentation, elliptic curves

This is a follow-up on ticket #4933 and #5851. I plan to work on following files

* padic_height.py
* ell_modular_symbols.py
* ell_tate_curve.py
* padic_lseries.py
* sha_tate.py

Issue created by migration from https://trac.sagemath.org/ticket/5853





---

archive/issue_comments_046224.json:
```json
{
    "body": "Very good!   Nice to know I have been setting a good example.\n\nChris, in case you have not yet picked this up, debugging the restification involves the following.\n\n1. Make a new clone.\n2. In the new clone run \"sage -docbuild reference html\".  The first time takes a while.\n3. Point your browser at the place it says (prepend \"file://\" and append \"index.html\")\n4. If you are adding a new file to the ref manual, add a suitable line to (for example) $SAGE_ROOT/devel/sage/doc/en/reference/plane_curves.rst\n5. After making some edits, after doing \"sage -b\" then as well as doing \"sage -t\" on the file, also do (again) \"sage -docbuild reference html\" which will pick up that the file has changed and rebuild the html page.  Of course the page needs to be reloaded in the browser.\n\nNot all of that was obvious to me, so I hope it helps!",
    "created_at": "2009-04-22T13:34:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5853",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5853#issuecomment-46224",
    "user": "cremona"
}
```

Very good!   Nice to know I have been setting a good example.

Chris, in case you have not yet picked this up, debugging the restification involves the following.

1. Make a new clone.
2. In the new clone run "sage -docbuild reference html".  The first time takes a while.
3. Point your browser at the place it says (prepend "file://" and append "index.html")
4. If you are adding a new file to the ref manual, add a suitable line to (for example) $SAGE_ROOT/devel/sage/doc/en/reference/plane_curves.rst
5. After making some edits, after doing "sage -b" then as well as doing "sage -t" on the file, also do (again) "sage -docbuild reference html" which will pick up that the file has changed and rebuild the html page.  Of course the page needs to be reloaded in the browser.

Not all of that was obvious to me, so I hope it helps!



---

archive/issue_comments_046225.json:
```json
{
    "body": "Attachment\n\nto be applied after tickets in #5846 and #5851",
    "created_at": "2009-04-24T15:20:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5853",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5853#issuecomment-46225",
    "user": "wuthrich"
}
```

Attachment

to be applied after tickets in #5846 and #5851



---

archive/issue_comments_046226.json:
```json
{
    "body": "No no, this patch is not right, do not even look at it. Sorry!!!!",
    "created_at": "2009-04-24T15:24:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5853",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5853#issuecomment-46226",
    "user": "wuthrich"
}
```

No no, this patch is not right, do not even look at it. Sorry!!!!



---

archive/issue_comments_046227.json:
```json
{
    "body": "Attachment\n\nReplaces the previous ticket as before this applies to 3.4.1 + #5846 and #5851",
    "created_at": "2009-04-24T15:45:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5853",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5853#issuecomment-46227",
    "user": "wuthrich"
}
```

Attachment

Replaces the previous ticket as before this applies to 3.4.1 + #5846 and #5851



---

archive/issue_comments_046228.json:
```json
{
    "body": "replaces all before.",
    "created_at": "2009-04-24T21:02:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5853",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5853#issuecomment-46228",
    "user": "wuthrich"
}
```

replaces all before.



---

archive/issue_comments_046229.json:
```json
{
    "body": "Attachment\n\nreplaces all before",
    "created_at": "2009-04-24T21:02:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5853",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5853#issuecomment-46229",
    "user": "wuthrich"
}
```

Attachment

replaces all before



---

archive/issue_comments_046230.json:
```json
{
    "body": "What do we learn : never try to submit a patch just before catching the train.\nSorry about this patching mess. \n\nOnly the very last patch counts. I applied it successfully against 3.4.1 + #4933 and #5851. It produces three doctest-errors in ell_rational_field with --long, but they are there even without my patch it seems to me.\n\nOne might decide against including ell_modular_symbols. The main documentation is in ell_rational_field. Of course I did not include padic_height, since it is deprecated anyway.\n\nI do not know how to solve the issue of the alias power_series producing double documentation. I do not know how the references to article should be done correctly.",
    "created_at": "2009-04-24T21:10:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5853",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5853#issuecomment-46230",
    "user": "wuthrich"
}
```

What do we learn : never try to submit a patch just before catching the train.
Sorry about this patching mess. 

Only the very last patch counts. I applied it successfully against 3.4.1 + #4933 and #5851. It produces three doctest-errors in ell_rational_field with --long, but they are there even without my patch it seems to me.

One might decide against including ell_modular_symbols. The main documentation is in ell_rational_field. Of course I did not include padic_height, since it is deprecated anyway.

I do not know how to solve the issue of the alias power_series producing double documentation. I do not know how the references to article should be done correctly.



---

archive/issue_comments_046231.json:
```json
{
    "body": "Great work!  The patch trac_5853_2.patch applies fine to 3.4.2.alpha0.  There a docbuild glitch in ell_rational_field.py which has nothing to do with this patch.  The new sections in the manual look great. All doctests in elliptic_curves pass (as of course they should since this patch only touches docstring, apart from a few very small things).",
    "created_at": "2009-04-26T19:56:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5853",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5853#issuecomment-46231",
    "user": "cremona"
}
```

Great work!  The patch trac_5853_2.patch applies fine to 3.4.2.alpha0.  There a docbuild glitch in ell_rational_field.py which has nothing to do with this patch.  The new sections in the manual look great. All doctests in elliptic_curves pass (as of course they should since this patch only touches docstring, apart from a few very small things).



---

archive/issue_comments_046232.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-30T00:32:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5853",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5853#issuecomment-46232",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_046233.json:
```json
{
    "body": "Merged trac_5853_2.patch in Sage 3.4.2.rc0.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-30T00:32:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5853",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5853#issuecomment-46233",
    "user": "mabshoff"
}
```

Merged trac_5853_2.patch in Sage 3.4.2.rc0.

Cheers,

Michael
