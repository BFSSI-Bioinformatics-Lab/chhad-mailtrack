from django.db import models
from django.utils import timezone
from django.urls import reverse
from pathlib import Path
from chhad_mailtrack.users.models import User
from simple_history.models import HistoricalRecords

# Create your models here.
STATUS_CHOICES = (
    ('NOT_ASSIGNED', 'Not Assigned'),
    ('IN_PROGRESS', 'In Progress'),
    ('WAITING_FOR_APPROVAL', 'Waiting for Approval'),
    ('COMPLETED', 'Completed')
)

HEAD = (
    ('Section head A', 'Section head A'),
    ('Section head B', 'Section head B'),
    ('Not Applicable / Other', 'Not Applicable / Other')
)

CORRESP_TYPE = (
    ('Allergens', 'Allergens'),
    ('Incidentals', 'Incidentals'),
    ('Contaminant', 'Contaminant'),
    ('Food Additive', 'Food Additive'),
    ('Not Applicable / Other', 'Not Applicable / Other')
)

TRACK = (
    ('Submissions', 'Submissions'),
    ('Projects', 'Projects'),
    ('Public Inquiries', 'Public Inquiries'),
    ('Not Applicable / Other', 'Not Applicable / Other')
)

SECTION = (
    ('Toxicological Evaluation', 'Toxicological Evaluation'),
    ('Bureau of Nutritional Sciences', 'Bureau of Nutritional Sciences'),
    ('Toxicology Section', 'Toxicology Section'),
    ('Not Applicable / Other', 'Not Applicable / Other')
)

OUTGOING = (
    ('YES', 'Yes'),
    ('NO', 'No'),
    ('Not Applicable / Other', 'Not Applicable / Other')
)

ASAP = (
    ('YES', 'Yes'),
    ('NO', 'No'),
    ('Not Applicable / Other', 'Not Applicable / Other')
)

class Query(models.Model):
    name = 'query'

    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='NOT_ASSIGNED')
    number_ref = models.IntegerField(blank=True, null=True)
    correspondence_numb = models.CharField(max_length=500, blank=True, null=True)
    # quarter = models.CharField(max_length=50, choices=QUARTER, default='Not Applicable / Other')

    date_input = models.DateTimeField(default=timezone.now)
    date_due = models.DateField(blank=True, null=True)
    date_initial_email = models.DateField(blank=True, null=True)
    date_chhad_received = models.DateField(blank=True, null=True)
    date_assigned_to_evaluator = models.DateField(blank=True, null=True)
    date_to_sections_head_for_approval = models.DateField(blank=True, null=True)
    date_completed = models.DateField(blank=True, null=True)

    evaluator = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    section_head = models.CharField(max_length=500, choices=HEAD, default='Not Applicable / Other')

    company_name = models.CharField(max_length=500, blank=True, null=True)
    contact = models.CharField(max_length=500, blank=True, null=True)
    corresp_type = models.CharField(max_length=50, choices=CORRESP_TYPE,
                                    default='Not Applicable / Other')
    track = models.CharField(max_length=50, choices=TRACK,
                            default='Not Applicable / Other')
    section = models.CharField(max_length=50, choices=SECTION,
                                default='Not Applicable / Other')
    is_outgoing = models.CharField(max_length=50, choices=OUTGOING,
                               default='Not Applicable / Other')
    asap = models.CharField(max_length=50, choices=ASAP,
                                   default='Not Applicable / Other')

    subject_line = models.TextField(null=True, blank=True)
    remarks = models.TextField(null=True, blank=True)
    query_response = models.TextField(null=True, blank=True)

    key_words = models.CharField(max_length=500, blank=True, null=True)

    peer_review = models.CharField(max_length=500, blank=True, null=True)
    file_numb = models.CharField(max_length=500, blank=True, null=True)
    referred_by = models.CharField(max_length=500, blank=True, null=True)
    additional_information = models.TextField(null=True, blank=True)

    updated = models.DateTimeField(auto_now=True)
    history = HistoricalRecords()

    class Meta:
        app_label = "api"
        verbose_name = 'Query'
        verbose_name_plural = 'Queries'

    def __str__(self):
        return f"{self.id}: {self.subject_line}"

    # How to find the url of any entry
    def get_absolute_url(self):
        return reverse('query_detail', kwargs={'pk': self.pk})

    # def keywords_as_list(self):
    #     return self.key_words.split(',')
    def keywords_as_list(self):
        if self.key_words:
            return self.key_words.split(',')
        return []



class UserActivity(models.Model):
    name = 'userActivity'
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    session_key = models.CharField(max_length=40, db_index=True)
    login = models.DateTimeField(auto_now_add=True)
    logout = models.DateTimeField(null=True, default=None)

    class Meta:
        app_label = "api"
        verbose_name = 'UserActivity'
        verbose_name_plural = 'UserActivity'
