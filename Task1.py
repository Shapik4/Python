a = input("Какую страну производителей машин вы предпочитаете? ")
b = input(f"Какого производителя из страны {a} вы предпочитаете?")
c = int(input(f"Какой ценовой диапозон среди машин марки {b} вас устраивает?"))
if c<10000:
    print("Вам подойдут машини 90-х")
elif c>10000 and c<40000:
    print("Вам подойдут машини 2000-х")
elif c>40000:
    print("Вам подойдут машини нового поколения")
    
    
