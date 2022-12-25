# Issue 7197: basic statistics functions

archive/issues_007197.json:
```json
{
    "body": "Assignee: mhampton\n\nKeywords: statistics, mean, median, mode, standard deviation\n\nBasic statistics functions for a new class in Sage. Only descriptive statistics right now.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7197\n\n",
    "created_at": "2009-10-12T23:26:09Z",
    "labels": [
        "component: statistics",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "basic statistics functions",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7197",
    "user": "https://trac.sagemath.org/admin/accounts/users/amhou"
}
```
Assignee: mhampton

Keywords: statistics, mean, median, mode, standard deviation

Basic statistics functions for a new class in Sage. Only descriptive statistics right now.

Issue created by migration from https://trac.sagemath.org/ticket/7197





---

archive/issue_comments_059581.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-10-14T02:52:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7197",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7197#issuecomment-59581",
    "user": "https://trac.sagemath.org/admin/accounts/users/amhou"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_059582.json:
```json
{
    "body": "Some comments:\n\n1. The arguments for std and variance don't seem very user-friendly.  I think it would be much better to have \"sample=True/False\" or \"population=True/False\", or maybe something more general like numpy: \"ddof=<number>\" (delta degrees of freedom), where the denominator is n-ddof (so ddof=1 is sample, ddof=0 is population).\n\n2. When calling the std or variance methods of the object, the population vs. sample distinction is ignored.\n\n2. Why are these methods in a class?  They don't seem to use any benefits of a class; they just seem to be standalone functions.  It seems like it would make much more sense to me to have these methods be just functions inside of the module.  We can still import them into a namespace called \"stats\".",
    "created_at": "2009-10-14T21:33:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7197",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7197#issuecomment-59582",
    "user": "https://github.com/jasongrout"
}
```

Some comments:

1. The arguments for std and variance don't seem very user-friendly.  I think it would be much better to have "sample=True/False" or "population=True/False", or maybe something more general like numpy: "ddof=<number>" (delta degrees of freedom), where the denominator is n-ddof (so ddof=1 is sample, ddof=0 is population).

2. When calling the std or variance methods of the object, the population vs. sample distinction is ignored.

2. Why are these methods in a class?  They don't seem to use any benefits of a class; they just seem to be standalone functions.  It seems like it would make much more sense to me to have these methods be just functions inside of the module.  We can still import them into a namespace called "stats".



---

archive/issue_comments_059583.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-10-14T21:33:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7197",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7197#issuecomment-59583",
    "user": "https://github.com/jasongrout"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_059584.json:
```json
{
    "body": "I should also say I'm glad you are working on these!  I was very surprised to learn a few weeks ago that Sage did not have a generic standard deviation function.  We needed it in the class I was teaching!",
    "created_at": "2009-10-14T21:34:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7197",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7197#issuecomment-59584",
    "user": "https://github.com/jasongrout"
}
```

I should also say I'm glad you are working on these!  I was very surprised to learn a few weeks ago that Sage did not have a generic standard deviation function.  We needed it in the class I was teaching!



---

archive/issue_comments_059585.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-10-26T06:05:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7197",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7197#issuecomment-59585",
    "user": "https://trac.sagemath.org/admin/accounts/users/amhou"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_059586.json:
```json
{
    "body": "Attachment [trac_7197_basic_stats.patch](tarball://root/attachments/some-uuid/ticket7197/trac_7197_basic_stats.patch) by amhou created at 2009-10-26 06:05:30\n\nPatch added. \n\nArguments for std and variance changed to \"bias = True/False\" for division by n and n-1 respectively.",
    "created_at": "2009-10-26T06:05:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7197",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7197#issuecomment-59586",
    "user": "https://trac.sagemath.org/admin/accounts/users/amhou"
}
```

Attachment [trac_7197_basic_stats.patch](tarball://root/attachments/some-uuid/ticket7197/trac_7197_basic_stats.patch) by amhou created at 2009-10-26 06:05:30

Patch added. 

Arguments for std and variance changed to "bias = True/False" for division by n and n-1 respectively.



---

archive/issue_comments_059587.json:
```json
{
    "body": "Changing assignee from mhampton to amhou.",
    "created_at": "2009-10-26T06:05:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7197",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7197#issuecomment-59587",
    "user": "https://trac.sagemath.org/admin/accounts/users/amhou"
}
```

Changing assignee from mhampton to amhou.



---

archive/issue_comments_059588.json:
```json
{
    "body": "Is there any way to have \"std_sample\" and \"std_population\" (and same for variance)?  When teaching very basic classes statistics, we just refer to them as population and sample std or variance.  Having specific functions (as excel or their calculators do) would make more sense to students.",
    "created_at": "2009-10-26T14:00:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7197",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7197#issuecomment-59588",
    "user": "https://github.com/jasongrout"
}
```

Is there any way to have "std_sample" and "std_population" (and same for variance)?  When teaching very basic classes statistics, we just refer to them as population and sample std or variance.  Having specific functions (as excel or their calculators do) would make more sense to students.



---

archive/issue_comments_059589.json:
```json
{
    "body": "Attachment [trac_7197_basic_stats_2.patch](tarball://root/attachments/some-uuid/ticket7197/trac_7197_basic_stats_2.patch) by amhou created at 2009-10-26 23:06:45",
    "created_at": "2009-10-26T23:06:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7197",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7197#issuecomment-59589",
    "user": "https://trac.sagemath.org/admin/accounts/users/amhou"
}
```

Attachment [trac_7197_basic_stats_2.patch](tarball://root/attachments/some-uuid/ticket7197/trac_7197_basic_stats_2.patch) by amhou created at 2009-10-26 23:06:45



---

archive/issue_comments_059590.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-10-26T23:37:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7197",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7197#issuecomment-59590",
    "user": "https://github.com/williamstein"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_059591.json:
```json
{
    "body": "REFEREE REPORT:\n\n0. All tests pass in the entire tree after applying this.\n\n1. I'm OK with not adding std_sample and std_population simply because R, matlab, mathematica all don't and the instructor can easily add some alias's for their class. \n\n2. Add copyright header block.\n\n3. Add a docstring section at the top with AUTHOR, overview of capabilities, etc. \n\n4. Don't import numpy at top level; it'll just get moved later since we should not import numpy/matplotlib/etc. at startup. \n\n5. For `def std(v, bias=False):` and any other function that handles special types, put in examples that illustrate that your code for handling these types works. \n\nFix all the above and I'll be happy with this patch!",
    "created_at": "2009-10-26T23:37:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7197",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7197#issuecomment-59591",
    "user": "https://github.com/williamstein"
}
```

REFEREE REPORT:

0. All tests pass in the entire tree after applying this.

1. I'm OK with not adding std_sample and std_population simply because R, matlab, mathematica all don't and the instructor can easily add some alias's for their class. 

2. Add copyright header block.

3. Add a docstring section at the top with AUTHOR, overview of capabilities, etc. 

4. Don't import numpy at top level; it'll just get moved later since we should not import numpy/matplotlib/etc. at startup. 

5. For `def std(v, bias=False):` and any other function that handles special types, put in examples that illustrate that your code for handling these types works. 

Fix all the above and I'll be happy with this patch!



---

archive/issue_comments_059592.json:
```json
{
    "body": "Attachment [trac_7197_part4.patch](tarball://root/attachments/some-uuid/ticket7197/trac_7197_part4.patch) by amhou created at 2009-11-08 00:49:39",
    "created_at": "2009-11-08T00:49:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7197",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7197#issuecomment-59592",
    "user": "https://trac.sagemath.org/admin/accounts/users/amhou"
}
```

Attachment [trac_7197_part4.patch](tarball://root/attachments/some-uuid/ticket7197/trac_7197_part4.patch) by amhou created at 2009-11-08 00:49:39



---

archive/issue_comments_059593.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-11-08T00:50:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7197",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7197#issuecomment-59593",
    "user": "https://trac.sagemath.org/admin/accounts/users/amhou"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_059594.json:
```json
{
    "body": "Attachment [trac_7197_basic_stats_part5.patch](tarball://root/attachments/some-uuid/ticket7197/trac_7197_basic_stats_part5.patch) by amhou created at 2009-11-12 22:16:54",
    "created_at": "2009-11-12T22:16:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7197",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7197#issuecomment-59594",
    "user": "https://trac.sagemath.org/admin/accounts/users/amhou"
}
```

Attachment [trac_7197_basic_stats_part5.patch](tarball://root/attachments/some-uuid/ticket7197/trac_7197_basic_stats_part5.patch) by amhou created at 2009-11-12 22:16:54



---

archive/issue_comments_059595.json:
```json
{
    "body": "REPORT 2:\n\n1. a little too spartan:\n\n```\n\"\"\"\nBasic Statistics\n\nThis file contains basic descriptive functions.\n\nAUTHOR:\n    - Andrew Hou (11/06/2009)\n...\n\"\"\"\n```\n\n\n2. Make sure there is a test that tests this code:\n\n```\n    \"\"\"\n    if hasattr(v, 'mean'): return v.mean()\n```\n\n\n3. Same for mode:\n\n```\n    if hasattr(v, 'mode'): return v.mode()\n```\n\n\n4. Same for this:\n\n```\n    if hasattr(v, 'standard_deviation'): return v.standard_deviation(bias=bias)\n```\n\n\n5. Type checking in python should always use isinstance:\n\n```\n    if type(v) is numpy.ndarray:\n    if type(v) == numpy.ndarray:\n```\n\nshould be\n\n```\n     if isinstance(v, numpy.ndarray):\n```\n\n\n6. Test this:\n\n```\n    if hasattr(v, 'variance'): return v.variance(bias = bias)\n```\n\n\n7. Change this:\n\n```\n    if bias == True:\n        # population variance\n        if isinstance(x, (int,long)):\n            return x/ZZ(len(v))\n        return x/len(v)\n    elif bias == False:\n```\n\nto\n\n```\n    if bias:\n        # population variance\n        if isinstance(x, (int,long)):\n            return x/ZZ(len(v))\n        return x/len(v)\n    else:\n```\n\n\n\n8. Make sure this is tested:\n\n```\n    if hasattr(v, 'median'): return v.median()\n```\n\n\n9. Weird \"\"\" in moving_average:\n\n```\n \t318\t                                                                                    \"\"\" \n \t319\t    x = []    \n```\n\n\n10. Change\n\n```\n    bin_size = len(v)/bins     \n```\n\nto floor division:\n\n```\n    bin_size = int(len(v)//bins)\n```\n\n\n11. You can do this at the very end of each docstring if you want...\n\n```\n    AUTHOR:\n\n       - Andrew Hou (11/06/2009)\n```\n",
    "created_at": "2009-11-12T22:43:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7197",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7197#issuecomment-59595",
    "user": "https://github.com/williamstein"
}
```

REPORT 2:

1. a little too spartan:

```
"""
Basic Statistics

This file contains basic descriptive functions.

AUTHOR:
    - Andrew Hou (11/06/2009)
...
"""
```


2. Make sure there is a test that tests this code:

```
    """
    if hasattr(v, 'mean'): return v.mean()
```


3. Same for mode:

```
    if hasattr(v, 'mode'): return v.mode()
```


4. Same for this:

```
    if hasattr(v, 'standard_deviation'): return v.standard_deviation(bias=bias)
```


5. Type checking in python should always use isinstance:

```
    if type(v) is numpy.ndarray:
    if type(v) == numpy.ndarray:
```

should be

```
     if isinstance(v, numpy.ndarray):
```


6. Test this:

```
    if hasattr(v, 'variance'): return v.variance(bias = bias)
```


7. Change this:

```
    if bias == True:
        # population variance
        if isinstance(x, (int,long)):
            return x/ZZ(len(v))
        return x/len(v)
    elif bias == False:
```

to

```
    if bias:
        # population variance
        if isinstance(x, (int,long)):
            return x/ZZ(len(v))
        return x/len(v)
    else:
```



8. Make sure this is tested:

```
    if hasattr(v, 'median'): return v.median()
```


9. Weird """ in moving_average:

```
 	318	                                                                                    """ 
 	319	    x = []    
```


10. Change

```
    bin_size = len(v)/bins     
```

to floor division:

```
    bin_size = int(len(v)//bins)
```


11. You can do this at the very end of each docstring if you want...

```
    AUTHOR:

       - Andrew Hou (11/06/2009)
```




---

archive/issue_comments_059596.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-11-12T22:43:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7197",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7197#issuecomment-59596",
    "user": "https://github.com/williamstein"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_059597.json:
```json
{
    "body": "Attachment [trac_7197_part6.patch](tarball://root/attachments/some-uuid/ticket7197/trac_7197_part6.patch) by amhou created at 2009-11-16 08:15:38",
    "created_at": "2009-11-16T08:15:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7197",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7197#issuecomment-59597",
    "user": "https://trac.sagemath.org/admin/accounts/users/amhou"
}
```

Attachment [trac_7197_part6.patch](tarball://root/attachments/some-uuid/ticket7197/trac_7197_part6.patch) by amhou created at 2009-11-16 08:15:38



---

archive/issue_comments_059598.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-11-16T08:15:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7197",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7197#issuecomment-59598",
    "user": "https://trac.sagemath.org/admin/accounts/users/amhou"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_059599.json:
```json
{
    "body": "Issues:\n\n* Delete \"Included as of 11/06/2009\" and reword.\n\n* Fix: \"returns the most common occuring member of a sample.\"  (and occurring is the right spelling)\n\n* \"Functions have also been imported under the namespace 'stats'.\"  Change to not use the passive voice.  I.e., \"The functions are available in the namespace *stats*, i.e., you can use them by typing *stats.mean*, *stats.median*, etc.\"\n\n* Change all ' to * in the top section.   * (two single quotes as separate characters) means \"monospace\" in ReST markup.",
    "created_at": "2009-11-17T00:30:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7197",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7197#issuecomment-59599",
    "user": "https://github.com/williamstein"
}
```

Issues:

* Delete "Included as of 11/06/2009" and reword.

* Fix: "returns the most common occuring member of a sample."  (and occurring is the right spelling)

* "Functions have also been imported under the namespace 'stats'."  Change to not use the passive voice.  I.e., "The functions are available in the namespace *stats*, i.e., you can use them by typing *stats.mean*, *stats.median*, etc."

* Change all ' to * in the top section.   * (two single quotes as separate characters) means "monospace" in ReST markup.



---

archive/issue_comments_059600.json:
```json
{
    "body": "Attachment [trac_7197_part8.patch](tarball://root/attachments/some-uuid/ticket7197/trac_7197_part8.patch) by amhou created at 2009-11-17 01:00:09",
    "created_at": "2009-11-17T01:00:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7197",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7197#issuecomment-59600",
    "user": "https://trac.sagemath.org/admin/accounts/users/amhou"
}
```

Attachment [trac_7197_part8.patch](tarball://root/attachments/some-uuid/ticket7197/trac_7197_part8.patch) by amhou created at 2009-11-17 01:00:09



---

archive/issue_comments_059601.json:
```json
{
    "body": "Attachment [trac_7197_part9.patch](tarball://root/attachments/some-uuid/ticket7197/trac_7197_part9.patch) by amhou created at 2009-11-20 22:56:52",
    "created_at": "2009-11-20T22:56:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7197",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7197#issuecomment-59601",
    "user": "https://trac.sagemath.org/admin/accounts/users/amhou"
}
```

Attachment [trac_7197_part9.patch](tarball://root/attachments/some-uuid/ticket7197/trac_7197_part9.patch) by amhou created at 2009-11-20 22:56:52



---

archive/issue_comments_059602.json:
```json
{
    "body": "Attachment [trac_7197_part10.patch](tarball://root/attachments/some-uuid/ticket7197/trac_7197_part10.patch) by @williamstein created at 2009-11-24 01:04:03",
    "created_at": "2009-11-24T01:04:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7197",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7197#issuecomment-59602",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_7197_part10.patch](tarball://root/attachments/some-uuid/ticket7197/trac_7197_part10.patch) by @williamstein created at 2009-11-24 01:04:03



---

archive/issue_comments_059603.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-11-24T01:04:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7197",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7197#issuecomment-59603",
    "user": "https://github.com/williamstein"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_059604.json:
```json
{
    "body": "All of the above patches folded together.  Apply only this patch.",
    "created_at": "2009-11-25T06:45:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7197",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7197#issuecomment-59604",
    "user": "https://github.com/mwhansen"
}
```

All of the above patches folded together.  Apply only this patch.



---

archive/issue_comments_059605.json:
```json
{
    "body": "Attachment [trac_7197.patch](tarball://root/attachments/some-uuid/ticket7197/trac_7197.patch) by @mwhansen created at 2009-11-29 05:07:20",
    "created_at": "2009-11-29T05:07:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7197",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7197#issuecomment-59605",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_7197.patch](tarball://root/attachments/some-uuid/ticket7197/trac_7197.patch) by @mwhansen created at 2009-11-29 05:07:20



---

archive/issue_events_007416.json:
```json
{
    "actor": "@mwhansen",
    "created_at": "2009-11-29T05:07:20Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7197",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7197#event-7416"
}
```



---

archive/issue_comments_059606.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-29T05:07:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7197",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7197#issuecomment-59606",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed
