def calculate_love_score(name1,name2):
    result=name1+name2
    lower_names= result.lower()
    tcount=lower_names.count('t')
    rcount=lower_names.count('r')
    ucount=lower_names.count('u')
    ecount=lower_names.count('e')
    totalTrue=tcount+rcount+ucount+ecount

    lcount=lower_names.count('l')
    ocount=lower_names.count('o')
    vcount=lower_names.count('v')
    ecount=lower_names.count('e')
    totalLove=lcount+ocount+vcount+ecount

    print(f"Love score = {totalTrue}{totalLove}")

calculate_love_score('kanye West','kim kardashian')





