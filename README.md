
# Desktop Screenshot Tool

A simple Python tool that captures a screenshot of the entire desktop screen and sends it to a specified Discord webhook. The tool also includes the user's external IP address in the message content.

## Features
- Captures the entire desktop screen and saves it temporarily.
- Sends the screenshot as a file attachment to a Discord webhook.
- Includes the user's external IP address in the message.

## Requirements
- **Python 3.6 or higher**
- **Libraries**:
  - `Pillow`
  - `requests`

You can install the required libraries using the following command:

```bash
pip install pillow requests
```

## How It Works
1. **Capture Screenshot**: The tool uses the `PIL` (Pillow) library to capture a screenshot of the entire screen.
2. **Send to Discord Webhook**: The tool sends the screenshot to the provided Discord webhook URL along with the user's external IP address in the message content.
3. **Cleanup**: The screenshot is saved temporarily in `C:\Users\%USERNAME%\AppData\Local\Temp` and deleted after being sent to the webhook.

## Usage
1. Clone this repository or download the script.

```bash
git clone https://github.com/eteb/desktop-screenshot-tool.git
```

2. Navigate to the directory:

```bash
cd desktop-screenshot-tool
```

3. Replace the `WEBHOOK_URL` variable in the script with your own Discord webhook URL.

```python
WEBHOOK_URL = 'YOUR_DISCORD_WEBHOOK_URL'
```

4. Run the script:

```bash
python screenshot_tool.py
```


## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Disclaimer
This tool is intended for **research purposes only**. Please ensure you have permission before using it to capture and share screenshots.

## All Rights Reserved
All rights reserved to **aselterik**. Unauthorized use, distribution, or modification of this code is prohibited.

## Author
GitHub: [eteb](https://github.com/eteb)

---

Feel free to contribute or suggest improvements by opening an issue or pull request.
