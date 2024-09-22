import requests
from bs4 import BeautifulSoup

def scan_website(url):
    # Send an HTTP GET request to the website
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find all the payment gateway links on the page
        payment_gateways = soup.find_all('a')
        
        # Check for 2D and 3D payment gateways
        has_2d_gateway = False
        has_3d_gateway = False
        
        for gateway in payment_gateways:
            gateway_url = gateway.get('href')
            if gateway_url and ('paypal' in gateway_url or 'paymentwall' in gateway_url):
                has_2d_gateway = True
            elif gateway_url and ('stripe' in gateway_url or 'braintree' in gateway_url):
                has_3d_gateway = True
        
        # Print the results
        print(f"Website: {url}")
        print(f"2D Payment Gateway (Unsafe): {has_2d_gateway}")
        print(f"3D Payment Gateway (Safe): {has_3d_gateway}")
    else:
        print(f"Failed to access the website: {url}")

# Example usage
website_url = 'https://example.com'
scan_website(website_url)