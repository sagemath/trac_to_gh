# Issue 5777: [with package and patches, needs review] update to pynac 0.1.5

archive/issues_005777.json:
```json
{
    "body": "Assignee: burcin\n\nCC:  wstein mhansen ncalexan robertwb\n\nThere is a new version of pynac with the following changes:\n\n* Change printing of pi (Pi -> pi)\n* Delay evaluation of special functions until .evalf() is called\n* Add precision parameter to .evalf()\n\nI am opening a new ticket, since the patches require separate review.\n\nThe package is here:\n\nhttp://sage.math.washington.edu/home/burcin/pynac/pynac-0.1.5.spkg\n\nAttached patches need to be applied to Sage, they depend on #5753.\n\nI got an infinite loop trying to convert to `ComplexField` in the second patch, hence the additions to sage/rings/complex_field.py. Robert, am I doing something wrong here?\n\nIssue created by migration from https://trac.sagemath.org/ticket/5777\n\n",
    "created_at": "2009-04-13T16:07:10Z",
    "labels": [
        "symbolics",
        "major",
        "bug"
    ],
    "title": "[with package and patches, needs review] update to pynac 0.1.5",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5777",
    "user": "burcin"
}
```
Assignee: burcin

CC:  wstein mhansen ncalexan robertwb

There is a new version of pynac with the following changes:

* Change printing of pi (Pi -> pi)
* Delay evaluation of special functions until .evalf() is called
* Add precision parameter to .evalf()

I am opening a new ticket, since the patches require separate review.

The package is here:

http://sage.math.washington.edu/home/burcin/pynac/pynac-0.1.5.spkg

Attached patches need to be applied to Sage, they depend on #5753.

I got an infinite loop trying to convert to `ComplexField` in the second patch, hence the additions to sage/rings/complex_field.py. Robert, am I doing something wrong here?

Issue created by migration from https://trac.sagemath.org/ticket/5777





---

archive/issue_comments_045176.json:
```json
{
    "body": "fix doctests for printing changes",
    "created_at": "2009-04-13T16:07:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5777",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5777#issuecomment-45176",
    "user": "burcin"
}
```

fix doctests for printing changes



---

archive/issue_comments_045177.json:
```json
{
    "body": "Attachment\n\nallow setting precision for numerical approximation",
    "created_at": "2009-04-24T14:20:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5777",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5777#issuecomment-45177",
    "user": "burcin"
}
```

Attachment

allow setting precision for numerical approximation



---

archive/issue_comments_045178.json:
```json
{
    "body": "Rebased attachment:trac_5777-02-precision.patch for 3.4.1.",
    "created_at": "2009-04-24T14:21:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5777",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5777#issuecomment-45178",
    "user": "burcin"
}
```

Rebased attachment:trac_5777-02-precision.patch for 3.4.1.



---

archive/issue_comments_045179.json:
```json
{
    "body": "add doctests for exceptions raised during hashing",
    "created_at": "2009-05-05T23:12:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5777",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5777#issuecomment-45179",
    "user": "burcin"
}
```

add doctests for exceptions raised during hashing



---

archive/issue_comments_045180.json:
```json
{
    "body": "Attachment\n\nsupport pickling pynac expressions",
    "created_at": "2009-05-05T23:12:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5777",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5777#issuecomment-45180",
    "user": "burcin"
}
```

Attachment

support pickling pynac expressions



---

archive/issue_comments_045181.json:
```json
{
    "body": "Attachment\n\nsupport pickling symbolic functions",
    "created_at": "2009-05-05T23:13:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5777",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5777#issuecomment-45181",
    "user": "burcin"
}
```

Attachment

support pickling symbolic functions



---

archive/issue_comments_045182.json:
```json
{
    "body": "doctests for the changes in behavior of exp",
    "created_at": "2009-05-05T23:13:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5777",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5777#issuecomment-45182",
    "user": "burcin"
}
```

doctests for the changes in behavior of exp



---

archive/issue_comments_045183.json:
```json
{
    "body": "Attachment\n\nI put a preliminary version of the new pynac package here:\n\nhttp://sage.math.washington.edu/home/burcin/pynac/pynac-0.1.6.spkg\n\nI haven't actually committed the version information to the pynac repository yet. I plan to wait until this gets reviewed, and see if there are any last minute changes needed.\n\nThe newly uploaded patches:\n\n* attachment:trac_5777-11-hash_doctests.patch\n* attachment:trac_5777-12-pickle_expression.patch\n* attachment:trac_5777-13-pickle_sfunction.patch\n* attachment:trac_5777-14-exp.patch\n\ncorrespond to the changes in the new package.\n\nThe changes in pynac are:\n* Fix error handling in Number_T::hash().\n* Add support for archiving numeric and function objects.\n* Fix comparison bug in mul.\n* Fix gcc warnings about conversion of strings to char*.\n* Change exp to not prints exponents of 1.\n* Add power method to exp so that `(e<sup>x)</sup>y -> e^(x*y)`.\n\nNote that this fixes #5944, which I consider a blocker.",
    "created_at": "2009-05-05T23:19:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5777",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5777#issuecomment-45183",
    "user": "burcin"
}
```

Attachment

I put a preliminary version of the new pynac package here:

http://sage.math.washington.edu/home/burcin/pynac/pynac-0.1.6.spkg

I haven't actually committed the version information to the pynac repository yet. I plan to wait until this gets reviewed, and see if there are any last minute changes needed.

The newly uploaded patches:

* attachment:trac_5777-11-hash_doctests.patch
* attachment:trac_5777-12-pickle_expression.patch
* attachment:trac_5777-13-pickle_sfunction.patch
* attachment:trac_5777-14-exp.patch

correspond to the changes in the new package.

The changes in pynac are:
* Fix error handling in Number_T::hash().
* Add support for archiving numeric and function objects.
* Fix comparison bug in mul.
* Fix gcc warnings about conversion of strings to char*.
* Change exp to not prints exponents of 1.
* Add power method to exp so that `(e<sup>x)</sup>y -> e^(x*y)`.

Note that this fixes #5944, which I consider a blocker.



---

archive/issue_comments_045184.json:
```json
{
    "body": "Changing assignee from burcin to mhansen.",
    "created_at": "2009-05-19T01:48:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5777",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5777#issuecomment-45184",
    "user": "mhansen"
}
```

Changing assignee from burcin to mhansen.



---

archive/issue_comments_045185.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-05-19T01:48:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5777",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5777#issuecomment-45185",
    "user": "mhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_045186.json:
```json
{
    "body": "I have all of Burcin's changes that apply to 4.0.rc0 in symbolics_final1.patch.  These work with the pynac-0.1.6.spkg.\n\nThese get a positive review from me.  I've based the new symbolics changes on these.",
    "created_at": "2009-05-19T01:48:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5777",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5777#issuecomment-45186",
    "user": "mhansen"
}
```

I have all of Burcin's changes that apply to 4.0.rc0 in symbolics_final1.patch.  These work with the pynac-0.1.6.spkg.

These get a positive review from me.  I've based the new symbolics changes on these.



---

archive/issue_comments_045187.json:
```json
{
    "body": "Attachment\n\nMerged in Sage 4.0.rc0.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-20T23:44:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5777",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5777#issuecomment-45187",
    "user": "mabshoff"
}
```

Attachment

Merged in Sage 4.0.rc0.

Cheers,

Michael



---

archive/issue_comments_045188.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-20T23:44:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5777",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5777#issuecomment-45188",
    "user": "mabshoff"
}
```

Resolution: fixed
