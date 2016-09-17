from collections import OrderedDict

for x in range(0,10):

    output = open('dics{}.dat'.format(x), 'w+')
    mrr = open('mrr{}.dat'.format(x), 'w+')
    with open('predictions{}.dat'.format(x), 'r') as inputFile:
        lines = inputFile.readlines()
        for i, line in enumerate(lines):
            classes = line.split(' ')
            predicted=line[0]

            mappedClasses={}
            # output.write('{} '.format(predicted))
            for j,value in enumerate(classes[1:]):
                mappedClasses[j+1]=value.rstrip()
                print 'valueClass: {}'.format(value)
                output.write('{} {}'.format(j,value))

            ranking = sorted(mappedClasses.items(), key=lambda (k,v):v)
            rankLine=''
            for k, (classRank,value) in enumerate(ranking):
                # print 'classRank: {}'.format(classRank)
                # print 'value: {}'.format(value)
                # print 'k: {}'.format(k)
                recip = 1.0 / (k+1)
                # print 'recip: {:.5f}'.format(recip)
                rank='{}:{}'.format(classRank,recip)
                rankLine=rankLine.lstrip()+' '+rank
            mrr.write(rankLine+'\n')
            print rankLine
    output.close
    mrr.close
