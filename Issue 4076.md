# Issue 4076: notebook -- <$> ... </$> and <$$> ... </$$> don't work in the notebook as the help page claims

Issue created by migration from https://trac.sagemath.org/ticket/4076

Original creator: TimothyClemans

Original creation time: 2008-09-08 12:38:54

Assignee: boothby

Help page claims:

```
Begin an input block with %html and it will be output as HTML. Use the <sage>...</sage> tag to do computations in an HTML block and have the typeset output inserted. Use <$>...</$> and <$$>...</$$> to insert typeset math in the HTML block. This does not require latex.
```



The html function clearly doesn't properly deal with the < and >. 

```
sage: html(r'let <$>K = \mathbb{Q} 17 (\sqrt{-2})</$>')
<html><font color='black'>let <<span class="math">>K = \mathbb{Q} 17 (\sqrt{-2})</</span>></font></html>

sage: html(r'let <$$>K = \mathbb{Q} 17 (\sqrt{-2})</$$>')
<html><font color='black'>let <<div class="math">>K = \mathbb{Q} 17 (\sqrt{-2})</</div>></font></html>
```


The output should be the same as 

```
sage: html(r'let $K = \mathbb{Q} 17 (\sqrt{-2})$')
<html><font color='black'>let <span class="math">K = \mathbb{Q} 17 (\sqrt{-2})</span></font></html>

sage: html(r'let $$K = \mathbb{Q} 17 (\sqrt{-2})$$')
<html><font color='black'>let <div class="math">K = \mathbb{Q} 17 (\sqrt{-2})</div></font></html>
```


This is based on the bug report given on 8/25/08 by john.perry`@`usm.edu available at http://spreadsheets.google.com/pub?key=pCwvGVwSMxTzT6E2xNdo5fA


---

Attachment


---

Comment by mhansen created at 2008-09-08 14:10:05

Isn't the right fix to correct the documentation instead?  I don't see why we'd want to support <$>, etc.


---

Comment by TimothyClemans created at 2008-09-08 18:04:12

I thought about that doing that, but decided to be back compatible with old documentation.


---

Comment by mhansen created at 2008-09-09 01:41:27

I think the documentation fix is the correct one since there's no real reason to support <$> and <$$> and it's just more cruft to carry around.


---

Attachment

Patch sage-4076_2.patch fixes the documentation.


---

Comment by jhpalmieri created at 2008-10-17 23:08:00

I'm confused; am I just supposed to use sage-4076_2.patch and ignore sage-4076_1.patch?  If so, this gets a positive review -- it's a simple change to the notebook help page.


---

Comment by jhpalmieri created at 2008-10-24 17:29:09

I'm giving *sage-4076_2.patch* a positive review; it should be merged.  As far as I can tell, *sage-4076_1.patch* is not needed, and should be discarded.


---

Comment by mabshoff created at 2008-10-26 13:41:56

I think sage-4076_1.patch is still needed. 

Timothy: can you comment?

Cheers,

Michael


---

Comment by TimothyClemans created at 2008-10-26 18:47:51

I don't think the first one is needed.


---

Comment by mabshoff created at 2008-10-27 02:11:25

Merged in Sage 3.2.alpha1


---

Comment by mabshoff created at 2008-10-27 02:11:25

Resolution: fixed
