<details>
<summary>
Place holder
</summary>
Foo
</details>
### Day 0: Wynton


*Helpful resources:*
- [Wynton Website](https://wynton.ucsf.edu/hpc/index.html)


##### What is Wynton?
<details>
<summary>
What is Wynton?
</summary>
A Wynton is a **High Performance Computing (HPC) cluster** system made up of many interconnected computers (called nodes) that work together to allow many users execute programs and process data. It's commonly used in research to run simulations, analyze big datasets, or perform tasks that would take too long on a regular computer. Instead of relying on a single machine, you can tap into the combined power of the entire cluster, making it possible to handle more intensive computational tasks.
</details>



#### Make an Account:
- [Request or Update an Account](https://wynton.ucsf.edu/hpc/about/join.html#request-or-update-an-account)
  - _(Let’s get this done prior, ideally on day 1)_

Unlike everyday computers, Wynton is Accessible only via the ***terminal***. 
<details>
<summary>
What is the terminal?
</summary>
The **terminal** is a text-based interface that allows you to interact directly with your computer typing commands, rather than using a graphical interface (like clicking on icons, etc). It might seem intimidating at first, but it's a powerful tool that gives you a lot of control over your computational environment.
</details>
#### Sign into Wynton ([main page](https://wynton.ucsf.edu/hpc/get-started/access-cluster.html)):
  - Open terminal via: `command ⌘ + space ␣` to open Mac spotlight _(note the need for a Windows option)_
  - Type "terminal" to open the terminal.
  - This is the terminal, type `ssh your_name@log1.wynton.ucsf.edu`
  - Enter your password.
  - If successful, you should see something like this:

```
[zack@log1 ~]$ ssh zack@log1.wynton.ucsf.edu
zack@log1.wynton.ucsf.edu's password:
Last failed login: Mon Aug 19 14:43:45 PDT 2024 from 172.26.44.11 on ssh:notty
There were 2 failed login attempts since the last successful login.
Last login: Mon Aug 19 14:43:27 2024 from 172.26.44.11
######################################################################
#           All connections are monitored and recorded.              #
#      Disconnect IMMEDIATELY if you are not an authorized user!     #
######################################################################

Welcome to the Wynton HPC environment.

For instructions, please see <https://wynton.ucsf.edu/hpc/>.  The
support team holds office hours from 11am-noon on Tuesdays at:

<https://zoom.us/j/97716031058?pwd=NXhaeUtHVStWbklmSXhOVWJoM1BQQT09>
Meeting ID: 977 1603 1058, Password: 783363

Space on /wynton is for temporary storage of active data only.  Unused
data should be moved to your own storage ASAP.  Wynton storage is not
backed up, and stuff happens ...

Change of password takes up to 10 minutes to be effective. Please see
<https://wynton.ucsf.edu/hpc/howto/change-pwd.html> for instructions.

IMPORTANT: Data containing Protected Health Information (PHI) must not
be transferred to, mounted on, or processed on Wynton other than in
the Wynton PHI environment. To apply for a Wynton PHI account, please
see <https://wynton.ucsf.edu/hpc/about/wynton-phi.html>.

This login node is for job submission only.  The system administrators
reserve the right to kill any long running processes on these nodes
without warning.  Use a development node from prototyping.
[zack@log1 ~]$
```

<details> 
<summary>Click to expand!</summary> 
```python   # Your code here   def example_function():       print("This is a collapsible code segment!")```

</details>

Welcome to Wynton!


#### Wynton Slack


<details>
  <summary>Click me</summary>
  
  ### Heading
  1. Foo
  2. Bar
     * Baz
     * Qux

  ### Some Javascript
  ```js
  function logSomething(something) {
    console.log('Something', something);
  }
  ```
</details>
