import os
import glob
import re

directory = r"D:\aghado01\codex-scientiae\compendia\ph"
out_file = os.path.join(directory, "tmp", "headers.txt")

with open(out_file, "w", encoding="utf-8") as f_out:
    for filepath in glob.glob(os.path.join(directory, "*.md")):
        filename = os.path.basename(filepath)
        if filename in ["_CONTENTS.md", "REF-MPH.md", "REF-PH.md"]:
            continue
        with open(filepath, "r", encoding="utf-8") as f_in:
            for line_no, line in enumerate(f_in, 1):
                if re.match(r"^#+ ", line):
                    f_out.write(f"{filename}:{line_no}: {line}")
