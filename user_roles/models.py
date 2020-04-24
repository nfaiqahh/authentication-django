# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.db import models

# Create your models here.

class Permohonan(models.Model):
    id = models.AutoField(primary_key=True)
    contractor = models.CharField(max_length=50)
    
    contractor_name = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=11)
    company_name = models.CharField(max_length=100)
    company_address = models.CharField(max_length=500)
    STATUS_PERMOHONAN = (
        ('P', 'Dalam Permohonan'),
        ('T', 'Ditolak'),
        ('L', 'Diluluskan'),
    )
    request_status = models.CharField(max_length=1, choices=STATUS_PERMOHONAN, default='P')
    class Meta:
        permissions = (
            ('can_approve', "Can approve Permohonan"),
            ('can_reject', "Can reject Permohonan"),
            ('can_submit', "Can submit Permohonan"),
        )