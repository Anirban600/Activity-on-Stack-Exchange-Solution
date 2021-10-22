cat Badges.xml | grep -o 'Name="[^"]*' | cut -c 7- | sort | uniq -c
badges=`cat Badges.xml | grep -o 'Name="[^"]*"' | sort | uniq -c | wc -l`
echo
echo Total number of badges is : $badges
