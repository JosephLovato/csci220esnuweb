from django import forms

esnu_choices = (
    ('E', 'E'),
    ('S', 'S'),
    ('N', 'N'),
    ('U', 'U')
)

sn_choices = (
    ('S', 'S'),
    ('N', 'N'),
)


class GradeCalcForm(forms.Form):
    project_1_programming = forms.ChoiceField(choices=sn_choices)
    project_2_programming = forms.ChoiceField(choices=sn_choices)
    project_3_programming = forms.ChoiceField(choices=sn_choices)
    project_4_programming = forms.ChoiceField(choices=sn_choices)
    project_5_programming = forms.ChoiceField(choices=sn_choices)

    project_1_analysis = forms.ChoiceField(choices=esnu_choices)
    project_2_analysis = forms.ChoiceField(choices=esnu_choices)
    project_3_analysis = forms.ChoiceField(choices=esnu_choices)
    project_4_analysis = forms.ChoiceField(choices=esnu_choices)
    project_5_analysis = forms.ChoiceField(choices=esnu_choices)

    midterm = forms.ChoiceField(choices=esnu_choices)
    final = forms.ChoiceField(choices=esnu_choices)

    def programming_group(self):
        return [self[name] for name in filter(lambda x: "programming" in x, self.fields.values())]

    def analysis_group(self):
        return [self[name] for name in filter(lambda x: "analysis" in x, self.fields.values())]

    def comprehension_group(self):
        return [self.midterm, self.final]
