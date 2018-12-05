from datetime import datetime

with open('input.txt', 'r') as f:
    lines = f.readlines()

def isGuardEvent(event):
    if('#' in event):
        return True
    return False

def isWakeEvent(event):
    if('wakes' in event):
        return True
    return False

def isSleepEvent(event):
    if('asleep' in event):
        return True
    return False

def getGuardId(event):
    words = event.split(' ')
    for word in words:
        if(word[0] == "#"):
            return word[1:]



class Event:
    def __init__(self, timestamp, event):
        self.timestamp = timestamp
        self.event = event
    def __repr__(self):
        return self.timestamp.strftime('%Y-%m-%d %H:%M') + " " + self.event


entries = []
for line in lines:
    timestamp = datetime.strptime(line[1:17], '%Y-%m-%d %H:%M')
    event = line [19:]
    entries.append(Event(timestamp, event))


entries.sort(key = lambda r: r.timestamp)


guardSleep = {}

for entry in entries:
    if(isGuardEvent(entry.event)):
        currentGuard = getGuardId(entry.event)
    if(isSleepEvent(entry.event)):
        sleepTimeStamp = entry.timestamp
    if(isWakeEvent(entry.event)):
        delta = entry.timestamp - sleepTimeStamp
        if(currentGuard in guardSleep):
            print('MINUTES: ' + str((delta.seconds//60)%60))
            guardSleep[currentGuard] += (delta.seconds//60)%60
        else:
            guardSleep[currentGuard] = (delta.seconds//60)%60
print(guardSleep)

print('Max: ' + max(guardSleep, key=guardSleep.get))

print(650*401)