from ast import comprehension
from django.views.generic import TemplateView
from django.template import loader
from django.shortcuts import render
# from gradecalculator.esnucalc.esnu_grade_calculations import compute_programming_score
from gradecalculator.forms import GradeCalcForm
from gradecalculator.esnucalc.esnu_grade_calculations import *


class MainView(TemplateView):
    template_name = 'index.html'

    def get(self, request):
        form = GradeCalcForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = GradeCalcForm(request.POST)
        programming_scores_raw = []
        analysis_scores_raw = []
        if form.is_valid():
            cleaned = form.cleaned_data
            programming_scores_raw.append(cleaned['project_1_programming'])
            programming_scores_raw.append(cleaned['project_2_programming'])
            programming_scores_raw.append(cleaned['project_3_programming'])
            programming_scores_raw.append(cleaned['project_4_programming'])
            programming_scores_raw.append(cleaned['project_5_programming'])
            analysis_scores_raw.append(cleaned['project_1_analysis'])
            analysis_scores_raw.append(cleaned['project_2_analysis'])
            analysis_scores_raw.append(cleaned['project_3_analysis'])
            analysis_scores_raw.append(cleaned['project_4_analysis'])
            analysis_scores_raw.append(cleaned['project_5_analysis'])
            midterm = convert_to_score(cleaned['midterm'])
            final = convert_to_score(cleaned['final'])

        programming_scores = []
        analysis_scores = []
        for r in programming_scores_raw:
            programming_scores.append(convert_to_score(r))
        for r in analysis_scores_raw:
            analysis_scores.append(convert_to_score(r))

        programming_score = compute_programming_score(programming_scores)
        analysis_score = compute_analysis_score(analysis_scores)
        comprehension_score = compute_comprehension_score(final, midterm)
        final_grade = compute_final_score(
            [programming_score, analysis_score, comprehension_score])

        args = {'form': form,
                'programming_score': score_to_string(programming_score),
                'analysis_score': score_to_string(analysis_score),
                'comprehension_score': score_to_string(comprehension_score),
                'final_grade': final_grade
                }
        return render(request, self.template_name, args)
