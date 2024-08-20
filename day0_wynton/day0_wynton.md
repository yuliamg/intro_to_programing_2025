Here's the cleaned-up and reformatted version of your Wynton tutorial:

---

## Day 0: Introduction to Wynton

### Helpful Resources
- [Wynton Website](https://wynton.ucsf.edu/hpc/index.html)

### What is Wynton?

Wynton is a **High Performance Computing (HPC) cluster** composed of many interconnected computers (nodes) that collaborate to allow users to execute programs and process large datasets. It is commonly used in research for simulations, analyzing big datasets, or performing tasks that would be too time-consuming on a regular computer. Wynton enables you to leverage the combined power of the entire cluster, making it possible to handle more intensive computational tasks.

### Getting Started: Creating a Wynton Account
- [Request or Update an Account](https://wynton.ucsf.edu/hpc/about/join.html#request-or-update-an-account)
  - _(It's ideal to complete this on Day 1)_

### Accessing Wynton

Wynton is only accessible via the ***terminal***.

<details>
<summary>What is the terminal?</summary>
The **terminal** is a text-based interface that allows you to interact directly with your computer by typing commands, rather than using a graphical interface like clicking on icons. It might seem intimidating at first, but it's a powerful tool that gives you a lot of control over your computational environment.
</details>

### Signing into Wynton
- Open the terminal:
  - On Mac: Use `command ⌘ + space ␣` to open Spotlight, then type "terminal" to open it.
  - _(Note: A Windows option should be added)_
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

## Running Your First Job: 'Hello World' on the Wynton Cluster

The Wynton cluster consists of a large number of compute nodes ready to execute users' tasks (jobs). Since all compute nodes are configured similarly, it doesn’t matter which node your analysis runs on. To manage resources and ensure fair use, Wynton uses a job scheduler, which places your jobs in a queue and allocates resources as they become available.

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
  Documents  Downloads  tests  hello_world
  ```

#### 3. `cd`: Change Directory
- **Moves between directories**.
  ```sh
  [alice@wynton ~]$ cd tests
  [alice@wynton ~/tests]$
  ```

#### 4. `mkdir`: Make Directory
- **Creates a new directory**.
  ```sh
  [alice@wynton ~]$ mkdir tests
  ```

### Running a 'Hello World' Job

Now that you're familiar with basic commands, let's run a simple job on Wynton.

#### Step 1: Create a Script

1. **Navigate to your home directory** (if not already there):
   ```sh
   [alice@wynton ~]$ cd ~
   ```

2. **Create a directory** to store your script:
   ```sh
   [alice@wynton ~]$ mkdir tests
   ```

3. **Navigate to the `tests` directory**:
   ```sh
   [alice@wynton ~]$ cd tests
   ```

4. **Create a script** called `hello_world`:
   ```sh
   [alice@wynton ~/tests]$ nano hello_world
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
   [alice@wynton ~/tests]$ chmod ugo+x hello_world
   ```

#### Step 3: Run the Script Directly

6. **Test the script** by running it directly (optional but recommended):
   ```sh
   [alice@wynton ~/tests]$ ./hello_world
   Hello world, I am running on node wynton
   Mon Aug 19 16:31:29 PDT 2024
   ```

#### Step 4: Submit the Script as a Job

7. **Submit the script** to the job queue:
   ```sh
   [alice@wynton ~/tests]$ qsub -cwd -j yes hello_world
   Your job 201 ("hello_world") has been submitted
   ```

8. **Check the job status**:
   ```sh
   [alice@wynton ~/tests]$ qstat
   ```
   Initially, the job will be in a queued state (`qw`). Once it starts running, it will be in the running state (`r`).

#### Step 5: Review the Job Output

9. **Locate the output** in the current directory:
   ```sh
   [alice@wynton ~/tests]$ ls
   hello_world  hello_world.o201
   ```

10. **View the job output**:
    ```sh
    [alice@wynton ~/tests]$ cat hello_world.o201
    Hello world, I am running on node wynton
    Mon Aug 19 16:32:12 PDT 2024
    ```

Congratulations! You've successfully submitted and run a simple 'Hello World' job on the Wynton cluster.

## Additional Information

### Seeking Help

- **Wynton Support**:
  - Email: [support@wynton.ucsf.edu](mailto:support@wynton.ucsf.edu)
  - [Wynton Slack](https://join.slack.com/t/ucsf-wynton

/signup)

### Overview of Wynton Nodes

| Feature                                    | Login Nodes                                                         | Transfer Nodes                                         | Development Nodes                                                                                                                            | Compute Nodes                                 |
| ------------------------------------------ | ------------------------------------------------------------------- | ------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------- |
| **Hostname**                               | `log[1-2].wynton.ucsf.edu`                                          | `dt[1-2].wynton.ucsf.edu`                              | `dev[1-3]`, `gpudev1`                                                                                                                        | …                                             |
| **Purpose**                                | *Submit and query jobs. SSH to development nodes. File management.* | *Fast in- & outbound file transfers. File management.* | *Compile and install software. Prototype and test job scripts. Submit and query jobs. Version control (clone, pull, push). File management.* | *Running short and long-running job scripts.* |
| **Accessible via SSH from outside of cluster** | ✓ (2FA if outside of UCSF)                                          | ✓ (2FA if outside of UCSF)                             | no                                                                                                                                           | no                                            |
| **Network speed**                          | 1 Gbps                                                              | 10 Gbps                                                | 1 Gbps                                                                                                                                       | 1,10,40 Gbps                                  |
| **Core software**                          | Minimal                                                             | Minimal                                                | Same as compute nodes + compilers and source-code packages                                                                                   | Rocky 8 packages                              |
| **Job submission**                         | ✓                                                                   | no                                                     | ✓                                                                                                                                            | ✓                                             |

### Wynton Job Queues

| Queue Name | Maximum Runtime                                                        | Process Priority | Availability                                                       | Quota                                                                                    | Purpose                                                                      |
| ---------- | ---------------------------------------------------------------------- | ---------------- | ------------------------------------------------------------------ | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| **short.q**    | 30 minutes                                                             | 10 (medium)      | All compute nodes                                                  | 100 jobs per user                                                                        | Low-latency needs, e.g., pipeline prototyping and quick turn-around analysis |
| **long.q**     | 2 weeks (336 hours)                                                    | 19 (lowest)      | All compute nodes                                                  | Unlimited                                                                                | General needs                                                                |
| **member.q**   | 2 weeks (336 hours)                                                    | 0 (highest)      | All compute nodes (except GPU and institutionally purchased nodes) | Proportional to lab's [contributed share](https://wynton.ucsf.edu/hpc/about/shares.html) | Research groups needing more resources than communal queues                  |
| **gpu.q**      | 2 weeks (336 hours) (communal GPU nodes) or 2 hours (non-contributors) | 0 (highest)      | Specific GPU nodes                                                 | Unlimited                                                                                | Software utilizing GPUs                                                      |
| **4gpu.q**     | 2 weeks (336 hours) (contributors) or 2 hours (non-contributors)       | 0 (highest)      | Specific "All-4-GPU" nodes                                         | Unlimited                                                                                | Software needing to utilize all four GPUs on the node                        |
| **ondemand.q** | 2 weeks (336 hours)                                                    | 0 (highest)      | Institutionally purchased nodes                                    | Available upon application and approval                                                  | Scheduled high-priority computing needs or temporary paid priority access    |

To specify a queue, use the flag `-q {queue_name_here}` when submitting a job, e.g., `qsub -q long.q my_script`.

### Using Scratch Storage

- All nodes (compute and development) have local storage mounted as `/scratch`. The `/scratch` storage is fast—faster than system-wide storage such as home folders and `/wynton/scratch`—making it ideal for holding intermediate data files. Using local `/scratch` reduces the load on system-wide storage and the local network, benefiting everyone.

### Additional Tips

- **Email Notifications**: Get email notifications for job status by adding the flag `-m bea` to your `qsub` command, e.g., `qsub -m bea`.
- **Disk Quota**: Check your disk quota with:
  ```sh
  beegfs-ctl --getquota --storagepoolid=11 --uid "$USER"
  ```
  - Note: The displayed quota is double the actual size. For example, if it shows 1 TB, you have 500 GB available. [See more](https://wynton.ucsf.edu/hpc/howto/storage-size.html#user-disk-quota-on-wyntonhome-or-wyntonprotectedhome).

---

This revised tutorial now presents a clear, well-structured guide to help beginners navigate Wynton and successfully run their first job.