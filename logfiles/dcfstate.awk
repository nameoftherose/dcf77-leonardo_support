BEGIN{
state=""
timestamp=""
}
{gsub(/\r/,"")}
/MES*Z/{ts=$1" "$2;quality = $4" "$NF}
/Decode/{timestamp=$3" "$5}
/^ *[0-9]*, /{ts = $1}
/Clock state:/{state = $NF}
/^ *[0-9]*,/{scopeCount = $1}
/Tick:/{
if (timestamp != "") printf "%s ",timestamp ;else printf "%s ",ts;
printf "%s ", scopeCount
printf "%s ", state
printf "%s\n", quality
timestamp = ""
ts = "??.??.??(?,?)??:??:255 MEZ "
scopeCount = "      "
}
