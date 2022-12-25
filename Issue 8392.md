# Issue 8392: Check when defining a permutation by one-line notation (list of int)

archive/issues_008392.json:
```json
{
    "body": "Assignee: nborie\n\nCC:  sage-combinat billey\n\nKeywords: permutation, check, assert\n\nJust check the user give a good entry and for that move a method (robinson_schensted)\n\nFor now, sage accept that:\n\n```\nsage: Permutation([1,1,1,1,1])\n[1, 1, 1, 1, 1]\nsage: Permutation([-12,1,3])\n[-12, 1, 3]\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8392\n\n",
    "created_at": "2010-02-27T21:04:24Z",
    "labels": [
        "component: combinatorics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-5.11",
    "title": "Check when defining a permutation by one-line notation (list of int)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8392",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```
Assignee: nborie

CC:  sage-combinat billey

Keywords: permutation, check, assert

Just check the user give a good entry and for that move a method (robinson_schensted)

For now, sage accept that:

```
sage: Permutation([1,1,1,1,1])
[1, 1, 1, 1, 1]
sage: Permutation([-12,1,3])
[-12, 1, 3]
```


Issue created by migration from https://trac.sagemath.org/ticket/8392





---

archive/issue_comments_075026.json:
```json
{
    "body": "Attachment [trac_8392_check_permutation-nb.patch](tarball://root/attachments/some-uuid/ticket8392/trac_8392_check_permutation-nb.patch) by nborie created at 2010-03-01 00:25:28",
    "created_at": "2010-03-01T00:25:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8392",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8392#issuecomment-75026",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```

Attachment [trac_8392_check_permutation-nb.patch](tarball://root/attachments/some-uuid/ticket8392/trac_8392_check_permutation-nb.patch) by nborie created at 2010-03-01 00:25:28



---

archive/issue_comments_075027.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-03-02T18:20:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8392",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8392#issuecomment-75027",
    "user": "https://github.com/hivert"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_075028.json:
```json
{
    "body": "Hi Nicolas,\n\nIf you want your patch to be reviewed please check \"needs review\"...\n\nFor your information your patch breaks posets which use permutations starting from 0:\n\n```\n    sage: P = Posets.SymmetricGroupBruhatIntervalPoset([0,1,2,3], [2,3,0,1])\nException raised:\n...\n    ValueError: [0, 1, 2, 3] is not a Standard permutations\n```\n",
    "created_at": "2010-03-02T18:20:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8392",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8392#issuecomment-75028",
    "user": "https://github.com/hivert"
}
```

Hi Nicolas,

If you want your patch to be reviewed please check "needs review"...

For your information your patch breaks posets which use permutations starting from 0:

```
    sage: P = Posets.SymmetricGroupBruhatIntervalPoset([0,1,2,3], [2,3,0,1])
Exception raised:
...
    ValueError: [0, 1, 2, 3] is not a Standard permutations
```




---

archive/issue_comments_075029.json:
```json
{
    "body": "This patch is just a begining. I didn't check the 'needs review'. But really for now, I need the advises from any Veteran of combinatorics software.... \n\nSee http://groups.google.com/group/sage-combinat-devel/browse_thread/thread/c6a39caca9df29dc\n\nThanks in advance.",
    "created_at": "2010-03-02T18:35:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8392",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8392#issuecomment-75029",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```

This patch is just a begining. I didn't check the 'needs review'. But really for now, I need the advises from any Veteran of combinatorics software.... 

See http://groups.google.com/group/sage-combinat-devel/browse_thread/thread/c6a39caca9df29dc

Thanks in advance.



---

archive/issue_comments_075030.json:
```json
{
    "body": "The current patch breaks integer vectors; it would need to further fix WeightedIntegerVectors to not abuse anymore Permutation with multiple entries.\n\n\n```\nsage: WeightedIntegerVectors(8, [1,1,2]).list()\n------------------------------------------------------------\nTraceback (most recent call last):\n  File \"<ipython console>\", line 1, in <module>\n  File \"/opt/sage-5.0.rc0/local/lib/python2.7/site-packages/sage/categories/finite_enumerated_sets.py\", line 308, in list\n    self._list = self._list_from_iterator()\n  File \"/opt/sage-5.0.rc0/local/lib/python2.7/site-packages/sage/categories/finite_enumerated_sets.py\", line 142, in _list_from_iterator\n    return [x for x in self]\n  File \"/opt/sage-5.0.rc0/local/lib/python2.7/site-packages/sage/combinat/integer_vector_weighted.py\", line 259, in __iter__\n    yield perm._left_to_right_multiply_on_right(Permutation_class(x))\n  File \"/opt/sage-5.0.rc0/local/lib/python2.7/site-packages/sage/combinat/permutation.py\", line 910, in _left_to_right_multiply_on_right\n    #Pad the permutations if they are of\n  File \"/opt/sage-5.0.rc0/local/lib/python2.7/site-packages/sage/combinat/permutation.py\", line 286, in Permutation\n    if n != len(l) or sorted(l) != range(1,n+1):\nValueError: the list l (=[0, 0, 4]) must contain each integer of {1,...,n} one time\n```\n",
    "created_at": "2012-05-09T14:44:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8392",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8392#issuecomment-75030",
    "user": "https://github.com/nthiery"
}
```

The current patch breaks integer vectors; it would need to further fix WeightedIntegerVectors to not abuse anymore Permutation with multiple entries.


```
sage: WeightedIntegerVectors(8, [1,1,2]).list()
------------------------------------------------------------
Traceback (most recent call last):
  File "<ipython console>", line 1, in <module>
  File "/opt/sage-5.0.rc0/local/lib/python2.7/site-packages/sage/categories/finite_enumerated_sets.py", line 308, in list
    self._list = self._list_from_iterator()
  File "/opt/sage-5.0.rc0/local/lib/python2.7/site-packages/sage/categories/finite_enumerated_sets.py", line 142, in _list_from_iterator
    return [x for x in self]
  File "/opt/sage-5.0.rc0/local/lib/python2.7/site-packages/sage/combinat/integer_vector_weighted.py", line 259, in __iter__
    yield perm._left_to_right_multiply_on_right(Permutation_class(x))
  File "/opt/sage-5.0.rc0/local/lib/python2.7/site-packages/sage/combinat/permutation.py", line 910, in _left_to_right_multiply_on_right
    #Pad the permutations if they are of
  File "/opt/sage-5.0.rc0/local/lib/python2.7/site-packages/sage/combinat/permutation.py", line 286, in Permutation
    if n != len(l) or sorted(l) != range(1,n+1):
ValueError: the list l (=[0, 0, 4]) must contain each integer of {1,...,n} one time
```




---

archive/issue_comments_075031.json:
```json
{
    "body": "Changing assignee from nborie to @tscrim.",
    "created_at": "2012-05-10T02:24:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8392",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8392#issuecomment-75031",
    "user": "https://github.com/tscrim"
}
```

Changing assignee from nborie to @tscrim.



---

archive/issue_comments_075032.json:
```json
{
    "body": "Taking over to work on for Sage Days 38.",
    "created_at": "2012-05-10T02:24:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8392",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8392#issuecomment-75032",
    "user": "https://github.com/tscrim"
}
```

Taking over to work on for Sage Days 38.



---

archive/issue_comments_075033.json:
```json
{
    "body": "Changing keywords from \"permutation, check, assert\" to \"permutation, check, assert, days38\".",
    "created_at": "2012-05-10T02:24:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8392",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8392#issuecomment-75033",
    "user": "https://github.com/tscrim"
}
```

Changing keywords from "permutation, check, assert" to "permutation, check, assert, days38".



---

archive/issue_comments_075034.json:
```json
{
    "body": "I'm going to recycle this ticket due to #13742.",
    "created_at": "2013-02-01T13:32:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8392",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8392#issuecomment-75034",
    "user": "https://github.com/tscrim"
}
```

I'm going to recycle this ticket due to #13742.



---

archive/issue_comments_075035.json:
```json
{
    "body": "Changing keywords from \"permutation, check, assert, days38\" to \"permutation, check, days38\".",
    "created_at": "2013-02-01T13:32:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8392",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8392#issuecomment-75035",
    "user": "https://github.com/tscrim"
}
```

Changing keywords from "permutation, check, assert, days38" to "permutation, check, days38".



---

archive/issue_comments_075036.json:
```json
{
    "body": "For patchbot:\n\nApply: trac_8392-check_permutation-ts.patch",
    "created_at": "2013-02-13T21:30:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8392",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8392#issuecomment-75036",
    "user": "https://github.com/tscrim"
}
```

For patchbot:

Apply: trac_8392-check_permutation-ts.patch



---

archive/issue_comments_075037.json:
```json
{
    "body": "Changing keywords from \"permutation, check, days38\" to \"permutation, check, days38, days45\".",
    "created_at": "2013-02-13T21:30:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8392",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8392#issuecomment-75037",
    "user": "https://github.com/tscrim"
}
```

Changing keywords from "permutation, check, days38" to "permutation, check, days38, days45".



---

archive/issue_comments_075038.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2013-02-13T21:30:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8392",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8392#issuecomment-75038",
    "user": "https://github.com/tscrim"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_075039.json:
```json
{
    "body": "For patchbot:\n\nApply: trac_8392-check_permutation-ts.patch",
    "created_at": "2013-02-15T01:06:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8392",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8392#issuecomment-75039",
    "user": "https://github.com/tscrim"
}
```

For patchbot:

Apply: trac_8392-check_permutation-ts.patch



---

archive/issue_comments_075040.json:
```json
{
    "body": "Fixed doctests and updated documentation.\n\nFor patchbot:\n\nApply: trac_8392-check_permutation-ts.patch",
    "created_at": "2013-02-15T16:11:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8392",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8392#issuecomment-75040",
    "user": "https://github.com/tscrim"
}
```

Fixed doctests and updated documentation.

For patchbot:

Apply: trac_8392-check_permutation-ts.patch



---

archive/issue_comments_075041.json:
```json
{
    "body": "Hi,\n\nThe name of the ticket has nothing to do with what the ticket contains. You must change either one or the other !\n\nYour changes to Word are not valid. Imagine that I am working on the alphabet of tableaux and I want a word of length two (containing two tableaux)...\n\nTwo comments, some others will come later\n* sage/combinat/permutation.py, line 2905 you may change the ugly izip(list(range(1, len(self)+1)), self) with izip(xrange(1,len(self)+1), self)\n* sage/combinat/rsk.py, line 114 \"an method\" -> \"a method\"\n\nVincent",
    "created_at": "2013-02-15T17:04:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8392",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8392#issuecomment-75041",
    "user": "https://github.com/videlec"
}
```

Hi,

The name of the ticket has nothing to do with what the ticket contains. You must change either one or the other !

Your changes to Word are not valid. Imagine that I am working on the alphabet of tableaux and I want a word of length two (containing two tableaux)...

Two comments, some others will come later
* sage/combinat/permutation.py, line 2905 you may change the ugly izip(list(range(1, len(self)+1)), self) with izip(xrange(1,len(self)+1), self)
* sage/combinat/rsk.py, line 114 "an method" -> "a method"

Vincent



---

archive/issue_comments_075042.json:
```json
{
    "body": "I've made the changes. Now to construct a word using RSK, one will use the optional argument `RSK_data`.\n\nFor patchbot:\n\nApply: trac_8392-check_permutation-ts.patch",
    "created_at": "2013-02-16T00:42:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8392",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8392#issuecomment-75042",
    "user": "https://github.com/tscrim"
}
```

I've made the changes. Now to construct a word using RSK, one will use the optional argument `RSK_data`.

For patchbot:

Apply: trac_8392-check_permutation-ts.patch



---

archive/issue_comments_075043.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2013-02-16T00:43:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8392",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8392#issuecomment-75043",
    "user": "https://github.com/tscrim"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_075044.json:
```json
{
    "body": "Vincent has told me that he is okay with the documentation and current implementation but cannot review the math. I'm cc-ing Sara since she was interested in this patch.",
    "created_at": "2013-02-16T04:31:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8392",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8392#issuecomment-75044",
    "user": "https://github.com/tscrim"
}
```

Vincent has told me that he is okay with the documentation and current implementation but cannot review the math. I'm cc-ing Sara since she was interested in this patch.



---

archive/issue_comments_075045.json:
```json
{
    "body": "Rebased on #6495.",
    "created_at": "2013-02-19T15:17:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8392",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8392#issuecomment-75045",
    "user": "https://github.com/tscrim"
}
```

Rebased on #6495.



---

archive/issue_comments_075046.json:
```json
{
    "body": "Minor documentation tweaks which depend on #13605.\n\nFor patchbot:\n\nApply: trac_8392-check_permutation-ts.patch",
    "created_at": "2013-02-22T19:01:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8392",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8392#issuecomment-75046",
    "user": "https://github.com/tscrim"
}
```

Minor documentation tweaks which depend on #13605.

For patchbot:

Apply: trac_8392-check_permutation-ts.patch



---

archive/issue_comments_075047.json:
```json
{
    "body": "Forgot to refresh...\n\nFor patchbot:\n\nApply: trac_8392-check_permutation-ts.patch",
    "created_at": "2013-02-22T19:02:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8392",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8392#issuecomment-75047",
    "user": "https://github.com/tscrim"
}
```

Forgot to refresh...

For patchbot:

Apply: trac_8392-check_permutation-ts.patch



---

archive/issue_comments_075048.json:
```json
{
    "body": "Added Edelman-Greene insertion to the patch as well.\n\nFor patchbot:\n\nApply: trac_8392-check_permutation-ts.patch",
    "created_at": "2013-03-07T17:43:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8392",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8392#issuecomment-75048",
    "user": "https://github.com/tscrim"
}
```

Added Edelman-Greene insertion to the patch as well.

For patchbot:

Apply: trac_8392-check_permutation-ts.patch



---

archive/issue_comments_075049.json:
```json
{
    "body": "Rebased over #8703.",
    "created_at": "2013-04-15T15:47:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8392",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8392#issuecomment-75049",
    "user": "https://github.com/tscrim"
}
```

Rebased over #8703.



---

archive/issue_comments_075050.json:
```json
{
    "body": "Rebased over #14459.",
    "created_at": "2013-05-08T15:38:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8392",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8392#issuecomment-75050",
    "user": "https://github.com/tscrim"
}
```

Rebased over #14459.



---

archive/issue_comments_075051.json:
```json
{
    "body": "Rebased over #14319 due to minor docstring conflicts.",
    "created_at": "2013-05-09T14:33:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8392",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8392#issuecomment-75051",
    "user": "https://github.com/tscrim"
}
```

Rebased over #14319 due to minor docstring conflicts.



---

archive/issue_comments_075052.json:
```json
{
    "body": "For patchbot:\n\nApply trac_8392-check_permutation-ts.patch",
    "created_at": "2013-05-09T14:34:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8392",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8392#issuecomment-75052",
    "user": "https://github.com/tscrim"
}
```

For patchbot:

Apply trac_8392-check_permutation-ts.patch



---

archive/issue_comments_075053.json:
```json
{
    "body": "I'm fussing about corner cases as usual, but I think this here might use some fix:\n\n```\nsage: Permutation([])  # This is be the identity permutation in S_0.\n[]\nsage: Permutation([]).cycle_string()    # OK.\n'()'\nsage: Permutation('()')    # This should give the S_0 identity back -- but it doesn't.\n[1]\nsage: Permutation('')     # Does this maybe? No.\n---------------------------------------------------------------------------\nValueError                                Traceback (most recent call last)\n<ipython-input-29-3df27d9d4d7a> in <module>()\n----> 1 Permutation('')\n\n/home/darij/sage-5.10.beta2/local/lib/python2.7/site-packages/sage/combinat/permutation.pyc in Permutation(l, check_input)\n    430         cycle_list = []\n    431         for c in cycles:\n--> 432             cycle_list.append(map(int, c.split(\",\")))\n    433 \n    434         return from_cycles(max([max(c) for c in cycle_list]), cycle_list)\n\nValueError: invalid literal for int() with base 10: ''\nsage: Permutation(())       # What about this?\n[1]\n```\n\n\nTravis, why did you replace \"standard\" by \"semi-standard\" in ``robinson_schensted``?",
    "created_at": "2013-05-12T04:55:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8392",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8392#issuecomment-75053",
    "user": "https://github.com/darijgr"
}
```

I'm fussing about corner cases as usual, but I think this here might use some fix:

```
sage: Permutation([])  # This is be the identity permutation in S_0.
[]
sage: Permutation([]).cycle_string()    # OK.
'()'
sage: Permutation('()')    # This should give the S_0 identity back -- but it doesn't.
[1]
sage: Permutation('')     # Does this maybe? No.
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-29-3df27d9d4d7a> in <module>()
----> 1 Permutation('')

/home/darij/sage-5.10.beta2/local/lib/python2.7/site-packages/sage/combinat/permutation.pyc in Permutation(l, check_input)
    430         cycle_list = []
    431         for c in cycles:
--> 432             cycle_list.append(map(int, c.split(",")))
    433 
    434         return from_cycles(max([max(c) for c in cycle_list]), cycle_list)

ValueError: invalid literal for int() with base 10: ''
sage: Permutation(())       # What about this?
[1]
```


Travis, why did you replace "standard" by "semi-standard" in ``robinson_schensted``?



---

archive/issue_comments_075054.json:
```json
{
    "body": "apply after trac_8392-check_permutation-ts.patch",
    "created_at": "2013-05-12T06:45:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8392",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8392#issuecomment-75054",
    "user": "https://github.com/darijgr"
}
```

apply after trac_8392-check_permutation-ts.patch



---

archive/issue_comments_075055.json:
```json
{
    "body": "Attachment [trac_8392-review_patch-dg.patch](tarball://root/attachments/some-uuid/ticket8392/trac_8392-review_patch-dg.patch) by @darijgr created at 2013-05-12 06:49:44\n\nI've just reviewed the math: [attachment:trac_8392-review_patch-dg.patch].\n\nDocumentation extended (please check my formatting!), Edelman-Greene insertion fixed (it used to do the same as normal RSK), an is_increasing() method for tableaux added (since we're already doing Edelman-Greene...), and some more doc fixes made (including the changes that were formerly in #14131).\n\nI have not fixed the issues in my previous comment; I don't know our stance on them.",
    "created_at": "2013-05-12T06:49:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8392",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8392#issuecomment-75055",
    "user": "https://github.com/darijgr"
}
```

Attachment [trac_8392-review_patch-dg.patch](tarball://root/attachments/some-uuid/ticket8392/trac_8392-review_patch-dg.patch) by @darijgr created at 2013-05-12 06:49:44

I've just reviewed the math: [attachment:trac_8392-review_patch-dg.patch].

Documentation extended (please check my formatting!), Edelman-Greene insertion fixed (it used to do the same as normal RSK), an is_increasing() method for tableaux added (since we're already doing Edelman-Greene...), and some more doc fixes made (including the changes that were formerly in #14131).

I have not fixed the issues in my previous comment; I don't know our stance on them.



---

archive/issue_comments_075056.json:
```json
{
    "body": "Hey Darij,\n\nI've folded your review patch in and made some additional tweaks to the docs. I can't believe how badly I coded the EG insertion. I reverted it back to standard since when I first wrote this patch, permutations could take inputs with repetition.\n\nAs for your previous comment, that is outside of the scope of this patch since it deals with input for permutations. I think there already is a ticket about this somewhere (or related to it), but I don't remember the number off hand.\n\nBest,\n\nTravis",
    "created_at": "2013-05-14T22:16:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8392",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8392#issuecomment-75056",
    "user": "https://github.com/tscrim"
}
```

Hey Darij,

I've folded your review patch in and made some additional tweaks to the docs. I can't believe how badly I coded the EG insertion. I reverted it back to standard since when I first wrote this patch, permutations could take inputs with repetition.

As for your previous comment, that is outside of the scope of this patch since it deals with input for permutations. I think there already is a ticket about this somewhere (or related to it), but I don't remember the number off hand.

Best,

Travis



---

archive/issue_comments_075057.json:
```json
{
    "body": "I also deprecated the `robinson_schensted()` method for permutations.\n\nFor patchbot:\n\nApply: trac_8392-check_permutation-ts.patch",
    "created_at": "2013-05-14T22:17:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8392",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8392#issuecomment-75057",
    "user": "https://github.com/tscrim"
}
```

I also deprecated the `robinson_schensted()` method for permutations.

For patchbot:

Apply: trac_8392-check_permutation-ts.patch



---

archive/issue_comments_075058.json:
```json
{
    "body": "Travis -\n\nA couple quick comments on the documentation:\n\nIn the docstring for sage.combinat.rsk.RSK:\n\n- In the first paragraph \"as known as two-line...\" should be \"also known as two-line...\" ?\n\n-In your description of the algorithm p and q are first referenced as your insertion and recording tableaux and then they become P and Q in the next paragraph and in this paragraph p appears to be a generalized permutation.\n\nIn the docstring for sage.combinat.rsk.RSK_inverse:\n\n- I think you forgot a colon at the end of the sentence beginning \"Same for Edelman-Greene ...\"\n\nHaven't played with the functions yet (except for your examples), but plan to soon.\n\n-Jeff\n",
    "created_at": "2013-05-18T22:23:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8392",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8392#issuecomment-75058",
    "user": "https://github.com/jeffpferreira"
}
```

Travis -

A couple quick comments on the documentation:

In the docstring for sage.combinat.rsk.RSK:

- In the first paragraph "as known as two-line..." should be "also known as two-line..." ?

-In your description of the algorithm p and q are first referenced as your insertion and recording tableaux and then they become P and Q in the next paragraph and in this paragraph p appears to be a generalized permutation.

In the docstring for sage.combinat.rsk.RSK_inverse:

- I think you forgot a colon at the end of the sentence beginning "Same for Edelman-Greene ..."

Haven't played with the functions yet (except for your examples), but plan to soon.

-Jeff




---

archive/issue_comments_075059.json:
```json
{
    "body": "Hey Jeff,\n\nThanks for catching that. Fixed.\n\nBest,\n\nTravis",
    "created_at": "2013-05-19T01:12:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8392",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8392#issuecomment-75059",
    "user": "https://github.com/tscrim"
}
```

Hey Jeff,

Thanks for catching that. Fixed.

Best,

Travis



---

archive/issue_comments_075060.json:
```json
{
    "body": "Travis,\n\nCan you add some more checks for invalid input? For example there is no problem doing this:\n\n\n```\nsage: RSK([1],[1,2])  # Words are different length\nsage: RSK([2,1],[1,1])  # Not a generalized permutation\n\n```\n\nI am using the definition of generalized permutation in Stanley EC2 Chapter 7.\n\n- Jeff",
    "created_at": "2013-05-22T22:11:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8392",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8392#issuecomment-75060",
    "user": "https://github.com/jeffpferreira"
}
```

Travis,

Can you add some more checks for invalid input? For example there is no problem doing this:


```
sage: RSK([1],[1,2])  # Words are different length
sage: RSK([2,1],[1,1])  # Not a generalized permutation

```

I am using the definition of generalized permutation in Stanley EC2 Chapter 7.

- Jeff



---

archive/issue_comments_075061.json:
```json
{
    "body": "Hey Jeff,\n\nI added the extra safety checks.\n\nBest,\n\nTravis",
    "created_at": "2013-05-24T01:18:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8392",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8392#issuecomment-75061",
    "user": "https://github.com/tscrim"
}
```

Hey Jeff,

I added the extra safety checks.

Best,

Travis



---

archive/issue_comments_075062.json:
```json
{
    "body": "Looks good. It's going to be nice to have these functions around.",
    "created_at": "2013-05-24T19:01:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8392",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8392#issuecomment-75062",
    "user": "https://github.com/jeffpferreira"
}
```

Looks good. It's going to be nice to have these functions around.



---

archive/issue_comments_075063.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-05-24T19:01:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8392",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8392#issuecomment-75063",
    "user": "https://github.com/jeffpferreira"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_075064.json:
```json
{
    "body": "Jeff, thanks for doing the final review. Darij thanks for doing the initial review.",
    "created_at": "2013-05-24T19:08:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8392",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8392#issuecomment-75064",
    "user": "https://github.com/tscrim"
}
```

Jeff, thanks for doing the final review. Darij thanks for doing the initial review.



---

archive/issue_comments_075065.json:
```json
{
    "body": "Rebased to `5.10.beta4` (some fuzz).\n\nFor patchbot:\n\nApply: trac_8392-check_permutation-ts.patch",
    "created_at": "2013-05-25T02:17:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8392",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8392#issuecomment-75065",
    "user": "https://github.com/tscrim"
}
```

Rebased to `5.10.beta4` (some fuzz).

For patchbot:

Apply: trac_8392-check_permutation-ts.patch



---

archive/issue_comments_075066.json:
```json
{
    "body": "\n```\ndochtml.log:[combinat ] /mazur/release/merger/sage-5.10.rc0/local/lib/python2.7/site-packages/sage/combinat/rsk.py:docstring of sage.combinat.rsk.RobinsonSchenstedKnuth:121: WARNING: Duplicate explicit target name: \"knu1970\".\ndochtml.log:[combinat ] /mazur/release/merger/sage-5.10.rc0/local/lib/python2.7/site-packages/sage/combinat/rsk.py:docstring of sage.combinat.rsk.RobinsonSchenstedKnuth:126: WARNING: Duplicate explicit target name: \"eg1987\".\ndochtml.log:[combinat ] /mazur/release/merger/sage-5.10.rc0/local/lib/python2.7/site-packages/sage/combinat/rsk.py:docstring of sage.combinat.rsk.RobinsonSchenstedKnuth:121: WARNING: duplicate citation Knu1970, other instance in /mazur/release/merger/sage-5.10.rc0/devel/sage/doc/en/reference/combinat/sage/combinat/rsk.rst\ndochtml.log:[combinat ] /mazur/release/merger/sage-5.10.rc0/local/lib/python2.7/site-packages/sage/combinat/rsk.py:docstring of sage.combinat.rsk.RobinsonSchenstedKnuth:126: WARNING: duplicate citation EG1987, other instance in /mazur/release/merger/sage-5.10.rc0/devel/sage/doc/en/reference/combinat/sage/combinat/rsk.rst\n```\n",
    "created_at": "2013-05-27T13:43:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8392",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8392#issuecomment-75066",
    "user": "https://github.com/jdemeyer"
}
```


```
dochtml.log:[combinat ] /mazur/release/merger/sage-5.10.rc0/local/lib/python2.7/site-packages/sage/combinat/rsk.py:docstring of sage.combinat.rsk.RobinsonSchenstedKnuth:121: WARNING: Duplicate explicit target name: "knu1970".
dochtml.log:[combinat ] /mazur/release/merger/sage-5.10.rc0/local/lib/python2.7/site-packages/sage/combinat/rsk.py:docstring of sage.combinat.rsk.RobinsonSchenstedKnuth:126: WARNING: Duplicate explicit target name: "eg1987".
dochtml.log:[combinat ] /mazur/release/merger/sage-5.10.rc0/local/lib/python2.7/site-packages/sage/combinat/rsk.py:docstring of sage.combinat.rsk.RobinsonSchenstedKnuth:121: WARNING: duplicate citation Knu1970, other instance in /mazur/release/merger/sage-5.10.rc0/devel/sage/doc/en/reference/combinat/sage/combinat/rsk.rst
dochtml.log:[combinat ] /mazur/release/merger/sage-5.10.rc0/local/lib/python2.7/site-packages/sage/combinat/rsk.py:docstring of sage.combinat.rsk.RobinsonSchenstedKnuth:126: WARNING: duplicate citation EG1987, other instance in /mazur/release/merger/sage-5.10.rc0/devel/sage/doc/en/reference/combinat/sage/combinat/rsk.rst
```




---

archive/issue_comments_075067.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2013-05-27T13:43:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8392",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8392#issuecomment-75067",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_075068.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2013-05-27T20:23:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8392",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8392#issuecomment-75068",
    "user": "https://github.com/tscrim"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_075069.json:
```json
{
    "body": "Fixed. Errors were due to references being in a function that had an alias.",
    "created_at": "2013-05-27T20:23:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8392",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8392#issuecomment-75069",
    "user": "https://github.com/tscrim"
}
```

Fixed. Errors were due to references being in a function that had an alias.



---

archive/issue_comments_075070.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2013-05-28T12:58:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8392",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8392#issuecomment-75070",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_075071.json:
```json
{
    "body": "This needs to be rebased such that it applies on top of #14302.",
    "created_at": "2013-05-28T12:58:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8392",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8392#issuecomment-75071",
    "user": "https://github.com/jdemeyer"
}
```

This needs to be rebased such that it applies on top of #14302.



---

archive/issue_comments_075072.json:
```json
{
    "body": "Rebased",
    "created_at": "2013-05-28T14:49:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8392",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8392#issuecomment-75072",
    "user": "https://github.com/tscrim"
}
```

Rebased



---

archive/issue_comments_075073.json:
```json
{
    "body": "Attachment [trac_8392-check_permutation-ts.patch](tarball://root/attachments/some-uuid/ticket8392/trac_8392-check_permutation-ts.patch) by @tscrim created at 2013-05-28 14:49:30\n\nRebased over #14302.",
    "created_at": "2013-05-28T14:49:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8392",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8392#issuecomment-75073",
    "user": "https://github.com/tscrim"
}
```

Attachment [trac_8392-check_permutation-ts.patch](tarball://root/attachments/some-uuid/ticket8392/trac_8392-check_permutation-ts.patch) by @tscrim created at 2013-05-28 14:49:30

Rebased over #14302.



---

archive/issue_comments_075074.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2013-05-28T14:49:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8392",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8392#issuecomment-75074",
    "user": "https://github.com/tscrim"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_075075.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2013-06-06T12:31:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8392",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8392#issuecomment-75075",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed



---

archive/issue_comments_075076.json:
```json
{
    "body": "Thanks for writing this patch. I support the proposed clean up of the code, but I want to raise an objection to choices in the user interface:\n\n- I don't think that it is useful to deprecate the method `robinson_schensted`:\n\n  {{{\n  DeprecationWarning: p.robinson_schensted() is deprecated. Use instead RSK(p)\n  }}}\n\n  Telling users to use the RSK function instead of a method is not in the spirit of object-oriented programming. More importantly, it is totally unnecessary to deprecate the method.\n\n- Also, I disagree with importing `RSK, RSK_inverse, RobinsonSchenstedKnuth, RobinsonSchenstedKnuth_inverse` into the global namespace when one object could easily handle all of these.\n\n- Perhaps these names should not be capitalized since they are python functions and not classes. See the [developers guide](http://www.sagemath.org/doc/developer/conventions.html?highlight=camelcase#python-coding-conventions).",
    "created_at": "2013-08-17T17:31:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8392",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8392#issuecomment-75076",
    "user": "https://github.com/saliola"
}
```

Thanks for writing this patch. I support the proposed clean up of the code, but I want to raise an objection to choices in the user interface:

- I don't think that it is useful to deprecate the method `robinson_schensted`:

  {{{
  DeprecationWarning: p.robinson_schensted() is deprecated. Use instead RSK(p)
  }}}

  Telling users to use the RSK function instead of a method is not in the spirit of object-oriented programming. More importantly, it is totally unnecessary to deprecate the method.

- Also, I disagree with importing `RSK, RSK_inverse, RobinsonSchenstedKnuth, RobinsonSchenstedKnuth_inverse` into the global namespace when one object could easily handle all of these.

- Perhaps these names should not be capitalized since they are python functions and not classes. See the [developers guide](http://www.sagemath.org/doc/developer/conventions.html?highlight=camelcase#python-coding-conventions).



---

archive/issue_comments_075077.json:
```json
{
    "body": "I agree with Franco's comments!\n\nAnne",
    "created_at": "2013-08-17T17:35:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8392",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8392#issuecomment-75077",
    "user": "https://github.com/anneschilling"
}
```

I agree with Franco's comments!

Anne



---

archive/issue_comments_075078.json:
```json
{
    "body": "- The ability of doing RSK and EG is a great feature, but the documentation isn't very clear. What is `[3,3,2]` mean with EG insertion? Since it isn't a reduced word, how should this be interpreted? It's not invertible either:\n\n```\nsage: P, Q = RSK([3,3,2], insertion='EG')\nsage: P\n[[2, 3], [3]]\nsage: Q\n[[1, 2], [3]]\nsage: RSK_inverse(P, Q, insertion='EG')\nword: 232\n```\n\n\n- I would have expected that the output of `RSK` could be used as input to `RSK_inverse`:\n\n```\nsage: RSK_inverse(RSK([1,2]))\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n<ipython-input-154-cb6c9a6f810d> in <module>()\n----> 1 RSK_inverse(RSK([Integer(1),Integer(2)]))\n\nTypeError: RSK_inverse() takes at least 2 arguments (1 given)\n```\n",
    "created_at": "2013-08-17T18:03:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8392",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8392#issuecomment-75078",
    "user": "https://github.com/saliola"
}
```

- The ability of doing RSK and EG is a great feature, but the documentation isn't very clear. What is `[3,3,2]` mean with EG insertion? Since it isn't a reduced word, how should this be interpreted? It's not invertible either:

```
sage: P, Q = RSK([3,3,2], insertion='EG')
sage: P
[[2, 3], [3]]
sage: Q
[[1, 2], [3]]
sage: RSK_inverse(P, Q, insertion='EG')
word: 232
```


- I would have expected that the output of `RSK` could be used as input to `RSK_inverse`:

```
sage: RSK_inverse(RSK([1,2]))
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-154-cb6c9a6f810d> in <module>()
----> 1 RSK_inverse(RSK([Integer(1),Integer(2)]))

TypeError: RSK_inverse() takes at least 2 arguments (1 given)
```




---

archive/issue_comments_075079.json:
```json
{
    "body": "Hey Franco,\n\nReplying to [comment:38 saliola]:\n> Thanks for writing this patch. I support the proposed clean up of the code, but I want to raise an objection to choices in the user interface:\n> \n> - I don't think that it is useful to deprecate the method `robinson_schensted`:\n> \n>   {{{\n>   DeprecationWarning: p.robinson_schensted() is deprecated. Use instead RSK(p)\n>   }}}\n> \n>   Telling users to use the RSK function instead of a method is not in the spirit of object-oriented programming. More importantly, it is totally unnecessary to deprecate the method.\n\nIf we wanted to be fully OOP, then there needs to be a class of something like `RSKUsable` which has an abstract method `RSK()` where each type of object implements it's own version of RSK and `RSKUsable` would implement the row-insertion procedure. The problem with this is that we want to be able to handle (pairs of) lists, which we can't modify its class structure and I don't want to have to wrap a list as a word, and I also don't want to clutter up the MRO. Another reason why this is better as a function is most of the operation is independent of the type of object being passed in; all it does is it converts it into a pair of lists of the same size. Thus it provides a uniform interface for objects, and the fact that only permutations has such a method conflicts with this, so I think it is worthwhile to deprecate this.\n\n> - Also, I disagree with importing `RSK, RSK_inverse, RobinsonSchenstedKnuth, RobinsonSchenstedKnuth_inverse` into the global namespace when one object could easily handle all of these.\n\nThen what is your proposed interface? If the input is a pair of tableaux as a list or is given as input 2 tableaux, then run the inverse? Hence we should combine two functions which do completely different behavior into one as I think of RSK as a procedure in 1 direction? What about if someone only thinks of this as the Robinson-Schensted bijection and tries `RobinsonSchestead<tab>`? This is why I setup these aliases and imported them.\n\n> - Perhaps these names should not be capitalized since they are python functions and not classes. See the [developers guide](http://www.sagemath.org/doc/developer/conventions.html?highlight=camelcase#python-coding-conventions).\n\nFor the full name, probably yes it should be changed. For the shortname `RSK`, it is an acronym, so I think it is better and more likely to be found than `rsk`. See the bottom of [this section of the developers guide](http://www.sagemath.org/doc/developer/conventions.html?highlight=camelcase#python-coding-conventions).\n\n> The ability of doing RSK and EG is a great feature, but the documentation isn't very clear. What is [3,3,2] mean with EG insertion? Since it isn't a reduced word, how should this be interpreted?\n\nThe documentation could use some expansion.\n\n> I would have expected that the output of RSK could be used as input to RSK_inverse:\n\nThis is because it's more logical to me for the input to be 2 arguments where we can explicitly specify what they are (as arguments), than a single parameter taking a list and checking to make sure it has length 2 and explaining the (non-standard IMO) input form in the docsting. We could handle both forms of input, but this seems overly complicated, and I imagine python programmers would simply use the `*` to expand the list as inputs as in the EG examples. This could probably use another example (maybe so far as a docstring explanation, but I'm hesitant about that) that's not for EG insertion.\n\nBest,\n\nTravis",
    "created_at": "2013-08-18T16:02:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8392",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8392#issuecomment-75079",
    "user": "https://github.com/tscrim"
}
```

Hey Franco,

Replying to [comment:38 saliola]:
> Thanks for writing this patch. I support the proposed clean up of the code, but I want to raise an objection to choices in the user interface:
> 
> - I don't think that it is useful to deprecate the method `robinson_schensted`:
> 
>   {{{
>   DeprecationWarning: p.robinson_schensted() is deprecated. Use instead RSK(p)
>   }}}
> 
>   Telling users to use the RSK function instead of a method is not in the spirit of object-oriented programming. More importantly, it is totally unnecessary to deprecate the method.

If we wanted to be fully OOP, then there needs to be a class of something like `RSKUsable` which has an abstract method `RSK()` where each type of object implements it's own version of RSK and `RSKUsable` would implement the row-insertion procedure. The problem with this is that we want to be able to handle (pairs of) lists, which we can't modify its class structure and I don't want to have to wrap a list as a word, and I also don't want to clutter up the MRO. Another reason why this is better as a function is most of the operation is independent of the type of object being passed in; all it does is it converts it into a pair of lists of the same size. Thus it provides a uniform interface for objects, and the fact that only permutations has such a method conflicts with this, so I think it is worthwhile to deprecate this.

> - Also, I disagree with importing `RSK, RSK_inverse, RobinsonSchenstedKnuth, RobinsonSchenstedKnuth_inverse` into the global namespace when one object could easily handle all of these.

Then what is your proposed interface? If the input is a pair of tableaux as a list or is given as input 2 tableaux, then run the inverse? Hence we should combine two functions which do completely different behavior into one as I think of RSK as a procedure in 1 direction? What about if someone only thinks of this as the Robinson-Schensted bijection and tries `RobinsonSchestead<tab>`? This is why I setup these aliases and imported them.

> - Perhaps these names should not be capitalized since they are python functions and not classes. See the [developers guide](http://www.sagemath.org/doc/developer/conventions.html?highlight=camelcase#python-coding-conventions).

For the full name, probably yes it should be changed. For the shortname `RSK`, it is an acronym, so I think it is better and more likely to be found than `rsk`. See the bottom of [this section of the developers guide](http://www.sagemath.org/doc/developer/conventions.html?highlight=camelcase#python-coding-conventions).

> The ability of doing RSK and EG is a great feature, but the documentation isn't very clear. What is [3,3,2] mean with EG insertion? Since it isn't a reduced word, how should this be interpreted?

The documentation could use some expansion.

> I would have expected that the output of RSK could be used as input to RSK_inverse:

This is because it's more logical to me for the input to be 2 arguments where we can explicitly specify what they are (as arguments), than a single parameter taking a list and checking to make sure it has length 2 and explaining the (non-standard IMO) input form in the docsting. We could handle both forms of input, but this seems overly complicated, and I imagine python programmers would simply use the `*` to expand the list as inputs as in the EG examples. This could probably use another example (maybe so far as a docstring explanation, but I'm hesitant about that) that's not for EG insertion.

Best,

Travis



---

archive/issue_comments_075080.json:
```json
{
    "body": "Hi Travis,\n\nReplying to [comment:41 tscrim]:\n> If we wanted to be fully OOP, then there needs to be a class of something like `RSKUsable` which has an abstract method `RSK()` where each type of object implements it's own version of RSK and `RSKUsable` would implement the row-insertion procedure. The problem with this is that we want to be able to handle (pairs of) lists, which we can't modify its class structure and I don't want to have to wrap a list as a word, and I also don't want to clutter up the MRO. Another reason why this is better as a function is most of the operation is independent of the type of object being passed in; all it does is it converts it into a pair of lists of the same size. Thus it provides a uniform interface for objects, and the fact that only permutations has such a method conflicts with this, so I think it is worthwhile to deprecate this.\n\nIf a user makes a permutation p, it would be natural to try p.<tab completion> to see all methods. Currently p.robinson_schensted() works and it is the most natural entry point. There is no reason to deprecate this method, it can just be a one-line function returning RSK(p).\n\n> > - Also, I disagree with importing `RSK, RSK_inverse, RobinsonSchenstedKnuth, RobinsonSchenstedKnuth_inverse` into the global namespace when one object could easily handle all of these.\n> \n> Then what is your proposed interface? \n\nCouldn't you just use options for the inverse?\n\n> > The ability of doing RSK and EG is a great feature, but the documentation isn't very clear. What is [3,3,2] mean with EG insertion? Since it isn't a reduced word, how should this be interpreted?\n> \n> The documentation could use some expansion.\n\nRight now it is not clear at all that the input to the Edelman-Greene correspondence are reduced words. Also, if you want to put all insertion algorithms in one method, it might be better to call it insertion_algorithms rather than RSK since RSK is just one of them and I as a user would not think that Edelman-Greene would be under RSK. Or you should have Edelman-Greene as a different method. Plus the documentation definitely needs more details! At least you need to explain what the input is with the various options.\n\nBest,\n\nAnne",
    "created_at": "2013-08-19T06:55:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8392",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8392#issuecomment-75080",
    "user": "https://github.com/anneschilling"
}
```

Hi Travis,

Replying to [comment:41 tscrim]:
> If we wanted to be fully OOP, then there needs to be a class of something like `RSKUsable` which has an abstract method `RSK()` where each type of object implements it's own version of RSK and `RSKUsable` would implement the row-insertion procedure. The problem with this is that we want to be able to handle (pairs of) lists, which we can't modify its class structure and I don't want to have to wrap a list as a word, and I also don't want to clutter up the MRO. Another reason why this is better as a function is most of the operation is independent of the type of object being passed in; all it does is it converts it into a pair of lists of the same size. Thus it provides a uniform interface for objects, and the fact that only permutations has such a method conflicts with this, so I think it is worthwhile to deprecate this.

If a user makes a permutation p, it would be natural to try p.<tab completion> to see all methods. Currently p.robinson_schensted() works and it is the most natural entry point. There is no reason to deprecate this method, it can just be a one-line function returning RSK(p).

> > - Also, I disagree with importing `RSK, RSK_inverse, RobinsonSchenstedKnuth, RobinsonSchenstedKnuth_inverse` into the global namespace when one object could easily handle all of these.
> 
> Then what is your proposed interface? 

Couldn't you just use options for the inverse?

> > The ability of doing RSK and EG is a great feature, but the documentation isn't very clear. What is [3,3,2] mean with EG insertion? Since it isn't a reduced word, how should this be interpreted?
> 
> The documentation could use some expansion.

Right now it is not clear at all that the input to the Edelman-Greene correspondence are reduced words. Also, if you want to put all insertion algorithms in one method, it might be better to call it insertion_algorithms rather than RSK since RSK is just one of them and I as a user would not think that Edelman-Greene would be under RSK. Or you should have Edelman-Greene as a different method. Plus the documentation definitely needs more details! At least you need to explain what the input is with the various options.

Best,

Anne
