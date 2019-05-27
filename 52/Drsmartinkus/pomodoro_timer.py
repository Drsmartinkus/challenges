from datetime import datetime, timedelta

print("-----Welcome to Pomodoro Timer-----")

duration = input("Please set duration in minutes: ")
if int(duration) <= 0:
	raise ValueError("duration should be greater than 0")
start_time = datetime.today()
end_time = start_time + timedelta(minutes=int(duration))
print("Pomodoro Timer set to: {0}".format(duration))

repeat = True
while repeat:
	if end_time == datetime.today():
		end_time = datetime.today() + timedelta(minutes=int(duration))
		print("Time for a break!")
