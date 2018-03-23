TookanApi
=====
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

 
# Create new Task
payload = {.....} # Describe your paylaod
new_task = tookan.create_taske(payload)
 
# Get task by job_id
get_task = tookan.get_task(job_id=8456122)
 
# Get all tasks, you can pass different parameters like filter
all_task = tookan.get_all_tasks(job_status=1, job_type=0)
 
# Delete task by job_id
delete = tookan.delete_task(job_id=8465968)
 
# Update task
tookan.update_task(job_id=8680331, job_status=2)
 
```

Agent
```python 
# You can pass different parameters like filters.
# If you not pass fleet_id, return all agents
tookan.get_agent(fleet_id=70441)
```