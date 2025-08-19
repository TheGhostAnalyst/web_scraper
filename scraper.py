import requests
import re

def scrape(url):
    response = requests.get(url)
    return response.text
    
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Referer': 'https://google.com'
}

response = requests.get('https://httpbin.org/headers', headers=headers)

ip = requests.get('https://api.ipify.org').text
print(f"Your public IP address is: {ip}")

ask = input("Do you want to scrape a webpage for emails or links: ").strip().lower()  
if ask == "emails":
    print("You chose to scrape emails.")
    enter = input("Enter the URL to scrape for emails (eg., example.com): ").strip()
    fish = (f"https://{enter}")
    url = fish  
    page = scrape(url)


    # Regex to find emails
    email_pattern = re.compile(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", re.IGNORECASE)

    # Find all emails
    email = email_pattern.findall(page)

    # Remove duplicates and print
    emails = list(set(email))  # Optional: removes duplicates
    for mail in emails:
        print(f"Email found: {mail}")
elif ask == "links":
    print("You chose to scrape links.")
    url = input("Enter the URL to scrape for links (eg., example.com): ").strip()
    fish2 = (f"https://{url}")
    url = fish2
    page = scrape(url)

    # Regex to find href links
    link_pattern = re.compile(r'href=[\'"]([^\'"]+)["\']', re.IGNORECASE)



    links = list(set(link_pattern.findall(page)))  # remove duplicates
    for link in links:
        print(f"Link found: {link}")
else:
    print("Invalid option. Please choose 'emails' or 'links'.")
