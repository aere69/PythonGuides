import aiofiles
import os
import asyncio
import time

async def clean_up(folder_path, days_old):
    now = time.time()
    cutoff_time = now - (days_old * 86400)
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.getmtime(file_path) < cutoff_time:
            await aiofiles.os.remove(file_path)
            print(f"Deleted {filename}")

folder = '/path/to/your/folder'
asyncio.run(clean_up(folder, 30))