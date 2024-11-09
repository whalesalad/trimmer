from collections import defaultdict
from shared import Window, Door, Slider

MARGIN_FT = 2

entry_door = Door("Entry Door", w=30.25, h=81.5)
closet_door = Door("Closet Door", w=34.75, h=80.5)
bathrom_door = Door("Bathroom Door", w=28.5, h=81.75)
window = Window("Window", w=6925, h=33.375)
slider = Slider("Slider", w=72.5, h=80.5)

room = {
    "entry_door": entry_door,
    "closet_door": closet_door,
    "bathroom_door": bathrom_door,
    "window": window,
    "slider": slider
}

# questions
# what is the total number of each component we will need?

def main():
    all_components = defaultdict(list)

    for opening in room.values():
        for component, count in opening.components_v.items():
            all_components[component].append(count * opening.height)
        for component, count in opening.components_h.items():
            all_components[component].append(count * opening.width)

    print("\nTotal length of each component needed:")
    for component, counts in all_components.items():
        total_inches = sum(counts)
        total_feet = round(total_inches / 12) + MARGIN_FT
        print(f"{component}: {total_feet} feet")

if __name__ == '__main__':
    main()