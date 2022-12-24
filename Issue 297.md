# Issue 297: polymake -- create a build package for the optional SAGE package polymake-2.3

archive/issues_000297.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  sage-combinat jpflori\n\nIt seems much has changed since polymake v 2.2, so this might be difficult.\nAlso, they have interactive scripts, which one has to deal with.  Yuck.\n\nI did try just building from scratch and it seemed to work without any funny\nbusiness with GMP, etc. \n\nIf you work on this, email wstein`@`gmail.com\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/297\n\n",
    "created_at": "2007-02-26T22:13:14Z",
    "labels": [
        "combinatorics",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "polymake -- create a build package for the optional SAGE package polymake-2.3",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/297",
    "user": "@williamstein"
}
```
Assignee: @williamstein

CC:  sage-combinat jpflori

It seems much has changed since polymake v 2.2, so this might be difficult.
Also, they have interactive scripts, which one has to deal with.  Yuck.

I did try just building from scratch and it seemed to work without any funny
business with GMP, etc. 

If you work on this, email wstein`@`gmail.com


Issue created by migration from https://trac.sagemath.org/ticket/297





---

archive/issue_comments_001404.json:
```json
{
    "body": "Changing assignee from @williamstein to mabshoff.",
    "created_at": "2007-08-23T07:23:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/297",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/297#issuecomment-1404",
    "user": "mabshoff"
}
```

Changing assignee from @williamstein to mabshoff.



---

archive/issue_comments_001405.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-08-23T07:23:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/297",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/297#issuecomment-1405",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_001406.json:
```json
{
    "body": "Replying to [ticket:297 was]:\n> It seems much has changed since polymake v 2.2, so this might be difficult.\n> Also, they have interactive scripts, which one has to deal with.  Yuck.\n> \n> I did try just building from scratch and it seemed to work without any funny\n> business with GMP, etc. \n> \n> If you work on this, email wstein`@`gmail.com\n\nOk, I did some investigation. We need to modify support/configure.pl:\n\nAround line 273:\n\n```\n$InstallTop ||= $multi ? \"/usr/local/share/polymake\" : \"/usr/local/polymake\";\nif (!$silent) {\n   print \"\\nWhere should \", ($multi ? \"the architecture-independent part of \" : \"\"), \"polymake be installed? \";\n   answer_path($InstallTop);\n}\n```\n\nInstead of answer_path($InstallTop) we just should assign $InstallTop=getenv($SAGE_LOCAL) (or something alike, my perl is slightly rusty).\n\nWe also need to add Sage's gmp to $Libs around line 614 somewhere.\n\nCheers,\n\nMichael",
    "created_at": "2007-08-23T10:24:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/297",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/297#issuecomment-1406",
    "user": "mabshoff"
}
```

Replying to [ticket:297 was]:
> It seems much has changed since polymake v 2.2, so this might be difficult.
> Also, they have interactive scripts, which one has to deal with.  Yuck.
> 
> I did try just building from scratch and it seemed to work without any funny
> business with GMP, etc. 
> 
> If you work on this, email wstein`@`gmail.com

Ok, I did some investigation. We need to modify support/configure.pl:

Around line 273:

```
$InstallTop ||= $multi ? "/usr/local/share/polymake" : "/usr/local/polymake";
if (!$silent) {
   print "\nWhere should ", ($multi ? "the architecture-independent part of " : ""), "polymake be installed? ";
   answer_path($InstallTop);
}
```

Instead of answer_path($InstallTop) we just should assign $InstallTop=getenv($SAGE_LOCAL) (or something alike, my perl is slightly rusty).

We also need to add Sage's gmp to $Libs around line 614 somewhere.

Cheers,

Michael



---

archive/issue_comments_001407.json:
```json
{
    "body": "I created packages for a prerelease version of polymake before this workshop:\n\nhttp://polymake.org/doku.php/workshop0311\n\nThe package and its dependencies are here:\n\nhttp://sage.math.washington.edu/home/burcin/polymake/\n\nThese packages were just for convenience. They are not ready for review. :)\n\nI also started writing a python wrapper to libPolymake. It's not useful for anything yet, but I could make it useful and release it if there is interest.",
    "created_at": "2011-05-31T14:22:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/297",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/297#issuecomment-1407",
    "user": "@burcin"
}
```

I created packages for a prerelease version of polymake before this workshop:

http://polymake.org/doku.php/workshop0311

The package and its dependencies are here:

http://sage.math.washington.edu/home/burcin/polymake/

These packages were just for convenience. They are not ready for review. :)

I also started writing a python wrapper to libPolymake. It's not useful for anything yet, but I could make it useful and release it if there is interest.



---

archive/issue_comments_001408.json:
```json
{
    "body": "There has definitely been interest in this from various people I've spoken to over the years.  Also, it would be good to have it be an optional spkg for this.  Note the current version is now 2.12 (Burcin's was 2.9).",
    "created_at": "2013-01-29T20:59:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/297",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/297#issuecomment-1408",
    "user": "@kcrisman"
}
```

There has definitely been interest in this from various people I've spoken to over the years.  Also, it would be good to have it be an optional spkg for this.  Note the current version is now 2.12 (Burcin's was 2.9).



---

archive/issue_comments_001409.json:
```json
{
    "body": "This is, in the aggregate, a dup of #5488, #13768, and #14116.  Take your pick :)  In particular, Burcin extended his work and it was integrated into Sage in the latter two tickets, which have *much* more information.",
    "created_at": "2014-11-20T14:06:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/297",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/297#issuecomment-1409",
    "user": "@kcrisman"
}
```

This is, in the aggregate, a dup of #5488, #13768, and #14116.  Take your pick :)  In particular, Burcin extended his work and it was integrated into Sage in the latter two tickets, which have *much* more information.



---

archive/issue_comments_001410.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2014-11-20T14:06:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/297",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/297#issuecomment-1410",
    "user": "@kcrisman"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_001411.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-11-20T14:07:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/297",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/297#issuecomment-1411",
    "user": "@kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_001412.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2014-11-28T20:58:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/297",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/297#issuecomment-1412",
    "user": "@vbraun"
}
```

Resolution: duplicate
