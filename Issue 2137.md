# Issue 2137: implement loading of pyx files when loading .sage files (probably relatively easy; in sage/misc/*)

archive/issues_002137.json:
```json
{
    "body": "Assignee: was\n\nCC:  mvngu\n\n\n```\n\n\nOn Feb 9, 2008 7:58 PM, mb <bestvina@gmail.com> wrote:\n> \n> Hello,\n> \n> I have a basic question about using pyrex from a sage script. Suppose\n> I have a file \"test.pyx\":\n> \n> def f(int n):\n>         return n\n> \n> Then from the sage interpreter I can use it:\n> \n> sage: load \"test.pyx\"\n> Compiling test.pyx...\n> sage: f(3)\n> 3\n> \n> But I'd like to use it from a script, e.g. \"main.sage\":\n> \n> load \"test.pyx\"\n> print f(3)\n> \n> Then I get:\n> \n> mb@hvar:~$ sage main.sage\n> Traceback (most recent call last):\n>   File \"main.py\", line 4, in <module>\n>     print f(Integer(3))\n> NameError: name 'f' is not defined\n> \n> I tried modifying test.pyx by inserting the word \"public\" after \"def\"\n> but it didn't help. Is there any way of doing this?\n\nThis is not implemented yet, though it will be implemented.   \nThere is a partial workaround that might be enough for you now.\n\n(1) Create test.pyx and main.sage as follows:\nteragon:tmp was$ more test.pyx\ndef f(int n):\n    return n\nteragon:tmp was$ more main.sage\nprint f(3)\n\n(2) You can use main.sage if you do the following:\nsage: load test.pyx\nCompiling test.pyx...\nsage: load main.sage\n3\n\nWilliam\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2137\n\n",
    "created_at": "2008-02-10T06:38:47Z",
    "labels": [
        "user interface",
        "major",
        "bug"
    ],
    "title": "implement loading of pyx files when loading .sage files (probably relatively easy; in sage/misc/*)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2137",
    "user": "was"
}
```
Assignee: was

CC:  mvngu


```


On Feb 9, 2008 7:58 PM, mb <bestvina@gmail.com> wrote:
> 
> Hello,
> 
> I have a basic question about using pyrex from a sage script. Suppose
> I have a file "test.pyx":
> 
> def f(int n):
>         return n
> 
> Then from the sage interpreter I can use it:
> 
> sage: load "test.pyx"
> Compiling test.pyx...
> sage: f(3)
> 3
> 
> But I'd like to use it from a script, e.g. "main.sage":
> 
> load "test.pyx"
> print f(3)
> 
> Then I get:
> 
> mb@hvar:~$ sage main.sage
> Traceback (most recent call last):
>   File "main.py", line 4, in <module>
>     print f(Integer(3))
> NameError: name 'f' is not defined
> 
> I tried modifying test.pyx by inserting the word "public" after "def"
> but it didn't help. Is there any way of doing this?

This is not implemented yet, though it will be implemented.   
There is a partial workaround that might be enough for you now.

(1) Create test.pyx and main.sage as follows:
teragon:tmp was$ more test.pyx
def f(int n):
    return n
teragon:tmp was$ more main.sage
print f(3)

(2) You can use main.sage if you do the following:
sage: load test.pyx
Compiling test.pyx...
sage: load main.sage
3

William
```


Issue created by migration from https://trac.sagemath.org/ticket/2137





---

archive/issue_comments_014015.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2009-01-23T07:10:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2137",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2137#issuecomment-14015",
    "user": "AlexGhitza"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_014016.json:
```json
{
    "body": "I think this is fixed, since the example in the description works for me:\n\n```sh\n$ sage main.sage \nCompiling test.pyx...\n3\n```\n\n\nShould we close this ticket?",
    "created_at": "2010-02-14T20:00:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2137",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2137#issuecomment-14016",
    "user": "mpatel"
}
```

I think this is fixed, since the example in the description works for me:

```sh
$ sage main.sage 
Compiling test.pyx...
3
```


Should we close this ticket?



---

archive/issue_comments_014017.json:
```json
{
    "body": "Changing status from new to needs_info.",
    "created_at": "2010-02-14T20:00:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2137",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2137#issuecomment-14017",
    "user": "mpatel"
}
```

Changing status from new to needs_info.



---

archive/issue_comments_014018.json:
```json
{
    "body": "Closing this ticket as fixed:\n\n```\n[mvngu@sage sage-4.3.3.alpha0]$ cat test.pyx\ndef f(int n):\n    return n\n[mvngu@sage sage-4.3.3.alpha0]$ cat main.sage\nload(\"test.pyx\")\nprint f(3)\n[mvngu@sage sage-4.3.3.alpha0]$ ./sage -version\n* Warning: this is a prerelease version, and it may be unstable.     *\n[mvngu@sage sage-4.3.3.alpha0]$ ./sage main.sage\nCompiling test.pyx...\n3\n```\n",
    "created_at": "2010-02-15T06:50:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2137",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2137#issuecomment-14018",
    "user": "mvngu"
}
```

Closing this ticket as fixed:

```
[mvngu@sage sage-4.3.3.alpha0]$ cat test.pyx
def f(int n):
    return n
[mvngu@sage sage-4.3.3.alpha0]$ cat main.sage
load("test.pyx")
print f(3)
[mvngu@sage sage-4.3.3.alpha0]$ ./sage -version
* Warning: this is a prerelease version, and it may be unstable.     *
[mvngu@sage sage-4.3.3.alpha0]$ ./sage main.sage
Compiling test.pyx...
3
```




---

archive/issue_comments_014019.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-02-15T06:50:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2137",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2137#issuecomment-14019",
    "user": "mvngu"
}
```

Resolution: fixed
