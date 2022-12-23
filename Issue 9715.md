# Issue 9715: Failing doctest in even_hole_free

archive/issues_009715.json:
```json
{
    "body": "Assignee: jason, ncohen, rlm\n\nCC:  dkirkby jason mpatel\n\nAs reported on :\n\nhttp://groups.google.com/group/sage-release/browse_thread/thread/fa2facb36603675a\n\nThe only random part being the graph generation, it shouldn't be hard to find a workaround....\n\n\n```\n>> sage -t  devel/sage-main/sage/graphs/graph.py\n>> **********************************************************************\n>> File \"/Volumes/E/sage-4.5.2.rc0/devel/sage-main/sage/graphs/graph.py\",\n>> line 1347:\n>>     sage: cycle.order() % 2 == 0\n>> Exception raised:\n>>     Traceback (most recent call last):\n>>       File \"/Volumes/E/sage-4.5.2.rc0/local/bin/ncadoctest.py\", line\n>> 1231, in run_one_test\n>>         self.run_one_example(test, example, filename, compileflags)\n>>       File \"/Volumes/E/sage-4.5.2.rc0/local/bin/sagedoctest.py\", line\n>> 38, in run_one_example\n>>         OrigDocTestRunner.run_one_example(self, test, example,\n>> filename, compileflags)\n>>       File \"/Volumes/E/sage-4.5.2.rc0/local/bin/ncadoctest.py\", line\n>> 1172, in run_one_example\n>>         compileflags, 1) in test.globs\n>>       File \"<doctest __main__.example_6[9]>\", line 1, in <module>\n>>         cycle.order() % Integer(2) == Integer(0)###line 1347:\n>>     sage: cycle.order() % 2 == 0\n>>     AttributeError: 'bool' object has no attribute 'order' \n```\n\n\nNathann\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9715\n\n",
    "created_at": "2010-08-10T03:37:28Z",
    "labels": [
        "graph theory",
        "major",
        "bug"
    ],
    "title": "Failing doctest in even_hole_free",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9715",
    "user": "ncohen"
}
```
Assignee: jason, ncohen, rlm

CC:  dkirkby jason mpatel

As reported on :

http://groups.google.com/group/sage-release/browse_thread/thread/fa2facb36603675a

The only random part being the graph generation, it shouldn't be hard to find a workaround....


```
>> sage -t  devel/sage-main/sage/graphs/graph.py
>> **********************************************************************
>> File "/Volumes/E/sage-4.5.2.rc0/devel/sage-main/sage/graphs/graph.py",
>> line 1347:
>>     sage: cycle.order() % 2 == 0
>> Exception raised:
>>     Traceback (most recent call last):
>>       File "/Volumes/E/sage-4.5.2.rc0/local/bin/ncadoctest.py", line
>> 1231, in run_one_test
>>         self.run_one_example(test, example, filename, compileflags)
>>       File "/Volumes/E/sage-4.5.2.rc0/local/bin/sagedoctest.py", line
>> 38, in run_one_example
>>         OrigDocTestRunner.run_one_example(self, test, example,
>> filename, compileflags)
>>       File "/Volumes/E/sage-4.5.2.rc0/local/bin/ncadoctest.py", line
>> 1172, in run_one_example
>>         compileflags, 1) in test.globs
>>       File "<doctest __main__.example_6[9]>", line 1, in <module>
>>         cycle.order() % Integer(2) == Integer(0)###line 1347:
>>     sage: cycle.order() % 2 == 0
>>     AttributeError: 'bool' object has no attribute 'order' 
```


Nathann


Issue created by migration from https://trac.sagemath.org/ticket/9715





---

archive/issue_comments_094789.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-08-10T04:10:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9715",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9715#issuecomment-94789",
    "user": "ncohen"
}
```

Attachment



---

archive/issue_comments_094790.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-08-10T04:15:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9715",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9715#issuecomment-94790",
    "user": "ncohen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_094791.json:
```json
{
    "body": "With this, the docstring does not depend on any -- possibly rare -- probabilistic event. Good to know that the docstrings reports errors that do not appear on 100 000 trials though. `:-D`\n\nNathann",
    "created_at": "2010-08-10T04:15:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9715",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9715#issuecomment-94791",
    "user": "ncohen"
}
```

With this, the docstring does not depend on any -- possibly rare -- probabilistic event. Good to know that the docstrings reports errors that do not appear on 100 000 trials though. `:-D`

Nathann



---

archive/issue_comments_094792.json:
```json
{
    "body": "This ticket is now invalid because of #10081 and #9422\n\nNathann",
    "created_at": "2010-10-19T14:41:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9715",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9715#issuecomment-94792",
    "user": "ncohen"
}
```

This ticket is now invalid because of #10081 and #9422

Nathann



---

archive/issue_comments_094793.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2010-10-19T21:54:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9715",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9715#issuecomment-94793",
    "user": "mpatel"
}
```

Resolution: duplicate



---

archive/issue_comments_094794.json:
```json
{
    "body": "Replying to [comment:2 ncohen]:\n> This ticket is now invalid because of #10081 and #9422\n\nAlso related: #9925.",
    "created_at": "2010-10-19T21:54:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9715",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9715#issuecomment-94794",
    "user": "mpatel"
}
```

Replying to [comment:2 ncohen]:
> This ticket is now invalid because of #10081 and #9422

Also related: #9925.
