'''

If a runner runs 10 miles in 30 minutes and 30 seconds,
What is his/her average speed in kilometers per hour? (Tip: 1 mile = 1.6 km)

'''

seconds = 30 / 3600
minutes = 30 / 60
time = seconds + minutes
avg = 10 / time
avg = avg * 1.6
print(avg)
