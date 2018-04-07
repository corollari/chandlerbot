for link in $(cat ../links); do
	wget $link
done
