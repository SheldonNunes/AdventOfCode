from datetime import datetime
import operator

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

def create_minutes() :
    minutes = []
    for i in range(60):
        minutes.append(0)
    return minutes

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
            print('GUARD: ' + str(currentGuard) + ', MINUTES: ' + str((delta.seconds//60)%60))
            guardSleep[currentGuard] += (delta.seconds//60)%60
        else:
            guardSleep[currentGuard] = (delta.seconds//60)%60
print(guardSleep)
max_id = max(guardSleep, key=guardSleep.get)
print('Max: ' + max_id)

guard_minutes = {}

for entry in entries:
    if(isGuardEvent(entry.event)):
        currentGuard = getGuardId(entry.event)
    if(isSleepEvent(entry.event)):
        sleepTimeStamp = entry.timestamp
    if(isWakeEvent(entry.event)):
        if(currentGuard not in guard_minutes):
            guard_minutes[currentGuard] = create_minutes()
        for i in range(sleepTimeStamp.minute, entry.timestamp.minute):
            guard_minutes[currentGuard][i] += 1



highest = 1
highestGuard = None
for guard in guard_minutes:
    for minutes in guard:
        print(minutes)
        if int(minutes) > int(highest):
            highest = minutes
            highestGuard = guard


print(highestGuard)
print(highest)

print(highestGuard * highest)

# print(len(minutes))
# print(minutes)
# print(guardSleep[max_id])

index, value = max(enumerate(minutes), key=operator.itemgetter(1))

# print(index)
# print(max_id)
# print(index * int(max_id))


# print(max_id * guardSleep[max_id])