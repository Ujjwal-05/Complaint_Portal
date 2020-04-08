from django import forms
PROBLEM_TYPE =(
    ("Ragging", "Ragging"),
    ("Administration", "Administration"),
    ("Faculty","Faculty"),
    ("Hostel","Hostel")
)

class ComplaintForm(forms.Form):
    problem_type = forms.ChoiceField(choices=PROBLEM_TYPE)
    title = forms.CharField(max_length=200)
    problem = forms.Textarea()