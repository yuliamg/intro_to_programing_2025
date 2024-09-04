# Introduction to Computing for Biophysicists
#### (AKA: Intro to Programming / Programming Fundamentals)
## Fall 2024 Syllabus

**Course Days/Hours:** Sept 10 – 12, 16 – 20 from 9-11AM
**Location:** GH 227 - Teaching Lab
**Instructor(s):** [Zack Mawaldi](mailto:zack.mawaldi@ucsf.edu)

## Course Description:
Computing is as essential as pipetting for success in graduate school. This practical course is intended to ensure that students without any background in scientific computing can become conversant in the fundamentals they need to succeed in our program, including:

- How to use the terminal, move and manipulate files
- How to script in Python
- How to basic data science / analysis via numpy, pandas, and graphing

We aim to introduce students to computational concepts by leveraging their algorithmic understanding of molecular biology. Students are already familiar with data structures (the genetic code is a dictionary) and for loops (5'-3' transcription) - the challenge is how to formally code what we already understand in a syntax that makes sense to a computer. 


Finally, with the development of new AI tools (ChatGPT, Github Co-pilot, etc), "no code" coding is now possible and gaining power. In fact, [a study has demonstrated that large language models can solve about 80% of introductory bioinformatic tasks, but the rest need additional prompting](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1011511). We hypothesize that students will be better able to leverage such tools with the fundamental algorithmic thinking we aim to introduce in this course. 


*Accommodations for students with disabilities*: The Graduate Division embraces all students, including students with documented disabilities. UCSF is committed to providing all students equal access to all of its programs, services, and activities. Student Disability Services (SDS) is the campus office that works with students who have disabilities to determine and coordinate reasonable accommodations. Students who have, or think they may have, a disability are invited to contact SDS (StudentDisability@ucsf.edu); or 415-476-6595) for a confidential discussion and to review the process for requesting accommodations in classroom and clinical settings. More information is available online at http://sds.ucsf.edu. Accommodations are never retroactive; therefore students are encouraged to register with Student Disability Services (http://sds.ucsf.edu/) as soon as they begin their programs. UCSF encourages students to engage in support seeking behavior via all of the resources available through Student Life, for consistent support and access to their programs.

*Commitment to Diversity, Equity and Inclusion*: The course instructor value the contributions, ideas and perspective of all students. It is my intent that students from diverse backgrounds be well-served by this course, that students' learning needs be addressed both in and out of class, and that the diversity that the students bring to this class be viewed as a resource, strength and benefit. It is my intent to present materials and activities that are respectful of diversity: gender identity, sexuality, disability, age, socioeconomic status, ethnicity, race, nationality, religion, and culture. However, we also acknowledge that computing systems were designed by people with biases and therefore likely have those biases built in. Additionally, the field is phasing out offensive terminology for some processes - but such terminology may be present in linked material from the class page. The instructor is committed to continuous improvement of teaching practices and our learning environment. I value input from students and your suggestions are encouraged and appreciated. Please let the course director or program leadership know ways to improve the effectiveness of the course for you personally, or for other students or student groups. (modeled after CCB and [Brown University's Diversity & Inclusion Syllabus Statements](https://www.brown.edu/sheridan/teaching-learning-resources/inclusive-teaching/statements))

## Course structure
This is a hands-on practical course - we will be moving at the pace of the student who completes the task last! This is my first time teaching this course and we expect that the level of prior knowledge will be quite heterogeneous. Students should keep in mind that the goal is to understand each aspect of what we are doing, not to finish first. There are no grades - this is about setting up a foundation for success in the Biophysics graduate program. 


We will begin with understanding the relationship between the terminal, filesystem, and the GUI. We will then move to  python scripting, grounding ourselves in creating python versions of different processes of the central dogma. Finally, if there is time, we will explore ways to handle and visualize data using plotting libraries. 

## Schedule

| **Day**       | **Date**       | **Theme**                   | Concepts                                                                                                                                                                                                                       |
| ------------- | -------------- | --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Wednesday** | **09/04/2024** | Wynton (onboarding)         | Terminal basics, ssh, scp, Wynton sign-up / sign-in, SGE, job creation + submission                                                                                                                                            |
| **Tuesday**   | **09/10/2024** | Terminal                    | Quick course intro; terminal basics: pwd, ls, cd, mkdir, touch, cp, mv, rm; text viewing (cat, head, tail); intro to vim; basic piping and redirection (\|, >, >>); simple bash scripting; Miniconda install (if time permits) |
| **Wednesday** | **09/11/2024** | Python Day1                 | Algorithms and algorithmic + programming and Python concepts (writing and running scripts, basic maths, commenting, variables, strings, slicing, user input) + `greeter.py`                                                    |
| **Thursday**  | **09/12/2024** | Python Day2                 | Lists, for and while loops, if, elif, else, boolean expressions, indentation, file handling + `transcriber.py`                                                                                                                 |
| **Friday**    | **09/13/2024** | **BP RETREAT** (no meeting) | **BP RETREAT** (no meeting)                                                                                                                                                                                                    |
| ###           | ###            | ###                         | ###                                                                                                                                                                                                                            |
| **Monday**    | **09/16/2024** | Python Day3                 | Dictionaries, functions, quick glance at OOP, + Mini project (`DNA_to_AA.py`)                                                                                                                                                  |
| **Tuesday**   | **09/17/2024** | Numpy + Graphing Day1       | Jupyter Notebook, Arrays, array types, operations, axis, slicing, array visualization, matplotlib, plt                                                                                                                         |
| **Wednesday** | **09/18/2024** | Pandas + Graphing Day2      | Pandas, dataframe, csv→dataframe, dict→dataframe, dataframe→csv                                                                                                                                                                |
| **Thursday**  | **09/19/2024** | Buffer day                  |                                                                                                                                                                                                                                |
| **Friday**    | **09/20/2024** | Buffer day                  |                                                                                                                                                                                                                                |
