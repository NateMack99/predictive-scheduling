"""
Use this to reformat the csv files in training_data into json with keys:
'prompt': input prompt
'length': output length in tokens (using qwen tokenizer) 
Currently only supports Qwen
"""


import json
import csv
from pathlib import Path
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained(
    "Qwen/Qwen2.5-7B-Instruct"
)

name = input("file name: ")
out_name = str(Path(name).with_suffix(".json"))
print(out_name)
with open(name, "r") as inf, open(out_name, "w", encoding="utf-8") as outf:
    inf.__next__()
    for row in csv.reader(inf):
        prompt = row[0]
        response = row[1]
        print(response)
        if not prompt or response is None:
            continue

        length = len(
            tokenizer.encode(
                response,
                add_special_tokens=False,
            )
        )

        outf.write(json.dumps({
            "prompt": prompt,
            "length": length,
        }, ensure_ascii=False) + "\n")