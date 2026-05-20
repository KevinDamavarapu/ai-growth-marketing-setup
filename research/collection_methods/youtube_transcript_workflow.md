# YouTube Transcript Collection Workflow

## Objective

Collect and organize high-signal transcript material from long-form SEO and AI-related interviews for structured research and analysis.

---

## Method Used

# API-Assisted Transcript Collection Workflow

## Objective

To improve transcript collection scalability and reduce manual extraction effort, an API-assisted transcript workflow was added using Python and the `youtube-transcript-api` library.

---

## Workflow Overview

### Step 1 — Identify Relevant Videos

Relevant expert interviews, podcasts, and educational videos are selected based on:
- AI SEO relevance
- growth marketing relevance
- operational insight quality
- practical workflow discussions

---

### Step 2 — Extract Video ID

Example:

```text
https://youtu.be/qujABKOAThA?si=oA9ynxBf4ZAWDEbq
```

Correct video ID:

```text
qujABKOAThA
```

Important:
The `?si=` parameter is NOT part of the video ID.

---

### Step 3 — Run Transcript Fetching Script

Command:

```bash
python fetch_transcript.py
```

The workflow uses:
- Python
- youtube-transcript-api

to fetch publicly available YouTube transcripts automatically.

---

### Step 4 — Store Raw Transcript

Generated transcripts are stored inside:

```text
research/youtube-transcripts/[expert-name]/raw-transcript-1.md
```

Timestamps are preserved to maintain:
- traceability,
- source integrity,
- and reference clarity.

---

### Step 5 — Generate Structured Analysis

The raw transcript is analyzed to produce:
- summaries,
- key insights,
- operational takeaways,
- and conclusions.

These are documented separately inside:
```text
video-1.md
```

---

# Workflow Advantages

- Faster transcript collection
- Improved scalability
- Structured transcript formatting
- Better research consistency
- Reduced manual effort
- Easier transcript archiving

---

# Limitations

- Some videos disable public transcripts
- Auto-generated captions may contain inaccuracies
- Certain videos may require manual fallback transcription
- Scripts must be executed from the correct project directory

---

# Fallback Method

If API transcript extraction fails:
1. Open YouTube transcript panel manually
2. Copy transcript directly from YouTube
3. Preserve timestamps when possible
4. Store transcript in raw transcript archive

Transcript collection was performed using YouTube’s built-in transcript feature.

Workflow used:
- Manual transcript extraction from YouTube
- AI-assisted organization and summarization using Claude Code and Codex
- Manual review and cleanup for accuracy and relevance

---

## Workflow Steps

1. Identify relevant long-form interviews and podcasts
2. Open YouTube transcript panel
3. Copy transcript content manually
4. Extract high-signal sections related to:
   - AI search
   - SEO workflows
   - content structure
   - LLM optimization
   - visibility strategies
5. Organize insights into structured markdown research documents
6. Add summaries, annotations, and strategic observations

---

## Why This Approach Was Chosen

Long-form podcast interviews often contain:
- nuanced operational insights
- future-facing SEO strategy
- detailed AI search discussions
- practical workflow observations

Manual extraction combined with AI-assisted organization provided a lightweight but effective research workflow without requiring custom scraping infrastructure.

---

## Observations

- Long-form interviews provide significantly richer insights than short-form social content
- AI tools help accelerate organization and synthesis, but manual filtering is still necessary
- Structured transcript segmentation improves readability and research quality