__author__ = 'Tallman'
def bubble_1(bubbleList):
    listLength = len(bubbleList)
    while listLength > 0:
        for i in range(listLength - 1):
            if bubbleList[i] > bubbleList[i+1]:
                bubbleList[i] = bubbleList[i] + bubbleList[i+1]
                bubbleList[i+1] = bubbleList[i] - bubbleList[i+1]
                bubbleList[i] = bubbleList[i] - bubbleList[i+1]
        listLength -= 1
    print bubbleList

def bubble(bubbleList):
    listLength = len(bubbleList)
    while listLength > 0:
        for i in range(listLength - 1):
            if bubbleList[i] > bubbleList[i+1]:
                temp = bubbleList[i+1]
                bubbleList[i+1] = bubbleList[i]
                bubbleList[i] = temp
        listLength -= 1
    print bubbleList

def isLeap(year):
    if year%4 == 0:
        if year%100 == 0:
            if year%400 == 0:
                Leap = 1
            else:Leap = 0
        else:Leap = 1
    else:Leap = 0
    if Leap==1:
        print year,"is a leap year"
    else:
        print year,"is not a leap year"
    #print year,Leap







if __name__ == '__main__':
    bubbleList = [3, 4, 1, 2, 5, 8, 0]
    bubble(bubbleList)
    bubbleList = [3, 4, 11, 26, 564, 8, 0,111,1111,12312312,12,123,1,53,12,123,124123412,123,9]
    bubble(bubbleList)

    isLeap(2016)
    isLeap(2017)
    isLeap(2014)
    isLeap(2000)
    isLeap(1800)

rain_speed = 8
if rain_speed < 5:
    print "Just a Scotch mist"
else:
    print "It's a real Cow-quaker out there"