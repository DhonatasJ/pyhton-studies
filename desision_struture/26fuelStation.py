fuel = input("Insert A-alcohol, G-gasoline: ");
lt = float(input("How mush liters: "));
alcoholPrice = 1.9;
gasolinePrice = 2.5;
desc20Less = 0;
desc20Grand = 0;
desc20LessG = 0;
desc20GrandG = 0;
if lt > 0 and lt <= 20:
    desc20Less = alcoholPrice - ((alcoholPrice / 100) * 3);
else:
    desc20Grand = alcoholPrice - ((alcoholPrice / 100) * 5);

if lt > 0 and lt <= 20:
    desc20LessG = alcoholPrice - ((gasolinePrice / 100) * 4);
else:
    desc20GrandG = alcoholPrice - ((gasolinePrice / 100) * 6);


def alcohol(desc20Less, desc20Grand, lt):
    if desc20Less != 0:
        liquidA = lt * desc20Less
        return liquidA;
    elif desc20Grand != 0:
        liquidA1 = lt * desc20Grand
        return liquidA1;

def gasoline(desc20LessG, desc20GrandG, lt):
    if desc20LessG != 0:
        liquidA = lt * desc20LessG
        return liquidA;
    elif desc20GrandG != 0:
        liquidA1 = lt * desc20GrandG
        return liquidA1;


if fuel == "A":
     print(f"You must pay R${round(alcohol(desc20Less, desc20Grand, lt),2)}");
elif fuel == "G":
    print(f"You must pay R${round(gasoline(desc20LessG, desc20GrandG, lt),2)}");
else:
    print("ERROR: Only select \"A\" to alcohol or \"G\" to gasoline, please try again...");
