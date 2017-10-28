import logging
import arrow

from api.provider import APIProvider

logger = logging.getLogger(__name__)


class TookanApi(object):
    def __init__(self, api_provider):
        self.api_provider = api_provider

    @classmethod
    def create_client(cls, api_key, user_id):
        api_provider = APIProvider(
            api_key=api_key,
            user_id=user_id
        )
        return cls(api_provider)

    def instance_task(self):
        return Task(self.api_provider)

    def instance_agent(self):
        return Agent(self.api_provider)


class Task(object):
    def __init__(self, api_provider):
        self.api_provider = api_provider

    def create(self, payload, auto_assignment=True):

        # Set init default auto_assignment in false
        payload["auto_assignment"] = "0"
        if auto_assignment:
            payload["auto_assignment"] = "1"

        response = self.api_provider.consume(resource='Task', action='create_task', payload=payload)

        return response['data']

    def get(self, job_id=None, order_id=None):
        # Init Payload
        payload = {}

        if job_id is not None and order_id is None:
            payload['job_id'] = job_id
            action = 'get_task_details'
        else:
            payload['order_id'] = order_id
            action = 'get_task_details_by_order_id'

        response = self.api_provider.consume(resource='Task', action=action, payload=payload, with_user=True)
        return response['data']

    def get_all(self, job_status, job_type=None, start_date=None,
                end_date=None, custom_fields=None, is_pagination=None,
                requested_page=None, customer_id=None):

        # "job_status": Filter the list of tasks via their status
        # "job_type": Filter via Job Type - 0 for Pick Up, 1 for Delivery, 2 for Appointment and 3 for FOS
        # "start_date": Start Date for the date range
        # "end_date": End Date for the date range
        # "custom_fields": You can pass this flag as 1, if you want the custom fields data
        #  to be included in the response. default is 0
        # "is_pagination": You can set this as 1 to enable pagination.
        # "requested_page": Current(Which) page according to the page number of tasks in the filter.
        # "customer_id": Filter the list based on the customer id.

        # Example {
        #   "job_status": 1,
        #   "job_type": 1,
        #   "start_date": "2016-08-20",
        #   "end_date": "2016-08-20",
        #   "custom_fields": 0,
        #   "is_pagination": 1,
        #   "requested_page": 1,
        #   "customer_id": ""
        # }

        payload = {
            'job_status': job_status,
            'job_type': job_type or 1,
            'start_date': start_date or str(arrow.now().date()),
            'end_date': end_date or str(arrow.now().date()),
            'custom_fields': custom_fields or 0,
            'is_pagination': is_pagination or 1,
            'requested_page': requested_page or 1,
            'customer_id': customer_id or ""
        }

        response = self.api_provider.consume(resource='Task', action='get_all_tasks', payload=payload)
        return response

    def update(self, job_id, job_status):
        payload = {
            'job_id': job_id,
            'job_status': job_status
        }
        response = self.api_provider.consume(resource='Task', action='update_task_status', payload=payload)
        return response['data']

    def delete(self, job_id):
        payload = {'job_id': job_id}
        response = self.api_provider.consume(resource='Task', action='delete_task', payload=payload)
        return response['data']


class Agent(object):
    def __init__(self, api_provider):
        self.api_provider = api_provider

    def get(self, fleet_id=None, team_id=None, tags=None, latitude=None, longitude=None, geofence=None):
        # Set payload
        payload = {
            'team_id': team_id,
            'tags': tags,
            'latitude': latitude,
            'longitude': longitude,
            'geofence':  geofence
        }

        # Set action
        if fleet_id is None:
            action = 'get_available_agents'
        else:
            action = 'get_available_agents?fleet_id={0}'.format(fleet_id)

        response = self.api_provider.consume(resource='Agent', action=action, payload=payload)
        return response['data']
