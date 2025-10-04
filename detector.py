#!/usr/bin/env python3
import requests
import whois
from urllib.parse import urlparse

def check_suspicious_url(url):
    suspicious_keywords = ['login', 'verify', 'account', 'secure', 'banking']
    domain = urlparse(url).netloc
    
    print(f"Checking URL: {url}")
    print(f"Domain: {domain}")
    
    # Check domain age
    try:
        domain_info = whois.whois(domain)
        if domain_info.creation_date:
            print(f"Domain created: {domain_info.creation_date}")
    except:
        print("Could not retrieve domain info")
    
    # Check for suspicious keywords
    for keyword in suspicious_keywords:
        if keyword in url.lower():
            print(f"Suspicious keyword found: {keyword}")

# Add this to accept user input
if __name__ == "__main__":
    url = input("Enter URL to check: ")
    check_suspicious_url(url)