import re
import json

pairs=[]
chatterbot=[]
character="Chandler"
transcripts=open("transcripts", encoding="ISO-8859-1").read()
#print(transcripts)
ocurrences=re.findall(r"<p>.*:<.*> ([^<]*).*</p>[\n]*<p>.*Chandler.*:<.*> ([^<]*)</p>", transcripts)
print(len(ocurrences))

#print(ocurrences)
for line in ocurrences:
    question=line[0]
    question=re.sub("\([^\)]*\)", "", question)
    question=re.sub("\\n", " ", question)
    answer=line[1]
    answer=re.sub("\([^\)]*\)", "", answer)
    answer=re.sub("\\n", " ", answer)
    pairs.append({"question":question, "answer":answer})
    chatterbot.append([question, answer])
#open("pairs.json", "w").write(json.dumps(pairs))
print(len(pairs))
open("chatterbot.json", "w").write(json.dumps({"conversations":chatterbot}))

'''   line=line.replace("<em>", "*");
    line=line.replace("</em>", "*");
    matched=re.match(r"<p>.*: ([^<]*).*</p>.*<p>.*Chandler.*: ([^<]*)</p>", line)
'''   
