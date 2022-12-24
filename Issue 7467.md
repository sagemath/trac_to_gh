# Issue 7467: Make SageNB use `setuptools` instead of `distutils`

archive/issues_007467.json:
```json
{
    "body": "Assignee: boothby\n\nCC:  @qed777 @williamstein\n\nCurrently, SageNB makes use of `distutils`. The standard method of package distribution, though, is [setuptools](http://peak.telecommunity.com/DevCenter/setuptools). This has several advantages, the foremost being a `setup.py develop` command, which bypasses the need to reinstall the package in order to propagate a change, as well as the ability to upload the package to PyPI with a single command. There is also additional functionality regards packaging, etc.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7467\n\n",
    "created_at": "2009-11-15T05:05:48Z",
    "labels": [
        "notebook",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "Make SageNB use `setuptools` instead of `distutils`",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7467",
    "user": "@TimDumol"
}
```
Assignee: boothby

CC:  @qed777 @williamstein

Currently, SageNB makes use of `distutils`. The standard method of package distribution, though, is [setuptools](http://peak.telecommunity.com/DevCenter/setuptools). This has several advantages, the foremost being a `setup.py develop` command, which bypasses the need to reinstall the package in order to propagate a change, as well as the ability to upload the package to PyPI with a single command. There is also additional functionality regards packaging, etc.

Issue created by migration from https://trac.sagemath.org/ticket/7467





---

archive/issue_comments_062883.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-11-15T05:17:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7467",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7467#issuecomment-62883",
    "user": "@TimDumol"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_062884.json:
```json
{
    "body": "This should do it.",
    "created_at": "2009-11-15T05:17:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7467",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7467#issuecomment-62884",
    "user": "@TimDumol"
}
```

This should do it.



---

archive/issue_comments_062885.json:
```json
{
    "body": "Attachment [trac_7467-setuptools.patch](tarball://root/attachments/some-uuid/ticket7467/trac_7467-setuptools.patch) by @TimDumol created at 2009-11-15 05:45:48\n\nMakes `setup.py` use `setuptools` instead of `distutils`. Depends on #7402 for things to work properly.",
    "created_at": "2009-11-15T05:45:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7467",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7467#issuecomment-62885",
    "user": "@TimDumol"
}
```

Attachment [trac_7467-setuptools.patch](tarball://root/attachments/some-uuid/ticket7467/trac_7467-setuptools.patch) by @TimDumol created at 2009-11-15 05:45:48

Makes `setup.py` use `setuptools` instead of `distutils`. Depends on #7402 for things to work properly.



---

archive/issue_comments_062886.json:
```json
{
    "body": "Attachment [trac_7467-setuptools.2.patch](tarball://root/attachments/some-uuid/ticket7467/trac_7467-setuptools.2.patch) by @TimDumol created at 2009-11-15 06:09:57\n\nAdded necessary .hgignore lines.",
    "created_at": "2009-11-15T06:09:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7467",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7467#issuecomment-62886",
    "user": "@TimDumol"
}
```

Attachment [trac_7467-setuptools.2.patch](tarball://root/attachments/some-uuid/ticket7467/trac_7467-setuptools.2.patch) by @TimDumol created at 2009-11-15 06:09:57

Added necessary .hgignore lines.



---

archive/issue_comments_062887.json:
```json
{
    "body": "What are your thoughts about\n\n* [On packaging](http://www.b-list.org/weblog/2008/dec/14/packaging/)\n* [A Few Corrections To \u201cOn Packaging\u201d](http://blog.ianbicking.org/2008/12/14/a-few-corrections-to-on-packaging/)\n\n?  I found these links at [Tools of the Modern Python Hacker: Virtualenv, Fabric and Pip](http://clemesha.org/blog/2009/jul/05/modern-python-hacker-tools-virtualenv-fabric-pip/).",
    "created_at": "2009-11-15T06:23:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7467",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7467#issuecomment-62887",
    "user": "@qed777"
}
```

What are your thoughts about

* [On packaging](http://www.b-list.org/weblog/2008/dec/14/packaging/)
* [A Few Corrections To “On Packaging”](http://blog.ianbicking.org/2008/12/14/a-few-corrections-to-on-packaging/)

?  I found these links at [Tools of the Modern Python Hacker: Virtualenv, Fabric and Pip](http://clemesha.org/blog/2009/jul/05/modern-python-hacker-tools-virtualenv-fabric-pip/).



---

archive/issue_comments_062888.json:
```json
{
    "body": "Replying to [comment:2 mpatel]:\n> What are your thoughts about\n> \n>  * [On packaging](http://www.b-list.org/weblog/2008/dec/14/packaging/)\n>  * [A Few Corrections To \u201cOn Packaging\u201d](http://blog.ianbicking.org/2008/12/14/a-few-corrections-to-on-packaging/)\n> \n> ?  I found these links at [Tools of the Modern Python Hacker: Virtualenv, Fabric and Pip](http://clemesha.org/blog/2009/jul/05/modern-python-hacker-tools-virtualenv-fabric-pip/).\n\nThese tools are orthogonal to usage of `setuptools`, to note.\n\nI personally make use of Virtualenv and Pip all the time for deployment. They're very useful for keeping one's site-packages clean.",
    "created_at": "2009-11-15T06:42:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7467",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7467#issuecomment-62888",
    "user": "@TimDumol"
}
```

Replying to [comment:2 mpatel]:
> What are your thoughts about
> 
>  * [On packaging](http://www.b-list.org/weblog/2008/dec/14/packaging/)
>  * [A Few Corrections To “On Packaging”](http://blog.ianbicking.org/2008/12/14/a-few-corrections-to-on-packaging/)
> 
> ?  I found these links at [Tools of the Modern Python Hacker: Virtualenv, Fabric and Pip](http://clemesha.org/blog/2009/jul/05/modern-python-hacker-tools-virtualenv-fabric-pip/).

These tools are orthogonal to usage of `setuptools`, to note.

I personally make use of Virtualenv and Pip all the time for deployment. They're very useful for keeping one's site-packages clean.



---

archive/issue_comments_062889.json:
```json
{
    "body": "Thanks for the clarification.  What if we use [pip](http://pip.openplans.org/) (i.e., `pip.py`) as SageNB's installer?  The uninstall facility might allow us to select among different development versions (and their [requirements](http://pip.openplans.org/requirement-format.html)) in a *clean* way.  Currently, extraneous files can \"accumulate\" in `site-packages/sagenb` until I do `rm -rf` and reinstall.\n\nDisclaimer: I'm not familiar with `distutils`, `pip`, or `setuptools`.\n\nOn #7447: Can we query the installed version of a package with `setuptools` and/or `pip`?",
    "created_at": "2009-11-15T07:48:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7467",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7467#issuecomment-62889",
    "user": "@qed777"
}
```

Thanks for the clarification.  What if we use [pip](http://pip.openplans.org/) (i.e., `pip.py`) as SageNB's installer?  The uninstall facility might allow us to select among different development versions (and their [requirements](http://pip.openplans.org/requirement-format.html)) in a *clean* way.  Currently, extraneous files can "accumulate" in `site-packages/sagenb` until I do `rm -rf` and reinstall.

Disclaimer: I'm not familiar with `distutils`, `pip`, or `setuptools`.

On #7447: Can we query the installed version of a package with `setuptools` and/or `pip`?



---

archive/issue_comments_062890.json:
```json
{
    "body": "Replying to [comment:4 mpatel]:\n> [...]\n> On #7447: Can we query the installed version of a package with `setuptools` and/or `pip`?\n\nI believe something like this should do the trick:\n\n\n```\nfrom pkg_resources import Requirement, working_set\nversion = working_set.find9Requirement.parse('sagenb')).version\n```\n",
    "created_at": "2009-11-15T08:01:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7467",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7467#issuecomment-62890",
    "user": "@TimDumol"
}
```

Replying to [comment:4 mpatel]:
> [...]
> On #7447: Can we query the installed version of a package with `setuptools` and/or `pip`?

I believe something like this should do the trick:


```
from pkg_resources import Requirement, working_set
version = working_set.find9Requirement.parse('sagenb')).version
```




---

archive/issue_comments_062891.json:
```json
{
    "body": "Replying to [comment:5 timdumol]:\n> Replying to [comment:4 mpatel]:\n> > [...]\n> > On #7447: Can we query the installed version of a package with `setuptools` and/or `pip`?\n> \n> I believe something like this should do the trick:\n> \n> {{{\n> from pkg_resources import Requirement, working_set\n> version = working_set.find9Requirement.parse('sagenb')).version\n> }}}\n\nSorry, I meant `working_set.find(Requirement.parse('sagenb')).version`",
    "created_at": "2009-11-15T08:02:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7467",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7467#issuecomment-62891",
    "user": "@TimDumol"
}
```

Replying to [comment:5 timdumol]:
> Replying to [comment:4 mpatel]:
> > [...]
> > On #7447: Can we query the installed version of a package with `setuptools` and/or `pip`?
> 
> I believe something like this should do the trick:
> 
> {{{
> from pkg_resources import Requirement, working_set
> version = working_set.find9Requirement.parse('sagenb')).version
> }}}

Sorry, I meant `working_set.find(Requirement.parse('sagenb')).version`



---

archive/issue_comments_062892.json:
```json
{
    "body": "Replying to [comment:4 mpatel]:\n> Thanks for the clarification.  What if we use [pip](http://pip.openplans.org/) (i.e., `pip.py`) as SageNB's installer?  The uninstall facility might allow us to select among different development versions (and their [requirements](http://pip.openplans.org/requirement-format.html)) in a *clean* way.  Currently, extraneous files can \"accumulate\" in `site-packages/sagenb` until I do `rm -rf` and reinstall.\n> [..]\n\nWow, that feature's new. I don't see why not, although it would mean adding another package to Sage.",
    "created_at": "2009-11-15T08:04:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7467",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7467#issuecomment-62892",
    "user": "@TimDumol"
}
```

Replying to [comment:4 mpatel]:
> Thanks for the clarification.  What if we use [pip](http://pip.openplans.org/) (i.e., `pip.py`) as SageNB's installer?  The uninstall facility might allow us to select among different development versions (and their [requirements](http://pip.openplans.org/requirement-format.html)) in a *clean* way.  Currently, extraneous files can "accumulate" in `site-packages/sagenb` until I do `rm -rf` and reinstall.
> [..]

Wow, that feature's new. I don't see why not, although it would mean adding another package to Sage.



---

archive/issue_comments_062893.json:
```json
{
    "body": "I get\n\n```python\nsage: from pkg_resources import Requirement, working_set\nsage: working_set.find(Requirement.parse('sagenb')).version\nAttributeError: 'NoneType' object has no attribute 'version'\n```\n\n\nOn using pip: We could just add `pip.py`, according to [this](http://pip.openplans.org/#using-pip-with-virtualenv).",
    "created_at": "2009-11-15T08:15:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7467",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7467#issuecomment-62893",
    "user": "@qed777"
}
```

I get

```python
sage: from pkg_resources import Requirement, working_set
sage: working_set.find(Requirement.parse('sagenb')).version
AttributeError: 'NoneType' object has no attribute 'version'
```


On using pip: We could just add `pip.py`, according to [this](http://pip.openplans.org/#using-pip-with-virtualenv).



---

archive/issue_comments_062894.json:
```json
{
    "body": "Replying to [comment:8 mpatel]:\n> I get\n> {{{\n> #!python\n> sage: from pkg_resources import Requirement, working_set\n> sage: working_set.find(Requirement.parse('sagenb')).version\n> AttributeError: 'NoneType' object has no attribute 'version'\n> }}}\n> \n> On using pip: We could just add `pip.py`, according to [this](http://pip.openplans.org/#using-pip-with-virtualenv).\n\nI believe detection of version using `pkg_resources` requires it be installed by `setuptools`, i.e., this patch.",
    "created_at": "2009-11-15T08:17:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7467",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7467#issuecomment-62894",
    "user": "@TimDumol"
}
```

Replying to [comment:8 mpatel]:
> I get
> {{{
> #!python
> sage: from pkg_resources import Requirement, working_set
> sage: working_set.find(Requirement.parse('sagenb')).version
> AttributeError: 'NoneType' object has no attribute 'version'
> }}}
> 
> On using pip: We could just add `pip.py`, according to [this](http://pip.openplans.org/#using-pip-with-virtualenv).

I believe detection of version using `pkg_resources` requires it be installed by `setuptools`, i.e., this patch.



---

archive/issue_comments_062895.json:
```json
{
    "body": "OK, or pip, I suppose.  Thanks.  I'll put a note at #7447.",
    "created_at": "2009-11-15T08:19:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7467",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7467#issuecomment-62895",
    "user": "@qed777"
}
```

OK, or pip, I suppose.  Thanks.  I'll put a note at #7447.



---

archive/issue_comments_062896.json:
```json
{
    "body": "Although I'm not very familar with `distutils` or `setuptools`, this works for and looks good to me.  A spkg built with `spkg-dist` installs properly.  Moreover, we can query the `sagenb` version just as indicated in the comments above.",
    "created_at": "2009-12-05T23:56:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7467",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7467#issuecomment-62896",
    "user": "@qed777"
}
```

Although I'm not very familar with `distutils` or `setuptools`, this works for and looks good to me.  A spkg built with `spkg-dist` installs properly.  Moreover, we can query the `sagenb` version just as indicated in the comments above.



---

archive/issue_comments_062897.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-05T23:56:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7467",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7467#issuecomment-62897",
    "user": "@qed777"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_062898.json:
```json
{
    "body": "+1!",
    "created_at": "2009-12-08T07:19:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7467",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7467#issuecomment-62898",
    "user": "@williamstein"
}
```

+1!



---

archive/issue_comments_062899.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-12-08T07:19:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7467",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7467#issuecomment-62899",
    "user": "@williamstein"
}
```

Resolution: fixed
