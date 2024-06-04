import os

credentials = {
    'email': os.getenv('EMAIL', 'customer2@practicesoftwaretesting.com'),
    'password': os.getenv('PASSWORD', 'welcome01')
}
