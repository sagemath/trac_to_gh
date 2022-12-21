# Issue 9608: Docbuild warnings in sage/interfaces/matlab.py

Issue created by migration from Trac.

Original creator: mpatel

Original creation time: 2010-07-27 07:08:40

Assignee: mvngu

CC:  ddrake mhansen rossk leif

Docbuild warnings in Sage 4.5.2.alpha1:

```sh
$ ./sage -docbuild all html -j
[...]
/mnt/usb1/scratch/mpatel/tmp/sage-4.5.2.alpha1/local/lib/python2.6/site-packages/sage/interfaces/matlab.py:docstring of sage.interfaces.matlab.Matlab.strip_answer:6: (WARNING/2) Block quote ends without a blank line; unexpected unindent.
/mnt/usb1/scratch/mpatel/tmp/sage-4.5.2.alpha1/local/lib/python2.6/site-packages/sage/interfaces/matlab.py:docstring of sage.interfaces.matlab.Matlab.strip_answer:9: (WARNING/2) Block quote ends without a blank line; unexpected unindent.
[...]
```


Possibly related ticket: #2119.


---

Attachment

Make the docstring raw


---

Comment by mpatel created at 2010-07-27 07:55:46

Changing status from new to needs_review.


---

Comment by ddrake created at 2010-07-27 08:23:22

A one-character patch! Nice.

It does get rid of the warning for me, but I'd like to understand why the docstring needs to be raw. How does that fix the unindent warning?


---

Comment by mpatel created at 2010-07-27 08:44:37

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

Comment by ddrake created at 2010-07-28 01:13:05

Replying to [comment:3 mpatel]:
> Not using a raw string but replacing the `\n`s with `\\n`s should also work.

Hrm, doing that doesn't fix the problem -- the function then gets a string with no newlines, but with literal "\n" bits.

I'm almost certain that making the docstring raw is the right thing to do, but I'd like to have someone who knows more about doctesting and Sphinx look at this.


---

Comment by jhpalmieri created at 2010-07-28 05:40:15

> Hrm, doing that doesn't fix the problem -- the function then gets a string with no newlines, but with literal "\n" bits.

Isn't that what you want?  You're defining s to be a particular string, one containing "\n" in it (to give a newline), and you want each "\n" to appear as such in the reference manual.  That is,  `s = '\nans =\n\n     2\n'` is a valid way to define a python string, and it should appear this way in the reference manual.  If you want to define a string containing actual new lines, you would have to use triple quotes, wouldn't you?

This makes sense to me, and I've seen other docstring errors and fixes just like this in the past.  The particular docstring here looks much better after the patch, and there are no warnings.  Positive review.


---

Comment by jhpalmieri created at 2010-07-28 05:40:15

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-07-29 04:50:55

Resolution: fixed
