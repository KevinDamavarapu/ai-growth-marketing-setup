print("Script started successfully")
from youtube_transcript_api import YouTubeTranscriptApi

# Replace with your actual YouTube video ID
video_id = "4KyYqe1s_XY"

try:
    ytt_api = YouTubeTranscriptApi()
    transcript = ytt_api.fetch(video_id)

    with open("sample_output.txt", "w", encoding="utf-8") as file:
        for entry in transcript:
            file.write(f"{entry.start:.2f}s: {entry.text}\n")

    print("Transcript fetched successfully and saved to sample_output.txt")

except Exception as e:
    print("Error fetching transcript:")
    print(e)