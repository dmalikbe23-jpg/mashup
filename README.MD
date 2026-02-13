# 🎵 Title: YouTube Mashup Generator

---

## 1. Methodology

The project follows the below workflow:

```
User Input (Singer, No. of Videos, Duration, Email)
        ↓
Fetch YouTube Videos (yt-dlp)
        ↓
Convert Video to Audio (MoviePy / FFmpeg)
        ↓
Trim Audio to Required Duration (pydub)
        ↓
Merge All Audios into Single File
        ↓
Create ZIP File
        ↓
Send ZIP via Email (SMTP)
```

---

## 2. Description

The **YouTube Mashup Generator** is a Python-based application that:

- Downloads N YouTube videos of a given singer
- Converts videos to audio format (.mp3)
- Cuts the first T seconds from each audio
- Merges all trimmed audios into one single mashup file
- Creates a ZIP file of the final output
- Sends the ZIP file to the user via email

### 🔹 Technologies Used

- Python 3.11
- yt-dlp (YouTube Downloader)
- MoviePy (Video to Audio Conversion)
- FFmpeg (Audio Processing Backend)
- pydub (Audio Editing & Merging)
- Flask (Web Interface)
- SMTP (Email Sending)

---

## 3. Input / Output

### ✅ Input (Web Form / CLI)

| Parameter        | Description |
|------------------|-------------|
| Singer Name      | Name of the singer |
| Number of Videos | Number of YouTube videos to download |
| Duration (sec)   | Duration to cut from each video |
| Email ID         | Email to receive the ZIP file |

### ✅ Example Input

```
Singer Name: Sharry Maan
Number of Videos: 5
Duration: 20
Email: example@gmail.com
```

---

### 🎧 Output

- Trimmed MP3 files stored in `/audios`
- Final merged file: `output.mp3`
- ZIP file sent to user's email

---

## 4. Screenshot of Interface

![alt text](<Screenshot 2026-02-13 232429.png>)
---

## 5. Conclusion

This project demonstrates integration of:

- YouTube video extraction
- Audio processing
- File handling
- Web development
- Email automation

It combines multiple Python libraries to create a complete end-to-end multimedia mashup system.

---

# 🚀 Developed By

Disha Malik  
Roll Number: 102303141

