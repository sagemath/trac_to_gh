# Issue 3733: notebook -- add something to reference manual about user-customizable css (easy ticket)

Issue created by migration from https://trac.sagemath.org/ticket/3733

Original creator: was

Original creation time: 2008-07-28 05:41:36

Assignee: boothby


```
I am working on a project this summer that uses SAGE to assemble some
interactive Calculus lessons, and I was hoping to do something like
this. So thank you very much!

Will this be placed in the manual or the Wiki?

regards
john perry

On May 27, 9:57 am, "William Stein" <wst...@gmail.com> wrote:
> Hi,
>
> I've always wondered why nobody creates nice stylized "skins", etc.
> for the notebook.
> It just occurred to me that though I made it trivial to change the
> notebook css on the
> fly, nobody knows how.  If you would like to make your Sage notebook
> look totally
> different, here's a quick tutorial (assumes you are not using the
> vmware version of
> the notebook):
>
> 1. See attached screenshot.
>
> 2. Start your *own* notebook server running locally on your computer.
>
> 3. Make a new file $HOME/.sage/notebook.css with these contents:
>
> textarea.cell_input {
>   color:#003300;
>   border: 0px;
>   font-family: monaco;
>
> }
>
> div.cell_not_evaluated {
>     border-left: 3px solid #ff8888;
>
> }
>
> td.cell_number_running {
>    border-left:20px solid orange;
>
> }
>
> 4. Press refresh in your web browser and observe that the above css takes
> effect thus changing the style of your notebook.
>
> 5. You can change a lot.  To get a feel for the options seehttp://localhost:8000/css/main.css
> where 8000 is replaced by whatever port your notebook runs on.
>
> This feature has been in Sage for two years, but I don't think anybody
> has ever used it.
>
>  -- William
```



---

Comment by was created at 2009-11-19 23:26:47

Changing status from new to needs_review.


---

Attachment

Note only does this add the remark to the manual, but also sphinxifies the ``notebook?`` docstring.


---

Comment by timdumol created at 2009-12-06 07:39:18

I didn't know this existed until now. Positive review. I've added a few more improvements to the ReST docstring at #7611.


---

Comment by was created at 2009-12-08 19:59:55

Resolution: fixed


---

Comment by was created at 2009-12-08 19:59:55

merged into sagenb-0.4.6.
