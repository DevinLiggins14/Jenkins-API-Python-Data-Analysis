import jenkins
from datetime import datetime

# Connect to Jenkins API with correct credentials
server = jenkins.Jenkins('http://localhost:8080', username='root', password='your_password')  # Use your actual password or API token

# Job name (replace with your actual job name)
job_name = 'build-job'  # Replace 'build-job' with your job name

# Fetch job information
job_info = server.get_job_info(job_name)

# Get the last 50 builds
builds = job_info['builds'][:50]

print(f"Displaying the last {len(builds)} builds for job: {job_name}\n")

# Fetch and display details for each build
for build in builds:
    build_number = build['number']
    build_info = server.get_build_info(job_name, build_number)

    # Extract relevant information
    build_start_timestamp = build_info['timestamp'] / 1000  # Convert from ms to seconds
    build_start_time = datetime.fromtimestamp(build_start_timestamp).strftime('%Y-%m-%d %H:%M:%S')
    build_duration = build_info['duration'] / 1000  # Duration in seconds
    build_end_time = datetime.fromtimestamp(build_start_timestamp + build_duration).strftime('%Y-%m-%d %H:%M:%S')
    build_status = build_info['result']

    # Display the information in a readable format
    print(f"Build #{build_number}")
    print(f"  Status: {build_status}")
    print(f"  Start Time: {build_start_time}")
    print(f"  End Time: {build_end_time}")
    print(f"  Duration: {build_duration:.2f} seconds")
    print("-" * 50)
