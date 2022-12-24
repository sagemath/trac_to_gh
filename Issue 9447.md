# Issue 9447: "except:" count in sage too high

archive/issues_009447.json:
```json
{
    "body": "Assignee: AlexGhitza\n\nsage: len(search_src(\"except:\",interact=False).splitlines())\n312\n\n\nThis number should be much lower.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9447\n\n",
    "created_at": "2010-07-07T09:48:31Z",
    "labels": [
        "algebra",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "\"except:\" count in sage too high",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9447",
    "user": "wjlaffin"
}
```
Assignee: AlexGhitza

sage: len(search_src("except:",interact=False).splitlines())
312


This number should be much lower.

Issue created by migration from https://trac.sagemath.org/ticket/9447





---

archive/issue_comments_090530.json:
```json
{
    "body": "Changing assignee from AlexGhitza to jason.",
    "created_at": "2010-07-07T10:04:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9447",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9447#issuecomment-90530",
    "user": "wjlaffin"
}
```

Changing assignee from AlexGhitza to jason.



---

archive/issue_comments_090531.json:
```json
{
    "body": "Changing component from algebra to misc.",
    "created_at": "2010-07-07T10:04:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9447",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9447#issuecomment-90531",
    "user": "wjlaffin"
}
```

Changing component from algebra to misc.



---

archive/issue_comments_090532.json:
```json
{
    "body": "These all seem to be gone in `5.9.beta1`:\n\n```\ntravis@travis-virtualbox:~/sage-5.9.beta1/devel/sage-main/sage$ grep -R \"except:\" .\n./numerical/backends/glpk_backend.cpp:            /*except:*/ {\n./structure/list_clone_timings_cy.c:        /*except:*/ {\n./plot/plot3d/bugs.txt:        except:       # TODO -- this would catch control-C,etc. -- FIX THIS TO CATCH WHAT IS RAISED!!!!\n./libs/singular/function.cpp:        /*except:*/ {\n\nsage: len(search_src(\"except:\",interact=False).splitlines())\n0\n```\n",
    "created_at": "2013-04-01T19:53:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9447",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9447#issuecomment-90532",
    "user": "tscrim"
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

archive/issue_comments_090533.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2013-04-01T19:53:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9447",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9447#issuecomment-90533",
    "user": "tscrim"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_090534.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-04-02T06:12:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9447",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9447#issuecomment-90534",
    "user": "novoselt"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_090535.json:
```json
{
    "body": "Resolution: worksforme",
    "created_at": "2013-04-03T15:12:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9447",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9447#issuecomment-90535",
    "user": "jdemeyer"
}
```

Resolution: worksforme
