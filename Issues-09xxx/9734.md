# Issue 9734: METATICKET Doc test failures on 32-bit Solaris 10 and 32-bit OpenSolaris on x86 CPUs.

archive/issues_009734.json:
```json
{
    "body": "Assignee: drkirkby\n\nCC:  @jaapspies @jhpalmieri\n\nAlthough the 32-bit SPARC version of Sage passes all doc tests, there are still issues on 32-bit versions of Solaris/OpenSolaris on x86 hardware. This ticket summaries lists only failures on 32-bit builds, versions on x86 processors. \n\n64-bit versions have far more failures, and will need another ticket to address them. \n\n|        |              |                |         |\n|--------|--------------|----------------|---------|\n|**Test**|**Solaris 10**| **OpenSolaris**|**Notes**|\n|`doc/en/tutorial/tour_advanced.rs`|Passed|#9736|gfan|\n|`doc/rf/tutorial/tour_advanced.rs`|Passed|#9736|gfan|\n|`sage/lfunctions/sympow.py`|#9703|#9703|SYMPOW is also busted on Cygwin & ArchLinux (see #9166)|\n|`sage/modular/hecke/submodule.py`|#9703|#9703|SYMPOW|\n|`sage/modular/abvar/abvar.p`|#9703|#9703|SYMPOW|\n|`sage/rings/polynomial/groebner_fan.py`|Passed|#9736|Gfan|\n|`sage/schemes/elliptic_curves/ell_rational_field.py`|#9703|#9703|SYMPOW|\n|`sage/rings/polynomial/multi_polynomial_ideal.py`|Passed|#9736|Gfan|\n|`sage/symbolic/expression.pyx`|#9689+#9693|#9689+#9693|numerical noise and missing zero|\n|`sage/stats/hmm/chmm.pyx`|#9735|#9735|numerical noise. **Positive review**|\nAt this early stage of the 32-bit ports to Solaris 10 and OpenSolaris on x86 processors, it would appear the problems fall into 3 areas\n\n* Numerical noise. \n* [SYMPOW](http://www.sagemath.org/doc/reference/sage/lfunctions/sympow.html) on both Solaris 10 and OpenSolaris.\n* [Gfan](http://www.math.tu-berlin.de/~jensen/software/gfan/gfan.html) - only on OpenSolaris. \n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9734\n\n",
    "closed_at": "2015-09-12T13:58:43Z",
    "created_at": "2010-08-12T16:09:46Z",
    "labels": [
        "component: porting: solaris",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "METATICKET Doc test failures on 32-bit Solaris 10 and 32-bit OpenSolaris on x86 CPUs.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9734",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: drkirkby

CC:  @jaapspies @jhpalmieri

Although the 32-bit SPARC version of Sage passes all doc tests, there are still issues on 32-bit versions of Solaris/OpenSolaris on x86 hardware. This ticket summaries lists only failures on 32-bit builds, versions on x86 processors. 

64-bit versions have far more failures, and will need another ticket to address them. 

|        |              |                |         |
|--------|--------------|----------------|---------|
|**Test**|**Solaris 10**| **OpenSolaris**|**Notes**|
|`doc/en/tutorial/tour_advanced.rs`|Passed|#9736|gfan|
|`doc/rf/tutorial/tour_advanced.rs`|Passed|#9736|gfan|
|`sage/lfunctions/sympow.py`|#9703|#9703|SYMPOW is also busted on Cygwin & ArchLinux (see #9166)|
|`sage/modular/hecke/submodule.py`|#9703|#9703|SYMPOW|
|`sage/modular/abvar/abvar.p`|#9703|#9703|SYMPOW|
|`sage/rings/polynomial/groebner_fan.py`|Passed|#9736|Gfan|
|`sage/schemes/elliptic_curves/ell_rational_field.py`|#9703|#9703|SYMPOW|
|`sage/rings/polynomial/multi_polynomial_ideal.py`|Passed|#9736|Gfan|
|`sage/symbolic/expression.pyx`|#9689+#9693|#9689+#9693|numerical noise and missing zero|
|`sage/stats/hmm/chmm.pyx`|#9735|#9735|numerical noise. **Positive review**|
At this early stage of the 32-bit ports to Solaris 10 and OpenSolaris on x86 processors, it would appear the problems fall into 3 areas

* Numerical noise. 
* [SYMPOW](http://www.sagemath.org/doc/reference/sage/lfunctions/sympow.html) on both Solaris 10 and OpenSolaris.
* [Gfan](http://www.math.tu-berlin.de/~jensen/software/gfan/gfan.html) - only on OpenSolaris. 



Issue created by migration from https://trac.sagemath.org/ticket/9734





---

archive/issue_events_024364.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/drkirkby",
    "created_at": "2010-08-12T18:18:24Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9734",
    "milestone": "sage-4.5.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9734#event-24364"
}
```



---

archive/issue_comments_095028.json:
```json
{
    "body": "I discovered the GFAN issues were a mistake on my part, so #9736 was closed as invalid, and those doctest failures can be ignored. \n\nDave",
    "created_at": "2010-08-15T23:50:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9734",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9734#issuecomment-95028",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

I discovered the GFAN issues were a mistake on my part, so #9736 was closed as invalid, and those doctest failures can be ignored. 

Dave



---

archive/issue_events_024365.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9734",
    "milestone": "sage-4.5.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9734#event-24365"
}
```



---

archive/issue_events_024366.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9734",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9734#event-24366"
}
```



---

archive/issue_events_024367.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9734",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9734#event-24367"
}
```



---

archive/issue_events_024368.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9734",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9734#event-24368"
}
```



---

archive/issue_events_024369.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9734",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9734#event-24369"
}
```



---

archive/issue_events_024370.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9734",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9734#event-24370"
}
```



---

archive/issue_events_024371.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9734",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9734#event-24371"
}
```



---

archive/issue_events_024372.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9734",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9734#event-24372"
}
```



---

archive/issue_events_024373.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2015-09-07T06:11:56Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9734",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9734#event-24373"
}
```



---

archive/issue_events_024374.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2015-09-07T06:11:56Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9734",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9734#event-24374"
}
```



---

archive/issue_comments_095029.json:
```json
{
    "body": "All linked tickets are closed, so I guess we can close this.",
    "created_at": "2015-09-07T06:11:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9734",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9734#issuecomment-95029",
    "user": "https://github.com/jdemeyer"
}
```

All linked tickets are closed, so I guess we can close this.



---

archive/issue_comments_095030.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2015-09-07T06:11:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9734",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9734#issuecomment-95030",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_095031.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2015-09-07T06:12:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9734",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9734#issuecomment-95031",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_024375.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2015-09-12T13:58:43Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9734",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9734#event-24375"
}
```



---

archive/issue_comments_095032.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2015-09-12T13:58:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9734",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9734#issuecomment-95032",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed
