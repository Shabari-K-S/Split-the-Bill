"""
    FLET based mobile app for a Simple Split the Bill

    This app allows users to input the total bill amount and the number of people to split the bill with.
"""


from flet import *
from typing import Dict

# Colors used 
colors: Dict[str, str] = {
    "border": "#D9D9D9",
    "text": "#000000"
}

# Main Method 
def main(page: Page):
    # Page setup
    page.title = "Split the Bill"
    page.padding = padding.all(10)
    page.theme_mode = ThemeMode.LIGHT
    page.fonts = {
        "Roboto": "https://github.com/johnkil/Android-RobotoTextView/raw/refs/heads/master/robototextview/src/main/assets/fonts/Roboto-Regular.ttf"
    }
    page.appbar = AppBar(
        title=Text("Split the Bill", size=40, weight=FontWeight.BOLD, font_family="Roboto")
    )

    # Reference Variable 
    amount_ref = Ref[TextField]()
    tip_ref = Ref[Dropdown]()
    person_ref = Ref[TextField]()
    total_per_person_ref = Ref[Column]()

    def change(e):
        """
          This method get the user input and split the bill
        """
        try:
            value = amount_ref.current.value
            tip_val_ref = {"0%":0,"5%": 0.05,"10%": 0.10,"15%": 0.15,"20%": 0.20}
            tip_val = tip_val_ref[tip_ref.current.value]
            value_with_tip = int(value) + (int(value) * tip_val)
            result = float(value_with_tip) / int(person_ref.current.value)        
            print(value, value_with_tip, result)
            total_per_person_ref.current.controls = [
                Text("Total Per Person", size=22,font_family="Roboto"),
                Text(f"$ {result:.2f}", size=42,font_family="Roboto")
            ]
            page.update()
        except Exception as e:
            print("Not all the value is passed")

    # Here user will input the total amount
    _amount = Container(
        content=Column(
            controls=[
                Text("Enter the amount", size=16,font_family="Roboto"),
                TextField(ref=amount_ref, keyboard_type=KeyboardType.NUMBER, prefix_text="$ ", on_change=change, border_color=colors["border"])
            ]
        ),
        padding=10
        
    )

    # Here user will input tip
    _tip = Container(
        content=Column(
            controls=[
                Text("Select the tip amount (%)", size=16,font_family="Roboto"),
                Dropdown(
                    ref=tip_ref,
                    width=int(page.width * 0.95),
                    value="0%",
                    options=[
                        dropdown.Option("0%"),
                        dropdown.Option("5%"),
                        dropdown.Option("10%"),
                        dropdown.Option("15%"),
                        dropdown.Option("20%"),
                    ],
                    border_color=colors["border"],
                    on_change=change
                )
            ]
        ),
        padding=10
    )

    # Here I will get total number of people from user
    _number_of_people = Container(
        content=Column(
            controls=[
                Text("Number of people", size=16,font_family="Roboto"),
                TextField(ref=person_ref, keyboard_type=KeyboardType.NUMBER, suffix_text=" people", on_change=change, border_color=colors["border"])
            ]
        ),
        padding=10
        
    )

    # Here I will display the total amount cost for each person
    _total_per_person = Container(
        content=Column(
            controls=[
                Text("Total per person", size=22, font_family="Roboto"),
                Text(f"$ 0", size=42, font_family="Roboto")
            ],
            ref=total_per_person_ref
        ),
        padding=10,
        border=Border(
            top=BorderSide(1, colors["border"]),
            left=BorderSide(1, colors["border"]),
            bottom=BorderSide(1, colors["border"]),
            right=BorderSide(1, colors["border"])
        ),
        margin=10,
        width=page.width,
        border_radius=BorderRadius(
            top_left=8,
            bottom_left=8,
            top_right=8,
            bottom_right=8
        )
    )

    # This is the main container
    _main_container = SafeArea(
        content=Column(
            controls=[
                _amount,
                _tip,
                _number_of_people,
                _total_per_person
            ]
        )
    )

    # Adding main container to the page
    page.add(
        _main_container
    )

# Driver Code
if __name__ == "__main__":
    app(target=main)
