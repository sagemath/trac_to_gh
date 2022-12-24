# Issue 9426: Docbuilder ignores return code from subprocess.call()

archive/issues_009426.json:
```json
{
    "body": "Assignee: mvngu\n\nCC:  jdemeyer\n\n`devel/sage/doc/common/builder.py`:\n\nIn `builder_helper.f()`:\n\n```\n...\n        logger.warning(build_command)\n        subprocess.call(build_command, shell=True)\n\n        logger.warning(\"Build finished.  The built documents can be found in %s\", output_dir)\n...\n```\n\n\nIn `class DocBuilder`:\n\n```\n    def pdf(self):\n        \"\"\"\n        Builds the PDF files for this document.  This is done by first\n        (re)-building the LaTeX output, going into that LaTeX\n        directory, and running 'make all-pdf' there.\n\n        EXAMPLES::\n\n            sage: import os, sys; sys.path.append(os.environ['SAGE_DOC']+'/common/'); import builder\n            sage: b = builder.DocBuilder('tutorial')\n            sage: b.pdf() #not tested\n        \"\"\"\n        self.latex()\n        os.chdir(self._output_dir('latex'))\n        subprocess.call('make all-pdf', shell=True)\n\n        pdf_dir = self._output_dir('pdf')\n        for pdf_file in glob.glob('*.pdf'):\n            shutil.move(pdf_file, os.path.join(pdf_dir, pdf_file))\n\n        logger.warning(\"Build finished.  The built documents can be found in %s\", pdf_dir)\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9426\n\n",
    "created_at": "2010-07-04T22:05:00Z",
    "labels": [
        "documentation",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Docbuilder ignores return code from subprocess.call()",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9426",
    "user": "leif"
}
```
Assignee: mvngu

CC:  jdemeyer

`devel/sage/doc/common/builder.py`:

In `builder_helper.f()`:

```
...
        logger.warning(build_command)
        subprocess.call(build_command, shell=True)

        logger.warning("Build finished.  The built documents can be found in %s", output_dir)
...
```


In `class DocBuilder`:

```
    def pdf(self):
        """
        Builds the PDF files for this document.  This is done by first
        (re)-building the LaTeX output, going into that LaTeX
        directory, and running 'make all-pdf' there.

        EXAMPLES::

            sage: import os, sys; sys.path.append(os.environ['SAGE_DOC']+'/common/'); import builder
            sage: b = builder.DocBuilder('tutorial')
            sage: b.pdf() #not tested
        """
        self.latex()
        os.chdir(self._output_dir('latex'))
        subprocess.call('make all-pdf', shell=True)

        pdf_dir = self._output_dir('pdf')
        for pdf_file in glob.glob('*.pdf'):
            shutil.move(pdf_file, os.path.join(pdf_dir, pdf_file))

        logger.warning("Build finished.  The built documents can be found in %s", pdf_dir)
```



Issue created by migration from https://trac.sagemath.org/ticket/9426





---

archive/issue_comments_089920.json:
```json
{
    "body": "It's trivial to change *the message* on non-zero return values, but I think errors should somehow be propagated, s.t. doc build errors aren't drowned in the flood of other messages.",
    "created_at": "2010-07-04T22:53:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9426",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9426#issuecomment-89920",
    "user": "leif"
}
```

It's trivial to change *the message* on non-zero return values, but I think errors should somehow be propagated, s.t. doc build errors aren't drowned in the flood of other messages.



---

archive/issue_comments_089921.json:
```json
{
    "body": "Changing this to blocker at least for now...",
    "created_at": "2010-07-05T11:07:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9426",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9426#issuecomment-89921",
    "user": "rlm"
}
```

Changing this to blocker at least for now...



---

archive/issue_comments_089922.json:
```json
{
    "body": "Changing priority from critical to blocker.",
    "created_at": "2010-07-05T11:07:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9426",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9426#issuecomment-89922",
    "user": "rlm"
}
```

Changing priority from critical to blocker.



---

archive/issue_comments_089923.json:
```json
{
    "body": "Changing priority from blocker to major.",
    "created_at": "2010-07-11T19:32:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9426",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9426#issuecomment-89923",
    "user": "rlm"
}
```

Changing priority from blocker to major.



---

archive/issue_comments_089924.json:
```json
{
    "body": "Changing keywords from \"\" to \"Sphinx documentation builder error\".",
    "created_at": "2010-11-03T16:07:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9426",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9426#issuecomment-89924",
    "user": "leif"
}
```

Changing keywords from "" to "Sphinx documentation builder error".



---

archive/issue_comments_089925.json:
```json
{
    "body": "Should a docbuild error just cause an exception to be raised, thus ending the build?  That wouldn't be hard to implement, I think.",
    "created_at": "2010-11-03T20:28:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9426",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9426#issuecomment-89925",
    "user": "jhpalmieri"
}
```

Should a docbuild error just cause an exception to be raised, thus ending the build?  That wouldn't be hard to implement, I think.



---

archive/issue_comments_089926.json:
```json
{
    "body": "Replying to [comment:6 jhpalmieri]:\n> Should a docbuild error just cause an exception to be raised, thus ending the build?  That wouldn't be hard to implement, I think.\n\nI would have implemented that if I felt it was appropriate. ;-)\n\nAn error in a single document should IMHO not stop / break the whole build, but should be propagated and reported (also) at the end, in a summary. Same for warnings, but even harder to implement. (See also #10200.)\n\nI actually do not understand why we do an equivalent of `os.system(\"sphinx ...\")`; as far as I know, Sphinx is itself written in Python and its functionality should therefore be directly accessible to us from the `builder.py` script. This way we would easily get the warnings as well.",
    "created_at": "2010-11-03T20:54:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9426",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9426#issuecomment-89926",
    "user": "leif"
}
```

Replying to [comment:6 jhpalmieri]:
> Should a docbuild error just cause an exception to be raised, thus ending the build?  That wouldn't be hard to implement, I think.

I would have implemented that if I felt it was appropriate. ;-)

An error in a single document should IMHO not stop / break the whole build, but should be propagated and reported (also) at the end, in a summary. Same for warnings, but even harder to implement. (See also #10200.)

I actually do not understand why we do an equivalent of `os.system("sphinx ...")`; as far as I know, Sphinx is itself written in Python and its functionality should therefore be directly accessible to us from the `builder.py` script. This way we would easily get the warnings as well.



---

archive/issue_comments_089927.json:
```json
{
    "body": "Replying to [comment:7 leif]:\n> Replying to [comment:6 jhpalmieri]:\n> > Should a docbuild error just cause an exception to be raised, thus ending the build?  That wouldn't be hard to implement, I think.\n> \n> I would have implemented that if I felt it was appropriate. ;-)\n\nLooks as if #10191 does exactly that, but only in one of the two cases.",
    "created_at": "2010-11-03T20:59:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9426",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9426#issuecomment-89927",
    "user": "leif"
}
```

Replying to [comment:7 leif]:
> Replying to [comment:6 jhpalmieri]:
> > Should a docbuild error just cause an exception to be raised, thus ending the build?  That wouldn't be hard to implement, I think.
> 
> I would have implemented that if I felt it was appropriate. ;-)

Looks as if #10191 does exactly that, but only in one of the two cases.



---

archive/issue_comments_089928.json:
```json
{
    "body": "I was unaware of this ticket and created #10191 (for the case where Sphinx fails catastrophically and aborts) and #10200 (for the case where Sphinx gives a WARNING or ERROR but continues).",
    "created_at": "2010-11-04T08:19:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9426",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9426#issuecomment-89928",
    "user": "jdemeyer"
}
```

I was unaware of this ticket and created #10191 (for the case where Sphinx fails catastrophically and aborts) and #10200 (for the case where Sphinx gives a WARNING or ERROR but continues).



---

archive/issue_comments_089929.json:
```json
{
    "body": "Replying to [comment:7 leif]:\n> An error in a single document should IMHO not stop / break the whole build, but should be propagated and reported (also) at the end, in a summary. Same for warnings, but even harder to implement. (See also #10200.)\n\nThis is actually implemented now in #10200 (needs_review).\n\nI propose to close this ticket as duplicate (given #10200).",
    "created_at": "2010-11-08T16:18:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9426",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9426#issuecomment-89929",
    "user": "jdemeyer"
}
```

Replying to [comment:7 leif]:
> An error in a single document should IMHO not stop / break the whole build, but should be propagated and reported (also) at the end, in a summary. Same for warnings, but even harder to implement. (See also #10200.)

This is actually implemented now in #10200 (needs_review).

I propose to close this ticket as duplicate (given #10200).



---

archive/issue_comments_089930.json:
```json
{
    "body": "Close as duplicate of #10200.",
    "created_at": "2010-11-09T09:31:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9426",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9426#issuecomment-89930",
    "user": "mvngu"
}
```

Close as duplicate of #10200.



---

archive/issue_comments_089931.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2010-11-09T09:31:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9426",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9426#issuecomment-89931",
    "user": "mvngu"
}
```

Resolution: duplicate
