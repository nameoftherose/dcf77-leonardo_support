#creates a csv file with all quality data
#assumes minicom timestamped log file
/MES*Z/{
gsub(/\[/,"",$1);gsub(/\]/,"",$2)
gsub(/\(|\)|:|\-/,",",$7) #p
gsub(/\(|\)|:|\-/,",",$8) #s
gsub(/\(|\)|:|\-/,",",$9) #m
gsub(/\(|\)|:|\-/,",",$10) #h
gsub(/\(|\)|:|\-/,",",$11) #wd
gsub(/\(|\)|:|\-/,",",$12) #D
gsub(/\(|\)|:|\-/,",",$13) #M
gsub(/\(|\)|:|\-/,",",$14) #Y
print $1" "$2","$6","$7","$8$9$10$11$12$13$14
}