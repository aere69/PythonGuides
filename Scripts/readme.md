# Pyhton Automation Scripts

1. [Bulk Rename](bulk_rename.py)
Here’s a simple script that renames multiple files in a folder based on a given pattern.
This script searches for files containing `old_name_part` in their names and replaces it with `new_name_part`.

2. [Automatic Backup](./auto_backup.py)
This script will copy all files from one directory to another for backup purposes using Python’s `shutil` module.

3. [Internet Download](./internet_dowload.py)
Here’s a simple script to download files from URLs. Download files from the internet using `aiohttp` library.

4. [Automate Email](./automate_email.py)
Automate sending emails using `smtplib` library. This script will send a simple email with a subject and body to a specified recipient. Make sure to enable less secure apps in Gmail if you use this method.

5. [Task Scheduler](./task_scheduler.py)
Scheduling tasks can be done easily using the `schedule` library, which allows you to automate tasks like sending an email or running a backup script at specific times.

6. [Web Scraping for Data Collection](./web_scraping.py)
Using `aiohttp` for asynchronous HTTP requests instead of the synchronous `requests` library can make web scraping more efficient.This scropt retrieves multiple pages in parallel using `BeautifulSoup` library.

7. [Automate Social Media](./sm_automation.py)
Do you manage social media accounts?, then you can automate posting by using the libraries like `Tweepy` (for Twitter) and `Instagram-API` (for Instagram) that allow you to post automatically.

8. [PDF Document Generation](./pdf_generation.py)
Automate PDF Document generation by using libraries like `Fpdf`.

9. [Monitor Website](./site_monitor.py)
Automate monitoring of website uptime using the requests library, that can periodically check if a website is online or not.

10. [Email Auto-Reply](./autoreply.py)
Set up an auto-reply, using the `imaplib` and `smtplib` libraries to automatically reply to emails.

11. [File Cleanup](./file_cleanup.py)
File cleanup, particularly for deleting or moving old files to maintain organized directories. Simple script that deletes files older than a specified number of days using the `os` and `time` modules.

12. [Password Generator](./password_generator.py)
Automate strong, unique passwords generation, essential for security, using the `random` module.
Simple script that generates random passwords of a specified length, incorporating letters, digits, and special characters to enhance security.

13. [Task Reminder](./task_reminder.py)
Create a task tracker or reminder using the `datetime` and `asyncio` modules.

14. [Monitor System](./system_monitor.py)
Monitor system resources (CPU, Memory Usage) using `psutil` library.

15. [Batch Image Resize](./image_resize.py)
Resize images in bulk, using the `Pillow` library.

16. [Backup to Cloud](./cloud_backup.py)
Automating backups to cloud services like Google Drive is made possible with Python using libraries such as `pydrive`.

17. [Data to Excel](./data_to_excel.py)
Enter data into Excel, ussing the `openpyxl` library.

18. [Data Cleaning](./data_cleaning.py)
automate data-cleaning from large datasets, remove empty rows from a CSV file.

19. [Extract Text from Image](./text_from_image.py)
Extract text from images using the `pytesseract` library, which can be useful when you need to digitize printed content or extract text from scanned documents.
