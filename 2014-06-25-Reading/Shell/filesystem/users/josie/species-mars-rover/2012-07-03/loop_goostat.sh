for filename in *[AB].txt; do  echo $filename;  bash goostats $filename stat-$filename; done

