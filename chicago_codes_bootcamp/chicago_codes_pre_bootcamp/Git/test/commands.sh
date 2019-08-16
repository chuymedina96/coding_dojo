cd ~/Desktop
mkdir test
touch index.html styles.css commands.txt
cp index.html ./index_2.html
cd ~/Desktop
mkdir destination
mv test/index_2.html ~/Desktop/destination
cd ~/Desktop/test && rm -rf styles.css

