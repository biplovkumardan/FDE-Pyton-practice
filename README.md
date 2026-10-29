**Tutorial Path:** https://learn.nareshit.com/courses/take/new-course-1343/multimedia/79328352-session-12-27th-oct 

***Issue 1:***
**Fix jupyter notebook path issue**

<img width="555" height="805" alt="image" src="https://github.com/user-attachments/assets/d126ad96-d9b9-452c-9f68-305b1cb63413" />



***Issue 2:***
**If notebook module not found**

<img width="844" height="108" alt="image" src="https://github.com/user-attachments/assets/335a7e04-45bf-44d3-839c-b072b07cd27c" />




***Altrnative solution:***
I am using **Anaconda Prompt** to open a notebook:

(base) C:\Users\Hi>cd /d D:\Study\FDE\myGitLocalRepos\Python-Practice-FDE\FDE-Pyton-practice

(base) D:\Study\FDE\myGitLocalRepos\Python-Practice-FDE\FDE-Pyton-practice>jupyter notebook

<img width="802" height="100" alt="image" src="https://github.com/user-attachments/assets/3a148c00-01d2-4a40-b87f-1795f9be08a4" />



****Git Steps: IMPORTANT****

**To Update the GitHub with updated file:**
<img width="1117" height="747" alt="image" src="https://github.com/user-attachments/assets/a776346e-5901-4062-97a5-4bfb814772aa" />


***Issue 3:***

I think i know the reason for this merge issue. I used to update ReadMe.md file directly in GitHub. But the ipynb files, I am updating in my local working directory and try to push my ipynb files. That time this merge conflict is coming. Help me to rectify my mistake and correct steps to do the merge or pull before push in github

![alt text](image.png)

![alt text](image-1.png)


You hit the nail on the head! Your diagnosis is 100% correct.

When you edit files (like README.md) directly on the GitHub website, GitHub creates a brand-new commit on the remote repository. Your local laptop doesn't know about that commit yet. Meanwhile, when you work on your .ipynb files locally and try to push, Git realizes that the remote history and your local history have diverged, resulting in that merge prompt.

To avoid this headache in the future, you should follow the Golden Rule of Git: Always Pull Before You Push (and ideally, pull before you even start working).

![alt text](image-2.png)

![alt text](image-3.png)
