import feedparser
from bs4 import BeautifulSoup
import os
import re
  
def getNews(url):
        # 1️⃣ Parse the RSS feed
    rss_url = url  
    feed = feedparser.parse(rss_url)
    fileName=feed.feed.get("title")
    # 2️⃣ Folder to save text files
    output_folder = "app/files/"+ fileName

    os.makedirs(output_folder, exist_ok=True)

    # 3️⃣ Iterate over entries
    for i, entry in enumerate(feed.entries, start=0):
        # Get basic info
        title = entry.get("title", f"article_{i}")
        safe_title = "".join(c if c.isalnum() or c in " -_" else "_" for c in title)  # safe filename

        # Get content
        if "content" in entry:
            html_content = entry.content[0].value
        else:
            html_content = entry.get("summary", "")

        html_content = f"{title}\n\n{html_content}"
        # Clean HTML
        soup = BeautifulSoup(html_content, "html.parser")
        text_content = soup.get_text(separator="\n").strip()
        # Replace 2 or more newlines with a single newline
        text_content = re.sub(r'\n+', '\n', text_content)
        # Save to text file
        file_path = os.path.join(output_folder, f"{safe_title}.txt")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(text_content)

    print(f"Saved {len(feed.entries)} articles as text files in '{output_folder}'")

