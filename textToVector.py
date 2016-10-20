from collections import Counter
import csv, collections, re, os

bagsofwords=[]
classes=[]
classSummary=[]

def parseBags(row,list,classes):
    title = row[2].lstrip().rstrip()
    className = row[1]
    # classID = classEnum.get(className)

    bagofwords = collections.Counter(re.findall(r'\w+', title.lower()))
    list.append(bagofwords)
    classes.append(className)
    classSummary.append(className)
    # print title
    # print bagofwords

with open('marioEspinoza.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')

    for i,row in enumerate(spamreader):
        if i>0:
            parseBags(row,bagsofwords,classes)

    sumbags = sum(bagsofwords, collections.Counter())
    mostCommon = sumbags.most_common()
    # print 'Dimensions: {}'.format(len(sumbags))
    # print 'Sumbags: {}'.format(sumbags)
    # print 'Most common: {}'.format(mostCommon)

    print 'Total Clases: {}'.format(Counter(classSummary))
    print 'Total Clases: {}'.format(sum(Counter(classSummary).values()))

    for n in range(0,10):
        trainFile = open('train{}.txt'.format(n),'w+')
        testFile = open('test{}.txt'.format(n),'w+')
        completefile = open('complete{}.txt'.format(n),'w+')

        for i,v in enumerate(bagsofwords):

            dic=dict(v)
            # print 'dic: {}'.format(dic)
            # print 'class: {}'.format(classes[i])
            fileLine='{}'.format(classes[i])
            for index, (word,count) in enumerate(mostCommon):
                # print 'index: {}'.format(index)
                # print 'word: {}'.format(word)
                # print 'count: {}'.format(count)

                if dic.get(word) > 0:
                    feat = ' {}:{}'.format(index+1,dic[word])
                    fileLine+=feat
            if i%10==n:
                trainFile.write(fileLine+'\n')
            else:
                testFile.write(fileLine+'\n')

        testFile.close
        trainFile.close

    for x in range(0,10):
        modelFile = open('model{}.txt'.format(x),'w+')
        predictionsFile = open('predictions{}.txt'.format(x),'w+')
        # importer = 'bin/mallet import-svmlight --input archivoEntrenamiento%s.txt --output training%s.mallet' % (x,x)
        learn='../SVM/svm_multiclass/svm_multiclass_learn -c 5000 train{}.txt model{}.txt >> resultL{}.txt'.format(x,x,x)
        print learn
        classify='../SVM/svm_multiclass/svm_multiclass_classify ./test{}.txt ./model{}.txt ./predictions{}.txt >> resultC{}.txt'.format(x,x,x,x)
        print classify
        os.system(learn)
        print 'learn ready'
        os.system(classify)
        print 'classify ready'
