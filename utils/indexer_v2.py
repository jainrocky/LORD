import os, sys, warnings

algo_chart={
    'gy': 'Greedy Algorithms',
    'dp': 'Dynamic Programming',
    'ne': 'Naive Approach',
    'ms': 'Miscellaneous',
    'dc': 'Divide & Conquer',
    }
table_head = ['Name',
              'Best-case',
              'Average-case',
              'Worst-case',
              'Misc']

if __name__=='__main__':
    algo_path = os.path.join(os.path.dirname(__file__), '..', 'ALGO')
    ds_path = os.path.join(os.path.dirname(__file__), '..', 'DS')
    sys.path.append(algo_path)
    sys.path.append(ds_path)
    from pattern_searching.kmp__pattern_search import find_all

    algo_content = {'ms': []}
##    print(algo_path)

    folders = os.listdir(algo_path)
    for folder in folders:
        f = open(os.path.join(algo_path, folder, 'README.md'), 'r')
        lines = f.readlines()
        f.close()
        n = len(lines)
        i=0
        while i < n:
            heading = lines[i].strip()
            if heading.startswith('## '):
                row_content = { e:'' for e in table_head }
                row_content['Name']='[{}]({})'.format(heading[3:], 'ALGO/'+folder+'/'+heading[3:]+'.py')
                while i < n-1 and not lines[i+1].strip().startswith('## '):
                    line = lines[i+1].strip()
                    if line.startswith('* ') and line.find(': ') > 0:
                        key, value = line[2:].split(': ')
                        if key in table_head:
                            row_content[key]=value
                        elif  key == 'Category':
                            if value in algo_content:
                                algo_content[value].append(row_content)
                            else:
                                algo_content[value]= [row_content]
                    i+=1
            i+=1
        
        
    n = len(table_head)
    with open('../README.md', 'r+') as f:
        text = f.read()
        pattern = '## Content'
        ind = find_all(pattern, text)
        f.seek(ind[0]+len(pattern)+2)
        for k in sorted(algo_content):
            f.write('\n\n### '+algo_chart[k])
            f.write('\n\n'+' | '.join(table_head))
            f.write('\n'+' | '.join(['--']*n))
            
            for data in algo_content[k]:
                f.write('\n'+' | '.join( data.values() ) )
                
    print('Update Successfully!')
                





















                            
