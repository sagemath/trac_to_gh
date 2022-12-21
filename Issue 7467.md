# Issue 7467: Make SageNB use `setuptools` instead of `distutils`

Issue created by migration from Trac.

Original creator: timdumol

Original creation time: 2009-11-15 05:05:48

Assignee: boothby

CC:  mpatel was

Currently, SageNB makes use of `distutils`. The standard method of package distribution, though, is [setuptools](http://peak.telecommunity.com/DevCenter/setuptools). This has several advantages, the foremost being a `setup.py develop` command, which bypasses the need to reinstall the package in order to propagate a change, as well as the ability to upload the package to PyPI with a single command. There is also additional functionality regards packaging, etc.


---

Comment by timdumol created at 2009-11-15 05:17:31

Changing status from new to needs_review.


---

Comment by timdumol created at 2009-11-15 05:17:31

This should do it.


---

Attachment

Makes `setup.py` use `setuptools` instead of `distutils`. Depends on #7402 for things to work properly.


---

Attachment

Added necessary .hgignore lines.


---

Comment by mpatel created at 2009-11-15 06:23:16

What are your thoughts about

 * [On packaging](http://www.b-list.org/weblog/2008/dec/14/packaging/)
 * [A Few Corrections To “On Packaging”](http://blog.ianbicking.org/2008/12/14/a-few-corrections-to-on-packaging/)

?  I found these links at [Tools of the Modern Python Hacker: Virtualenv, Fabric and Pip](http://clemesha.org/blog/2009/jul/05/modern-python-hacker-tools-virtualenv-fabric-pip/).


---

Comment by timdumol created at 2009-11-15 06:42:50

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

Comment by mpatel created at 2009-11-15 07:48:31

Thanks for the clarification.  What if we use [pip](http://pip.openplans.org/) (i.e., `pip.py`) as SageNB's installer?  The uninstall facility might allow us to select among different development versions (and their [requirements](http://pip.openplans.org/requirement-format.html)) in a _clean_ way.  Currently, extraneous files can "accumulate" in `site-packages/sagenb` until I do `rm -rf` and reinstall.

Disclaimer: I'm not familiar with `distutils`, `pip`, or `setuptools`.

On #7447: Can we query the installed version of a package with `setuptools` and/or `pip`?


---

Comment by timdumol created at 2009-11-15 08:01:18

Replying to [comment:4 mpatel]:
> [...]
> On #7447: Can we query the installed version of a package with `setuptools` and/or `pip`?

I believe something like this should do the trick:


```
from pkg_resources import Requirement, working_set
version = working_set.find9Requirement.parse('sagenb')).version
```



---

Comment by timdumol created at 2009-11-15 08:02:07

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

Comment by timdumol created at 2009-11-15 08:04:35

Replying to [comment:4 mpatel]:
> Thanks for the clarification.  What if we use [pip](http://pip.openplans.org/) (i.e., `pip.py`) as SageNB's installer?  The uninstall facility might allow us to select among different development versions (and their [requirements](http://pip.openplans.org/requirement-format.html)) in a _clean_ way.  Currently, extraneous files can "accumulate" in `site-packages/sagenb` until I do `rm -rf` and reinstall.
> [..]

Wow, that feature's new. I don't see why not, although it would mean adding another package to Sage.


---

Comment by mpatel created at 2009-11-15 08:15:46

I get

```python
sage: from pkg_resources import Requirement, working_set
sage: working_set.find(Requirement.parse('sagenb')).version
AttributeError: 'NoneType' object has no attribute 'version'
```


On using pip: We could just add `pip.py`, according to [this](http://pip.openplans.org/#using-pip-with-virtualenv).


---

Comment by timdumol created at 2009-11-15 08:17:38

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

Comment by mpatel created at 2009-11-15 08:19:45

OK, or pip, I suppose.  Thanks.  I'll put a note at #7447.


---

Comment by mpatel created at 2009-12-05 23:56:03

Although I'm not very familar with `distutils` or `setuptools`, this works for and looks good to me.  A spkg built with `spkg-dist` installs properly.  Moreover, we can query the `sagenb` version just as indicated in the comments above.


---

Comment by mpatel created at 2009-12-05 23:56:03

Changing status from needs_review to positive_review.


---

Comment by was created at 2009-12-08 07:19:55

+1!


---

Comment by was created at 2009-12-08 07:19:55

Resolution: fixed
