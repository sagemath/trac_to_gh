# Issue 9447: "except:" count in sage too high

archive/issues_009447.json:
```json
{
    "body": "Assignee: @aghitza\n\nsage: len(search_src(\"except:\",interact=False).splitlines())\n312\n\n\nThis number should be much lower.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9447\n\n",
    "created_at": "2010-07-07T09:48:31Z",
    "labels": [
        "component: algebra",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "\"except:\" count in sage too high",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9447",
    "user": "https://trac.sagemath.org/admin/accounts/users/wjlaffin"
}
```
Assignee: @aghitza

sage: len(search_src("except:",interact=False).splitlines())
312


This number should be much lower.

Issue created by migration from https://trac.sagemath.org/ticket/9447





---

archive/issue_comments_090382.json:
```json
{
    "body": "Changing assignee from @aghitza to @jasongrout.",
    "created_at": "2010-07-07T10:04:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9447",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9447#issuecomment-90382",
    "user": "https://trac.sagemath.org/admin/accounts/users/wjlaffin"
}
```

Changing assignee from @aghitza to @jasongrout.



---

archive/issue_comments_090383.json:
```json
{
    "body": "Changing component from algebra to misc.",
    "created_at": "2010-07-07T10:04:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9447",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9447#issuecomment-90383",
    "user": "https://trac.sagemath.org/admin/accounts/users/wjlaffin"
}
```

Changing component from algebra to misc.



---

archive/issue_comments_090384.json:
```json
{
    "body": "These all seem to be gone in `5.9.beta1`:\n\n```\ntravis@travis-virtualbox:~/sage-5.9.beta1/devel/sage-main/sage$ grep -R \"except:\" .\n./numerical/backends/glpk_backend.cpp:            /*except:*/ {\n./structure/list_clone_timings_cy.c:        /*except:*/ {\n./plot/plot3d/bugs.txt:        except:       # TODO -- this would catch control-C,etc. -- FIX THIS TO CATCH WHAT IS RAISED!!!!\n./libs/singular/function.cpp:        /*except:*/ {\n\nsage: len(search_src(\"except:\",interact=False).splitlines())\n0\n```\n",
    "created_at": "2013-04-01T19:53:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9447",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9447#issuecomment-90384",
    "user": "https://github.com/tscrim"
}
```

These all seem to be gone in `5.9.beta1`:

```
travis@travis-virtualbox:~/sage-5.9.beta1/devel/sage-main/sage$ grep -R "except:" .
./numerical/backends/glpk_backend.cpp:            /*except:*/ {
./structure/list_clone_timings_cy.c:        /*except:*/ {
./plot/plot3d/bugs.txt:        except:       # TODO -- this would catch control-C,etc. -- FIX THIS TO CATCH WHAT IS RAISED!!!!
./libs/singular/function.cpp:        /*except:*/ {

sage: len(search_src("except:",interact=False).splitlines())
0
```




---

archive/issue_comments_090385.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2013-04-01T19:53:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9447",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9447#issuecomment-90385",
    "user": "https://github.com/tscrim"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_090386.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-04-02T06:12:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9447",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9447#issuecomment-90386",
    "user": "https://github.com/novoselt"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_009604.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-04-03T15:12:26Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9447",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9447#event-9604"
}
```



---

archive/issue_comments_090387.json:
```json
{
    "body": "Resolution: worksforme",
    "created_at": "2013-04-03T15:12:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9447",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9447#issuecomment-90387",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: worksforme
