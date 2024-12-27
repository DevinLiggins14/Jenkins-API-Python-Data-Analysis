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

I will run the `Job-Duration-Metrics.py` script under `worker_scripts`. This Python script connects to the local Jenkins server, retrieves build durations for the `Demo-Sleep-Job`, and calculates the average build duration.

The `DurationMetrics` class initializes with a Jenkins username and password, allowing authentication to connect to the Jenkins server. The script then calculates the total build duration and the number of builds, allowing it to compute the average build duration in seconds.

The build durations are plotted over time using `matplotlib`, and a graph is displayed showing the relationship between the time of execution and build duration. The script outputs the average build duration and generates a time-based plot of the job's build durations.


<br/> The output <br/>
<img src="https://github.com/user-attachments/assets/66130738-62b8-4a14-8545-caeabc1f23a7"/>
<br/> The script output successfully retrieves information about the Jenkins Demo-Sleep-Job, including a list of its builds. However, it seems the script isn't outputting the build durations or visualizing the data yet.

To gather and visualize the job durations using matplotlib, I need to extract the build timestamps (start and end times) and calculate the durations. I will modify the script so that it fetches the timestamp and duration for each build. The duration is in milliseconds, so it's converted to seconds. Also the script should plot the build durations using matplotlib. <br/> 

```py
import jenkins
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

# Connect to Jenkins server
jenkins_url = 'http://10.1.12.145:8080'
username = 'admin'
password = 'admin_password'  # Replace with your Jenkins admin password
server = jenkins.Jenkins(jenkins_url, username=username, password=password)

# Get job names
job_names = server.get_jobs()
print(f"Available Jobs: {[job['name'] for job in job_names]}")

# Get build information for a specific job
job_name = 'Demo-Sleep-Job'
job_info = server.get_job_info(job_name)
print(f"Job Info for {job_name}: {job_info}")

# Extract build numbers and URLs
builds = job_info['builds']
build_numbers = [build['number'] for build in builds]
build_urls = [build['url'] for build in builds]

# Initialize lists for build durations
build_durations = []

# Loop through builds and fetch start and end times to calculate durations
for build_number in build_numbers:
    build_info = server.get_build_info(job_name, build_number)
    timestamp_start = build_info['timestamp']
    timestamp_end = build_info['timestamp'] + build_info['duration']  # Assuming duration is in milliseconds
    duration_seconds = (timestamp_end - timestamp_start) / 1000  # Convert milliseconds to seconds
    build_durations.append(duration_seconds)

# Plot the build durations
plt.figure(figsize=(10, 6))
plt.plot(build_numbers, build_durations, marker='o', color='b', linestyle='-', label='Build Duration')
plt.title(f'Build Durations for {job_name}')
plt.xlabel('Build Number')
plt.ylabel('Duration (seconds)')
plt.grid(True)
plt.xticks(np.arange(min(build_numbers), max(build_numbers) + 1, 1))
plt.legend()
plt.show()

```

<img src="https://github.com/user-attachments/assets/02a4cf05-bbc5-4fa5-8ce1-8877931cbaf7"/>
<br/> The following message is due to the fact that the script is running from a non interactive enviroment: /root/Job-Duration-Metrics.py:46: UserWarning: FigureCanvasAgg is non-interactive, and thus cannot be shown
  plt.show()

 <br/>
I will make some changes so that the data of the jobs start and stop time can be viewed within the Linux CLI in real time
 <br/> 

```.py
import jenkins
import time
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

# Connect to Jenkins API (CHANGE USERNAME AND PASSWORD)
server = jenkins.Jenkins('http://localhost:8080', username='username', password='password')

# Start time of the job
start_time = datetime.now()

# Print start time
print(f"Job started at: {start_time.strftime('%Y-%m-%d %H:%M:%S')}")

# Example job trigger (replace 'your_job_name' with your actual job)
job_name = 'Job Name'
server.build_job(job_name)

# Wait for job completion (for demonstration purposes, adjust based on your job's duration)
time.sleep(10)  # Adjust this for your job's expected duration

# Fetch job details (replace with actual job name and build number)
last_build = server.get_job_info(job_name)['lastBuild']
build_number = last_build['number']
build_info = server.get_build_info(job_name, build_number)

# Collecting job data (replace with actual metrics)
build_duration = build_info['duration'] / 1000  # Duration in seconds
job_status = build_info['result']

# Plotting the job duration (just an example, adjust as needed)
durations = [build_duration]
status = ['Success' if job_status == 'SUCCESS' else 'Failure']

# Create a bar plot
fig, ax = plt.subplots()
ax.bar(status, durations, color='green' if job_status == 'SUCCESS' else 'red')
ax.set_ylabel('Duration (seconds)')
ax.set_title(f"Job Duration: {job_name} - {job_status}")

# Show the plot on screen
plt.show()

# Stop time of the job
end_time = datetime.now()

# Print end time
print(f"Job ended at: {end_time.strftime('%Y-%m-%d %H:%M:%S')}")

# Print total duration
total_duration = end_time - start_time
print(f"Total duration: {total_duration}")



```



https://github.com/user-attachments/assets/4cd7f145-3b73-49ff-9ebd-f560e1843b47




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
