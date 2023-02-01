from argparse import Action
import email
from django import forms

visit_type=(
    ('screening','SCREENING'),
    ('basline','BASELINE'),
    ('visit1','VISIT1'),
    ('visit2','VISIT2'),
    ('visit3','VISIT3'),
    ('visit4','VISIT4'),
    ('visit5','VISIT5'),
    ('completionvisit','COMPLETIONVISIT'),
)
 

class physical_examination_details:
    study_name = forms.CharField(label='StudyName', widget=forms.TextInput({"placeholder": "Study Name"}))
    site_no = forms.CharField(label='SiteNo', widget=forms.TextInput({"placeholder": "Site No"}))
    patient_id = forms.CharField(label='patientid', widget=forms.TextInput({"patient id": "PatientID"}))
    visit_date = forms.CharField(label='VisitDate', widget=forms.DateField())
    visit_type = forms.ChoiceField(label='VisitType', choices=visit_type)

    class vital_signs:
        hr = forms.CharField(label='hr', widget=forms.TextInput({"placeholder": "HR"}))
        br = forms.CharField(label='hr', widget=forms.TextInput({"placeholder": "BR"}))
        temperature = forms.CharField(label='temperature', widget=forms.TextInput({"placeholder": "Temperature"}))
    class growth:
        weight = forms.IntegerField(label='weight', widget=forms.TextInput({"placeholder": "weight"}))
        height = forms.IntegerField(label='height', widget=forms.TextInput({"placeholder": "height"}))
    
    class gen_appearance:
        normal_or_Abnormal=(
            ('normal','NORMAL'),
            ('abnormal','ABNORMAL'),
            ('notexamined', 'NOTEXAMINED')
        )
        change_from_Baseline=(
            ('yes','YES'),
            ('no','NO'),
            ('n/a', 'N/A')
        )
        normal_or_abnormal = forms.ChoiceField(label='Normal_or_Abnormal', choices=normal_or_Abnormal)
        if_abnormal = forms.CharField(label='ifAbnormal', widget=forms.Textarea({"placeholder": "If Abnormal, Describe"}))
        change_from_baseline = forms.ChoiceField(label='change from baseline', choices=change_from_Baseline)
        
        fatigued =(
            ('yes','YES'),
            ('no','NO'),
            ('n/a', 'N/A')
        )
        fever =(
            ('yes','YES'),
            ('no','NO'),
            ('n/a', 'N/A')
        )

    class heent:
        normal_or_Abnormal=(
            ('normal','NORMAL'),
            ('abnormal','ABNORMAL'),
            ('notexamined', 'NOTEXAMINED')
        )
        change_from_Baseline=(
            ('yes','YES'),
            ('no','NO'),
            ('n/a', 'N/A')
        )
        headache =(
            ('yes','YES'),
            ('no','NO'),
            ('n/a', 'N/A')
        )
        rash_or_spots =(
            ('yes','YES'),
            ('no','NO'),
            ('n/a', 'N/A')
        )
        normal_or_abnormal = forms.ChoiceField(label='Normal_or_Abnormal', choices=normal_or_Abnormal)
        if_abnormal = forms.CharField(label='ifAbnormal', widget=forms.Textarea({"placeholder": "If Abnormal, Describe"}))
        change_from_baseline = forms.ChoiceField(label='change from baseline', choices=change_from_Baseline)
    
    class skin:
        rash_or_spots =(
            ('yes','YES'),
            ('no','NO'),
            ('n/a', 'N/A')
        )
        acne =(
            ('yes','YES'),
            ('no','NO'),
            ('n/a', 'N/A')
        )
        tattos =(
            ('yes','YES'),
            ('no','NO'),
            ('n/a', 'N/A')
        )
    
    class neck:
        normal_or_Abnormal=(
            ('normal','NORMAL'),
            ('abnormal','ABNORMAL'),
            ('notexamined', 'NOTEXAMINED')
        )
        change_from_Baseline=(
            ('yes','YES'),
            ('no','NO'),
            ('n/a', 'N/A')
        )
        normal_or_abnormal = forms.ChoiceField(label='Normal_or_Abnormal', choices=normal_or_Abnormal)
        if_abnormal = forms.CharField(label='ifAbnormal', widget=forms.Textarea({"placeholder": "If Abnormal, Describe"}))
        change_from_baseline = forms.ChoiceField(label='change from baseline', choices=change_from_Baseline)
    
    class chest_and_lungs:
        normal_or_Abnormal=(
            ('normal','NORMAL'),
            ('abnormal','ABNORMAL'),
            ('notexamined', 'NOTEXAMINED')
        )
        change_from_Baseline=(
            ('yes','YES'),
            ('no','NO'),
            ('n/a', 'N/A')
        )
        normal_or_abnormal = forms.ChoiceField(label='Normal_or_Abnormal', choices=normal_or_Abnormal)
        if_abnormal = forms.CharField(label='ifAbnormal', widget=forms.Textarea({"placeholder": "If Abnormal, Describe"}))
        change_from_baseline = forms.ChoiceField(label='change from baseline', choices=change_from_Baseline)
    
    class cardiovascular:
        normal_or_Abnormal=(
            ('normal','NORMAL'),
            ('abnormal','ABNORMAL'),
            ('notexamined', 'NOTEXAMINED')
        )
        change_from_Baseline=(
            ('yes','YES'),
            ('no','NO'),
            ('n/a', 'N/A')
        )
        normal_or_abnormal = forms.ChoiceField(label='Normal_or_Abnormal', choices=normal_or_Abnormal)
        if_abnormal = forms.CharField(label='ifAbnormal', widget=forms.Textarea({"placeholder": "If Abnormal, Describe"}))
        change_from_baseline = forms.ChoiceField(label='change from baseline', choices=change_from_Baseline)
    
    class abdomen:
        normal_or_Abnormal=(
            ('normal','NORMAL'),
            ('abnormal','ABNORMAL'),
            ('notexamined', 'NOTEXAMINED')
        )
        change_from_Baseline=(
            ('yes','YES'),
            ('no','NO'),
            ('n/a', 'N/A')
        )
        normal_or_abnormal = forms.ChoiceField(label='Normal_or_Abnormal', choices=normal_or_Abnormal)
        if_abnormal = forms.CharField(label='ifAbnormal', widget=forms.Textarea({"placeholder": "If Abnormal, Describe"}))
        change_from_baseline = forms.ChoiceField(label='change from baseline', choices=change_from_Baseline)
    
    class genitourinary:
        normal_or_Abnormal=(
            ('normal','NORMAL'),
            ('abnormal','ABNORMAL'),
            ('notexamined', 'NOTEXAMINED')
        )
        change_from_Baseline=(
            ('yes','YES'),
            ('no','NO'),
            ('n/a', 'N/A')
        )
        normal_or_abnormal = forms.ChoiceField(label='Normal_or_Abnormal', choices=normal_or_Abnormal)
        if_abnormal = forms.CharField(label='ifAbnormal', widget=forms.Textarea({"placeholder": "If Abnormal, Describe"}))
        change_from_baseline = forms.ChoiceField(label='change from baseline', choices=change_from_Baseline)
    
    class restal:
        normal_or_Abnormal=(
            ('normal','NORMAL'),
            ('abnormal','ABNORMAL'),
            ('notexamined', 'NOTEXAMINED')
        )
        change_from_Baseline=(
            ('yes','YES'),
            ('no','NO'),
            ('n/a', 'N/A')
        )
        normal_or_abnormal = forms.ChoiceField(label='Normal_or_Abnormal', choices=normal_or_Abnormal)
        if_abnormal = forms.CharField(label='ifAbnormal', widget=forms.Textarea({"placeholder": "If Abnormal, Describe"}))
        change_from_baseline = forms.ChoiceField(label='change from baseline', choices=change_from_Baseline)
