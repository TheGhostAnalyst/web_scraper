import requests
import re
from datetime import datetime
from pathlib import Path
def save(links):
    with open('scrapped_links.txt', 'a') as f:
        now = datetime.now()
        timestamp = now.strftime('%Y-%m-%d %H:%M')
        f.write(f"######################################\n{timestamp}\n")
        for link in links:
            f.write(f"{link}\n")

def out(url, ask):
    the_path = Path('scrapped_links.txt').resolve()
    print(f'Your scrapped {ask} for {url} has been saved in {the_path} ')

def keep(emails):
    with open('scrapped_emails.txt', 'a') as f:
        now = datetime.now()
        timestamp = now.strftime('%Y-%m-%d %H:%M')
        f.write(f"######################################\n{timestamp}\n")
        for email in emails:
            f.write(f"{email}\n")
def result(url, ask):
    the_path = Path('scrapped_emails.txt').resolve()
    print(f'Your scrapped {ask} for {url} has been saved in {the_path} ')

def scrape(url, headers=None):
    response = requests.get(url, headers=headers)
    return response.text

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Referer': 'https://google.com'
}

# Get and display your IP
# Get and display your IP
ip = requests.get('https://api.ipify.org').text
print(f"Your public IP address is: {ip}")

# Ask the user what to scrape
ask = input("Do you want to scrape a webpage for emails or links: ").strip().lower()

if ask == "emails":
    print("You chose to scrape emails.")
    enter = input("Enter the URL to scrape for emails (eg., example.com): ").strip()
    url = f"https://{enter}"
    page = scrape(url, headers=headers)

    # Regex to find emails
    email_pattern = re.compile(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", re.IGNORECASE)
    emails = list(set(email_pattern.findall(page)))
    print('Mails found:')
    for mail in emails:
        print(mail)
    keep(emails)
    result(url,ask)

elif ask == "links":
    print("You chose to scrape links.")
    enter = input("Enter the URL to scrape for links (eg., example.com): ").strip()
    url = f"https://{enter}"
    page = scrape(url, headers=headers)

    # Regex to find href links
    link_pattern = re.compile(r'href=[\'"]([^\'"]+)["\']', re.IGNORECASE)
    links = list(set(link_pattern.findall(page)))
    print('Links found:')
    for link in links:
        print(link)
    save(links)
    out(url, ask)

else:
    print("Invalid option. Please choose 'emails' or 'links'.")
