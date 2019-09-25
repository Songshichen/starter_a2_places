"""
Name:Shichen Song
Date:25/09/2019
Brief Project Description:
GitHub URL:
"""
class SongsToLearnApp(App):
    def __init__(self, **kwargs):
        """
            To install all the required widgets for the layout of kivy app
        """
        super().__init__(**kwargs)
        self.place_list = PlaceCollection()

        # Create the status label in bottom and top
        self.top_label = Label(text="", id="count_label")
        self.status_label = Label(text="")

        # The layout widget in left side
        self.sort_label = Label(text="Sort by:")

        # Adding the sort selection
        self.spinner = Spinner(text='Name', values=('Name', 'Country', 'Priority', 'Visited'))
        self.add_place_label = Label(text="Add New Place...")
        self.name_label = Label(text="Country:")
        self.name_text_input = TextInput(write_tab=False, multiline=False)
        self.country_label = Label(text="Name:")
        self.country_text_input = TextInput(write_tab=False, multiline=False)
        self.priority_label = Label(text="Priority:")
        self.priority_text_input = TextInput(write_tab=False, multiline=False)

        # Create the button for add and clear of bottom widget
        self.add_place_button = Button(text='Add Place')
        self.clear_button = Button(text='Clear')

    def right_widgets(self):
        """
            This function is used to building the right layout with widgets based on the created list
        """
        # Sets the count label
        self.top_label.text = "Places to visit: " + str(self.place_list.count_required_places()) + ". visited: " + str(
            self.place_list.count_visited_places())

        # Using for loop to check the place status in the place list and change or set the color base on the place status
        for place in self.place_list.places:
            # If the status is 'n, the place background color of button will change
            if place[0].status == 'n':
                place_button = Button(
                    text='' + place[0].name + ' ' + "in" + ' ' + place[0].country + ', ' + "priority" + ' ' + str(place[0].priority)
                         , id=place[0].name)
                place_button.background_color = [0, 88, 88, 0.3]
            # If the status is 'y', the place background color of button will change
            else:
                place_button = Button(
                    text='' + place[0].name + ' ' + " in " + ' ' + place[0].country + ', ' + "priority" + ' '+ str(place[0].priority)
                         + ' '+ "(visited)", id=place[0].name)
                place_button.background_color = [88, 89, 0, 0.3]
            place_button.bind(on_release=self.click_button)
            self.root.ids.rightLayout.add_widget(place_button)

    def click_button(self, button):
        """
            This function is used for handling on click for created place button
        """
        # If user click the place that is visited change it to required to visit and update the status bar
        if self.place_list.get_places(button.id).status == 'v':
            self.place_list.get_places(button.id).status = 'n'
            self.root.ids.bottomLayout.text = "You need to visit " + str(self.place_list.get_places(button.id).name)
        # If user click the place that is required change it visited and update the status bar
        else:
            self.place_list.get_places(button.id).status = 'v'
            self.root.ids.bottomLayout.text = "You have visited " + str(self.place_list.get_places(button.id).name)
        self.sort_places()
        self.root.ids.rightLayout.clear_widgets()
        self.right_widgets()

    def sort_places(self,*args):
        """
            This function handle the sorts base on user selection
        """
        self.place_list.sort(self.spinner.text)
        self.root.ids.rightLayout.clear_widgets()
        self.right_widgets()

    def build(self):
        """
            This function is used to open the kivy app and put some object
        """
        self.title = "TravelTracker"
        self.root = Builder.load_file('app.kv')
        self.place_list.load_places()
        self.place_list.sort('Name')
        self.build_widgets()
        self.right_widgets()

    def build_widgets(self):
        """
            This function is to build the left side layout base on created widgets
        """
        self.root.ids.leftLayout.add_widget(self.sort_label)
        self.root.ids.leftLayout.add_widget(self.spinner)
        self.root.ids.leftLayout.add_widget(self.add_place_label)
        self.root.ids.leftLayout.add_widget(self.name_label)
        self.root.ids.leftLayout.add_widget(self.name_text_input)
        self.root.ids.leftLayout.add_widget(self.country_label)
        self.root.ids.leftLayout.add_widget(self.country_text_input)
        self.root.ids.leftLayout.add_widget(self.priority_label)
        self.root.ids.leftLayout.add_widget(self.priority_text_input)
        self.root.ids.leftLayout.add_widget(self.add_place_button)
        self.root.ids.leftLayout.add_widget(self.clear_button)
        self.root.ids.leftLayout.add_widget(self.top_label)
        # Sorting spinner by setting on click, put clear button and add place button
        self.spinner.bind(text=self.sort_places)
        self.add_place_button.bind(on_release=self.add_place_event)
        self.clear_button.bind(on_release=self.clear_input)

    def add_place_event(self, *args):
        """
            This function is used to check the add_place input(error checking)
        """
        # It is to check all the required input is typed by user, if one of the required input is not completed,
                                                                                        # It will print the error
        if str(self.name_text_input.text).strip() == '' or str(self.country_text_input.text).strip() == '' or str(
                self.priority_text_input.text).strip() == '':
            self.root.ids.bottomLayout.text = "All fields must be completed"
        else:
            try:
                # When the priority is smaller than 0,print the error message
                if int(self.priority_text_input.text) < 0:
                    self.root.ids.bottomLayout.text = "Please enter a valid number"
                # If all the input is correct, then create a place object in place_list class
                else:
                    self.place_list.add_place(self.name_text_input.text, self.country_text_input.text, int(self.
                                                                                                priority_text_input.text))
                    self.place_list.sort(self.spinner.text)
                    self.clear_input()
                    self.root.ids.rightLayout.clear_widgets()
                    self.right_widgets()
            # Print the error message when it is string error
            except ValueError:
                self.root.ids.bottomLayout.text = "Please enter a valid number"

    def clear_input(self, *args):
        """
            This function is used to clear all the input and status bar
        """
        self.name_text_input.text = ""
        self.country_text_input.text = ""
        self.priority_text_input.text = ""
        self.root.ids.bottomLayout.text = ""

    def final(self):
        # Save all the change to CSV file
        self.place_list.file_save()


if __name__ == '__main__':
    app = SongsToLearnApp()
    app.run()

