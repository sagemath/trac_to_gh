# Issue 7636: add decorator to make functions symbolic

archive/issues_007636.json:
```json
{
    "body": "Assignee: burcin\n\nCC:  kcrisman\n\nWe should make a decorator that converts a Python function to a symbolic function, similar to those created by `sage.symbolic.function_factory.function`.\n\nExample:\n\n\n```\n@sage.symbolic.function.symbolic\ndef my_func(x, n):\n     if x < 0: return 0\n     else: return exp(-1/x^n)\n```\n\n\nsage-devel thread:\n\nhttp://groups.google.com/group/sage-devel/browse_thread/thread/902cf2ae1a06cf6e\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7636\n\n",
    "created_at": "2009-12-09T10:19:40Z",
    "labels": [
        "symbolics",
        "major",
        "enhancement"
    ],
    "title": "add decorator to make functions symbolic",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7636",
    "user": "burcin"
}
```
Assignee: burcin

CC:  kcrisman

We should make a decorator that converts a Python function to a symbolic function, similar to those created by `sage.symbolic.function_factory.function`.

Example:


```
@sage.symbolic.function.symbolic
def my_func(x, n):
     if x < 0: return 0
     else: return exp(-1/x^n)
```


sage-devel thread:

http://groups.google.com/group/sage-devel/browse_thread/thread/902cf2ae1a06cf6e


Issue created by migration from https://trac.sagemath.org/ticket/7636


