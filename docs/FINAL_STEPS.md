# Final steps (issues #7 and #8)

## 1. Merge the recorded clips into one mp4

Put every clip in one folder, named in presentation order:
`01_shriya_task.mp4`, `02_chase_eda.mp4`, `03_woosik_modeling.mp4`, `04_aung_evaluation.mp4`, `05_shriya_related.mp4`

```bash
# list the clips in order
for f in 0*.mp4; do echo "file '$f'"; done > clips.txt
# re-encode to H.264 + AAC so it plays everywhere (clips from different recorders can differ)
ffmpeg -f concat -safe 0 -i clips.txt -c:v libx264 -preset medium -crf 23 -c:a aac -b:a 128k -movflags +faststart final_video.mp4
```

No ffmpeg? `brew install ffmpeg` on Mac. iMovie or Zoom recordings exported as mp4 also work.

Target length: 20 minutes (the spec says do not go more than ~10% over).

## 2. Upload the video

1. Upload `final_video.mp4` to Google Drive
2. Share > General access > **Anyone with the link** (Viewer)
3. Copy the link into `video_url.txt` (one line, nothing else)

## 3. Export the notebook

1. Put `task_5_train.csv` next to the notebook
2. Kernel > Restart & Run All (about 15 to 20 minutes), check there are no errors and every section is filled in
3. File > Save and Export Notebook As > HTML
4. Rename the file to `workbook.html`

## 4. Check before submitting

```bash
pip install requests
python tools/check_submission.py
```

It mirrors the autograder: HTML header, Drive link downloadable, larger than 1 MB, mp4 format.

## 5. Submit on Gradescope (before 12/1 morning)

* Upload `workbook.html` and `video_url.txt`
* Add all 4 group members to the submission
* Confirm the autograder output says everything is okay
