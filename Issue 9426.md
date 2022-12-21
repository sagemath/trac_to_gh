# Issue 9426: Docbuilder ignores return code from subprocess.call()

Issue created by migration from Trac.

Original creator: leif

Original creation time: 2010-07-04 22:05:00

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




---

Comment by leif created at 2010-07-04 22:53:35

It's trivial to change _the message_ on non-zero return values, but I think errors should somehow be propagated, s.t. doc build errors aren't drowned in the flood of other messages.


---

Comment by rlm created at 2010-07-05 11:07:02

Changing this to blocker at least for now...


---

Comment by rlm created at 2010-07-05 11:07:02

Changing priority from critical to blocker.


---

Comment by rlm created at 2010-07-11 19:32:53

Changing priority from blocker to major.


---

Comment by leif created at 2010-11-03 16:07:00

Changing keywords from "" to "Sphinx documentation builder error".


---

Comment by jhpalmieri created at 2010-11-03 20:28:13

Should a docbuild error just cause an exception to be raised, thus ending the build?  That wouldn't be hard to implement, I think.


---

Comment by leif created at 2010-11-03 20:54:46

Replying to [comment:6 jhpalmieri]:
> Should a docbuild error just cause an exception to be raised, thus ending the build?  That wouldn't be hard to implement, I think.

I would have implemented that if I felt it was appropriate. ;-)

An error in a single document should IMHO not stop / break the whole build, but should be propagated and reported (also) at the end, in a summary. Same for warnings, but even harder to implement. (See also #10200.)

I actually do not understand why we do an equivalent of `os.system("sphinx ...")`; as far as I know, Sphinx is itself written in Python and its functionality should therefore be directly accessible to us from the `builder.py` script. This way we would easily get the warnings as well.


---

Comment by leif created at 2010-11-03 20:59:47

Replying to [comment:7 leif]:
> Replying to [comment:6 jhpalmieri]:
> > Should a docbuild error just cause an exception to be raised, thus ending the build?  That wouldn't be hard to implement, I think.
> 
> I would have implemented that if I felt it was appropriate. ;-)

Looks as if #10191 does exactly that, but only in one of the two cases.


---

Comment by jdemeyer created at 2010-11-04 08:19:41

I was unaware of this ticket and created #10191 (for the case where Sphinx fails catastrophically and aborts) and #10200 (for the case where Sphinx gives a WARNING or ERROR but continues).


---

Comment by jdemeyer created at 2010-11-08 16:18:29

Replying to [comment:7 leif]:
> An error in a single document should IMHO not stop / break the whole build, but should be propagated and reported (also) at the end, in a summary. Same for warnings, but even harder to implement. (See also #10200.)

This is actually implemented now in #10200 (needs_review).

I propose to close this ticket as duplicate (given #10200).


---

Comment by mvngu created at 2010-11-09 09:31:19

Close as duplicate of #10200.


---

Comment by mvngu created at 2010-11-09 09:31:19

Resolution: duplicate
