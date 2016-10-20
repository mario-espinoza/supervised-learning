from collections import OrderedDict
from sklearn.metrics import confusion_matrix

for x in range(0,10):

    output = open('dics{}.dat'.format(x), 'w+')
    mrr = open('mrr{}.dat'.format(x), 'w+')

    rankValues = []
    manual=[]
    predictions=[]

    with open('train{}.dat'.format(x), 'r') as trainfile:
        lines = trainfile.readlines()
        for i, line in enumerate(lines):
            classes = line.split(' ')
            manual.append(line[0])
    trainfile.close

    with open('predictions{}.dat'.format(x), 'r') as predictionFile:
        lines = predictionFile.readlines()
        for i, line in enumerate(lines):
            classes = line.split(' ')
            predicted=line[0]
            predictions.append(predicted)
            print 'predicted {}'.format(predicted)

            mappedClasses={}
            print 'classes {}'.format(classes)
            # output.write('{} '.format(predicted))
            for j,clas in enumerate(classes[1:]):
                # print clas
                mappedClasses[j+1]=clas.rstrip()
                print 'valueClass: {}'.format(clas)
                output.write('{} {}'.format(j,clas))

            ranking = sorted(mappedClasses.items(), key=lambda (k,v):v)
            rankLine=''
            for k, (classRank,value) in enumerate(ranking):
                # print 'classRank: {}'.format(classRank)
                # print 'value: {}'.format(value)
                # print 'k: {}'.format(k)
                recip = 1.0 / (k+1)
                # print 'recip: {:.5f}'.format(recip)
                rank='{}:{}'.format(classRank,recip)
                st = '{}'.format(classRank)
                if st == predicted:
                    print 'classRank: {}, predicted: {}, recip: {}'.format(classRank,predicted,recip)
                    rankValues.append(recip)
                rankLine=rankLine.lstrip()+' '+rank
            mrr.write(rankLine+'\n')
            print rankLine
    predictionFile.close

    confusion_matrix(manual, predictions)

    average =  'average: {}'.format(sum(rankValues)/len(rankValues))
    print average
    output.write(average)
    output.close
    mrr.close
