# Issue 6892: [with patch, needs review] change dollar signs to backticks

archive/issues_006892.json:
```json
{
    "body": "Assignee: jhpalmieri\n\nIn [a discussion on sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/8fa0d854b6928f2b?tvc=2), people thought it was a good idea to allow the use of dollar signs, not just backquotes, to delimit math in Sage docstrings.  The attached patch does this.  It does this by working with the autodoc extension to Sphinx: autodoc reads the docstring, which then gets processed by the new function `process_dollars`, which does various regular expression search-and-replacements.\n\nConsequences of this: if you want to use a literal dollar sign in a docstring, you have to escape it with a  backslash.  If you have some complicated math with lots of nested math/text constructions like \"\\text{blah $x=y$ blah}\", this might screw up.  It will handle one nesting, turning\n\n```\n$f(x) = \\text{zero if $x$ is prime}$\n```\n\ninto\n\n```\n`f(x) = \\text{zero if $x$ is prime}`\n```\n\nand leaving \n\n```\n`f(z) = \\text{two if $z$ is an integer}`\n```\n\nunchanged; these should be processed correctly by both the html and pdf documentation builders.\n\nThe patch also changes some docstrings: either fixing minor misformattings which I noticed while testing this, or fixing things which break (like a docstring with a math environment with a missing closing dollar sign) when dollar signs are converted to backquotes.\n\nSeems to work with Sphinx versions 0.5.1 (currently included in Sage) and 0.6.3 (see #6586).\n\nIssue created by migration from https://trac.sagemath.org/ticket/6892\n\n",
    "created_at": "2009-09-04T21:26:11Z",
    "labels": [
        "documentation",
        "major",
        "enhancement"
    ],
    "title": "[with patch, needs review] change dollar signs to backticks",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6892",
    "user": "jhpalmieri"
}
```
Assignee: jhpalmieri

In [a discussion on sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/8fa0d854b6928f2b?tvc=2), people thought it was a good idea to allow the use of dollar signs, not just backquotes, to delimit math in Sage docstrings.  The attached patch does this.  It does this by working with the autodoc extension to Sphinx: autodoc reads the docstring, which then gets processed by the new function `process_dollars`, which does various regular expression search-and-replacements.

Consequences of this: if you want to use a literal dollar sign in a docstring, you have to escape it with a  backslash.  If you have some complicated math with lots of nested math/text constructions like "\text{blah $x=y$ blah}", this might screw up.  It will handle one nesting, turning

```
$f(x) = \text{zero if $x$ is prime}$
```

into

```
`f(x) = \text{zero if $x$ is prime}`
```

and leaving 

```
`f(z) = \text{two if $z$ is an integer}`
```

unchanged; these should be processed correctly by both the html and pdf documentation builders.

The patch also changes some docstrings: either fixing minor misformattings which I noticed while testing this, or fixing things which break (like a docstring with a math environment with a missing closing dollar sign) when dollar signs are converted to backquotes.

Seems to work with Sphinx versions 0.5.1 (currently included in Sage) and 0.6.3 (see #6586).

Issue created by migration from https://trac.sagemath.org/ticket/6892





---

archive/issue_comments_056941.json:
```json
{
    "body": "Attachment [trac_6892-dollars.patch](tarball://root/attachments/some-uuid/ticket6892/trac_6892-dollars.patch) by jhpalmieri created at 2009-09-04 21:26:48",
    "created_at": "2009-09-04T21:26:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6892",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6892#issuecomment-56941",
    "user": "jhpalmieri"
}
```

Attachment [trac_6892-dollars.patch](tarball://root/attachments/some-uuid/ticket6892/trac_6892-dollars.patch) by jhpalmieri created at 2009-09-04 21:26:48



---

archive/issue_comments_056942.json:
```json
{
    "body": "minor rebase for 4.1.2.alpha1; tiny changes to conf.py and ambient_g0.py",
    "created_at": "2009-09-16T03:03:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6892",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6892#issuecomment-56942",
    "user": "ddrake"
}
```

minor rebase for 4.1.2.alpha1; tiny changes to conf.py and ambient_g0.py



---

archive/issue_comments_056943.json:
```json
{
    "body": "Attachment [trac_6892-dollars-rebased.patch](tarball://root/attachments/some-uuid/ticket6892/trac_6892-dollars-rebased.patch) by jhpalmieri created at 2009-09-22 03:01:13\n\nrebased against 4.1.2.alpha2, plus a little documentation",
    "created_at": "2009-09-22T03:01:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6892",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6892#issuecomment-56943",
    "user": "jhpalmieri"
}
```

Attachment [trac_6892-dollars-rebased.patch](tarball://root/attachments/some-uuid/ticket6892/trac_6892-dollars-rebased.patch) by jhpalmieri created at 2009-09-22 03:01:13

rebased against 4.1.2.alpha2, plus a little documentation



---

archive/issue_comments_056944.json:
```json
{
    "body": "Apply only trac_6892-dollars-rebased.patch.  This adds a little documentation in the developer's guide about using dollar signs instead of backticks.",
    "created_at": "2009-09-22T03:01:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6892",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6892#issuecomment-56944",
    "user": "jhpalmieri"
}
```

Apply only trac_6892-dollars-rebased.patch.  This adds a little documentation in the developer's guide about using dollar signs instead of backticks.



---

archive/issue_comments_056945.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2009-10-05T07:35:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6892",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6892#issuecomment-56945",
    "user": "mhansen"
}
```

Looks good to me.



---

archive/issue_comments_056946.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-10-16T04:49:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6892",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6892#issuecomment-56946",
    "user": "mhansen"
}
```

Resolution: fixed
