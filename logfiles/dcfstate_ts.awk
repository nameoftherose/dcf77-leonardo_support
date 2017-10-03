BEGIN{
state=""
timestamp=""
}
{gsub(/\] *[0-9][0-9]*:[01] \./,"] ")}
/\] 1000,/{next}
{gsub(/\r/,"")}
/MES*Z/{ts=$3" "$4;quality = $6" "$NF;pl=$7;gsub(/p.*:/,"",pl);gsub(/\)/,"",pl);}
{timestamp=substr($1" "$2,2,19)}
#/^ *[0-9]*, /{ts = $2}
/Clock state:/{state = $NF}
/\] *[0-9]*,/{scopeCount = $3}
/Tick:/{
if (timestamp != "") printf "%s ",timestamp ;else printf "%s ",ts;
printf "%s ", scopeCount
printf "%s ", state
printf "%s ", quality
printf "%s\n", pl
timestamp = ""
ts = "??.??.??(?,?)??:??:255 MEZ "
scopeCount = (scopeCount+1i)","
}
