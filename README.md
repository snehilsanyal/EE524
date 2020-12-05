## Welcome to EE524 (Jul-Nov 2020)

## [Final submission for Projects: 6th December 2020]()
## [Viva Examination on 6th and 7th December 2020]()

Hello friends... Hope you are safe and sound.

I hope you are all excited to learn about Machine Learning. In this semester, you must be going through the Machine Learning Course offerred by Professor [Manas Kamal Bhuyan](https://www.iitg.ac.in/mkb/) sir. 

This is the official course webpage for the course EE524 Machine Learning Laboratory which will complement the course Introduction to Machine Learning. We will be using [Python](https://www.python.org/) an open source software to run our codes.


```python
import os
import glob
import numpy as np
import pandas as pd
import tensorflow as tf
sess = tf.Session()
op = sess.graph.get_operations()
print([m.name for m in op]) #print the name of operations
print([m.values() for m in op]) #print the tensor produced by these operations
```


As mentioned, in the [instruction manual](https://drive.google.com/file/d/1WB9rOMm190cqKGt-76TFDTX6vgbtsUts/view?usp=sharing) we will also use libraries like Numpy, Matplotlib, Pandas and Scikit-Learn.
> A breakthrough in Machine Learning 
>
> would be worth 10 microsofts. 
> 
> -Bill Gates 


> A baby learns to crawl, walk and then run.
>
> We are in the crawling stage, when it comes to applying Machine Learning.
> 
> -Dave Waters


### Objectives of this lab:
1. Learn about the concepts in Machine Learning from data generation, handling, preprocessing.
2. Learn about different algorithms in Machine Learning.
3. Improve coding skills in Python.
4. Implement these concepts on your own.
5. Create something as an outcome of this lab course.


### Lab evaluation Structure:
- **Continuous Evaluations:** 50 Marks (Through Assignments)
- **Viva:** 20 Marks (After all submissions)
- **Mini Project:** 30 Marks (Will be given after 6th Lab Session)


### Timeline:
We have a total of 12 labs in this session. Everything will be online due to the pandemic. We will try to complete most of the important algorithms required for you to have a good background in Machine Learning. We will be pushing assignments, have doubt sessions and will evaluate your assignments. Assignments will be weekly.


- **Weekly Assignment:** Each Monday in the Outlook Group [Grp_grp_ee-524ml-lab](https://iitgoffice.sharepoint.com/sites/Grp_grp_ee-524ml-lab) and [Slack Channel](https://app.slack.com/client/T01A6UP4R9Q)
- **Doubt Sessions:** Every Friday via [MS Teams](https://teams.microsoft.com/_#/school/conversations/General?threadId=19:a65717b18fe94e899fa357c2f8ace118@thread.tacv2&ctx=channel)
- **Assignment Submission:** Every Sunday (EOD) in the assignments branch of this [github repository](https://github.com/snehilsanyal/EE524/tree/assignments).

### Announcements:

- **7th December 2020** Viva for batch 2
- **6th December 2020** Final submission of projects and Viva for batch 1
- **23rd November 2020** Assignment 7 has been released, Project titles submission start
- **18th November 2020** Assignment 6 has been released
- **9th November 2020** Assignment 5 has been released
- **17th Oct 2020** Assignment 4 has been released
- **7th Oct 2020** Assignment 3 has been released
- **22nd Sept 2020** Assignment 2 has been released
- **7th Sept 2020**: Assignment 1 has been released
- **11th Sept 2020**: Doubt Session for Assignment 1 is over
- **17th Sept 2020**: Assignment Submission link is released
- **20th Sept 2020**: Submission Deadline for Assignment 1
- **22nd Sept 2020**: Assignment 2 has been released
- **25th Sept 2020**: Doubt session for submission and Assignment 2 is over
- **4th Oct 2020**: Assignment 2 Submission Deadline.  


### Assignments:

1. **Assignment 1 (Ungraded):**
**Fundamentals of Python**  
Release Date: 7th September 2020  
Doubt Session: 11th September 2020  
Submission Date: 20th September 2020  
[Instruction Manual](https://drive.google.com/file/d/1WB9rOMm190cqKGt-76TFDTX6vgbtsUts/view?usp=sharing) | [PDF](Assignments/Assignment_1.pdf) | [Resources]() | [Solution](https://github.com/snehilsanyal/EE524/blob/assignments/Assignment1/Vasantha_204102302/ML%20(%20Assignment-1)%20(2).ipynb)

2. **Assignment 2 (Graded): Linear Regression and Error Surfaces**  
Release Date: 22nd Sept 2020  
Doubt Session: 2nd Oct 2020  
Submission Date: 4th Oct 2020  
[Assignment](Assignments/Assignment_2.pdf) | [Resources](https://machinelearningmastery.com/linear-regression-for-machine-learning/) | [Solution](https://github.com/snehilsanyal/EE524/blob/assignments/Assignment2/NileshGupta_206102031/Assignment2.ipynb)


3. **Assignment 3(a) (Graded): Basic Plotting**  
Release Date: 7th Oct 2020  
Doubt Session: 10th Oct 2020  
Submission Date: 11th Oct 2020  
[Assignment](Assignments/Assignment_3a.pdf) | [Resources](https://www.tutorialspoint.com/matplotlib/matplotlib_simple_plot.htm) | [Solution](https://github.com/snehilsanyal/EE524/blob/assignments/Assignment3/AviKhandelwal_204102301/AviKhandelwal_204102301_Assignment_3a.ipynb) 

4. **Assignment 4 (Graded):**
**Bayes Theorem and Naive Bayes Classifier**  
Release Date: 17th October 2020  
Doubt Session: 24th October 2020  
Submission Date: 27th October 2020  
[Assignment](Assignments/Assignment_4.pdf) | [Resources]() | [Solution](https://github.com/snehilsanyal/EE524/blob/assignments/Assignment4/AviKhandelwal_204102301_Assignment-4.ipynb) 

5. **Assignment 5 (Graded):**
**K Nearest Neighbours and K Means Algorithm**  
Release Date: 9th November 2020  
Doubt Session: 13th November 2020  
Submission Date: 15th November 2020  
[Assignment](Assignments/Assignment_5.pdf) | [Dataset](Assignments/dataset.csv) | [Solution](https://github.com/snehilsanyal/EE524/blob/assignments/Assignment5/BibekGoswami_206102011/Assignment5.ipynb)

6. **Assignment 6 (Graded):**
**Support Vector Machines, PCA and LDA**  
Release Date: 18th November 2020  
Submission Date: 29th November 2020  
[Assignment](Assignments/Assignment6.pdf) | [Dataset](Assignments/dataset.csv) | [Solution](https://github.com/snehilsanyal/EE524/blob/assignments/Assignment6/SonuKumari_204102314/Assignment_6_ML_LAB.ipynb) 

7. **Assignment 7 (Graded):**
Release Date: 23rd November 2020  
Submission Date: 29th November 2020  
[Assignment](Assignments/Assignment7.pdf) | [Dataset](Assignments/dataset.csv) | [Solution](https://github.com/snehilsanyal/EE524/blob/assignments/Assignment7/BibekGoswami_206102011/Assignment_7.ipynb) 
****

### Team communication:
1. [Slack Channel EE524](https://app.slack.com/client/T01A6UP4R9Q) (For conversation and doubts)
2. [Moodle Link](https://www.iitg.ac.in/moodle/course/view.php?id=790) (Theory course)
3. [Outlook Group](https://iitgoffice.sharepoint.com/sites/Grp_grp_ee-524ml-lab)
4. [Github Repository](https://github.com/snehilsanyal/EE524/tree/assignments) (For submitting assignments)


### Resources:
1. [Python Course](https://www.youtube.com/watch?v=oVp1vrfL_w4&list=PLQVvvaa0QuDe8XSftW-RAxdo6OmaeL85M)
2. [Youtube Machine Learning](https://www.youtube.com/watch?v=PPLop4L2eGk&list=PLLssT5z_DsK-h9vYZkQkYNWcItqhlRJLN) and [Coursera Machine Learning](https://www.coursera.org/learn/machine-learning)
3. [NPTEL PK Biswas Pattern Recognition](https://www.youtube.com/watch?v=U5xsX2ersHQ&list=PLbRMhDVUMngcx-ATexXZH_-u1wsIGIiyS)
4. [Numpy Tutorial](https://www.youtube.com/watch?v=QUT1VHiLmmI)
5. [Pandas Tutorial](https://www.youtube.com/watch?v=yzIMircGU5I&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y)
6. [Matplotlib Tutorial](https://www.youtube.com/watch?v=q7Bo_J8x_dw&list=PLQVvvaa0QuDfefDfXb9Yf0la1fPDKluPF)
7. Youtube channels for your reference:
 [Socratica](https://www.youtube.com/user/SocraticaStudios)|
 [SentDex](https://www.youtube.com/user/sentdex)|
 [Siraj Raval](https://www.youtube.com/channel/UCWN3xxRkmTPmbKwht9FuE5A)
 

### Teaching Assistants:
![Nadeem Atif](https://www.iitg.ac.in/mkb/wp-content/uploads/2019/07/Atif.png)

**Nadeem Atif**: 
Research Scholar, 
EEE Department, IIT Guwahati |
Email: atif176102103@iitg.ac.in |
Contact: 7302099843

![Snehil Sanyal](https://media-exp1.licdn.com/dms/image/C4E03AQGWGKkj-EB8kg/profile-displayphoto-shrink_200_200/0?e=1609977600&v=beta&t=RWpiEuwwZH7xHJgb19TLXY2d9dBWY-TviPVdZ84vldQ)

**Snehil Sanyal**:
Research Scholar,
EEE Department, IIT Guwahati |
Email: ssanyal@iitg.ac.in |
Contact: 9399690211 

**H Balaji**:
M.Tech 2nd year,
EEE Department, IIT Guwahati |
Email: hbalaji@iitg.ac.in |
Contact: 9441791359
