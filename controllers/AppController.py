class AppController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def update_label(label, stringvar):
        """
        Met à jour le texte d'un label en utilisant une StringVar.
        """
        text = stringvar.get()
        label.config(text=text)
        stringvar.set('merci')


    def change_number(self, input_number):
        print(input_number.get())
