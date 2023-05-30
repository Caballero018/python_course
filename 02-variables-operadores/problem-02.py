#!/usr/bin/python3
"""
Program that transforms a number of seconds into hours, minutes and seconds.
"""


seconds = int(input("Enter the number of seconds: "))
minutes = seconds // 60
hours = minutes // 60
print(f"Hours: {hours}\nMinutes: {minutes}\nSeconds: {seconds}")
