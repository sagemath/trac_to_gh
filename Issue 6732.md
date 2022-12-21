# Issue 6732: spell-check all modules under sage/server

Issue created by migration from Trac.

Original creator: mvngu

Original creation time: 2009-08-11 08:40:06

Assignee: tba

As the subject says.


---

Comment by mvngu created at 2009-08-11 17:23:04

based on Sage 4.1.1.rc2


---

Attachment


```
$ cd $SAGE_ROOT/devel/sage/sage/server/notebook; grep rrr *.py
./notebook.py:        except AttributeErrro:
```

Separate ticket?


---

Comment by mvngu created at 2009-08-11 23:02:01

Replying to [comment:2 mpatel]:
> {{{
> $ cd $SAGE_ROOT/devel/sage/sage/server/notebook; grep rrr *.py
> ./notebook.py:        except AttributeErrro:
> }}}
> Separate ticket?
Nice catch. Can you please open a ticket for that? Here's a relevant snippet from the file `sage/server/notebook/notebook.py`:

```
try:
    dir = self.__absdir
except AttributeErrro:
    dir = self.__dir
import shutil
# We ignore_errors because in rare parallel doctesting                  
# situations sometimes the directory gets cleaned up too                
# quickly, etc.                                                         
shutil.rmtree(dir, ignore_errors=True)
```

As I see it, this is a case where only some of the execution paths of the above code have been doctested. One should endeavour to test all the execution paths of a function. In particular, doctest the case where the try block is successfully executed. And also the case where the try block fails so that the flow of control then jumps to the except block, in which case the Python interpreter would complain about syntax errors. It would be nice to have some sort of static code analysis tool for Sage, something that would catch errors that would be reported by a compiler of a statically typed language such as C/C++, Java. See Dough Hellmann's [article](http://www.doughellmann.com/articles/CompletelyDifferent-2008-03-linters/index.html) for some inspiration on this issue.


---

Comment by mpatel created at 2009-08-13 01:03:49

Note: I haven't checked that these are the only spelling errors.

I think the "winner" here is `fludded`.


---

Comment by mvngu created at 2009-08-13 07:59:45

Resolution: fixed


---

Comment by mvngu created at 2009-08-13 07:59:45

Replying to [comment:4 mpatel]:
> Note: I haven't checked that these are the only spelling errors.
Given that I spell-checked all the modules in the Sage library in 3 days, I mostly used a spell checker (in particular, aspell) to do most of the hard work. Occasionally I did read some snippets from library files. The time constraint did not allow me to actually read through all the library files. That would catch many more typos, but would also require substantially more time than what has been allocated for the current release. The release of Sage 4.1.1 has been delayed for far too long now. Originally it was planned to be released on the 01st August 2009, but it has dragged on for over a week now, in part due to #6645 and some unexpected issues that needed to be sorted out.
