from covid import Covid
import matplotlib.pyplot as plt

#type country's first name as capital
country = input("Enter your country name:\n")

covidValue = Covid()
data = covidValue.get_status_by_country_name(country)
cadr = {
    key: data[key]
    for key in data.keys() & {"confirmed", "active", "deaths", "recovered"}
}

n = list(cadr.keys())
v = list(cadr.values())
print(cadr)

plt.title(country)
plt.bar(range(len(cadr)), v, tick_label=n)
plt.show()
