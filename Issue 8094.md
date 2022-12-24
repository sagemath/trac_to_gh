# Issue 8094: shortcuts for matrix transpose, complex conjugate, ...

archive/issues_008094.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @robertwb @rbeezer\n\nThe aim is to enhance `/sage/matrix/matrix*.pyx` files with a `__getattr__` mechanism to call `self.transpose()` and others more quickly. The attribute lookup mechanism provides a shortcut like `self.T` that is resolved to `self.transpose()`. \nShortcuts should be similar to other environments like `numpy`.\n\nAdditionally, `__setattr__` and `__delattr__` have to be implemented to avoid modification and deletion of these attributes.\n\nNotes: [python data model](http://docs.python.org/reference/datamodel.html#customizing-attribute-access).\n\nIssue created by migration from https://trac.sagemath.org/ticket/8094\n\n",
    "created_at": "2010-01-27T13:00:23Z",
    "labels": [
        "linear algebra",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.7.2",
    "title": "shortcuts for matrix transpose, complex conjugate, ...",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8094",
    "user": "@haraldschilly"
}
```
Assignee: @williamstein

CC:  @robertwb @rbeezer

The aim is to enhance `/sage/matrix/matrix*.pyx` files with a `__getattr__` mechanism to call `self.transpose()` and others more quickly. The attribute lookup mechanism provides a shortcut like `self.T` that is resolved to `self.transpose()`. 
Shortcuts should be similar to other environments like `numpy`.

Additionally, `__setattr__` and `__delattr__` have to be implemented to avoid modification and deletion of these attributes.

Notes: [python data model](http://docs.python.org/reference/datamodel.html#customizing-attribute-access).

Issue created by migration from https://trac.sagemath.org/ticket/8094





---

archive/issue_comments_070925.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-01-27T15:39:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8094",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8094#issuecomment-70925",
    "user": "@haraldschilly"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_070926.json:
```json
{
    "body": "This first patch adds .T for all kinds of matrices in matrix_dense.pyx and some docstrings.",
    "created_at": "2010-01-27T15:39:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8094",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8094#issuecomment-70926",
    "user": "@haraldschilly"
}
```

This first patch adds .T for all kinds of matrices in matrix_dense.pyx and some docstrings.



---

archive/issue_comments_070927.json:
```json
{
    "body": "`.T` has more tests and I think it works for all of them now.\n\nattachment *.2.patch should be deleted or ignored.",
    "created_at": "2010-01-27T18:09:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8094",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8094#issuecomment-70927",
    "user": "@haraldschilly"
}
```

`.T` has more tests and I think it works for all of them now.

attachment *.2.patch should be deleted or ignored.



---

archive/issue_comments_070928.json:
```json
{
    "body": "I deleted the .2.patch.",
    "created_at": "2010-01-28T06:42:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8094",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8094#issuecomment-70928",
    "user": "@jasongrout"
}
```

I deleted the .2.patch.



---

archive/issue_comments_070929.json:
```json
{
    "body": "Since these are cython files, why don't you use the Cython property functionality to implement this?\n\nhttp://docs.cython.org/docs/extension_types.html#properties\n\nRobert, is there an efficiency gain or some reason why one would prefer the Cython property statement to what is in this patch?",
    "created_at": "2010-01-28T06:44:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8094",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8094#issuecomment-70929",
    "user": "@jasongrout"
}
```

Since these are cython files, why don't you use the Cython property functionality to implement this?

http://docs.cython.org/docs/extension_types.html#properties

Robert, is there an efficiency gain or some reason why one would prefer the Cython property statement to what is in this patch?



---

archive/issue_comments_070930.json:
```json
{
    "body": "I thought that properties don't work in cython files, but yesterday I tried them (the decorator didn't work, but just the statement is fine) and they do. Thank's for the reference! I'll use them. The advantage is that then you have these shortcuts in autocomplete. It's also better to define them once and for all in matrix2.pyx - I think that's the best place?",
    "created_at": "2010-01-28T09:37:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8094",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8094#issuecomment-70930",
    "user": "@haraldschilly"
}
```

I thought that properties don't work in cython files, but yesterday I tried them (the decorator didn't work, but just the statement is fine) and they do. Thank's for the reference! I'll use them. The advantage is that then you have these shortcuts in autocomplete. It's also better to define them once and for all in matrix2.pyx - I think that's the best place?



---

archive/issue_comments_070931.json:
```json
{
    "body": "doin' it the cython way",
    "created_at": "2010-03-22T17:40:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8094",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8094#issuecomment-70931",
    "user": "@haraldschilly"
}
```

doin' it the cython way



---

archive/issue_comments_070932.json:
```json
{
    "body": "Attachment [8094-shortcut-matrix-transpose.patch](tarball://root/attachments/some-uuid/ticket8094/8094-shortcut-matrix-transpose.patch) by @haraldschilly created at 2010-03-22 17:41:10",
    "created_at": "2010-03-22T17:41:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8094",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8094#issuecomment-70932",
    "user": "@haraldschilly"
}
```

Attachment [8094-shortcut-matrix-transpose.patch](tarball://root/attachments/some-uuid/ticket8094/8094-shortcut-matrix-transpose.patch) by @haraldschilly created at 2010-03-22 17:41:10



---

archive/issue_comments_070933.json:
```json
{
    "body": "schilly: is this patch still needs_work, or should it be needs_review now?",
    "created_at": "2010-12-18T19:57:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8094",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8094#issuecomment-70933",
    "user": "@jasongrout"
}
```

schilly: is this patch still needs_work, or should it be needs_review now?



---

archive/issue_comments_070934.json:
```json
{
    "body": "jason: as far as i remember, the problem was that it was interfering with another matrix property (i.e. a doctest was failing and I didn't really understand why). so, the idea as it is coded works, but it's not ready for review.",
    "created_at": "2010-12-18T20:00:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8094",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8094#issuecomment-70934",
    "user": "@haraldschilly"
}
```

jason: as far as i remember, the problem was that it was interfering with another matrix property (i.e. a doctest was failing and I didn't really understand why). so, the idea as it is coded works, but it's not ready for review.



---

archive/issue_comments_070935.json:
```json
{
    "body": "I see one doctest in matrix2.pyx failing, but that's because the expected output was wrong (it's the test for M.H in the conjugate() method).",
    "created_at": "2010-12-18T20:04:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8094",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8094#issuecomment-70935",
    "user": "@jasongrout"
}
```

I see one doctest in matrix2.pyx failing, but that's because the expected output was wrong (it's the test for M.H in the conjugate() method).



---

archive/issue_comments_070936.json:
```json
{
    "body": "ah well, time has passed since i looked into it, but it was a doctest failure somewhere else. probably just another one that has to be modified ... or it isn't an issue any more ;)",
    "created_at": "2010-12-18T20:08:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8094",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8094#issuecomment-70936",
    "user": "@haraldschilly"
}
```

ah well, time has passed since i looked into it, but it was a doctest failure somewhere else. probably just another one that has to be modified ... or it isn't an issue any more ;)



---

archive/issue_comments_070937.json:
```json
{
    "body": "I'm uploading a reviewer patch and giving a positive review momentarily :).",
    "created_at": "2010-12-18T20:12:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8094",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8094#issuecomment-70937",
    "user": "@jasongrout"
}
```

I'm uploading a reviewer patch and giving a positive review momentarily :).



---

archive/issue_comments_070938.json:
```json
{
    "body": "woohoo \\o/",
    "created_at": "2010-12-18T20:16:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8094",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8094#issuecomment-70938",
    "user": "@haraldschilly"
}
```

woohoo \o/



---

archive/issue_comments_070939.json:
```json
{
    "body": "apply on top of previous patches",
    "created_at": "2010-12-18T20:22:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8094",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8094#issuecomment-70939",
    "user": "@jasongrout"
}
```

apply on top of previous patches



---

archive/issue_comments_070940.json:
```json
{
    "body": "Attachment [8094_matrix_shortcut_docs_reviewer.patch](tarball://root/attachments/some-uuid/ticket8094/8094_matrix_shortcut_docs_reviewer.patch) by @jasongrout created at 2010-12-18 20:25:25\n\nOkay, maybe my changes should be reviewed (since they fix some of the doc issues).  \n\nDoctests pass in matrix/*.py[x] with these patches applied, and Harald's code looks good, so positive review for his patch (given that my doctest patch is applied).  \n\nSomeone should verify my doctest changes are good.",
    "created_at": "2010-12-18T20:25:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8094",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8094#issuecomment-70940",
    "user": "@jasongrout"
}
```

Attachment [8094_matrix_shortcut_docs_reviewer.patch](tarball://root/attachments/some-uuid/ticket8094/8094_matrix_shortcut_docs_reviewer.patch) by @jasongrout created at 2010-12-18 20:25:25

Okay, maybe my changes should be reviewed (since they fix some of the doc issues).  

Doctests pass in matrix/*.py[x] with these patches applied, and Harald's code looks good, so positive review for his patch (given that my doctest patch is applied).  

Someone should verify my doctest changes are good.



---

archive/issue_comments_070941.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-12-18T20:25:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8094",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8094#issuecomment-70941",
    "user": "@jasongrout"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_070942.json:
```json
{
    "body": "Jason and Harald,\n\nThanks for putting this together.  I'd like to finish up getting this reviewed.  But two questions:\n\n1.  It seems like there is evidence of the shortcuts in each of the associated docstrings for the methods, but maybe it isn't always obvious.  Like  `A.I` seems to be buried along with the `~` version and has no real explanation that it is a property.  I find students get very confused with method calls with empty parentheses, and a property will just add to that, so I think it would be better to have some explanation.\n\n2.  #10471  implements `conjugate_transpose()` until we reclaim `adjoint()`.  So that would be the place to add in the shortcut.  Should we add that here since #10471 has a positive review, and maybe change the definition?\n\nI can do the above on a reviewer patch in the next day or two if necessary.\n\nRob",
    "created_at": "2010-12-19T19:08:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8094",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8094#issuecomment-70942",
    "user": "@rbeezer"
}
```

Jason and Harald,

Thanks for putting this together.  I'd like to finish up getting this reviewed.  But two questions:

1.  It seems like there is evidence of the shortcuts in each of the associated docstrings for the methods, but maybe it isn't always obvious.  Like  `A.I` seems to be buried along with the `~` version and has no real explanation that it is a property.  I find students get very confused with method calls with empty parentheses, and a property will just add to that, so I think it would be better to have some explanation.

2.  #10471  implements `conjugate_transpose()` until we reclaim `adjoint()`.  So that would be the place to add in the shortcut.  Should we add that here since #10471 has a positive review, and maybe change the definition?

I can do the above on a reviewer patch in the next day or two if necessary.

Rob



---

archive/issue_comments_070943.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2010-12-19T19:08:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8094",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8094#issuecomment-70943",
    "user": "@rbeezer"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_070944.json:
```json
{
    "body": "Attachment [trac-8094_matrix_shortcut_docs_reviewer2.patch](tarball://root/attachments/some-uuid/ticket8094/trac-8094_matrix_shortcut_docs_reviewer2.patch) by mraum created at 2011-08-05 17:24:59",
    "created_at": "2011-08-05T17:24:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8094",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8094#issuecomment-70944",
    "user": "mraum"
}
```

Attachment [trac-8094_matrix_shortcut_docs_reviewer2.patch](tarball://root/attachments/some-uuid/ticket8094/trac-8094_matrix_shortcut_docs_reviewer2.patch) by mraum created at 2011-08-05 17:24:59



---

archive/issue_comments_070945.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2011-08-05T17:28:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8094",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8094#issuecomment-70945",
    "user": "mraum"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_070946.json:
```json
{
    "body": "I added a further example in the documentation of conjugate_transpose.\n\nI am not sure whether 1. can be addressed at all. Typing m.T? I get the documentation of m. I would suggest to finish this anyway. It is a shame that this patch hasn't been merged for almost 2 years, and one doesn't need to tell students that they type m.T.",
    "created_at": "2011-08-05T17:28:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8094",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8094#issuecomment-70946",
    "user": "mraum"
}
```

I added a further example in the documentation of conjugate_transpose.

I am not sure whether 1. can be addressed at all. Typing m.T? I get the documentation of m. I would suggest to finish this anyway. It is a shame that this patch hasn't been merged for almost 2 years, and one doesn't need to tell students that they type m.T.



---

archive/issue_comments_070947.json:
```json
{
    "body": "Attachment [trac_8094-matrix-properties-more-documentation.patch](tarball://root/attachments/some-uuid/ticket8094/trac_8094-matrix-properties-more-documentation.patch) by @rbeezer created at 2011-08-22 21:55:33",
    "created_at": "2011-08-22T21:55:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8094",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8094#issuecomment-70947",
    "user": "@rbeezer"
}
```

Attachment [trac_8094-matrix-properties-more-documentation.patch](tarball://root/attachments/some-uuid/ticket8094/trac_8094-matrix-properties-more-documentation.patch) by @rbeezer created at 2011-08-22 21:55:33



---

archive/issue_comments_070948.json:
```json
{
    "body": "These are some of the earliest entries in the reference manual for `sage/matrix/matrix2.pyx`, so I think the documentation should include some examples, especially since the syntax is different (no parentheses).  However, INPUT and OUTPUT blocks feel like make-work, so I have not included that.\n\nI can give a positive review to everything up to my latest patch.  If somebody would review my (documentation-only) changes, this could be done.\n\nRob",
    "created_at": "2011-08-22T22:00:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8094",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8094#issuecomment-70948",
    "user": "@rbeezer"
}
```

These are some of the earliest entries in the reference manual for `sage/matrix/matrix2.pyx`, so I think the documentation should include some examples, especially since the syntax is different (no parentheses).  However, INPUT and OUTPUT blocks feel like make-work, so I have not included that.

I can give a positive review to everything up to my latest patch.  If somebody would review my (documentation-only) changes, this could be done.

Rob



---

archive/issue_comments_070949.json:
```json
{
    "body": "Good idea to add this documentation. Everything works fine.",
    "created_at": "2011-08-24T08:08:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8094",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8094#issuecomment-70949",
    "user": "mraum"
}
```

Good idea to add this documentation. Everything works fine.



---

archive/issue_comments_070950.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-08-24T08:08:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8094",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8094#issuecomment-70950",
    "user": "mraum"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_070951.json:
```json
{
    "body": "Maybe on another ticket, but can I ask for one more enhancement on this?  Can we make the following work:\n\n\n```\nmatrix(\"\"\"\n[1 2]\n[3 4]\n\"\"\")\n\n(i.e., any \"]\" or \"[\" next to row delimiters are stripped).  That would mean that I could cut and paste output from Sage back into Sage to make a matrix.",
    "created_at": "2011-08-24T13:11:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8094",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8094#issuecomment-70951",
    "user": "@jasongrout"
}
```

Maybe on another ticket, but can I ask for one more enhancement on this?  Can we make the following work:


```
matrix("""
[1 2]
[3 4]
""")

(i.e., any "]" or "[" next to row delimiters are stripped).  That would mean that I could cut and paste output from Sage back into Sage to make a matrix.



---

archive/issue_comments_070952.json:
```json
{
    "body": "Argh.   Wrong ticket; please ignore my comment!",
    "created_at": "2011-08-24T13:12:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8094",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8094#issuecomment-70952",
    "user": "@jasongrout"
}
```

Argh.   Wrong ticket; please ignore my comment!



---

archive/issue_comments_070953.json:
```json
{
    "body": "Replying to [comment:22 jason]:\n> Argh.   Wrong ticket; please ignore my comment!\n\nWhew!  ;-)",
    "created_at": "2011-08-24T15:09:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8094",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8094#issuecomment-70953",
    "user": "@rbeezer"
}
```

Replying to [comment:22 jason]:
> Argh.   Wrong ticket; please ignore my comment!

Whew!  ;-)



---

archive/issue_comments_070954.json:
```json
{
    "body": "Changing keywords from \"\" to \"sd32\".",
    "created_at": "2011-08-25T18:58:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8094",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8094#issuecomment-70954",
    "user": "@rbeezer"
}
```

Changing keywords from "" to "sd32".



---

archive/issue_comments_070955.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2011-09-12T15:18:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8094",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8094#issuecomment-70955",
    "user": "@nexttime"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_070956.json:
```json
{
    "body": "[attachment:8094-shortcut-matrix-transpose.patch] is not a Mercurial changeset.\n\n```\nabort: no username supplied (see \"hg help config\")\n```\n\nSorry, Harald. ;)",
    "created_at": "2011-09-12T15:18:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8094",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8094#issuecomment-70956",
    "user": "@nexttime"
}
```

[attachment:8094-shortcut-matrix-transpose.patch] is not a Mercurial changeset.

```
abort: no username supplied (see "hg help config")
```

Sorry, Harald. ;)



---

archive/issue_comments_070957.json:
```json
{
    "body": "Attachment [8094-shortcut-matrix-transpose-v2.patch](tarball://root/attachments/some-uuid/ticket8094/8094-shortcut-matrix-transpose-v2.patch) by @rbeezer created at 2011-09-18 04:15:56\n\nI did some maintenance on the main patch, naming it \"v2\".  Has Harald's user info and is now a proper hg patch.  I hope.  \n\nShould now be ready to go, since I did not change any code, so should not need a review.",
    "created_at": "2011-09-18T04:15:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8094",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8094#issuecomment-70957",
    "user": "@rbeezer"
}
```

Attachment [8094-shortcut-matrix-transpose-v2.patch](tarball://root/attachments/some-uuid/ticket8094/8094-shortcut-matrix-transpose-v2.patch) by @rbeezer created at 2011-09-18 04:15:56

I did some maintenance on the main patch, naming it "v2".  Has Harald's user info and is now a proper hg patch.  I hope.  

Should now be ready to go, since I did not change any code, so should not need a review.



---

archive/issue_comments_070958.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2011-09-18T04:15:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8094",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8094#issuecomment-70958",
    "user": "@rbeezer"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_070959.json:
```json
{
    "body": "Replying to [comment:27 rbeezer]:\n> I did some maintenance on the main patch, naming it \"v2\".  Has Harald's user info and is now a proper hg patch.  I hope.\n\nYep, sorry. I would have done it myself but failed to recall Harald's e-mail address that moment; then later was simply too busy to search which ticket it was...\n\n\n\n\n> Should now be ready to go, since I did not change any code, so should not need a review.\n\nThink so. Only meta data (including line numbers) differ.\n\nAs I had other trouble with the release, I think I can still include it.",
    "created_at": "2011-09-18T04:32:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8094",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8094#issuecomment-70959",
    "user": "@nexttime"
}
```

Replying to [comment:27 rbeezer]:
> I did some maintenance on the main patch, naming it "v2".  Has Harald's user info and is now a proper hg patch.  I hope.

Yep, sorry. I would have done it myself but failed to recall Harald's e-mail address that moment; then later was simply too busy to search which ticket it was...




> Should now be ready to go, since I did not change any code, so should not need a review.

Think so. Only meta data (including line numbers) differ.

As I had other trouble with the release, I think I can still include it.



---

archive/issue_comments_070960.json:
```json
{
    "body": "Same patch rebased on (prerelease) Sage 4.7.2.alpha3 because of fuzz 2.",
    "created_at": "2011-09-18T07:01:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8094",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8094#issuecomment-70960",
    "user": "@nexttime"
}
```

Same patch rebased on (prerelease) Sage 4.7.2.alpha3 because of fuzz 2.



---

archive/issue_comments_070961.json:
```json
{
    "body": "Attachment [trac_8094-matrix-properties-more-documentation-rebased_on_4.7.2.alpha3.patch](tarball://root/attachments/some-uuid/ticket8094/trac_8094-matrix-properties-more-documentation-rebased_on_4.7.2.alpha3.patch) by @nexttime created at 2011-09-18 07:01:49\n\nSame patch rebased on (prerelease) Sage 4.7.2.alpha3 because of fuzz 2.",
    "created_at": "2011-09-18T07:01:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8094",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8094#issuecomment-70961",
    "user": "@nexttime"
}
```

Attachment [trac_8094-matrix-properties-more-documentation-rebased_on_4.7.2.alpha3.patch](tarball://root/attachments/some-uuid/ticket8094/trac_8094-matrix-properties-more-documentation-rebased_on_4.7.2.alpha3.patch) by @nexttime created at 2011-09-18 07:01:49

Same patch rebased on (prerelease) Sage 4.7.2.alpha3 because of fuzz 2.



---

archive/issue_comments_070962.json:
```json
{
    "body": "Attached rebased versions of two patches because of fuzz 2.",
    "created_at": "2011-09-18T07:08:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8094",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8094#issuecomment-70962",
    "user": "@nexttime"
}
```

Attached rebased versions of two patches because of fuzz 2.



---

archive/issue_comments_070963.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-09-18T09:37:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8094",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8094#issuecomment-70963",
    "user": "@nexttime"
}
```

Resolution: fixed
