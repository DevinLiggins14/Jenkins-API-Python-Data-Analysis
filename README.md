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
<br/>  <br/>
<img src=""/>



## Step 2: 

<br/> 
 
<br/> 

<img src=""/>
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
