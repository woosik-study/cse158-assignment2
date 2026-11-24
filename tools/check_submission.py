"""Pre-submission check for CSE 158 Assignment 2.

Mirrors the checks in the assignment spec: workbook.html must be a real HTML export, and the
video link must be a downloadable mp4 larger than 1 MB (YouTube links are only checked for format).

Usage (from the repo root, with workbook.html and video_url.txt next to it):
    pip install requests
    python tools/check_submission.py
"""
import sys
import requests

ok = True


def fail(msg):
    global ok
    ok = False
    print("FAIL:", msg)


# 1. workbook.html
try:
    with open("workbook.html", encoding="utf8") as f:
        head = f.read(200)
    if head.startswith("<!DOCTYPE html>"):
        print("OK: workbook.html is an HTML export")
    else:
        fail("workbook.html does not start with <!DOCTYPE html> (export it from Jupyter, do not rename a .ipynb)")
except FileNotFoundError:
    fail("workbook.html not found")

# 2. video_url.txt
try:
    url = open("video_url.txt").read().strip()
except FileNotFoundError:
    fail("video_url.txt not found")
    url = ""

if url and ("youtube" in url or "youtu.be" in url):
    print("OK: YouTube link found. Make sure the video is Public or Unlisted:", url)
elif url:
    file_id = None
    if "id=" in url:
        file_id = url.split("id=")[1].split("/")[0].split("&")[0]
    elif "/d/" in url:
        file_id = url.split("/d/")[1].split("/")[0]
    if not file_id:
        fail("could not find a Google Drive file id in: " + url)
    else:
        dl = "https://drive.google.com/uc?export=download&id=" + file_id
        r = requests.get(dl, stream=True, timeout=60)
        chunk = next(r.iter_content(chunk_size=1024 * 1024))
        if len(chunk) < 1024 * 1024 and b"Virus scan warning" in chunk:
            uuid = chunk.decode("utf8", "ignore").split('uuid" value="')[1].split('"')[0]
            dl = f"https://drive.usercontent.google.com/download?id={file_id}&export=download&confirm=t&uuid={uuid}"
            r = requests.get(dl, stream=True, timeout=60)
            chunk = next(r.iter_content(chunk_size=1024 * 1024))
        if len(chunk) < 1024 * 1024:
            fail("downloaded less than 1 MB: the link is probably not shared as 'Anyone with the link', or not a video")
        elif chunk[4:8] != b"ftyp":
            fail("the file does not look like an mp4 (missing 'ftyp' header)")
        else:
            print("OK: Google Drive video downloads and looks like an mp4")

print("\nAll checks passed" if ok else "\nFix the items above before submitting")
sys.exit(0 if ok else 1)
