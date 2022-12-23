# Issue 3897: bug in local_information due to the lack of residue_field for ZZ

archive/issues_003897.json:
```json
{
    "body": "Assignee: was\n\nCC:  alexghitza\n\n\n```\nE = EllipticCurve([1,1])\nE.local_information(3)\n```\n\n\nyields\n\n\n```\n---------------------------------------------------------------------------\nAttributeError                            Traceback (most recent call last)\n\n/local/pmzcw/prog/sage-3.1.1/<ipython console> in <module>()\n\n/hades/staff/pmzcw/prog/sage/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_number_field.py in local_information(self, P, proof)\n    375         if isinstance(P, RingElement):\n    376             P = self.base_ring().ideal(P)\n--> 377         return self.integral_model()[0]._tate(P, proof)\n    378\n    379     def local_minimal_model(self, P, proof = None):\n\n/hades/staff/pmzcw/prog/sage/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_number_field.py in _tate(self, P, proof)\n    517         OK = K.maximal_order()\n    518         t = verbose(\"Running Tate's algorithm with P = %s\"%P, level=1)\n--> 519         F = OK.residue_field(P)\n    520         p = F.characteristic()\n    521         if P.is_principal():\n\nAttributeError: 'sage.rings.integer_ring.IntegerRing_class' object has no attribute 'residue_field'\n```\n\n\nThe problem is that ZZ has no object residue_field, while number rings have. Either one should add this function or write local_information separately for curves over QQ.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3897\n\n",
    "created_at": "2008-08-19T15:19:07Z",
    "labels": [
        "number theory",
        "minor",
        "bug"
    ],
    "title": "bug in local_information due to the lack of residue_field for ZZ",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3897",
    "user": "wuthrich"
}
```
Assignee: was

CC:  alexghitza


```
E = EllipticCurve([1,1])
E.local_information(3)
```


yields


```
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)

/local/pmzcw/prog/sage-3.1.1/<ipython console> in <module>()

/hades/staff/pmzcw/prog/sage/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_number_field.py in local_information(self, P, proof)
    375         if isinstance(P, RingElement):
    376             P = self.base_ring().ideal(P)
--> 377         return self.integral_model()[0]._tate(P, proof)
    378
    379     def local_minimal_model(self, P, proof = None):

/hades/staff/pmzcw/prog/sage/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_number_field.py in _tate(self, P, proof)
    517         OK = K.maximal_order()
    518         t = verbose("Running Tate's algorithm with P = %s"%P, level=1)
--> 519         F = OK.residue_field(P)
    520         p = F.characteristic()
    521         if P.is_principal():

AttributeError: 'sage.rings.integer_ring.IntegerRing_class' object has no attribute 'residue_field'
```


The problem is that ZZ has no object residue_field, while number rings have. Either one should add this function or write local_information separately for curves over QQ.

Issue created by migration from https://trac.sagemath.org/ticket/3897





---

archive/issue_comments_027860.json:
```json
{
    "body": "I am fixing this now....",
    "created_at": "2008-09-09T17:41:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3897",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3897#issuecomment-27860",
    "user": "cremona"
}
```

I am fixing this now....



---

archive/issue_comments_027861.json:
```json
{
    "body": "Attachment\n\nOK, so the patch 3897-residue-fields-ZZ.patch implements residue fields for ZZ.  ALong the way there were quite a few smallish fixes needed in related things, and while I was immersed in number_field.py etc I added a whole lot of docstrings and doctests there.\n\nThis applies to 3.1.2.rc1 AFTER the patches for #1951 which are related (they also relate to residue fields).\n\nAfter this has been accepted (after revision if necessary, of course!)  then we can start to work on the original problem: I know that local_information() still does not work for curves defined over Q.  \n\nChris:  I have started going through all the functions for elliptic curve over Q vs. curves over number fields, to make everything as consistent as possible.  These residue field extensions will help.",
    "created_at": "2008-09-10T16:39:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3897",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3897#issuecomment-27861",
    "user": "cremona"
}
```

Attachment

OK, so the patch 3897-residue-fields-ZZ.patch implements residue fields for ZZ.  ALong the way there were quite a few smallish fixes needed in related things, and while I was immersed in number_field.py etc I added a whole lot of docstrings and doctests there.

This applies to 3.1.2.rc1 AFTER the patches for #1951 which are related (they also relate to residue fields).

After this has been accepted (after revision if necessary, of course!)  then we can start to work on the original problem: I know that local_information() still does not work for curves defined over Q.  

Chris:  I have started going through all the functions for elliptic curve over Q vs. curves over number fields, to make everything as consistent as possible.  These residue field extensions will help.



---

archive/issue_comments_027862.json:
```json
{
    "body": "apply after 3897-residue-fields-ZZ.patch",
    "created_at": "2008-09-21T00:22:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3897",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3897#issuecomment-27862",
    "user": "AlexGhitza"
}
```

apply after 3897-residue-fields-ZZ.patch



---

archive/issue_comments_027863.json:
```json
{
    "body": "Attachment\n\nLooks good.  There were a few typos which are fixed in 3897-minor.patch.",
    "created_at": "2008-09-21T00:23:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3897",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3897#issuecomment-27863",
    "user": "AlexGhitza"
}
```

Attachment

Looks good.  There were a few typos which are fixed in 3897-minor.patch.



---

archive/issue_comments_027864.json:
```json
{
    "body": "Oops!  I take that back.  I noticed that there is no doctest checking if the reported bug was fixed, and running that example still does not work (although in a new way).  I'll see if I can track down what's happening.",
    "created_at": "2008-09-21T00:27:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3897",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3897#issuecomment-27864",
    "user": "AlexGhitza"
}
```

Oops!  I take that back.  I noticed that there is no doctest checking if the reported bug was fixed, and running that example still does not work (although in a new way).  I'll see if I can track down what's happening.



---

archive/issue_comments_027865.json:
```json
{
    "body": "Replying to [comment:6 AlexGhitza]:\n> Oops!  I take that back.  I noticed that there is no doctest checking if the reported bug was fixed, and running that example still does not work (although in a new way).  I'll see if I can track down what's happening.\n\nAlex: this patch is intended only to fix the residue field for ZZ issue;  now I have done that I am still working on getting local information to work properly.  So this is really two tickets.\n\nCould we merge and close this one and open a new one for the local info problem?  Or put the ZZ residue fields into a new patch which can be closed right away, with a cross-reference from this one?",
    "created_at": "2008-09-21T10:41:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3897",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3897#issuecomment-27865",
    "user": "cremona"
}
```

Replying to [comment:6 AlexGhitza]:
> Oops!  I take that back.  I noticed that there is no doctest checking if the reported bug was fixed, and running that example still does not work (although in a new way).  I'll see if I can track down what's happening.

Alex: this patch is intended only to fix the residue field for ZZ issue;  now I have done that I am still working on getting local information to work properly.  So this is really two tickets.

Could we merge and close this one and open a new one for the local info problem?  Or put the ZZ residue fields into a new patch which can be closed right away, with a cross-reference from this one?



---

archive/issue_comments_027866.json:
```json
{
    "body": "OK, despite my previous remark I have finished and the 3rd patch (to be applied after previous) sorts out the original issue.   More than that:\n* function _tidy_model() was wrong and has been fixed\n* New file ell_local_data.py defines a new class EllipticCurveLocalData which does the work; code moved to here from ell_number_field (especially the _tate() function implementing Tate's algorithm)\n* A few functions added to integer.pyx and rational.pyx so as to allow common code for QQ and other number fields.\n* Now all functions in ell_number_field.py work on curves defined over QQ in a consistent way.\n* Over QQ, new algorithm option \"generic\" in conductor() uses the generic number field code (slower, but shows consistency).",
    "created_at": "2008-09-22T18:00:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3897",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3897#issuecomment-27866",
    "user": "cremona"
}
```

OK, despite my previous remark I have finished and the 3rd patch (to be applied after previous) sorts out the original issue.   More than that:
* function _tidy_model() was wrong and has been fixed
* New file ell_local_data.py defines a new class EllipticCurveLocalData which does the work; code moved to here from ell_number_field (especially the _tate() function implementing Tate's algorithm)
* A few functions added to integer.pyx and rational.pyx so as to allow common code for QQ and other number fields.
* Now all functions in ell_number_field.py work on curves defined over QQ in a consistent way.
* Over QQ, new algorithm option "generic" in conductor() uses the generic number field code (slower, but shows consistency).



---

archive/issue_comments_027867.json:
```json
{
    "body": "John,\n\nThis is good stuff.  Unfortunately, your patch does not contain your new file ell_local_data.py.  I think you probably forgot to add it to the hg repository before exporting your patch.  You should go to devel/sage/sage and do \"hg add schemes/elliptic_curves/ell_local_data.py\", then refresh your patch 3897-local_data.patch and re-upload it to trac.",
    "created_at": "2008-09-23T06:58:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3897",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3897#issuecomment-27867",
    "user": "AlexGhitza"
}
```

John,

This is good stuff.  Unfortunately, your patch does not contain your new file ell_local_data.py.  I think you probably forgot to add it to the hg repository before exporting your patch.  You should go to devel/sage/sage and do "hg add schemes/elliptic_curves/ell_local_data.py", then refresh your patch 3897-local_data.patch and re-upload it to trac.



---

archive/issue_comments_027868.json:
```json
{
    "body": "Attachment\n\nOK, I've done that.  I'm still getting used to the \"hg q\" way of doing things, which doesn't have a commit stage -- so while I think the patch is correctly identified as due to me, there is not (I think) the usual one-line description.\n\nEnjoy.",
    "created_at": "2008-09-23T08:02:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3897",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3897#issuecomment-27868",
    "user": "cremona"
}
```

Attachment

OK, I've done that.  I'm still getting used to the "hg q" way of doing things, which doesn't have a commit stage -- so while I think the patch is correctly identified as due to me, there is not (I think) the usual one-line description.

Enjoy.



---

archive/issue_comments_027869.json:
```json
{
    "body": "Positive review.  I added another small patch deprecating local_information (since John's last patch renames it to local_data without any comment).  Apply all the patches in sequence.\n\n\nFor the record: at the moment, writing any function that deals with number fields involves one of the following unpleasant steps 1) write special code to deal with QQ or 2) add functionality to QQ so that it pretends to be a number field.  This leads to code duplication and obfuscation.  Also, whenever a bug is fixed or a feature is added to number fields, one has to remember to do the same with QQ.  Very sad!\n\nLooking at this situation, it feels very much like QQ should inherit from rings.number_field.NumberField_absolute rather than the current rings.number_field_base.NumberField.  This appears to be difficult to do because of circular imports; I've been thinking about the issue and hope to come up with at least some solution that will allow us to truly treat number fields and QQ on an equal footing.",
    "created_at": "2008-09-23T08:56:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3897",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3897#issuecomment-27869",
    "user": "AlexGhitza"
}
```

Positive review.  I added another small patch deprecating local_information (since John's last patch renames it to local_data without any comment).  Apply all the patches in sequence.


For the record: at the moment, writing any function that deals with number fields involves one of the following unpleasant steps 1) write special code to deal with QQ or 2) add functionality to QQ so that it pretends to be a number field.  This leads to code duplication and obfuscation.  Also, whenever a bug is fixed or a feature is added to number fields, one has to remember to do the same with QQ.  Very sad!

Looking at this situation, it feels very much like QQ should inherit from rings.number_field.NumberField_absolute rather than the current rings.number_field_base.NumberField.  This appears to be difficult to do because of circular imports; I've been thinking about the issue and hope to come up with at least some solution that will allow us to truly treat number fields and QQ on an equal footing.



---

archive/issue_comments_027870.json:
```json
{
    "body": "Alex,\n\nthe deprecated routine should still call the new function, i.e. a warning is issues, but the code still works.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-23T09:48:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3897",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3897#issuecomment-27870",
    "user": "mabshoff"
}
```

Alex,

the deprecated routine should still call the new function, i.e. a warning is issues, but the code still works.

Cheers,

Michael



---

archive/issue_comments_027871.json:
```json
{
    "body": "Attachment\n\nReplying to [comment:12 mabshoff]:\n> Alex,\n> \n> the deprecated routine should still call the new function, i.e. a warning is issues, but the code still works.\n> \n> Cheers,\n> \n> Michael\n\nI added a line to do that.  Trac would not let me replace Alex's, but it is a replacement.",
    "created_at": "2008-09-23T09:58:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3897",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3897#issuecomment-27871",
    "user": "cremona"
}
```

Attachment

Replying to [comment:12 mabshoff]:
> Alex,
> 
> the deprecated routine should still call the new function, i.e. a warning is issues, but the code still works.
> 
> Cheers,
> 
> Michael

I added a line to do that.  Trac would not let me replace Alex's, but it is a replacement.



---

archive/issue_comments_027872.json:
```json
{
    "body": "Merged all four patches in Sage 3.1.3.alpha1",
    "created_at": "2008-09-23T10:24:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3897",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3897#issuecomment-27872",
    "user": "mabshoff"
}
```

Merged all four patches in Sage 3.1.3.alpha1



---

archive/issue_comments_027873.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-23T10:24:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3897",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3897#issuecomment-27873",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_027874.json:
```json
{
    "body": "\"Looking at this situation, it feels very much like QQ should inherit from rings.number_field.NumberField?_absolute rather than the current rings.number_field_base.NumberField?. This appears to be difficult to do because of circular imports; I've been thinking about the issue and hope to come up with at least some solution that will allow us to truly treat number fields and QQ on an equal footing. \"\n\nThe original intention was that any functionality that could be implemented\nin a way that is common to both NumberField_absolute and QQ, should\nbe implemented in rings.number_field.NumberField.  Maybe you should just\nmove *all* such functionality up there?  If it can't be implemented there,\nhow will it make sense for QQ?\n\nAt least that was how the thinking went a year ago in the original implementation.\nThis may have turned out to be completely wrong.  Keep at it until you find\nthe right solution.",
    "created_at": "2008-09-23T15:42:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3897",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3897#issuecomment-27874",
    "user": "was"
}
```

"Looking at this situation, it feels very much like QQ should inherit from rings.number_field.NumberField?_absolute rather than the current rings.number_field_base.NumberField?. This appears to be difficult to do because of circular imports; I've been thinking about the issue and hope to come up with at least some solution that will allow us to truly treat number fields and QQ on an equal footing. "

The original intention was that any functionality that could be implemented
in a way that is common to both NumberField_absolute and QQ, should
be implemented in rings.number_field.NumberField.  Maybe you should just
move *all* such functionality up there?  If it can't be implemented there,
how will it make sense for QQ?

At least that was how the thinking went a year ago in the original implementation.
This may have turned out to be completely wrong.  Keep at it until you find
the right solution.



---

archive/issue_comments_027875.json:
```json
{
    "body": "I think William is probably right, but still I'm glad that these patches have been merged before we tried to solve everything!  The one I did implementing residue fields for ZZ was rather similar.  But that's now done!",
    "created_at": "2008-09-23T16:01:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3897",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3897#issuecomment-27875",
    "user": "cremona"
}
```

I think William is probably right, but still I'm glad that these patches have been merged before we tried to solve everything!  The one I did implementing residue fields for ZZ was rather similar.  But that's now done!



---

archive/issue_comments_027876.json:
```json
{
    "body": "William,\n\nI'm glad you commented on this.  That's exactly the path I had chosen to follow (after discussing it with Craig), so it's good to have confirmation from someone involved in the original design decision.",
    "created_at": "2008-09-23T22:37:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3897",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3897#issuecomment-27876",
    "user": "AlexGhitza"
}
```

William,

I'm glad you commented on this.  That's exactly the path I had chosen to follow (after discussing it with Craig), so it's good to have confirmation from someone involved in the original design decision.
