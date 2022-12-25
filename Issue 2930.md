# Issue 2930: CDF is slow, fix it.

archive/issues_002930.json:
```json
{
    "body": "Assignee: @garyfurnish\n\nCC:  @robertwb\n\nAdd a CDF pool, optimize CD creation.  \n\nIssue created by migration from https://trac.sagemath.org/ticket/2930\n\n",
    "created_at": "2008-04-15T06:13:29Z",
    "labels": [
        "component: basic arithmetic",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "CDF is slow, fix it.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2930",
    "user": "https://github.com/garyfurnish"
}
```
Assignee: @garyfurnish

CC:  @robertwb

Add a CDF pool, optimize CD creation.  

Issue created by migration from https://trac.sagemath.org/ticket/2930





---

archive/issue_comments_020131.json:
```json
{
    "body": "Attachment [trac_2930.patch](tarball://root/attachments/some-uuid/ticket2930/trac_2930.patch) by @garyfurnish created at 2008-04-15 06:14:24",
    "created_at": "2008-04-15T06:14:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2930",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2930#issuecomment-20131",
    "user": "https://github.com/garyfurnish"
}
```

Attachment [trac_2930.patch](tarball://root/attachments/some-uuid/ticket2930/trac_2930.patch) by @garyfurnish created at 2008-04-15 06:14:24



---

archive/issue_comments_020132.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-04-15T06:14:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2930",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2930#issuecomment-20132",
    "user": "https://github.com/garyfurnish"
}
```

Changing status from new to assigned.



---

archive/issue_comments_020133.json:
```json
{
    "body": "Not even close:\n\n```\n        sage -t -long devel/sage/sage/rings/polynomial/polynomial_element_generic.py # 4 doctests failed\n        sage -t -long devel/sage/sage/rings/polynomial/polynomial_element.pyx # 4 doctests failed\n        sage -t -long devel/sage/sage/rings/number_field/number_field_element.pyx # 7 doctests failed\n        sage -t -long devel/sage/sage/rings/real_double.pyx # 4 doctests failed\n        sage -t -long devel/sage/sage/rings/power_series_ring_element.pyx # 9 doctests failed\n        sage -t -long devel/sage/sage/rings/number_field/number_field.py # 3 doctests failed\n        sage -t -long devel/sage/sage/rings/complex_double.pyx # 21 doctests failed\n        sage -t -long devel/sage/sage/modules/free_module.py # 2 doctests failed\n        sage -t -long devel/sage/sage/modular/modform/numerical.py # 12 doctests failed\n        sage -t -long devel/sage/sage/plot/plot.py # 8 doctests failed\n        sage -t -long devel/sage/sage/misc/functional.py # 2 doctests failed\n        sage -t -long devel/sage/sage/matrix/matrix_real_double_dense.pyx # 4 doctests failed\n        sage -t -long devel/sage/sage/matrix/matrix_complex_double_dense.pyx # 26 doctests failed\n        sage -t -long devel/sage/sage/matrix/constructor.py # 1 doctests failed\n        sage -t -long devel/sage/sage/matrix/matrix2.pyx # 7 doctests failed\n        sage -t -long devel/sage/sage/interfaces/phc.py # 2 doctests failed\n        sage -t -long devel/sage/sage/functions/orthogonal_polys.py # 1 doctests failed\n        sage -t -long devel/sage/sage/functions/functions.py # 2 doctests failed\n        sage -t -long devel/doc/const/const.tex # 1 doctests failed\n        sage -t -long devel/sage/sage/calculus/calculus.py # 9 doctests failed\n```\n\n\nBack to the drawing board ;)\n\nCheers,\n\nMichael",
    "created_at": "2008-04-15T07:19:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2930",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2930#issuecomment-20133",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Not even close:

```
        sage -t -long devel/sage/sage/rings/polynomial/polynomial_element_generic.py # 4 doctests failed
        sage -t -long devel/sage/sage/rings/polynomial/polynomial_element.pyx # 4 doctests failed
        sage -t -long devel/sage/sage/rings/number_field/number_field_element.pyx # 7 doctests failed
        sage -t -long devel/sage/sage/rings/real_double.pyx # 4 doctests failed
        sage -t -long devel/sage/sage/rings/power_series_ring_element.pyx # 9 doctests failed
        sage -t -long devel/sage/sage/rings/number_field/number_field.py # 3 doctests failed
        sage -t -long devel/sage/sage/rings/complex_double.pyx # 21 doctests failed
        sage -t -long devel/sage/sage/modules/free_module.py # 2 doctests failed
        sage -t -long devel/sage/sage/modular/modform/numerical.py # 12 doctests failed
        sage -t -long devel/sage/sage/plot/plot.py # 8 doctests failed
        sage -t -long devel/sage/sage/misc/functional.py # 2 doctests failed
        sage -t -long devel/sage/sage/matrix/matrix_real_double_dense.pyx # 4 doctests failed
        sage -t -long devel/sage/sage/matrix/matrix_complex_double_dense.pyx # 26 doctests failed
        sage -t -long devel/sage/sage/matrix/constructor.py # 1 doctests failed
        sage -t -long devel/sage/sage/matrix/matrix2.pyx # 7 doctests failed
        sage -t -long devel/sage/sage/interfaces/phc.py # 2 doctests failed
        sage -t -long devel/sage/sage/functions/orthogonal_polys.py # 1 doctests failed
        sage -t -long devel/sage/sage/functions/functions.py # 2 doctests failed
        sage -t -long devel/doc/const/const.tex # 1 doctests failed
        sage -t -long devel/sage/sage/calculus/calculus.py # 9 doctests failed
```


Back to the drawing board ;)

Cheers,

Michael



---

archive/issue_comments_020134.json:
```json
{
    "body": "Changing keywords from \"\" to \"editor_gfurnish\".",
    "created_at": "2008-06-20T04:48:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2930",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2930#issuecomment-20134",
    "user": "https://github.com/craigcitro"
}
```

Changing keywords from "" to "editor_gfurnish".



---

archive/issue_comments_020135.json:
```json
{
    "body": "The idea of generic pools is a good one, but I am pretty sure this implementation has rotted. \n\nRobert: Any take here about doing something generic for pools?\n\nCheers,\n\nMichael",
    "created_at": "2008-11-30T08:16:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2930",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2930#issuecomment-20135",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The idea of generic pools is a good one, but I am pretty sure this implementation has rotted. 

Robert: Any take here about doing something generic for pools?

Cheers,

Michael



---

archive/issue_comments_020136.json:
```json
{
    "body": "Thanks for pinging me. Yes, I've put some thought into making generic pools, just haven't had the time to actually implement anything. \n\nThe ticket is still valid, but I don't think this patch (if it even passed test) is the way to go. \n\n- Robert",
    "created_at": "2008-12-02T12:54:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2930",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2930#issuecomment-20136",
    "user": "https://github.com/robertwb"
}
```

Thanks for pinging me. Yes, I've put some thought into making generic pools, just haven't had the time to actually implement anything. 

The ticket is still valid, but I don't think this patch (if it even passed test) is the way to go. 

- Robert



---

archive/issue_comments_020137.json:
```json
{
    "body": "Replying to [comment:6 robertwb]:\n\nHi,\n\n> Thanks for pinging me. Yes, I've put some thought into making generic pools, just haven't had the time to actually implement anything. \n\n:)\n \n> The ticket is still valid, but I don't think this patch (if it even passed test) is the way to go. \n\nI have created a wish list ticket at #4673 so we have a clean start and something more generic, i.e. the ticket is about creating the infrastructure. Once that is there we can add tickets for the classes that have not been converted. \n\nAs a consequence I am invalidating this ticket.\n\n> - Robert\n\nCheers,\n\nMichael",
    "created_at": "2008-12-02T13:01:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2930",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2930#issuecomment-20137",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Replying to [comment:6 robertwb]:

Hi,

> Thanks for pinging me. Yes, I've put some thought into making generic pools, just haven't had the time to actually implement anything. 

:)
 
> The ticket is still valid, but I don't think this patch (if it even passed test) is the way to go. 

I have created a wish list ticket at #4673 so we have a clean start and something more generic, i.e. the ticket is about creating the infrastructure. Once that is there we can add tickets for the classes that have not been converted. 

As a consequence I am invalidating this ticket.

> - Robert

Cheers,

Michael



---

archive/issue_comments_020138.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2008-12-02T13:01:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2930",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2930#issuecomment-20138",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: invalid



---

archive/issue_events_003132.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-12-02T13:01:00Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2930",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2930#event-3132"
}
```



---

archive/issue_comments_020139.json:
```json
{
    "body": "Sounds good to me.",
    "created_at": "2008-12-02T19:48:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2930",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2930#issuecomment-20139",
    "user": "https://github.com/robertwb"
}
```

Sounds good to me.
