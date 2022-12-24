# Issue 6737: change occurrences of "Pyrex" to "Cython"

archive/issues_006737.json:
```json
{
    "body": "Assignee: tba\n\nAll occurrences of \"Pyrex\" should now be changed to \"Cython\". See this [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/b9b7eea2d9575a7f) thread for some background information.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6737\n\n",
    "created_at": "2009-08-11T20:04:35Z",
    "labels": [
        "documentation",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "change occurrences of \"Pyrex\" to \"Cython\"",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6737",
    "user": "mvngu"
}
```
Assignee: tba

All occurrences of "Pyrex" should now be changed to "Cython". See this [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/b9b7eea2d9575a7f) thread for some background information.

Issue created by migration from https://trac.sagemath.org/ticket/6737





---

archive/issue_comments_055213.json:
```json
{
    "body": "\n```\nsage: search_src('pyrex')\nmatrix/matrix_modn_sparse.pyx:7:TODO: - move vectors into a pyrex vector class - add _add_ and\nserver/notebook/worksheet.py:3800:        elif system in ['cython', 'pyrex', 'sagex']:\ncombinat/expnums.pyx:126:    A vanilla python (but compiled via pyrex) implementation of\ncombinat/matrices/dancing_links.pyx:106:        # It is the *trick* needed to pickle pyrex extension types.\nrings/complex_interval.pyx:12:    -- Joel B. Mohler (2006-12-16): naive rewrite into pyrex\nrings/ring.pyx:1040:            #except AttributeError:   # for pyrex classes\nrings/rational.pyx:3172:def pyrex_rational_reconstruction(integer.Integer a, integer.Integer m):\nrings/rational.pyx:3194:        sage: sage.rings.rational.pyrex_rational_reconstruction(34, 100)\nrings/integer.pyx:596:                    # pyrex to play games with refcount for the None object, which\nrings/integer.pyx:622:                # we could skip the double lookup. Unfortunately pyrex doesn't\nrings/integer.pyx:670:        # It is the *trick* needed to pickle pyrex extension types.\nrings/integer.pyx:2616:        return rational.pyrex_rational_reconstruction(self, m)\nrings/complex_number.pyx:8:- Joel B. Mohler (2006-12-16): naive rewrite into pyrex\nrings/polynomial/polynomial_compiled.pyx:24:    pyrex.\ngraphs/generic_graph_pyx.pyx:74:    This kind of speed cannot be achieved by naive pyrexification of the\nmisc/all.py:74:pyrex = cython # synonym -- for now\ngsl/all.py:2:# http://wwwteor.mi.infn.it/%7Epernici/pyrexgsl/pyrexgsl.html\n```\n",
    "created_at": "2010-01-18T04:13:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6737",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6737#issuecomment-55213",
    "user": "@williamstein"
}
```


```
sage: search_src('pyrex')
matrix/matrix_modn_sparse.pyx:7:TODO: - move vectors into a pyrex vector class - add _add_ and
server/notebook/worksheet.py:3800:        elif system in ['cython', 'pyrex', 'sagex']:
combinat/expnums.pyx:126:    A vanilla python (but compiled via pyrex) implementation of
combinat/matrices/dancing_links.pyx:106:        # It is the *trick* needed to pickle pyrex extension types.
rings/complex_interval.pyx:12:    -- Joel B. Mohler (2006-12-16): naive rewrite into pyrex
rings/ring.pyx:1040:            #except AttributeError:   # for pyrex classes
rings/rational.pyx:3172:def pyrex_rational_reconstruction(integer.Integer a, integer.Integer m):
rings/rational.pyx:3194:        sage: sage.rings.rational.pyrex_rational_reconstruction(34, 100)
rings/integer.pyx:596:                    # pyrex to play games with refcount for the None object, which
rings/integer.pyx:622:                # we could skip the double lookup. Unfortunately pyrex doesn't
rings/integer.pyx:670:        # It is the *trick* needed to pickle pyrex extension types.
rings/integer.pyx:2616:        return rational.pyrex_rational_reconstruction(self, m)
rings/complex_number.pyx:8:- Joel B. Mohler (2006-12-16): naive rewrite into pyrex
rings/polynomial/polynomial_compiled.pyx:24:    pyrex.
graphs/generic_graph_pyx.pyx:74:    This kind of speed cannot be achieved by naive pyrexification of the
misc/all.py:74:pyrex = cython # synonym -- for now
gsl/all.py:2:# http://wwwteor.mi.infn.it/%7Epernici/pyrexgsl/pyrexgsl.html
```




---

archive/issue_comments_055214.json:
```json
{
    "body": "Removes Pyrex",
    "created_at": "2010-01-18T06:19:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6737",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6737#issuecomment-55214",
    "user": "gaer"
}
```

Removes Pyrex



---

archive/issue_comments_055215.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-18T06:24:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6737",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6737#issuecomment-55215",
    "user": "gaer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_055216.json:
```json
{
    "body": "Attachment [13638.patch](tarball://root/attachments/some-uuid/ticket6737/13638.patch) by gaer created at 2010-01-18 06:24:29",
    "created_at": "2010-01-18T06:24:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6737",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6737#issuecomment-55216",
    "user": "gaer"
}
```

Attachment [13638.patch](tarball://root/attachments/some-uuid/ticket6737/13638.patch) by gaer created at 2010-01-18 06:24:29



---

archive/issue_comments_055217.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-18T06:25:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6737",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6737#issuecomment-55217",
    "user": "@williamstein"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_055218.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-01-18T23:46:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6737",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6737#issuecomment-55218",
    "user": "@rlmill"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_055219.json:
```json
{
    "body": "rebased, apply only this patch",
    "created_at": "2010-01-19T00:15:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6737",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6737#issuecomment-55219",
    "user": "@rlmill"
}
```

rebased, apply only this patch



---

archive/issue_comments_055220.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-19T00:26:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6737",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6737#issuecomment-55220",
    "user": "@rlmill"
}
```

Resolution: fixed



---

archive/issue_comments_055221.json:
```json
{
    "body": "Attachment [trac_6737.patch](tarball://root/attachments/some-uuid/ticket6737/trac_6737.patch) by @rlmill created at 2010-01-19 00:26:13",
    "created_at": "2010-01-19T00:26:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6737",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6737#issuecomment-55221",
    "user": "@rlmill"
}
```

Attachment [trac_6737.patch](tarball://root/attachments/some-uuid/ticket6737/trac_6737.patch) by @rlmill created at 2010-01-19 00:26:13
