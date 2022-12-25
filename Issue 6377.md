# Issue 6377: exp(x) is broken at x=Infinity and x=-Infinity

archive/issues_006377.json:
```json
{
    "body": "Keywords: symbolic exp\n\nexponetial function exp(x) is broken at both x=-Infinity\nand x=Infinity\n\n\n```\nsage: exp(-Infinity)\n---------------------------------------------------------------------------\nRuntimeError                              Traceback (most recent call last)\n....\nRuntimeError: x*Infinity with non real x encountered.\n```\n\n\n\n\n```\nsage: exp(Infinity)\n---------------------------------------------------------------------------\nRuntimeError                              Traceback (most recent call last)\n....\nRuntimeError: x*Infinity with non real x encountered.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6377\n\n",
    "created_at": "2009-06-21T17:56:25Z",
    "labels": [
        "component: symbolics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.1",
    "title": "exp(x) is broken at x=Infinity and x=-Infinity",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6377",
    "user": "https://github.com/golam-m-hossain"
}
```
Keywords: symbolic exp

exponetial function exp(x) is broken at both x=-Infinity
and x=Infinity


```
sage: exp(-Infinity)
---------------------------------------------------------------------------
RuntimeError                              Traceback (most recent call last)
....
RuntimeError: x*Infinity with non real x encountered.
```




```
sage: exp(Infinity)
---------------------------------------------------------------------------
RuntimeError                              Traceback (most recent call last)
....
RuntimeError: x*Infinity with non real x encountered.
```


Issue created by migration from https://trac.sagemath.org/ticket/6377





---

archive/issue_comments_050931.json:
```json
{
    "body": "Set assignee to @burcin.",
    "created_at": "2009-06-22T13:02:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6377#issuecomment-50931",
    "user": "https://github.com/burcin"
}
```

Set assignee to @burcin.



---

archive/issue_comments_050932.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-06-22T13:02:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6377#issuecomment-50932",
    "user": "https://github.com/burcin"
}
```

Changing status from new to assigned.



---

archive/issue_comments_050933.json:
```json
{
    "body": "Good catch! After adding support for infinity in pynac, I forgot to add cases to handle infinity in the eval functions of special functions. \n\nThe fix for `exp()` needs to go into pynac. I don't know what other functions are effected by this. It would be good to try other special functions defined by Sage to see if they handle infinity, or other constants defined by Sage properly.",
    "created_at": "2009-06-22T13:02:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6377#issuecomment-50933",
    "user": "https://github.com/burcin"
}
```

Good catch! After adding support for infinity in pynac, I forgot to add cases to handle infinity in the eval functions of special functions. 

The fix for `exp()` needs to go into pynac. I don't know what other functions are effected by this. It would be good to try other special functions defined by Sage to see if they handle infinity, or other constants defined by Sage properly.



---

archive/issue_comments_050934.json:
```json
{
    "body": "Attachment [trac_6377-exp_infinity.patch](tarball://root/attachments/some-uuid/ticket6377/trac_6377-exp_infinity.patch) by @burcin created at 2009-07-31 23:52:10\n\ndoctests for the fix",
    "created_at": "2009-07-31T23:52:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6377#issuecomment-50934",
    "user": "https://github.com/burcin"
}
```

Attachment [trac_6377-exp_infinity.patch](tarball://root/attachments/some-uuid/ticket6377/trac_6377-exp_infinity.patch) by @burcin created at 2009-07-31 23:52:10

doctests for the fix



---

archive/issue_comments_050935.json:
```json
{
    "body": "I have a fix for this in my local pynac tree. I will make a new pynac package available soon.\n\nI checked all the functions defined in inifcns_trans.cpp in pynac. The remaining functions still need to be fixed.",
    "created_at": "2009-07-31T23:56:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6377#issuecomment-50935",
    "user": "https://github.com/burcin"
}
```

I have a fix for this in my local pynac tree. I will make a new pynac package available soon.

I checked all the functions defined in inifcns_trans.cpp in pynac. The remaining functions still need to be fixed.



---

archive/issue_comments_050936.json:
```json
{
    "body": "This now depends on the package linked from #6404.\n\nPlease follow the instructions on that ticket to apply & test.",
    "created_at": "2009-08-01T02:32:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6377#issuecomment-50936",
    "user": "https://github.com/burcin"
}
```

This now depends on the package linked from #6404.

Please follow the instructions on that ticket to apply & test.



---

archive/issue_comments_050937.json:
```json
{
    "body": "Hi Burcin,\n\nI tested this out. It looks fine to me. \n\nI guess, it would be good if we could follow some standard convention for \nvalues of these functions at their poles, brunch cuts. For example, following \nlooks odd to me\n\n```\nsage: arctan(-Infinity)\n-1/2*pi\nsage: tan(-pi/2)\nInfinity\n```\n\n\nMay be we should discuss this in sage-devel for adopting a convention for\nthese special values.\n\nThere are some other issues that would need future work. For example, you have\nfixed values of log at 0\n\n```\nsage: SR(0).log()\n-Infinity\n```\n\n\nHowever, following still raises error\n\n```\nsage: log(0)\nValueError ...\n```\n\n\nIn any case, this patch fixes lot of issues and should be included.\nThe remaining issues should be fixed later. I am going to give a positive\nreview shortly.",
    "created_at": "2009-08-02T18:51:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6377#issuecomment-50937",
    "user": "https://github.com/golam-m-hossain"
}
```

Hi Burcin,

I tested this out. It looks fine to me. 

I guess, it would be good if we could follow some standard convention for 
values of these functions at their poles, brunch cuts. For example, following 
looks odd to me

```
sage: arctan(-Infinity)
-1/2*pi
sage: tan(-pi/2)
Infinity
```


May be we should discuss this in sage-devel for adopting a convention for
these special values.

There are some other issues that would need future work. For example, you have
fixed values of log at 0

```
sage: SR(0).log()
-Infinity
```


However, following still raises error

```
sage: log(0)
ValueError ...
```


In any case, this patch fixes lot of issues and should be included.
The remaining issues should be fixed later. I am going to give a positive
review shortly.



---

archive/issue_comments_050938.json:
```json
{
    "body": "Note: I am giving partial positive review because I tested this patch against my stable sage-4.1. So if it applies cleanly on Sage-4.1.1.rc1 then that would be full positive from me.",
    "created_at": "2009-08-02T19:24:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6377#issuecomment-50938",
    "user": "https://github.com/golam-m-hossain"
}
```

Note: I am giving partial positive review because I tested this patch against my stable sage-4.1. So if it applies cleanly on Sage-4.1.1.rc1 then that would be full positive from me.



---

archive/issue_events_006625.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2009-08-03T00:31:27Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6377",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6377#event-6625"
}
```



---

archive/issue_comments_050939.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-08-03T00:31:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6377#issuecomment-50939",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_050940.json:
```json
{
    "body": "I applied patches in the following order:\n1. the spkg `pynac-0.1.8.p2.spkg` at #6404\n2. `trac_6404-conjugate_typesetting.patch`\n3. `trac_6401-real_imag_typesetting.patch`\n4. `trac_6377-exp_infinity.patch`\n5. `trac_6243-fderivative_hash.patch`\nAll doctests pass in my merge tree. So I'm changing #6404, #6401, #6377 and #6243 to positive review as per Golam's request.",
    "created_at": "2009-08-03T00:31:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6377#issuecomment-50940",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

I applied patches in the following order:
1. the spkg `pynac-0.1.8.p2.spkg` at #6404
2. `trac_6404-conjugate_typesetting.patch`
3. `trac_6401-real_imag_typesetting.patch`
4. `trac_6377-exp_infinity.patch`
5. `trac_6243-fderivative_hash.patch`
All doctests pass in my merge tree. So I'm changing #6404, #6401, #6377 and #6243 to positive review as per Golam's request.
