# Jenkins-API-Python-Data-Analysis
<h2>Description</h2>
<br/> 

<br />
<br/> 
<br/>




### **Prerequisites**  

| Requirement      | Version/Details              |
|------------------|------------------------------|
| Operating System | RHEL 9                       |
| Python Version   | Python 3.x                   |
| Jenkins Server   | Accessible with API enabled  |

## Python Modules
The following Python modules are required for this project. Install them using `pip`:
- **python-jenkins**: For interacting with the Jenkins API.
- **matplotlib**: For data visualization.
- **numpy**: For numerical data processing.

Install all modules with:
```bash
python3 -m pip install python-jenkins matplotlib numpy
```



## Step 1: Create a Jenkins Job

<br/> 
For this project create a Jenkins job that will trigger the sleep command at random in order to generate data
<br/> 

<img src="https://github.com/user-attachments/assets/8998af24-5bfa-49d8-9017-a50affa0781b"/>
<br/> Choose build periodically to have the build run on a cron schedule, also enter the following within execute shell  <br/>

```Bash
# Generate a random sleep duration between 1 and 10 seconds
SLEEP_DURATION=$((RANDOM % 10 + 1))
echo "Sleeping for $SLEEP_DURATION seconds..."
sleep $SLEEP_DURATION
echo "Completed sleeping for $SLEEP_DURATION seconds."
```

<img src="https://github.com/user-attachments/assets/171516f9-46ea-466b-a666-a5303faf1008"/>
<img src="https://github.com/user-attachments/assets/3b5e59f9-157d-4cbd-8e17-370b6b8bb293"/>
<br/> Next click build now and confirm the Job is running successfully  <br/>
<img src="https://github.com/user-attachments/assets/4ec4f476-8753-4923-90c0-3782bfeb7f3d"/>
<br/> It can also be observed that the job is running successfully every 2 minutes <br/> 
<img src="https://github.com/user-attachments/assets/34eb8214-00f2-4637-b819-92e57ce422d6"/>

## Step 2: Create and run the Python script

<br/> 
 I will run the Job-Duration-Metrics.py script under worker_scripts. This Python script connects to the local Jenkins server, retrieves build durations for the Demo-Sleep-Job, and calculates the average build duration. The DurationMetrics class initializes with a Jenkins username and password, allowing authentication to connect to the Jenkins server.  The script then calculates the total build duration and the number of builds, allowing it to compute the average build duration in seconds. The build durations are plotted over time using matplotlib, and a graph is displayed showing the relationship between the time of execution and build duration. The script outputs the average build duration and generates a time-based plot of the job's build durations.
<br/> 
<br/> The output <br/>
<img src="https://github.com/user-attachments/assets/66130738-62b8-4a14-8545-caeabc1f23a7"/>
<img src=""/>
<br/>  <br/>
<img src=""/>


## Step 3: 

<br/> 
 
<br/> 

<img src=""/>
<img src=""/>
<br/>  <br/>
<img src=""/>


## Step 4: 

<br/> 
 
<br/> 

<img src=""/>
<img src=""/>
<br/>  <br/>
<img src=""/>

## Step 5: 

<br/> 
 
<br/> 

<img src=""/>
<img src=""/>
<br/>  <br/>
<img src=""/>

## Step 6: 

<br/> 
 
<br/> 

<img src=""/>
<img src=""/>
<br/>  <br/>
<img src=""/>
