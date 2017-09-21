BEGIN{FS=","}
/\(/{next}
{
 split($1,f1,/ /)
 split($2,f2,/ /)
 gsub(/255 /,"-1,",$NF)
 gsub(/ /,",",$NF)
 print f1[1]" "f1[2]","f2[3]","$NF
}
