export PATH="$coreutils/bin"
declare -xp
mkdir $out/bin -p
echo "#!$py/bin/python" > $out/bin/hello
cat $src >> $out/bin/hello
chmod 755 $out/bin/hello
