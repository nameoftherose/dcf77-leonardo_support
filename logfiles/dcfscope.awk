BEGIN{
ts="..-..-.. . ..:..:.. .... .."
}
{gsub(/\r/,"")}
/Clock state:/{
state = substr($3,1,4)
}
/Decoded/{
gsub(/Decoded time: /,"")
ts=$0}
/^ *[0-9]*, /{
print ts,state,$0
}
END{
}

