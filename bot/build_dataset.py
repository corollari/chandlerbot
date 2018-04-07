import re
import json

pairs=[]
chatterbot=[]
character="Chandler"
transcripts=open("transcripts").read()
ocurrences=re.findall(r"<p><strong>.*</p>\n<p><strong>"+character+"</strong>: .*</p>", transcripts)
for line in ocurrences:
    line=line.replace("<em>", "*");
    line=line.replace("</em>", "*");
    matched=re.match(r"<p><strong>.*</strong>.*: ([^<]*).*</p>\n<p><strong>"+character+"</strong>: ([^<]*)</p>", line)
    question=str(matched.group(1))
    answer=str(matched.group(2))
    pairs.append({"question":question, "answer":answer})
    chatterbot.append([question, answer])
open("pairs.json", "w").write(json.dumps(pairs))
print(len(pairs))
open("chatterbot.json", "w").write(json.dumps({"conversations":chatterbot}))
