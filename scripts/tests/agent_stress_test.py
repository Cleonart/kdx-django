# locustfile.py
from locust import HttpUser, task, between, constant
import random
from datetime import datetime, timezone


class CompanyAPIUser(HttpUser):
    # Wait time between requests (simulates user think time)
    wait_time = between(1, 3)  # 1-3 seconds between requests

    host: str = 'http://localhost:8000'

    @task
    def get_companies(self):
        """ Test GET /api/v1/companies/ endpoint """
        headers: dict = {'accept': 'application/json'}
        with self.client.get(
            '/api/v1/companies/',
                headers=headers,
                catch_response=True) as response:

            if response.status_code == 200:
                response.success()

            else:
                msg: str = f'Failed with status code: {response.status_code}'
                response.failure(msg)


class OrderCreationUser(HttpUser):
    """User that creates orders every 5 seconds"""
    wait_time = constant(5)  # Exactly 5 seconds between requests
    host: str = 'http://localhost:8000'
    weight = 1  # Fewer of these users

    # Company codes from your 43 companies
    company_codes = [
        "TECH001", "TECH002", "TECH003", "TECH004", "TECH005",
        "FIN001", "FIN002", "FIN003", "FIN004", "FIN005",
        "MFG001", "MFG002", "MFG003", "MFG004", "MFG005",
        "RTL001", "RTL002", "RTL003", "RTL004", "RTL005",
        "HTH001", "HTH002", "HTH003", "HTH004", "HTH005",
        "EDU001", "EDU002", "EDU003", "EDU004", "EDU005",
        "LOG001", "LOG002", "LOG003", "LOG004", "LOG005",
        "ENR001", "ENR002", "ENR003",
        "CON001", "CON002", "CON003",
        "AGR001", "AGR002"
    ]

    @task
    def create_order(self):
        """ Test POST /api/v1/orders/ endpoint - runs every 5s """
        headers: dict = {
            'accept': 'application/json',
            'Content-Type': 'application/json',
        }

        # Generate order data
        order_data = {
            'company_id': 0,
            'company_code': random.choice(self.company_codes),
            'customer_id': 0,
            'customer_code': 'TEST12345',
            'order_date': datetime.now(timezone.utc).isoformat(),
            'notes': 'Sample order from load test',
            'lines': [
                {'product_name': f'test-{i:03d}',
                    'quantity': (i % 5) + 1, 'unit_price': '525.20'}
                for i in range(1, 101)  # Creates 100 line items
            ]
        }

        with self.client.post(
            '/api/v1/orders/',
            json=order_data,
            headers=headers,
                catch_response=True) as response:

            if response.status_code in [200, 201]:
                response.success()
            else:
                msg: str = f'Failed with status code: {response.status_code}'
                response.failure(msg)
