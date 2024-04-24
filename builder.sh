export PATH="$coreutils/bin"
declare -xp
mkdir $out
echo "#!$py/bin/python" > $out/hello.py
cat $src >> $out/hello.py
chmod 755 $out/hello.py
