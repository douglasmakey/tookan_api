###TookanApi

python sdk for TookanApi

Usage
=====

```python
from api.client import TookanApi

# Create client
tookan = TookanApi.create_client(api_key='KEY', user_id='UserID')
```

Instance Task
```python
# Get instance task
task = tookan.instance_task() 
 
# Create new Task
payload = {.....} # Describe your paylaod
new_task = task.create(payload)
 
# Get task by job_id
get_task = task.get(job_id=8456122)
 
# Get all tasks, you can pass different parameters like filter
all_task = task.get_all(job_status=1)
 
# Delete task by job_id
delete = task.delete(job_id=8465968)
 
# Update task
task.update(job_id=8680331, job_status=2)
 
```

Instance Agent
```python
agent = tookan.instance_agent()
 
# You can pass different parameters like filters.
# If you not pass fleet_id, return all agents
agent.get(fleet_id=70441)
```