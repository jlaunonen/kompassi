# encoding: utf-8

from datetime import date, datetime

from django import forms
from django.db.models import Q
from django.utils.timezone import now

from crispy_forms.layout import Layout, Fieldset

from core.forms import PersonForm
from core.models import Person
from core.utils import horizontal_form_helper, indented_without_label

from .models import AlternativeFormMixin, Signup, JobCategory, EmptySignupExtra, PersonnelClass, WorkPeriod



# http://stackoverflow.com/a/9754466
def calculate_age(born, today):
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))


class AdminPersonForm(PersonForm):
    age_now = forms.IntegerField(required=False, label=u'Ikä nyt')
    age_event_start = forms.IntegerField(required=False, label=u'Ikä tapahtuman alkaessa')

    def __init__(self, *args, **kwargs):
        event = kwargs.pop('event')
        super(AdminPersonForm, self).__init__(*args, **kwargs)

        self.fields['age_now'].widget.attrs['readonly'] = True
        self.fields['age_event_start'].widget.attrs['readonly'] = True
        if self.instance.birth_date is not None:
            self.fields['age_now'].initial = calculate_age(self.instance.birth_date, date.today())
            if event.start_time is not None:
                self.fields['age_event_start'].initial = calculate_age(self.instance.birth_date, event.start_time.date())

        # XXX copypasta
        self.helper.layout = Layout(
            'first_name',
            'surname',
            'nick',
            'preferred_name_display_style',
            'birth_date',
            'age_now', # not in PersonForm
            'age_event_start', # not in PersonForm
            'phone',
            'email',
            'may_send_info',
        )

    class Meta:
        model = Person
        fields = (
            'first_name',
            'surname',
            'nick',
            'preferred_name_display_style',
            'birth_date',
            'age_now', # not in PersonForm
            'age_event_start', # not in PersonForm
            'phone',
            'email',
            'may_send_info',
        )


class SignupFormMixin(object):
    def get_job_categories_query(self, event, admin=False):
        q = Q(event=event, personnel_classes__app_label='labour')

        if not admin:
            # For non-admin usage, restrict to public JCs only.
            q = q & Q(public=True)

            if self.instance.pk is not None:
                # Also include those the user is signed up to whether or not they are public.
                q = q | Q(signup_set=self.instance)

        return q

    def get_job_categories(self, event, admin=False):
        from .models import JobCategory
        job_categories_query = self.get_job_categories_query(event, admin)
        return JobCategory.objects.filter(job_categories_query).distinct().order_by('id')


class SignupForm(forms.ModelForm, SignupFormMixin):
    def __init__(self, *args, **kwargs):
        event = kwargs.pop('event')
        admin = kwargs.pop('admin')

        super(SignupForm, self).__init__(*args, **kwargs)

        self.fields['job_categories'].queryset = self.get_job_categories(event, admin)
        self.helper = horizontal_form_helper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Fieldset(u'Tehtävät',
                'job_categories'
            ),
        )

    def clean_job_categories(self):
        job_categories = self.cleaned_data['job_categories']

        if not all(jc.is_person_qualified(self.instance.person) for jc in job_categories):
            raise forms.ValidationError(u'Sinulla ei ole vaadittuja pätevyyksiä valitsemiisi tehtäviin.')

        return job_categories

    class Meta:
        model = Signup
        fields = ('job_categories',)

        widgets = dict(
            job_categories=forms.CheckboxSelectMultiple,
        )


class EmptySignupExtraForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SignupExtraForm, self).__init__(*args, **kwargs)
        self.helper = horizontal_form_helper()
        self.helper.form_tag = False

    class Meta:
        model = EmptySignupExtra
        exclude = ('signup',)


class SignupAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        event = kwargs.pop('event')

        super(SignupAdminForm, self).__init__(*args, **kwargs)

        self.fields['job_categories_accepted'].queryset = JobCategory.objects.filter(event=event)
        self.fields['personnel_classes'].queryset = PersonnelClass.objects.filter(event=event).order_by('priority')

        self.helper = horizontal_form_helper()
        self.helper.form_tag = False

    class Meta:
        model = Signup
        fields = (
            'job_title',
            'personnel_classes',
            'job_categories_accepted',
            'xxx_interim_shifts',
            'notes',
        )
        widgets = dict(
            personnel_classes=forms.CheckboxSelectMultiple,
            job_categories_accepted=forms.CheckboxSelectMultiple,
        )

    def clean_job_categories_accepted(self):
        job_categories_accepted = self.cleaned_data['job_categories_accepted']

        if self.instance.is_accepted and not job_categories_accepted and self.instance.job_categories.count() != 1:
            raise forms.ValidationError(u'Kun ilmoittautuminen on hyväksytty, tulee valita vähintään yksi tehtäväalue. Henkilön hakema tehtävä ei ole yksikäsitteinen, joten tehtäväaluetta ei voitu valita automaattisesti.')
        elif (self.instance.is_rejected or self.instance.is_cancelled) and job_categories_accepted:
            raise forms.ValidationError(u'Kun ilmoittautuminen on hylätty, mikään tehtäväalue ei saa olla valittuna.')

        return job_categories_accepted

    def clean_personnel_classes(self):
        personnel_classes = self.cleaned_data['personnel_classes']

        if self.instance.is_accepted and not personnel_classes:
            raise forms.ValidationError(u'Kun ilmoittautuminen on hyväksytty, tulee valita vähintään yksi Henkilöstöluokka.')
        elif (self.instance.is_rejected or self.instance.is_cancelled) and personnel_classes:
            raise forms.ValidationError(u'Kun ilmoittautuminen on hylätty, mikään Henkilöstöluokka ei saa olla valittuna.')

        return personnel_classes
