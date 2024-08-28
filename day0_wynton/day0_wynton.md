# Day 0: Introduction to Wynton

This tutorial is designed to familiarize UCSF 1st year Biophysics students to Wynton High Performance Computing (HPC) cluster. It covers everything from creating an account to running your first job, providing the backbone knowledge required to efficiently use Wynton’s resources. By the end, you'll be comfortable navigating Wynton and setting up + submitting jobs.


Credit: Most of the information from this page was cobbled together using content from [Wynton's website](https://wynton.ucsf.edu/hpc/index.html) + some writing and rewriting by Zack Mawaldi and ChatGPT. The person who did the cobbling was Zack. Special thanks to Karson Chrispens for feedback and contribution.

### Outline
- [Day 0: Introduction to Wynton](#day-0-introduction-to-wynton)
  - [What is Wynton?](#what-is-wynton)
  - [Getting Started: Creating a Wynton Account](#getting-started-creating-a-wynton-account)
  - [Accessing Wynton](#accessing-wynton)
  - [Signing into Wynton](#signing-into-wynton)
- [Running Your First Job: 'Hello World' on the Wynton Cluster](#running-your-first-job-hello-world-on-the-wynton-cluster)
  - [Basics of Terminal Use](#basics-of-terminal-use)
  - [Running a 'Hello World' Job](#running-a-hello-world-job)
  - [Wynton ↔ Your Computer File Transfer](#files-transfer-between-your-computer-and-wynton-with-scp)
- [Beyond the Basics](#beyond-the-basics)
  - [Overview of Wynton Nodes](#overview-of-wynton-nodes)
  - [Wynton Job Queues](#wynton-job-queues)
  - [Using Scratch Storage](#using-scratch-storage)
  - [Additional Info / Tips](#additional-info--tips)
- [Need Help?](#Need-Help?)
---
### What is Wynton?

Wynton is a **High Performance Computing (HPC) cluster** composed of many interconnected computers (nodes) that collaborate to allow users to execute programs and process large datasets. It is commonly used in research for simulations, analyzing big datasets, or performing tasks that would be too time-consuming on a regular computer. Wynton enables you to leverage the combined power of the entire cluster, making it possible to handle more intensive computational tasks.

### Getting Started: Creating a Wynton Account
- [Request or Update an Account](https://ucsf.service-now.com/ucsfit?id=ucsf_sc_cat_item&sys_id=68f9651f1bf47c50683e0ed8624bcbac&sysparm_category=40c0305b7b92d000e2dc8180984d4d9f) *(Ideally done Day 1 of on-boarding)*

If your account request was accepted, you should've received an email that looked liked this:
```
Dear zack,  
  
Your Wynton account has now been created.  Your account is 'zack' and   
your temporary password is '[REDACTED]'.  Please note that you should immediately   
go to https://www.cgl.ucsf.edu/admin/chpass.py to give yourself  
a permanent password.  Your temporary password will expire in one week.  
  
Also note that you are required to adhere to the Wynton HPC User Agreement  
https://wynton.ucsf.edu/hpc/about/user-agreement.html.  Information  
about Wynton is available at: https://wynton.ucsf.edu/hpc/ and information  
about getting help is available at: https://wynton.ucsf.edu/hpc/support/index.html
  
Wynton admins
```

Please follow the `https://www.cgl.ucsf.edu/admin/chpass.py` link to reset your password. Change it into a permanent, secure, and ideally memorable password.

Now that we have an account set up, let us access Wynton!
### Accessing Wynton

Wynton is only accessible via the ***terminal***.

<details>
<summary>What is the terminal?</summary>
The **terminal** is a text-based interface that allows you to interact directly with your computer by typing commands, rather than using a graphical interface like clicking on icons. It might seem intimidating at first, but it's a powerful tool that gives you a lot of control over your computational environment.
</details>

### Signing into Wynton
- Open the terminal:
  - On Mac: Use `command ⌘ + space ␣` to open Spotlight, then type "terminal" to open it.
  - (This tutorial assumes you're using Mac or Linux. See [WSL](http://google.com/search?q=Windows+Subsystem+for+Linux) for Windows users)
- In the terminal, type:
  ```sh
  ssh your_name@log1.wynton.ucsf.edu
  ```
- Enter your password.

<details>
<summary>If successful, you'll see something like this:</summary>

```console
alice@MacOS ~ % ssh alice@log1.wynton.ucsf.edu
alice@log1.wynton.ucsf.edu's password:
Last failed login: Mon Aug 19 14:43:45 PDT 2024 from 172.26.44.11 on ssh:notty
There were 2 failed login attempts since the last successful login.
Last login: Mon Aug 19 14:43:27 2024 from 172.26.44.11
######################################################################
#           All connections are monitored and recorded.              #
#      Disconnect IMMEDIATELY if you are not an authorized user!     #
######################################################################

Welcome to the Wynton HPC environment.

For instructions, please see <https://wynton.ucsf.edu/hpc/>. The
support team holds office hours from 11am-noon on Tuesdays at:

<https://zoom.us/j/97716031058?pwd=NXhaeUtHVStWbklmSXhOVWJoM1BQQT09>
Meeting ID: 977 1603 1058, Password: 783363

Space on /wynton is for temporary storage of active data only. Unused
data should be moved to your own storage ASAP. Wynton storage is not
backed up, and stuff happens ...

Change of password takes up to 10 minutes to be effective. Please see
<https://wynton.ucsf.edu/hpc/howto/change-pwd.html> for instructions.

IMPORTANT: Data containing Protected Health Information (PHI) must not
be transferred to, mounted on, or processed on Wynton other than in
the Wynton PHI environment. To apply for a Wynton PHI account, please
see <https://wynton.ucsf.edu/hpc/about/wynton-phi.html>.

This login node is for job submission only. The system administrators
reserve the right to kill any long running processes on these nodes
without warning. Use a development node for prototyping.
[alice@log1 ~]$
```


</details>

---

## Running Your First Job: 'Hello World' on the Wynton Cluster

The Wynton cluster consists of a large number of compute nodes ready to execute users' tasks (jobs). Since all compute nodes are configured similarly, it doesn’t matter which node your analysis runs on. To manage resources and ensure fair use, Wynton uses a job scheduler, which places your jobs in a queue and allocates resources as they become available. Wynton's scheduler is called [Son of Grid Engine](https://www.google.com/search?q=son+of+grid+engine).

### Basics of Terminal Use

Before running jobs on Wynton, familiarize yourself with some basic terminal commands:

#### 1. `pwd`: Print Working Directory
- **Displays the current directory** you are in.
  ```sh
  [alice@wynton ~]$ pwd
  /wynton/home/rotation/alice
  ```

#### 2. `ls`: List Directory Contents
- **Lists files and directories** in the current directory.
  ```sh
  [alice@wynton ~]$ ls
  Documents  Downloads
  ```
- (Note: `Documents  Downloads` is an example output. On Wynton, `~/` will most likely be empty.)

#### 3. `mkdir`: Make Directory
- **Creates a new directory**.
  ```sh
  [alice@wynton ~]$ mkdir tests

  [alice@wynton ~]$ ls
  Documents  Downloads  tests
  ```

#### 4. `cd`: Change Directory
- **Moves between directories**.
  ```sh
  [alice@wynton ~]$ cd tests
  [alice@wynton ~/tests]$

  [alice@wynton ~/tests]$ pwd
  /wynton/home/rotation/alice/tests

  [alice@wynton ~]$ cd ..
  [alice@wynton ~]$ pwd
  /wynton/home/rotation/alice
  
  [alice@wynton ~]$ ls
  Documents  Downloads  tests
  ```

### Running a 'Hello World' Job

Now that you're familiar with basic commands, let us set up and run a simple job!

#### Step 1: Create a Script

1. **Navigate to your home directory** (if not already there):
   ```sh
   [alice@wynton ~]$ cd ~
   ```

2. **Create a directory** to store your script (if not already created):
   ```sh
   [alice@wynton ~]$ mkdir tests
   ```

3. **Navigate to the `tests` directory**:
   ```sh
   [alice@wynton ~]$ cd tests
   ```

4. **Create a script** called `hello_world`:
   ```sh
   [alice@wynton ~/tests]$ nano hello_world.sh
   ```
   - Use `nano` (a terminal-based text editor) to enter the following script:
     ```sh
     #! /usr/bin/env bash
     #$ -S /bin/bash  # Run job as a Bash shell [IMPORTANT]
     #$ -cwd          # Run job in the current working directory

     echo "Hello world, I am running on node $HOSTNAME"
     sleep 10
     date
     ```
   - Save and exit the editor (`Ctrl+X`, then `Y`, then `Enter` if using `nano`).
   - Side-note: Of course, there are a plethora of terminal text editor other than `nano`. Notable ones are emacs, vi, vim, neovim, etc. Choose wisely! Obligatory xkcd:


<div align="center">
  <img src="https://imgs.xkcd.com/comics/real_programmers.png" alt="Real Programmers"/>
</div>


For future reference, here's a more detailed sample submission script provided by Wynton:

```sh
#!/bin/bash           # The shell language when run outside of the job scheduler
#$ -S /bin/bash       # The shell language when run via the job scheduler [IMPORTANT]
#$ -cwd               # Job should run in the current working directory
#$ -j y               # STDERR and STDOUT should be joined
#$ -l mem_free=1G     # Job requires up to 1 GiB of RAM per slot
#$ -l scratch=2G      # Job requires up to 2 GiB of local /scratch space
#$ -l h_rt=24:00:00   # Job requires up to 24 hours of runtime
#$ -r y               # If job crashes, it should be restarted

date
hostname

[[ -n "$JOB_ID" ]] && qstat -j "$JOB_ID"  # End-of-job summary, useful for debugging.
```

#### Step 2: Make the Script Executable

5. **Change the file permissions** to make it executable:
   ```sh
   [alice@wynton ~/tests]$ chmod ugo+x hello_world.sh
   ```

#### Step 3: Run the Script Directly

6. **Test the script** by running it directly (optional but recommended):
   ```sh
   [alice@wynton ~/tests]$ ./hello_world.sh
   Hello world, I am running on node wynton
   Mon Aug 19 16:31:29 PDT 2024
   ```

#### Step 4: Submit the Script as a Job

7. **Submit the script** to the job queue using `qsub`:
   ```sh
   [alice@wynton ~/tests]$ qsub hello_world.sh
   Your job 201 ("hello_world") has been submitted
   ```

8. **Check the job status** using `qstat`:
   ```sh
   [alice@wynton ~/tests]$ qstat
   ```
   Initially, the job will be in a queued state (`qw`). Once it starts running, it will be in the running state (`r`).

#### Step 5: Review the Job Output

9. **Locate the output** in the current directory:
   ```sh
   [alice@wynton ~/tests]$ ls
   hello_world.sh  hello_world.o201
   ```

10. **View the job output**:
    ```sh
    [alice@wynton ~/tests]$ cat hello_world.o201
    Hello world, I am running on node wynton
    Mon Aug 19 16:32:12 PDT 2024
    ```

Congratulations! You've successfully submitted and run a simple 'Hello World' job on the Wynton cluster.

Lastly, a lot of times you will need to copy job output files over to your local machine. We generally do this to look at and analyze the results of our jobs.

### Files Transfer Between Your Computer and Wynton with **`scp`**

The `scp` (secure copy) command allows you to securely transfer files between your machine and Wynton via SSH.

#### Wynton → Local Machine

To copy a file from Wynton to your local machine, on your local machine, type:

```sh
scp zack@dt1.wynton.ucsf.edu:/wynton/home/zack/tests/hello_world.o201 /path/to/local/destination/
```

Replace `zack` with your Wynton username, `/wynton/home/zack/hello_world.o201` of the path of the file on Wynton, and `/path/to/local/destination/` with the path where you want the file to be saved on your local machine. (Note: we are using the data transfer node, `dt1`, rather than `log1` for moving the file. This isn't necessary but is recommended. More on this below.)


#### Local Machine → Wynton

On your local machine:

```sh
scp /path/to/local/file zack@dt1.wynton.ucsf.edu:/wynton/home/zack/
```

Replace `/path/to/local/file` with the path to the file on your local machine, and `zack` with your Wynton username. `/wynton/home/zack/` is where the file will land.


#### Copying Entire Directories

To copy entire directories, use the recursive `-r` option with `scp`:

```sh
# Wynton to your local machine:
scp -r zack@dt1.wynton.ucsf.edu:/wynton/home/zack/tests /path/to/local/destination/

# Your machine to Wynton
scp -r /path/to/local/directory zack@log1.wynton.ucsf.edu:/wynton/home/zack/
```

Wohoo! You're are now proficient enough to start using Wynton 😎. We can't wait to see all the cool science you'll do by leverging Wynton!

## Beyond the basics

### Overview of Wynton Nodes
Sign into login, data transfer, and development nodes for logging in, transferring data, or prototyping / testing code. Simply `ssh log1@wynton.ucsf.edu` or `ssh dt1@wynton.ucsf.edu`. For development, you can`ssh dev1@wynton.ucsf.edu` but you have to be logged into Wynton first. Here's a quick overview of all of Wynton's nodes:

| Feature                                        | Login Nodes                                                         | Transfer Nodes                                         | Development Nodes                                                                                                                            | Compute Nodes                                 |
| ---------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------- |
| **Hostname**                                   | `log[1-2].wynton.ucsf.edu`                                          | `dt[1-2].wynton.ucsf.edu`                              | `dev[1-3]`, `gpudev1`                                                                                                                        | …                                             |
| **Purpose**                                    | *Submit and query jobs. SSH to development nodes. File management.* | *Fast in- & outbound file transfers. File management.* | *Compile and install software. Prototype and test job scripts. Submit and query jobs. Version control (clone, pull, push). File management.* | *Running short and long-running job scripts.* |
| **Accessible via SSH from outside of cluster** | ✓ (2FA if outside of UCSF)                                          | ✓ (2FA if outside of UCSF)                             | no                                                                                                                                           | no                                            |
| **Network speed**                              | 1 Gbps                                                              | 10 Gbps                                                | 1 Gbps                                                                                                                                       | 1,10,40 Gbps                                  |
| **Core software**                              | Minimal                                                             | Minimal                                                | Same as compute nodes + compilers and source-code packages                                                                                   | Rocky 8 packages                              |
| **Job submission**                             | ✓                                                                   | no                                                     | ✓                                                                                                                                            | ✓                                             |

### Wynton Job Queues
The cluster provides different queues that each is optimized for a different purpose. Some queues are faster because they are limited to 30min run times (`short.q`). Others are slower, but ensure that your job is allocated a GPU (`gpu.q`). 

To specify a queue, use the flag `-q {queue_name_here}` when submitting a job, e.g., `qsub -q long.q my_submission_script.sh`.

Here's a quick summary:

| Queue Name | Maximum Runtime                                                        | Process Priority | Availability                                                       | Quota                                                                                    | Purpose                                                                      |
| ---------- | ---------------------------------------------------------------------- | ---------------- | ------------------------------------------------------------------ | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| **short.q**    | 30 minutes                                                             | 10 (medium)      | All compute nodes                                                  | 100 jobs per user                                                                        | Low-latency needs, e.g., pipeline prototyping and quick turn-around analysis |
| **long.q**     | 2 weeks (336 hours)                                                    | 19 (lowest)      | All compute nodes                                                  | Unlimited                                                                                | General needs                                                                |
| **member.q**   | 2 weeks (336 hours)                                                    | 0 (highest)      | All compute nodes (except GPU and institutionally purchased nodes) | Proportional to lab's [contributed share](https://wynton.ucsf.edu/hpc/about/shares.html) | Research groups needing more resources than communal queues                  |
| **gpu.q**      | 2 weeks (336 hours) (communal GPU nodes) or 2 hours (non-contributors) | 0 (highest)      | Specific GPU nodes                                                 | Unlimited                                                                                | Software utilizing GPUs                                                      |
| **4gpu.q**     | 2 weeks (336 hours) (contributors) or 2 hours (non-contributors)       | 0 (highest)      | Specific "All-4-GPU" nodes                                         | Unlimited                                                                                | Software needing to utilize all four GPUs on the node                        |
| **ondemand.q** | 2 weeks (336 hours)                                                    | 0 (highest)      | Institutionally purchased nodes                                    | Available upon application and approval                                                  | Scheduled high-priority computing needs or temporary paid priority access    |

### Using Scratch Storage

- All nodes (compute and development) have local storage mounted as `/scratch`. The `/scratch` storage is faster than system-wide storage such as home folders and `/wynton/scratch`, making it ideal for holding intermediate data files. Using local `/scratch` reduces the load on system-wide storage and the local network, benefiting everyone.
- As the name implies, `/scratch` is susceptible to deletion without warning by Wynton admin. Do not hold precious data on it.

### Additional Info / Tips

- **Email Notifications**: Get email notifications for job status by adding the flag `-m bea` to your `qsub` command, e.g., `qsub -m bea`.
- **Disk Quota**: Check your disk quota with:
  ```sh
  beegfs-ctl --getquota --storagepoolid=11 --uid "$USER"
  ```
  - Note: The displayed quota is double the actual size. For example, if it shows 1 TB, you have 500 GB available. [See more](https://wynton.ucsf.edu/hpc/howto/storage-size.html#user-disk-quota-on-wyntonhome-or-wyntonprotectedhome).
- There are some ways to automatically sign into nodes without typing in your password every time. You can also log directly into `dev` nodes without first going to a login node. [This tutorial](https://wynton.ucsf.edu/hpc/howto/log-in-without-pwd.html) on the Wynton website will help.

### Good File System Practices (don't be *the* person who breaks Wynton)
- **Distribute Files:** Spread out files across multiple directories, including SGE output and error files.
- **Prefer Larger Files:** Use fewer, larger files rather than many small ones.
- **Limit Directory I/O:** Keep the number of reads and writes to a single directory reasonable.

---

## Need Help?
- [Wynton Website](https://wynton.ucsf.edu/hpc/index.html)
- **Wynton Staff Support**:
  - Email: [support@wynton.ucsf.edu](mailto:support@wynton.ucsf.edu)
  - Join the [Wynton Slack](https://join.slack.com/t/ucsf-wynton/signup)
