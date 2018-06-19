import pygal

piechart= pygal.Pie()
piechart.add('Computer Engineering',48)
piechart.add('Civil Engineering',192)
piechart.add('Electronics Engineering',48)
piechart.add('Electrical Engineering', 48)
piechart.add('Arcitecture Engineering',48)
piechart.add('Mechanical Engineering',48)
piechart.render()

bar = pygal.Bar()
bar.add('Aman',48)
bar.add('Amang G',52)
bar.render()

pie = pygal.Pie()
file = open('input.txt','r')
for line in file.read().splitlines():
  if line:
    name,value = line.split('-')
    pie.add(name, int(value))
pie.render()