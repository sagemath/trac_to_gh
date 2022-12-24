# Issue 4264: change E.a_invariants() for an elliptic curve to return a tuple

archive/issues_004264.json:
```json
{
    "body": "Assignee: was\n\nFor consistency with b_invariants, etc., and to emphasize immutability, it would be\ngood for E.a_invariants() to return a tuple.  Changing this could change lots of doctests, etc., so this isn't trivial.\n\nSee trac #4262 for a related ticket\n\nIssue created by migration from https://trac.sagemath.org/ticket/4264\n\n",
    "created_at": "2008-10-11T09:46:11Z",
    "labels": [
        "number theory",
        "major",
        "enhancement"
    ],
    "title": "change E.a_invariants() for an elliptic curve to return a tuple",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4264",
    "user": "was"
}
```
Assignee: was

For consistency with b_invariants, etc., and to emphasize immutability, it would be
good for E.a_invariants() to return a tuple.  Changing this could change lots of doctests, etc., so this isn't trivial.

See trac #4262 for a related ticket

Issue created by migration from https://trac.sagemath.org/ticket/4264





---

archive/issue_comments_031094.json:
```json
{
    "body": "Quick comment:  the cached `self.__ainvs` should actually *be* a tuple.  So the only code to change is in line 142 in `ell_generic.py`, from this\n\n```\n        self.__ainvs = ainvs\n```\n\nto this\n\n```\n        self.__aincs = tuple(ainvs)\n```\n\nas well as the doctests.",
    "created_at": "2008-10-13T11:51:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4264",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4264#issuecomment-31094",
    "user": "cremona"
}
```

Quick comment:  the cached `self.__ainvs` should actually *be* a tuple.  So the only code to change is in line 142 in `ell_generic.py`, from this

```
        self.__ainvs = ainvs
```

to this

```
        self.__aincs = tuple(ainvs)
```

as well as the doctests.



---

archive/issue_comments_031095.json:
```json
{
    "body": "I have made a patch (not yet attached) which implements this.   It was easy to do what was suggested (and make the consequent cosmetic changes in doctests from [...] to (...) ) but there were two similar but distinct other issues:\n\n* Several Sage functions (the `__init__` function in the EllipticCurve classes) expect the a-invs input parameters to be a list and not a tuple.  I tried changing them to accept tuples but it caused too many difficulites with parsing different input possibilities so I reverted that.\n* In several places where elliptic curves in other systems are initialised (e.g. mwrank, gp) lists are required for the parsing done by the wrappers.\n\nIn all the above I sorted everything out by inserting list(...) around `blah.ainvs()` or `blah.a_invariants()`, which works but is ugly.   Is there a better way?  Even just having a new function a_list() to be list(self.ainvs()) would be a bit cleaner.  We already have the unnecessary synonyms a_invariants() and ainvs().\n\nI'll wait for reaction before going further.  In particular, I have not yet tested anything outside the elliptic_curves directory, e.g. the tutorial.",
    "created_at": "2008-10-13T16:12:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4264",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4264#issuecomment-31095",
    "user": "cremona"
}
```

I have made a patch (not yet attached) which implements this.   It was easy to do what was suggested (and make the consequent cosmetic changes in doctests from [...] to (...) ) but there were two similar but distinct other issues:

* Several Sage functions (the `__init__` function in the EllipticCurve classes) expect the a-invs input parameters to be a list and not a tuple.  I tried changing them to accept tuples but it caused too many difficulites with parsing different input possibilities so I reverted that.
* In several places where elliptic curves in other systems are initialised (e.g. mwrank, gp) lists are required for the parsing done by the wrappers.

In all the above I sorted everything out by inserting list(...) around `blah.ainvs()` or `blah.a_invariants()`, which works but is ugly.   Is there a better way?  Even just having a new function a_list() to be list(self.ainvs()) would be a bit cleaner.  We already have the unnecessary synonyms a_invariants() and ainvs().

I'll wait for reaction before going further.  In particular, I have not yet tested anything outside the elliptic_curves directory, e.g. the tutorial.



---

archive/issue_comments_031096.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2008-10-13T16:12:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4264",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4264#issuecomment-31096",
    "user": "cremona"
}
```

Changing priority from major to minor.



---

archive/issue_comments_031097.json:
```json
{
    "body": "Changing assignee from was to davidloeffler.",
    "created_at": "2009-07-20T19:48:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4264",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4264#issuecomment-31097",
    "user": "davidloeffler"
}
```

Changing assignee from was to davidloeffler.



---

archive/issue_comments_031098.json:
```json
{
    "body": "Changing component from number theory to elliptic curves.",
    "created_at": "2009-07-20T19:48:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4264",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4264#issuecomment-31098",
    "user": "davidloeffler"
}
```

Changing component from number theory to elliptic curves.



---

archive/issue_comments_031099.json:
```json
{
    "body": "Doesn't 9 months go quickly?  I thought this had been fixed long ago.  No time now though...",
    "created_at": "2009-07-20T19:58:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4264",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4264#issuecomment-31099",
    "user": "cremona"
}
```

Doesn't 9 months go quickly?  I thought this had been fixed long ago.  No time now though...



---

archive/issue_comments_031100.json:
```json
{
    "body": "Remove assignee davidloeffler.",
    "created_at": "2009-10-09T09:13:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4264",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4264#issuecomment-31100",
    "user": "davidloeffler"
}
```

Remove assignee davidloeffler.



---

archive/issue_comments_031101.json:
```json
{
    "body": "I think we won't need a a_list. I'd prefer having list() everywhere, even if it is ugly.\n\nCould you post your first draft of a patch here ? I will try to work on it.\n\nChris.",
    "created_at": "2009-10-20T21:56:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4264",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4264#issuecomment-31101",
    "user": "wuthrich"
}
```

I think we won't need a a_list. I'd prefer having list() everywhere, even if it is ugly.

Could you post your first draft of a patch here ? I will try to work on it.

Chris.



---

archive/issue_comments_031102.json:
```json
{
    "body": "Replying to [comment:6 wuthrich]:\n> I think we won't need a a_list. I'd prefer having list() everywhere, even if it is ugly.\n> \n> Could you post your first draft of a patch here ? I will try to work on it.\n> \n> Chris.\n\nSorry, but after a year I am sure that it is lost for ever.  I should have uploaded it anyway with a \"needs more work\" tag.  Anyway, after a year of version changes it would never have merged without a lot of work.",
    "created_at": "2009-10-21T08:17:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4264",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4264#issuecomment-31102",
    "user": "cremona"
}
```

Replying to [comment:6 wuthrich]:
> I think we won't need a a_list. I'd prefer having list() everywhere, even if it is ugly.
> 
> Could you post your first draft of a patch here ? I will try to work on it.
> 
> Chris.

Sorry, but after a year I am sure that it is lost for ever.  I should have uploaded it anyway with a "needs more work" tag.  Anyway, after a year of version changes it would never have merged without a lot of work.



---

archive/issue_comments_031103.json:
```json
{
    "body": "That is alright. If I get to do it, I will start from scratch, then.",
    "created_at": "2009-10-21T09:35:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4264",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4264#issuecomment-31103",
    "user": "wuthrich"
}
```

That is alright. If I get to do it, I will start from scratch, then.



---

archive/issue_comments_031104.json:
```json
{
    "body": "exported against 4.2.",
    "created_at": "2009-11-02T13:11:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4264",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4264#issuecomment-31104",
    "user": "wuthrich"
}
```

exported against 4.2.



---

archive/issue_comments_031105.json:
```json
{
    "body": "Attachment [trac_4264.patch](tarball://root/attachments/some-uuid/ticket4264/trac_4264.patch) by wuthrich created at 2009-11-02 13:12:24\n\nI hope I did not miss any a_invs or a_invariants.",
    "created_at": "2009-11-02T13:12:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4264",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4264#issuecomment-31105",
    "user": "wuthrich"
}
```

Attachment [trac_4264.patch](tarball://root/attachments/some-uuid/ticket4264/trac_4264.patch) by wuthrich created at 2009-11-02 13:12:24

I hope I did not miss any a_invs or a_invariants.



---

archive/issue_comments_031106.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-11-02T13:12:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4264",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4264#issuecomment-31106",
    "user": "wuthrich"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_031107.json:
```json
{
    "body": "Looks good to me.  Passes all tests with -long.",
    "created_at": "2009-11-05T02:39:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4264",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4264#issuecomment-31107",
    "user": "mhansen"
}
```

Looks good to me.  Passes all tests with -long.



---

archive/issue_comments_031108.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-11-05T02:39:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4264",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4264#issuecomment-31108",
    "user": "mhansen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_031109.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-05T02:40:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4264",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4264#issuecomment-31109",
    "user": "mhansen"
}
```

Resolution: fixed
