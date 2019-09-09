poblation->  c1,c2,c3...ck   2<=k<=10
for each k, n individuals shall be generated
for each individual, a score shall be computed
sort individuals by score

choose the first m<n*9 with highest score that will have ofspring
cross m with everyoneElse, this will produce n*9*(n*9-1)/2-((n*9-m)*(n*9-1-m)/2) additional individuals
sort by score
n*9 shall survive because of their score, the rest of individuals die
repeat t times
 