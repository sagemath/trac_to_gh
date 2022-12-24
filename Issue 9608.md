# Issue 9608: Docbuild warnings in sage/interfaces/matlab.py

archive/issues_009608.json:
```json
{
    "body": "Assignee: mvngu\n\nCC:  @dandrake @mwhansen rossk @nexttime\n\nDocbuild warnings in Sage 4.5.2.alpha1:\n\n```sh\n$ ./sage -docbuild all html -j\n[...]\n/mnt/usb1/scratch/mpatel/tmp/sage-4.5.2.alpha1/local/lib/python2.6/site-packages/sage/interfaces/matlab.py:docstring of sage.interfaces.matlab.Matlab.strip_answer:6: (WARNING/2) Block quote ends without a blank line; unexpected unindent.\n/mnt/usb1/scratch/mpatel/tmp/sage-4.5.2.alpha1/local/lib/python2.6/site-packages/sage/interfaces/matlab.py:docstring of sage.interfaces.matlab.Matlab.strip_answer:9: (WARNING/2) Block quote ends without a blank line; unexpected unindent.\n[...]\n```\n\n\nPossibly related ticket: #2119.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9608\n\n",
    "created_at": "2010-07-27T07:08:40Z",
    "labels": [
        "documentation",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.2",
    "title": "Docbuild warnings in sage/interfaces/matlab.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9608",
    "user": "@qed777"
}
```
Assignee: mvngu

CC:  @dandrake @mwhansen rossk @nexttime

Docbuild warnings in Sage 4.5.2.alpha1:

```sh
$ ./sage -docbuild all html -j
[...]
/mnt/usb1/scratch/mpatel/tmp/sage-4.5.2.alpha1/local/lib/python2.6/site-packages/sage/interfaces/matlab.py:docstring of sage.interfaces.matlab.Matlab.strip_answer:6: (WARNING/2) Block quote ends without a blank line; unexpected unindent.
/mnt/usb1/scratch/mpatel/tmp/sage-4.5.2.alpha1/local/lib/python2.6/site-packages/sage/interfaces/matlab.py:docstring of sage.interfaces.matlab.Matlab.strip_answer:9: (WARNING/2) Block quote ends without a blank line; unexpected unindent.
[...]
```


Possibly related ticket: #2119.

Issue created by migration from https://trac.sagemath.org/ticket/9608





---

archive/issue_comments_093073.json:
```json
{
    "body": "Attachment [trac_9608-matlab_docbuild.patch](tarball://root/attachments/some-uuid/ticket9608/trac_9608-matlab_docbuild.patch) by @qed777 created at 2010-07-27 07:55:33\n\nMake the docstring raw",
    "created_at": "2010-07-27T07:55:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9608",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9608#issuecomment-93073",
    "user": "@qed777"
}
```

Attachment [trac_9608-matlab_docbuild.patch](tarball://root/attachments/some-uuid/ticket9608/trac_9608-matlab_docbuild.patch) by @qed777 created at 2010-07-27 07:55:33

Make the docstring raw



---

archive/issue_comments_093074.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-07-27T07:55:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9608",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9608#issuecomment-93074",
    "user": "@qed777"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_093075.json:
```json
{
    "body": "A one-character patch! Nice.\n\nIt does get rid of the warning for me, but I'd like to understand why the docstring needs to be raw. How does that fix the unindent warning?",
    "created_at": "2010-07-27T08:23:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9608",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9608#issuecomment-93075",
    "user": "@dandrake"
}
```

A one-character patch! Nice.

It does get rid of the warning for me, but I'd like to understand why the docstring needs to be raw. How does that fix the unindent warning?



---

archive/issue_comments_093076.json:
```json
{
    "body": "I think the problem with the original docstring is that the backslashes are not escaped, so perhaps Sphinx interprets the `\\n`s as newline characters and sees\n\n```python\n        \"\"\"                                                                     \n        Returns the string s with Matlab's answer prompt removed.               \n                                                                                \n        EXAMPLES::                                                              \n                                                                                \n            sage: s = '                                                         \nans =                                                                           \n                                                                                \n     2                                                                          \n'                                                                               \n            sage: matlab.strip_answer(s)                                        \n            '     2'                                                            \n        \"\"\"\n```\n\nNot using a raw string but replacing the `\\n`s with `\\\\n`s should also work.",
    "created_at": "2010-07-27T08:44:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9608",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9608#issuecomment-93076",
    "user": "@qed777"
}
```

I think the problem with the original docstring is that the backslashes are not escaped, so perhaps Sphinx interprets the `\n`s as newline characters and sees

```python
        """                                                                     
        Returns the string s with Matlab's answer prompt removed.               
                                                                                
        EXAMPLES::                                                              
                                                                                
            sage: s = '                                                         
ans =                                                                           
                                                                                
     2                                                                          
'                                                                               
            sage: matlab.strip_answer(s)                                        
            '     2'                                                            
        """
```

Not using a raw string but replacing the `\n`s with `\\n`s should also work.



---

archive/issue_comments_093077.json:
```json
{
    "body": "Replying to [comment:3 mpatel]:\n> Not using a raw string but replacing the `\\n`s with `\\\\n`s should also work.\n\nHrm, doing that doesn't fix the problem -- the function then gets a string with no newlines, but with literal \"\\n\" bits.\n\nI'm almost certain that making the docstring raw is the right thing to do, but I'd like to have someone who knows more about doctesting and Sphinx look at this.",
    "created_at": "2010-07-28T01:13:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9608",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9608#issuecomment-93077",
    "user": "@dandrake"
}
```

Replying to [comment:3 mpatel]:
> Not using a raw string but replacing the `\n`s with `\\n`s should also work.

Hrm, doing that doesn't fix the problem -- the function then gets a string with no newlines, but with literal "\n" bits.

I'm almost certain that making the docstring raw is the right thing to do, but I'd like to have someone who knows more about doctesting and Sphinx look at this.



---

archive/issue_comments_093078.json:
```json
{
    "body": "> Hrm, doing that doesn't fix the problem -- the function then gets a string with no newlines, but with literal \"\\n\" bits.\n\nIsn't that what you want?  You're defining s to be a particular string, one containing \"\\n\" in it (to give a newline), and you want each \"\\n\" to appear as such in the reference manual.  That is,  `s = '\\nans =\\n\\n     2\\n'` is a valid way to define a python string, and it should appear this way in the reference manual.  If you want to define a string containing actual new lines, you would have to use triple quotes, wouldn't you?\n\nThis makes sense to me, and I've seen other docstring errors and fixes just like this in the past.  The particular docstring here looks much better after the patch, and there are no warnings.  Positive review.",
    "created_at": "2010-07-28T05:40:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9608",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9608#issuecomment-93078",
    "user": "@jhpalmieri"
}
```

> Hrm, doing that doesn't fix the problem -- the function then gets a string with no newlines, but with literal "\n" bits.

Isn't that what you want?  You're defining s to be a particular string, one containing "\n" in it (to give a newline), and you want each "\n" to appear as such in the reference manual.  That is,  `s = '\nans =\n\n     2\n'` is a valid way to define a python string, and it should appear this way in the reference manual.  If you want to define a string containing actual new lines, you would have to use triple quotes, wouldn't you?

This makes sense to me, and I've seen other docstring errors and fixes just like this in the past.  The particular docstring here looks much better after the patch, and there are no warnings.  Positive review.



---

archive/issue_comments_093079.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-28T05:40:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9608",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9608#issuecomment-93079",
    "user": "@jhpalmieri"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_093080.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-29T04:50:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9608",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9608#issuecomment-93080",
    "user": "@qed777"
}
```

Resolution: fixed
