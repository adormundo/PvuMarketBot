import time
from plant_market import PlantMarket

def main():
    print("""
     ______     ___   _ __  __    _    ____  _  _______ _____ 
    |  _ \ \   / / | | |  \/  |  / \  |  _ \| |/ / ____|_   _|
    | |_) \ \ / /| | | | |\/| | / _ \ | |_) | ' /|  _|   | |  
    |  __/ \ V / | |_| | |  | |/ ___ \|  _ <| . \| |___  | |  
    |_|     \_/   \___/|_|  |_/_/   \_\_| \_\_|\_\_____| |_|  
                                by: ( ͡❛ᴗ ͡❛) Walffoaruzineo\n""")
    time.sleep(2)

    market = PlantMarket()
    market.search_plants()
    while True:
        plant_index = int(input("Insert plant index: "))
        market.buy_plant(plant_index)

if __name__ == "__main__":
    main()
