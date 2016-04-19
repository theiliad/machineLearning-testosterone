from sklearn import tree

'''
Please note that with machine learning, the more data you have, the more solid the results!

This is just a very very basic example of my previous experience with Scikit, that I decided to
recreate, but this time, using Google's ways offered in these Tutorials:

https://www.youtube.com/playlist?list=PLOU2XLYxmsIIuiBfYad6rFYQU_jL2ryal
'''

features = [[617], [668], [606], [562], [524], [471], [376]]
labels = ["25-34", "35-44", "45-54", "55-64", "65-74", "75-84", "85-100"]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)

loopUp = True

while (loopUp):
    testLevel = raw_input("Enter a Testerone Level Amount (type exit to kill): ")
    if (any(c.isalpha() for c in testLevel)):
        if (testLevel.lower() == "exit"):
            loopUp = False
    elif (float(testLevel) > 700 or float(testLevel) < 350):
        print "Please enter an amount between 350 and 700!"
    else:
        print "The person must be " + clf.predict([[float(testLevel)]]).tostring() + " years old"
