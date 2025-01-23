import random

## MAIN VARS ##
count = 0
id = 0

names = []
classes = []
students = []
flags = []
markers = []

## DUTIES ##
schflag = [[], [], [], [], []]  #1 2 1 1 1
natflag = [[], [], [], [], []]  #2 1 2 1 1
markerduty = [[], [], [], [], []]  #2

foyerhostel = [[], [], [], [], []]  #2
foyerlate = [[], [], [], [], []]  #2
guardhouse = [[], [], [], [], []]  #2
gatea = [[], [], [], [], []]  #3
gateb = [[], [], [], [], []]  #1
canteen = [[], [], [], [], []]  #2
lift1 = [[], [], [], [], []]  #2
lift2 = [[], [], [], [], []]  #1
levelpatrol = [[], [], [], [], []]  #4

## MORNING ROSTER ##
with open('FLAGS.txt', 'r') as q:
  fg = q.readlines()
  f_len = len(fg)
  for flag in fg:
    f_splitted = flag.split('\n')
    splitted_flag = f_splitted[0]

    flags.append(splitted_flag)

marker_temp = []
with open('MARKERS.txt', 'r') as b:
  mr = b.readlines()
  m_len = len(mr)
  for mrk in mr:
    m_splitted = mrk.split('\n')
    splitted_marker = m_splitted[0]
    markers.append(splitted_marker)
    marker_temp.append(splitted_marker)

## RECESS ROSTER ##

## SETUP ##
with open("NAMES.txt", "r") as f:
  ns = f.readlines()
  length = len(ns)
  for i in ns:
    name = i

    names.append(name[0])

while count < length:
  person = dict(name=f"{names[id]}", num=id, days=2)
  students.append(person)
  id += 1
  count += 1
## SETUP END ##

## ASSIGNING ##
for i in students:
  ynm = i.get('name')
  yct = i.get('id')

  ## TYPE SETTING ##
  if ynm in flags:
    i['type'] = 'flag'
    i['days'] -= 1
  if ynm in markers:
    i['type'] = 'marker'
    i['days'] -= 1
  else:
    i['type'] = 'normal'

## FLAGS DUTY ##
flag_temp = flags.copy()
nat_flag_duty = []
while len(nat_flag_duty) < 7:
  nat_flag_duty_c = random.choice(flag_temp)
  nat_flag_duty.append(nat_flag_duty_c)
  nat_flag_duty = list(dict.fromkeys(nat_flag_duty))

sch_flag_duty = []
while len(sch_flag_duty) < 6:
  sch_flag_duty_check = 0
  sch_flag_duty_c = random.choice(flag_temp)
  while sch_flag_duty_check < 1:
    if sch_flag_duty_c in nat_flag_duty:
      sch_flag_duty_c = random.choice(flag_temp)
    else:
      sch_flag_duty_check += 1
  sch_flag_duty.append(sch_flag_duty_c)
  sch_flag_duty = list(dict.fromkeys(sch_flag_duty))
## FLAG SETTING OVER ##

## MARKER SETTING ##
marker_duty = []
while len(marker_duty) < 13:
  marker_duty_c = random.choice(marker_temp)
  marker_duty.append(marker_duty_c)
  marker_duty = list(dict.fromkeys(marker_duty))

## MARKING SETTING OVER ##

## NORMAL SETTING ##
normal_duties = []
d_count = 0
while d_count in range(2):
  for y in students:
    y_work = y['days']
    y_name = y['name']
    if y_work >= 1:
      normal_duties.append(y_name)
      y['days'] -= 1
  d_count += 1

## DUTY SETTING IN ##


def dutyset(dutyarr, dutyend, n1, n2, n3, n4, n5):
  c = 0
  cnt = int(n1) + int(n2) + int(n3) + int(n4) + int(n5)
  for c in range(cnt):
    if c >= 0 and c < n1:
      dutyarr[0].append(dutyend[0])
    elif c > (n1 - 1) and c < (n2 + n1):
      dutyarr[1].append(dutyend[0])
    elif c > (n2 + n1 - 1) and c < (n3 + n2 + n1):
      dutyarr[2].append(dutyend[0])
    elif c > (n3 + n2 + n1 - 1) and c < (n4 + n3 + n2 + n1):
      dutyarr[3].append(dutyend[0])
    elif c > (n4 + n3 + n2 + n1 - 1) and c < (n5 + n4 + n3 + n2 + n1):
      dutyarr[4].append(dutyend[0])

    if len(dutyend) > 0:
      dutyend.pop(0)
    c += 1


def normalduty(dutyarr, n1, n2, n3, n4, n5):
  c = 0
  cnt = int(n1) + int(n2) + int(n3) + int(n4) + int(n5)
  for c in range(cnt):
    nchoice = random.choice(normal_duties)
    if c >= 0 and c < n1:
      while nchoice in dutyarr[0]:
        nchoice = random.choice(normal_duties)
      while nchoice in foyerhostel[0] or nchoice in foyerlate[
          0] or nchoice in guardhouse[0] or nchoice in gatea[
            0] or nchoice in gateb[0] or nchoice in canteen[
              0] or nchoice in lift1[0] or nchoice in lift2[0]:
        nchoice = random.choice(normal_duties)
      dutyarr[0].append(nchoice)
      normal_duties.remove(nchoice)

    elif c > (n1 - 1) and c < (n2 + n1):
      while nchoice in dutyarr[1]:
        nchoice = random.choice(normal_duties)
      while nchoice in foyerhostel[1] or nchoice in foyerlate[
          1] or nchoice in guardhouse[1] or nchoice in gatea[
            1] or nchoice in gateb[1] or nchoice in canteen[
              1] or nchoice in lift1[1] or nchoice in lift2[0]:
        nchoice = random.choice(normal_duties)
      dutyarr[1].append(nchoice)
      normal_duties.remove(nchoice)

    elif c > (n2 + n1 - 1) and c < (n3 + n2 + n1):
      while nchoice in dutyarr[2]:
        nchoice = random.choice(normal_duties)
      while nchoice in foyerhostel[2] or nchoice in foyerlate[
          2] or nchoice in guardhouse[2] or nchoice in gatea[
            2] or nchoice in gateb[2] or nchoice in canteen[
              2] or nchoice in lift1[2] or nchoice in lift2[2]:
        nchoice = random.choice(normal_duties)
      dutyarr[2].append(nchoice)
      normal_duties.remove(nchoice)

    elif c > (n3 + n2 + n1 - 1) and c < (n4 + n3 + n2 + n1):
      while nchoice in dutyarr[3]:
        nchoice = random.choice(normal_duties)
      while nchoice in foyerhostel[3] or nchoice in foyerlate[
          3] or nchoice in guardhouse[3] or nchoice in gatea[
            3] or nchoice in gateb[3] or nchoice in canteen[
              3] or nchoice in lift1[3] or nchoice in lift2[3]:
        nchoice = random.choice(normal_duties)
      dutyarr[3].append(nchoice)
      normal_duties.remove(nchoice)

    elif c > (n4 + n3 + n2 + n1 - 1) and c < (n5 + n4 + n3 + n2 + n1):
      while nchoice in dutyarr[4]:
        nchoice = random.choice(normal_duties)
      while nchoice in foyerhostel[4] or nchoice in foyerlate[
          4] or nchoice in guardhouse[4] or nchoice in gatea[
            4] or nchoice in gateb[4] or nchoice in canteen[
              4] or nchoice in lift1[4] or nchoice in lift2[4]:
        nchoice = random.choice(normal_duties)
      dutyarr[4].append(nchoice)
      normal_duties.remove(nchoice)


if __name__ == '__main__':
  dutyset(markerduty, marker_duty, 2, 2, 2, 2, 3)
  print(markerduty)
