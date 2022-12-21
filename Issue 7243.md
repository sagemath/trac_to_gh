# Issue 7243: bashisms in extcode-4.1.2/pari/dokchitser/testall

Issue created by migration from Trac.

Original creator: tabbott

Original creation time: 2009-10-19 00:09:55

Assignee: tbd

CC:  david.kirkby@onetel.net mhansen

In the extcode spkg, pari/dokchitser/testall uses bashisms but has a /bin/sh #! line:

#!/bin/sh
echo "\\r ex-bsw" | sage -gp
echo "\\r ex-chgen" | sage -gp

We should change the #! line to

#!/bin/bash



---

Attachment


---

Comment by mhansen created at 2009-10-19 04:08:00

Changing status from new to needs_review.


---

Comment by drkirkby created at 2009-12-03 05:12:23

Changing status from needs_review to needs_work.


---

Comment by drkirkby created at 2009-12-03 05:12:23

I think the


```

#!/usr/bin/env bash
```


(from memory, so might not be right)

is better, as bash is not always installed in /bin


```
bash-2.04$ uname -a
HP-UX hpbox B.11.11 U 9000/785 2016698240 unlimited-user license
bash-2.04$ ls /bin/bash
/bin/bash not found
bash-2.04$ which bash
/opt/OpenSource/bin/bash
bash-2.04$ which env
/usr/bin/env
bash-2.04$
```



---

Comment by tabbott created at 2009-12-16 21:34:13

Yeah, using '#!/usr/bin/env bash' should be correct.


---

Attachment


---

Comment by tabbott created at 2009-12-18 02:31:15

I posted a new patch reflecting that change.


---

Comment by drkirkby created at 2009-12-18 07:09:45

That looks safe and reliable to me, so I'll set this to 'needs review' then set it to 'positive'. 

Dave


---

Comment by drkirkby created at 2009-12-18 07:09:45

Changing status from needs_work to needs_review.


---

Comment by drkirkby created at 2009-12-18 07:09:53

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2009-12-19 23:45:35

Resolution: fixed
