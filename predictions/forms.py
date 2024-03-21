from django import forms

class MusicGenreForm(forms.Form):
    age = forms.IntegerField(label='Age', widget=forms.NumberInput(attrs={
        'class': 'block w-full px-4 py-2 mt-2 text-gray-700 bg-white border border-gray-200 rounded-md dark:bg-gray-800 dark:text-gray-300 dark:border-gray-600 focus:border-blue-400 focus:ring-blue-300 focus:ring-opacity-40 dark:focus:border-blue-300 focus:outline-none focus:ring required',
        'placeholder': 'Your Age...',
        }))
    gender = forms.ChoiceField(label='Gender', choices=[(1, 'Male'), (0, 'Female')], 
                               widget=forms.Select(attrs={
                                   'class': 'block w-full px-4 py-2 mt-2 text-gray-700 bg-white border border-gray-200 rounded-md dark:bg-gray-800 dark:text-gray-300 dark:border-gray-600 focus:border-blue-400 focus:ring-blue-300 focus:ring-opacity-40 dark:focus:border-blue-300 focus:outline-none focus:ring',
                                   
                                   }))
