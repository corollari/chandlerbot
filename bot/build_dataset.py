import re
import json

pairs=[]
chatterbot=[]
deepQA=""
character=""
transcripts=open("transcripts", encoding="ISO-8859-1").read()
#print(transcripts)
ocurrences=re.findall(r"<p>.*:<.*> ([^<]*).*</p>[\n]*<p>.*Joey.*:<.*> ([^<]*)</p>", transcripts)
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
    deepQA+=question+"\n"+answer+"\n===\n"
#open("pairs.json", "w").write(json.dumps(pairs))
print(len(pairs))
open("chatterbot_joey.json", "w").write(json.dumps({"conversations":chatterbot}))
open("deepQA_joey.txt", "w").write(deepQA[:-4])

'''   line=line.replace("<em>", "*");
    line=line.replace("</em>", "*");
    matched=re.match(r"<p>.*: ([^<]*).*</p>.*<p>.*Chandler.*: ([^<]*)</p>", line)
'''   
