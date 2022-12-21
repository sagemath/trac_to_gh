# Issue 2896: Notebook can't handle publishing of Umlauts (UTF-8)

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2008-04-12 12:05:51

Assignee: boothby

CC:  schilly

Keywords: utf-8

Lars Fischer wrote on [http://groups.google.com/group/sage-support/browse_thread/thread/a2e3a6c7e12a1e33 sage-support](http://groups.google.com/group/sage-support/browse_thread/thread/a2e3a6c7e12a1e33 sage-support) (and I edited for the bug report):

Please note that before I published the worksheet the Ü in the cells
were a Ü, after publishing, the "Ü" look like "�" in the published document.

My workflow was
 * New worksheet
 * Edit, and I inserted everything in the Edit-Field.
 * Use, and evaluate the first two cells.
 * Then I published.


```
print "Ü"
///
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
UnicodeDecodeError: 'utf8' codec can't decode byte 0xdc in position 0:
unexpected end of data
```



```
print "Ue" #print "Ü"
///
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
UnicodeDecodeError: 'utf8' codec can't decode byte 0xdc in position 0:
unexpected end of data
```




---

Comment by lars.fischer created at 2008-04-12 12:46:06

Changing keywords from "utf-8" to "utf-8, notebook, encoding".


---

Comment by lars.fischer created at 2008-04-12 12:46:06

Hello,

what happened when I click on publish, is only a symptom. My problem is really simple:
*I cannot use unicode inside a notebook cell.*

Please create a new empty worksheet and enter the next examples in different cells, to see the problem:

```
# this is what I want to do, but I only get exceptions
print 'Ü'
# also exceptions
print u'Ü'
print ur'Ü'

# This works but it is ugly. If I want to convince some students to use sage with this, they will laugh
print u'\xdc'   
# Ü 

# An this is interesting because the same question mark occurs when I hit for example publish:
print '\xdc'     
# �  
```


With best regards,

Lars Fischer


---

Comment by lars.fischer created at 2008-04-12 13:04:56

Hello,

When I open a new worksheet, I check that Firefox is set to unicode. I enter the print statements from my previous comment.

Then I click on Text. And it seems that the Text-View is no longer in Unicode. To see what I mean, please toggle Encoding between Unicode and Western. 

With best regards,

Lars Fischer


---

Comment by mabshoff created at 2008-04-20 05:53:59

This sounds very much like #1477. 

Cheers,

Michael


---

Comment by malb created at 2008-08-21 22:34:06

Changing assignee from boothby to tclemans.


---

Comment by AlexGhitza created at 2009-01-23 02:49:42

Changing type from defect to enhancement.


---

Comment by mabshoff created at 2009-03-23 21:38:16

Fixed via #4547 and #5211.

Cheers,

Michael


---

Comment by mabshoff created at 2009-03-23 21:38:16

Resolution: fixed
