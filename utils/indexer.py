import os, sys, warnings

algo_chart={
    'gy': 'Greedy Algorithms',
    'dp': 'Dynamic Programming',
    'ne': 'Naive Approach',
    'ms': 'Miscellaneous',
    'dc': 'Divide & Conquer',
    }

if __name__=='__main__':
    algo_path = os.path.join(os.path.dirname(__file__), '..', 'ALGO')
    ds_path = os.path.join(os.path.dirname(__file__), '..', 'DS')
    sys.path.append(algo_path)
    sys.path.append(ds_path)
    from pattern_searching.kmp__pattern_search import find_all

    algo_content = {'ms': []}

    
    for i, walk in enumerate(os.walk(algo_path)):
        if i!=0:
            dirs = walk[1]
            files = walk[2]
            for f in files:
                if f[-3:]=='.py':
                    q = f.split('__')
                    if len(q)>2 and q[0] in algo_chart:
                        if q[0] not in algo_content:
                            algo_content[q[0]] = []
                        algo_content[q[0]].append('[{}]({})'.format(f[4:], walk[0].split('..')[1].replace('\\', '/')+ '/' + f))
                    else:
                        algo_content['ms'].append('[{}]({})'.format(f, walk[0].split('..')[1].replace('\\', '/')+ '/' + f))
            
                    

    with open('../README.md', 'r+') as f:
        text = f.read()
        pattern = '## Content'
        ind = find_all(pattern, text)
        f.seek(ind[0]+len(pattern)+2)
        for k in sorted(algo_content):
            f.write('\n\n### '+algo_chart[k])
            for name in algo_content[k]:
                f.write('\n* '+name)
                
    print('Update Successfully!')
                





















                            
