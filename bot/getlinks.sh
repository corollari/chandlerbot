cat FriendsTranscripts.html | sed 's/    <li><a href="//' | sed 's/".*<\/li>//' | sed 's/<\/ul>.*<ul>//' | awk "/http.*/{print}" > links
