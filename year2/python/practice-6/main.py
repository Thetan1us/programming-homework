leads = ["Ivan@GMail.com", "ivan@gmail.com ", " vasya@mail.com", " maryna@urk.net"]
buyers = ["ivan@gmail.com ", "Vasya@mail.com", "max@ukr.net  "]

clean_leads = [email.strip().lower() for email in leads]
clean_buyers = [email.strip().lower() for email in buyers]

leads_set = set(clean_leads)
buyers_set = set(clean_buyers)

all_users = leads_set | buyers_set
loyal_clients = leads_set & buyers_set
potential_clients = leads_set - buyers_set

total_viewers = len(leads_set)
buyers_from_webinar = len(loyal_clients)

conversion_rate = (buyers_from_webinar / total_viewers) * 100 if total_viewers > 0 else 0.0

print(f"Загальна кількість унікальних користувачів: {len(all_users)}")
print("\nЛояльні клієнти (вебінар + покупка): ")
for mail in loyal_clients:
    print(mail)
print("\nПотенційні клієнти (вебінар без покупки): ")
for mail in potential_clients:
    print(mail)
print(f"\nКонверсія вебінару: {conversion_rate:.2f}%")