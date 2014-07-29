count=4
mkdir princeton_$count
cd princeton_$count
k=0
while read word; do cp ~/workspace/vocab_prep/audio_cache/$word.mp3 $k-$word.mp3; k=$(($k+2)); done < ../princeton$count.txt
#k=0;for file in *; do mv $file $k-$file; done
mp3wrap output.mp3 `ls -1 *.mp3 | sort`
cd -;
