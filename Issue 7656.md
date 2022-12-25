# Issue 7656: Bitset tricks

archive/issues_007656.json:
```json
{
    "body": "Assignee: tbd\n\nThere are some extra tricks in here: http://www.jjj.de/fxt/#fxtbook\n\nin the first chapter for doing bitset operations that ought to be applied to our Bitset class.  For example, there is a trick that allows you to count the number of bits in log time instead of linear time.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7656\n\n",
    "created_at": "2009-12-11T04:03:16Z",
    "labels": [
        "component: misc"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Bitset tricks",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7656",
    "user": "https://github.com/jasongrout"
}
```
Assignee: tbd

There are some extra tricks in here: http://www.jjj.de/fxt/#fxtbook

in the first chapter for doing bitset operations that ought to be applied to our Bitset class.  For example, there is a trick that allows you to count the number of bits in log time instead of linear time.

Issue created by migration from https://trac.sagemath.org/ticket/7656





---

archive/issue_comments_065374.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2010-05-11T20:49:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7656",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7656#issuecomment-65374",
    "user": "https://github.com/jasongrout"
}
```

Changing priority from major to minor.



---

archive/issue_comments_065375.json:
```json
{
    "body": "This FXTBook is the best book in the universe. I'm *EAGER* to read it.\n\nAbout the counting trick : there is a builtin gcc command called __builtin_popcount which may do wonders. It does count the bits in general (though I haven't found the corresponding code) -- it may well be the logarithmic way (+very nice trick btw), and in case the popcnt instruction is available on the processor, it is directly called.\n\nAnd I assure you for having compared the two that it does.... WONDERS :-D\n\nNathann",
    "created_at": "2011-05-02T16:19:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7656",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7656#issuecomment-65375",
    "user": "https://github.com/nathanncohen"
}
```

This FXTBook is the best book in the universe. I'm *EAGER* to read it.

About the counting trick : there is a builtin gcc command called __builtin_popcount which may do wonders. It does count the bits in general (though I haven't found the corresponding code) -- it may well be the logarithmic way (+very nice trick btw), and in case the popcnt instruction is available on the processor, it is directly called.

And I assure you for having compared the two that it does.... WONDERS :-D

Nathann



---

archive/issue_comments_065376.json:
```json
{
    "body": "If we can guarantee that gcc is used to compile the file, then great!  I think we can assume that for now, but it may not be true in the future.  Is there a preprocessor check we can put in or something?",
    "created_at": "2011-05-02T18:41:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7656",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7656#issuecomment-65376",
    "user": "https://github.com/jasongrout"
}
```

If we can guarantee that gcc is used to compile the file, then great!  I think we can assume that for now, but it may not be true in the future.  Is there a preprocessor check we can put in or something?



---

archive/issue_comments_065377.json:
```json
{
    "body": "I'd say \"test for ``__GNUC__`` with the preprocessor\". Though on these aspects I'd ask David first `:-D`\n\nhttp://gcc.gnu.org/onlinedocs/cpp/Common-Predefined-Macros.html\n\nNathann",
    "created_at": "2011-05-03T12:40:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7656",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7656#issuecomment-65377",
    "user": "https://github.com/nathanncohen"
}
```

I'd say "test for ``__GNUC__`` with the preprocessor". Though on these aspects I'd ask David first `:-D`

http://gcc.gnu.org/onlinedocs/cpp/Common-Predefined-Macros.html

Nathann



---

archive/issue_comments_065378.json:
```json
{
    "body": "Oh. Actually I already did and he advised to use this very piece of code \n\n```\n#ifdef __GNUC__\n /* Make use of GCC extensions here. */\n#else\n/* Add portable version here */\n#endif\n```\n\n\nGive to Caesar [..] `:-)`\n\nNathann",
    "created_at": "2011-05-03T12:45:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7656",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7656#issuecomment-65378",
    "user": "https://github.com/nathanncohen"
}
```

Oh. Actually I already did and he advised to use this very piece of code 

```
#ifdef __GNUC__
 /* Make use of GCC extensions here. */
#else
/* Add portable version here */
#endif
```


Give to Caesar [..] `:-)`

Nathann



---

archive/issue_comments_065379.json:
```json
{
    "body": "This ticket is very vague. It should either be made more concrete (like, **what** do you want to do with bitsets) or closed as \"invalid\".",
    "created_at": "2013-12-10T13:12:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7656",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7656#issuecomment-65379",
    "user": "https://github.com/jdemeyer"
}
```

This ticket is very vague. It should either be made more concrete (like, **what** do you want to do with bitsets) or closed as "invalid".



---

archive/issue_comments_065380.json:
```json
{
    "body": "...and it's probably superseded by #16937 also.",
    "created_at": "2014-09-11T09:12:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7656",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7656#issuecomment-65380",
    "user": "https://github.com/jdemeyer"
}
```

...and it's probably superseded by #16937 also.



---

archive/issue_comments_065381.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2014-09-11T09:12:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7656",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7656#issuecomment-65381",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_065382.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-09-11T09:12:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7656",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7656#issuecomment-65382",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_065383.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2014-09-15T14:56:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7656",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7656#issuecomment-65383",
    "user": "https://github.com/vbraun"
}
```

Resolution: duplicate
