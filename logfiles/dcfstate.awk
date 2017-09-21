BEGIN{
state=""
timestamp=""
}
{gsub(/\r/,"")}
/MES*Z/{ts=$1" "$2;quality = $4" "$NF;pl=$5;gsub(/p.*:/,"",pl);gsub(/\)/,"",pl)}
/Decode/{timestamp=$3" "$5}
/^ *[0-9]*, /{ts = $1}
/Clock state:/{state = $NF}
/^ *[0-9]*,/{scopeCount = $1}
/Tick:/{
if (timestamp != "") printf "%s ",timestamp ;else printf "%s ",ts;
printf "%s ", scopeCount
printf "%s ", state
printf "%s ", quality
printf "%s\n", pl
timestamp = ""
ts = "??.??.??(?,?)??:??:255 MEZ "
scopeCount = (scopeCount+1)","
}
