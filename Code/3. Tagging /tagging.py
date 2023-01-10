from collections import defaultdict
import operator
import heapq


#CREATE WEGIHTS FOR CATEGORIES USING HEAP 
#CREATE PROCESS FOR COMING UP WITH TAGGS

joinedTrans = ['68089712,bedok s a3/72cash withdrawal', 'paynow transfer to: penn ong othrpaynow transferfast / paynow transfer', '68089712,bd b intc fccash withdrawal', '136-49334-5 : |-bankfunds transfer', '136-49334-5 : |-bankfunds transfer', 'ccc -4119 : i-bankbill payment', 'interest earned', 'incoming paynow ref 0629790 from: lim zhenghao daniel othr transfer - mobilefast / paynow transfer', '136-49334-5 : |-bankfunds transfer', 'ccc -4119 : i-bankbill payment', 'fast / paynow transfer', '68089712,bedok s a3/72cash withdrawal', 'amex-3773 : i-bankbill payment', '68089712,bedok s a3/72cash withdrawal', 'paynow transfer to: mustafa abbas othrpaynow transferfast / paynow transfer2 a ow 2 ©68089712,bedok s a3/72cash withdrawal', 'paynow transfer to: mustafa abbas othrpaynow transferfast / paynow transfer', 'paynow transfer to: nutty nut othrpaynow transferfast / paynow transfer', '68089712,bd b intc fccash withdrawal', '68089712,bedok s a3/72cash withdrawal', 'paynow transfer to: lam may fong othrpaynow transferfast / paynow transfer', 'cpf se ses9416911ipayments or collections via giro', 'paynow transfer to: marcus wong othrchicken rice was coldfast / paynow transfer']

weights = defaultdict(dict)

categories_dict = {
    "withdrawal":"Withdrawal",
    "penn": "Misc",
    "136-49334-5": "Re-balancing",
    "bankbill": "Credit Card Payment",
    "interest": "Interest Earned",
    "lim zhenghao daniel": "Misc",
    "incoming": "Credit",
    "earned": "Credit",
    "paynow transfer": "Misc",
    "amex": "Credit Card Payment",
    "transfer to": "Debit",
    "mustafa": "Misc",
    "lam may fong": "Food",
    "cpf": "Tax"
    }

#print("len of trans", len(joinedTrans))
tagging1 = []
tagging2 = []

for i in range(0, len(joinedTrans)):
    tagging2.append("-")

for index, element in enumerate(joinedTrans):
    for key, value in categories_dict.items():
        if key in element:
            tagging1.append(value)
            if key in weights.keys():
                weights[key][value] += 1
            else:
                weights[key][value] = 1
            break

    for key, value in categories_dict.items():
        if key in element and categories_dict[key] != tagging1[index]:
            tagging2[index] = value + " " + str(index)
            break


#print(len(tagging1))
#print(len(tagging2))
#print("tagging 1 ----- ", tagging1)
#print("tagging 2 ----- ", tagging2)
#print("")

'''
ranking = []
for key in weights.keys():
    for key2 in weights[key].keys():
        #print(weights[key][key2])
        ranking.append(weights[key][key2])
        ranking.sort(reverse = True)
#print(ranking)

ranked_categories_dict = {}

for i in ranking:
    for key in weights.keys():
        for key2 in weights[key].keys():
            if i == weights[key][key2]:
                #print(key, key2, weights[key][key2])
                ranking.pop(0)
                ranked_categories_dict[key] = key2
                break

#print(ranked_categories_dict)

for key, value in categories_dict.items():
    if key not in ranked_categories_dict.keys():
        ranked_categories_dict[key] = value

#print("Normal --- ", categories_dict)
#print("Ranked --- ", ranked_categories_dict)


tagging3 = []
tagging4 = []

for i in range(0, len(joinedTrans)):
    tagging4.append("-")


for index, element in enumerate(joinedTrans):
    for key, value in ranked_categories_dict.items():
        if key in element:
            tagging3.append(value)
            break

    for key, value in ranked_categories_dict.items():
        if key in element and ranked_categories_dict[key] != tagging3[index]:
            tagging4[index] = value 
            break

#print(len(tagging3))
#print(len(tagging4))
#print("tagging 3 ----- ",tagging3)
#print("tagging 4 ----- ",tagging4)
#print("")
'''
print("BEFORE CATEGORISATION")
for i in joinedTrans:
    print(i)

print("")

print("AFTER CATEGORISATION")
for i, item in enumerate(joinedTrans):
    print(f"{tagging1[i]} ----- {item}")