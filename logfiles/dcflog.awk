BEGIN{
state="Clock state: useless"
ts=""
}
{gsub(/\r/,"")}
/Decoded/{gsub(/Decoded time: /,"");ts=$0}
/Clock state:/{
if (state != $0) {
   print ts," ",state,">",$3
   state = $0
   }
stats[$3] += 1
stats["total"] += 1
}
END{
   print ts," ",state
for (i in stats) print i,stats[i]
}

