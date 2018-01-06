corpus_dir=${1:?"Source directory of the corpus"}
out_file=${2:?"Filename for CSV output"}

echo '#Application,URL,SHA' > $out_file
for p in $corpus_dir/*; do
    if [[ -d $p ]]; then
        app=`basename $p`
        url=`git -C $p config --get remote.origin.url`
        sha=`git -C $p log --pretty=format:'%H' -n 1`
        echo $app,$url,$sha >> $out_file
    fi
done

    
