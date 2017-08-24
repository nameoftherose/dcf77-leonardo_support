BEGIN{
state="Clock state: useless"
ts=""
}
{gsub(/\r/,"")}
/Decoded/{
if (ts>$0) print "MONOTONICITY ERROR",ts,$0;
ts=$0}
/Clock state:/{
if (state != $0) {
   print ts," ",state,">",$3
   state = $0
   }
stats[$3] += 1
stats["total"] += 1
}
END{
st[1]="useless"
st[2]="dirty"
st[3]="synced"
st[4]="free"
st[5]="locked"
st[6]="unlocked"
st[7]="total"
   print ts," ",state
#for (i in stats) print i,stats[i]
for (i=1;i<=7;i++) print st[i],stats[st[i]]
}

