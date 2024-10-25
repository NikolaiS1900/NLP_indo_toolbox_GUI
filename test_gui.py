def perform_regex_search(self, event=None):
    """Handle regex search when the button is pressed."""
    # Get the user input and selected search type
    user_input_value = self.user_input.get().strip()  # Get and strip whitespace from user input
    search_type_value = self.selected_search_type  # This value is set in on_search_type_selected

    # Validate input
    if not user_input_value:
        messagebox.showwarning("Input Error", "Please enter a search term.")
        return

    if not search_type_value:
        messagebox.showwarning("Selection Error", "Please select a search type.")
        return

    # Store the selected search type and user input
    self.selected_search_type = search_type_value
    self.user_input_value = user_input_value  # Store the user input

    # Optionally, you can display the selected values or process them further
    messagebox.showinfo("Search Criteria", f"User Input: {self.user_input_value}\nSearch Type: {self.selected_search_type}")

    # Call methods to execute the search or further processing here
    # For example, you might call a method to perform the regex search based on the input and type
    # self.execute_regex_search(user_input_value, search_type_value)
