Mini Challenge #1
grades = [10, 50, 60, 10, 50, 60, 30, 50]
for grade in grades:
    if grade > 60:
        print(grade)
for grade in grades:
    if grade > 40:
        print(grade)
for grade in grades:
    if grade> 60:
        print(grade, "PASSED")
    else:
        print(grade, "FAILED")
for grade in grades:
    if grade > 40:
        print(grade, "PASSED")
    else:
        print(grade, "FAILED")
for grade in grades:
    print(grade * 1.10)

Mini Challenge #2
websites = ["google.com", "youtube.com", "facebook.com", "twitter.com", "instagram.com", "baidu.com", "wikipedia.org","yandex.ru", "yahoo.com"]
for site in websites:
    if site.endswith(".com"):
        print(site)
for site in websites:
    print(site.replace(".com", ".net"))
for site in websites:
    name = site.split(".")[0]   # Alles vor dem Punkt
    print(name.capitalize())

Mini Challenge #3
rest_rating = {
	"McDonald's": 6,
	"Foo": 10,
	"Ramen": 8,
	"Starbucks": 5
}
for name, rating in rest_rating.items():
    print(f"{name} was rated {rating}")
for name, rating in rest_rating.items():
    if rating > 7:
        print(name)
del rest_rating["Starbucks"]
