{gsub(//,"")
 split($1,f1,/ /)
 split($2,f2,/ /)
 gsub(/255/,"-1",$NF)
 print "20"f1[1]" "f1[2]","f2[3]","$NF
}
