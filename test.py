import json

a = 'https://list.jd.com/list.html?cat=9987,653,655&ev=exbrand_18374&page=1&sort=sort_rank_asc&trans=1&JL=6_0_0#J_main'
l = list(a)
l[69]='3'
a=''.join(l)
print(l)
print(a)