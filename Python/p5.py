class Solution(object):
    def convertTemperature(self, celsius):
        answer=[]
        kelvin=float(celsius+273.15)
        fahrenheit=float((celsius*1.80)+32.00)
        answer.append(kelvin)
        answer.append(fahrenheit)

        return answer
