# Issue 7515: Improved deprecation and renaming of function and methods.

archive/issues_007515.json:
```json
{
    "body": "Assignee: hivert\n\nCC:  combinat\n\nKeywords: deprecation:\n\nAlong the cleanup of combinat, a lot of methods and function get renamed. It is painfull to write backward compatibility aliases.\nThe patch given here should make it easier. I take also the chance to add a version optional argument to `deprecation` to store and print in which version of sage the method/function was deprecated.\n\nHere is an excerpt from the doc:\n\n```\n        sage: from sage.misc.misc import deprecated_function_alias\n        sage: g = deprecated_function_alias(number_of_partitions,\n        ...     'Sage Version 42.132, Release Date: 5123-04-01')\n        sage: g(5)\n        doctest:1: DeprecationWarning: (Since Sage Version 42.132, Release Date: 5123-04-01) g is deprecated. Please use number_of_partitions instead.\n        7\n```\n\nThis also works for methods:\n\n```\n        sage: from sage.misc.misc import deprecated_method_alias\n        sage: class cls(object):\n        ...      def new_meth(self): return 42\n        ...      old_meth = deprecated_method_alias(new_meth,\n        ...            'Sage Version 42.132, Release Date: 5123-04-01')\n        sage: cls().old_meth()\n        doctest:...: DeprecationWarning: (Since Sage Version 42.132, Release Date: 5123-04-01) old_meth is deprecated. Please use new_meth instead.\n        42\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7515\n\n",
    "created_at": "2009-11-22T17:19:12Z",
    "labels": [
        "misc",
        "major",
        "enhancement"
    ],
    "title": "Improved deprecation and renaming of function and methods.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7515",
    "user": "hivert"
}
```
Assignee: hivert

CC:  combinat

Keywords: deprecation:

Along the cleanup of combinat, a lot of methods and function get renamed. It is painfull to write backward compatibility aliases.
The patch given here should make it easier. I take also the chance to add a version optional argument to `deprecation` to store and print in which version of sage the method/function was deprecated.

Here is an excerpt from the doc:

```
        sage: from sage.misc.misc import deprecated_function_alias
        sage: g = deprecated_function_alias(number_of_partitions,
        ...     'Sage Version 42.132, Release Date: 5123-04-01')
        sage: g(5)
        doctest:1: DeprecationWarning: (Since Sage Version 42.132, Release Date: 5123-04-01) g is deprecated. Please use number_of_partitions instead.
        7
```

This also works for methods:

```
        sage: from sage.misc.misc import deprecated_method_alias
        sage: class cls(object):
        ...      def new_meth(self): return 42
        ...      old_meth = deprecated_method_alias(new_meth,
        ...            'Sage Version 42.132, Release Date: 5123-04-01')
        sage: cls().old_meth()
        doctest:...: DeprecationWarning: (Since Sage Version 42.132, Release Date: 5123-04-01) old_meth is deprecated. Please use new_meth instead.
        42
```



Issue created by migration from https://trac.sagemath.org/ticket/7515





---

archive/issue_comments_063656.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-11-22T17:23:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7515",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7515#issuecomment-63656",
    "user": "hivert"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_063657.json:
```json
{
    "body": "Adressed William comments on sage-devel.",
    "created_at": "2009-11-23T09:49:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7515",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7515#issuecomment-63657",
    "user": "hivert"
}
```

Adressed William comments on sage-devel.



---

archive/issue_comments_063658.json:
```json
{
    "body": "Attachment [trac_7515_method_alias_decorator-fh.patch](tarball://root/attachments/some-uuid/ticket7515/trac_7515_method_alias_decorator-fh.patch) by hivert created at 2009-11-30 10:13:08\n\nUpdated patch to remark on sage-devel (i.e. just put the version of deprecation, without the date). Reday for review.",
    "created_at": "2009-11-30T10:13:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7515",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7515#issuecomment-63658",
    "user": "hivert"
}
```

Attachment [trac_7515_method_alias_decorator-fh.patch](tarball://root/attachments/some-uuid/ticket7515/trac_7515_method_alias_decorator-fh.patch) by hivert created at 2009-11-30 10:13:08

Updated patch to remark on sage-devel (i.e. just put the version of deprecation, without the date). Reday for review.



---

archive/issue_comments_063659.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-11-30T12:00:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7515",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7515#issuecomment-63659",
    "user": "ncohen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_063660.json:
```json
{
    "body": "No problem with this one... Extremely useful :-)\n\nDo you think one should create a ticket saying \"replace all the deprecation warning using deprecated_function_alias whenever possible\" ?\n\nFirsdt, it would shorten Sage's code, plus everybody would see this is how we should set functions as deprecated instead of using the old method... I \"copy\" things very often in Sage's code, and if I am not working around an example of this, you can be sure I'd do it the other way :-)\n\nPositive review, thanks for your work !\n\nNathann",
    "created_at": "2009-11-30T12:00:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7515",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7515#issuecomment-63660",
    "user": "ncohen"
}
```

No problem with this one... Extremely useful :-)

Do you think one should create a ticket saying "replace all the deprecation warning using deprecated_function_alias whenever possible" ?

Firsdt, it would shorten Sage's code, plus everybody would see this is how we should set functions as deprecated instead of using the old method... I "copy" things very often in Sage's code, and if I am not working around an example of this, you can be sure I'd do it the other way :-)

Positive review, thanks for your work !

Nathann



---

archive/issue_comments_063661.json:
```json
{
    "body": "Replying to [comment:4 ncohen]:\n> No problem with this one... Extremely useful :-)\n> \n> Do you think one should create a ticket saying \"replace all the deprecation warning using deprecated_function_alias whenever possible\" ?\n\nThis would be surely a good idea, but I'm not sure I wan't to volunteer to do this one right now. There are a lot of deprecated things in sage. Here is a rough evaluation:\n\n```\ntomahawk-*/devel/sage-main $ grep deprecat **/*.py **/*.pyx | wc\n   1228   13940  168762\n```\n\nSo I'm opening the ticket but I currently don't accept it.\n\nCheers,\n\nFlorent",
    "created_at": "2009-11-30T12:19:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7515",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7515#issuecomment-63661",
    "user": "hivert"
}
```

Replying to [comment:4 ncohen]:
> No problem with this one... Extremely useful :-)
> 
> Do you think one should create a ticket saying "replace all the deprecation warning using deprecated_function_alias whenever possible" ?

This would be surely a good idea, but I'm not sure I wan't to volunteer to do this one right now. There are a lot of deprecated things in sage. Here is a rough evaluation:

```
tomahawk-*/devel/sage-main $ grep deprecat **/*.py **/*.pyx | wc
   1228   13940  168762
```

So I'm opening the ticket but I currently don't accept it.

Cheers,

Florent



---

archive/issue_comments_063662.json:
```json
{
    "body": "Perhaps it is possible to script it in emacs.... :-)",
    "created_at": "2009-11-30T12:21:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7515",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7515#issuecomment-63662",
    "user": "ncohen"
}
```

Perhaps it is possible to script it in emacs.... :-)



---

archive/issue_comments_063663.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2009-12-01T03:53:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7515",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7515#issuecomment-63663",
    "user": "mhansen"
}
```

Looks good to me.



---

archive/issue_comments_063664.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-12-01T03:53:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7515",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7515#issuecomment-63664",
    "user": "mhansen"
}
```

Resolution: fixed
