import datetime

from api import TookanApi


# Instance API
tookan = TookanApi.create_client(api_key='KEY', user_id='USERID')

# Set data for task 
# https://tookanapi.docs.apiary.io/#reference/task/create-task

payload = {
  "order_id": "654321",
  "job_description": "groceries delivery",
  "job_pickup_phone": "+1201555555",
  "job_pickup_name": "7 Eleven Store",
  "job_pickup_email": "",
  "job_pickup_address": "114, sansome street, San Francisco",
  "job_pickup_latitude": "30.7188978",
  "job_pickup_longitude": "76.810296",
  "job_pickup_datetime":str(datetime.date.today()), # Add Today or date in the future.
  "auto_assignment": "0",
  "has_pickup": "1",
  "has_delivery": "0",
  "layout_type": "0",
  "tracking_link": 1,
  "timezone": "300",
  "fleet_id": "",
  "notify": 1,
  "tags": "",
  "geofence": 0
}

new_task = tookan.create_task(payload)
print "New Task: {0}".format(new_task)

# Get task by job_id
get_task = tookan.get_task(job_id=new_task['job_id'])
print "Get Task with JobID = {0} : {1}".format(new_task['job_id'], get_task)
 
# Get all tasks, you can pass different parameters like filter
all_task = tookan.get_all_tasks(job_status=6, job_type=0)
print "All Tasks: {0}".format(all_task)
 
# Delete task by job_id
delete = tookan.delete_task(job_id=all_task['data'][0]['job_id'])
print "Task Remove with JobID = {0} : {1}".format(all_task['data'][0]['job_id'], delete)