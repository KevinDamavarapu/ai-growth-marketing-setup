# YouTube Transcript Fetcher

## Overview

This tool automates YouTube transcript collection for AI-powered SEO and growth marketing research workflows.

The script uses the `youtube-transcript-api` Python library to:
- fetch publicly available YouTube transcripts,
- extract timestamped dialogue,
- and save structured transcript outputs for downstream analysis.

The workflow was added to improve:
- research scalability,
- transcript consistency,
- and operational efficiency.

---

# Files

| File | Purpose |
|---|---|
| `fetch_transcript.py` | Main transcript fetching script |
| `requirements.txt` | Python dependencies |
| `sample_output.txt` | Example generated transcript output |
| `README.md` | Tool documentation |

---

# Installation

Install dependencies:

```bash
pip install -r requirements.txt
```

Or manually install:

```bash
pip install youtube-transcript-api
```

---

# Usage

Run the script:

```bash
python fetch_transcript.py
```

Update the `video_id` variable inside the script before execution.

Example:

```python
video_id = "qujABKOAThA"
```

---

# Output

The script generates:
- timestamped transcript text
- automatically saved into `sample_output.txt`

Example output:

```text
0.00s: If Google's AI overviews are killing your organic clicks...
4.24s: But the real shift might be even bigger...
```

---

# Notes

- Some videos may not expose public transcripts
- Some videos only provide auto-generated captions
- YouTube share links may contain additional `?si=` parameters that are NOT part of the actual video ID
- The script must be executed from the correct directory (`tools/transcript-fetcher/`)

---

# Why This Matters

This workflow demonstrates:
- AI-assisted research operations
- lightweight automation tooling
- API/library integration
- scalable transcript collection workflows
- operational content research systems