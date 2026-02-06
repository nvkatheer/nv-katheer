from django.db import models
from django.utils import timezone

class DailyRecordkatheer(models.Model):
    date = models.DateField(default=timezone.now)
    
    # Feed Data - Male Birds
    feed_male_morning = models.FloatField(null=True, blank=True)
    feed_male_morning_bundles = models.FloatField(null=True, blank=True)
    feed_male_evening = models.FloatField(null=True, blank=True)
    feed_male_evening_bundles = models.FloatField(null=True, blank=True)
    
    # Feed Data - Female Birds
    feed_female_morning = models.FloatField(null=True, blank=True)
    feed_female_morning_bundles = models.FloatField(null=True, blank=True)
    feed_female_evening = models.FloatField(null=True, blank=True)
    feed_female_evening_bundles = models.FloatField(null=True, blank=True)
    
    # Legacy fields for backward compatibility
    feed_morning = models.IntegerField(null=True, blank=True)
    feed_morning_bundles = models.FloatField(null=True, blank=True)
    feed_evening = models.IntegerField(null=True, blank=True)
    feed_evening_bundles = models.FloatField(null=True, blank=True)
    
    water_intake = models.FloatField(null=True, blank=True)
    
    # Egg Collection Data
    # Morning Collection
    tray_egg_morning = models.FloatField(null=True)
    total_egg_morning = models.FloatField(null=True)
    damaged_egg_morning = models.IntegerField(null=True)
    double_egg_morning = models.IntegerField(null=True)
    # Evening Collection
    tray_egg_evening = models.FloatField(null=True)
    total_egg_evening = models.FloatField(null=True)
    damaged_egg_evening = models.IntegerField(null=True)
    double_egg_evening = models.IntegerField(null=True)
    
    # Equipment Status
    artificial_insemination = models.CharField(max_length=3, default='No')  # Yes/No
    ai_hours = models.FloatField(null=True, blank=True)
    ai_birds_count = models.IntegerField(null=True, blank=True)  # Number of birds for AI
    fogger_used = models.CharField(max_length=3, default='No')  # Yes/No
    fogger_hours = models.FloatField(null=True, blank=True)
    fan_used = models.CharField(max_length=3, default='No')  # Yes/No
    fan_hours = models.FloatField(null=True, blank=True)
    light_used = models.CharField(max_length=3, default='No')  # Yes/No
    light_hours = models.FloatField(null=True, blank=True)
    
    # Other Metrics
    medicine = models.CharField(max_length=255, null=True, blank=True)
    notes = models.TextField(blank=True, null=True)
    
    # Temperature Data (6 times throughout the day)
    temperature_1 = models.FloatField(null=True, blank=True)  # Time 1
    temperature_2 = models.FloatField(null=True, blank=True)  # Time 2
    temperature_3 = models.FloatField(null=True, blank=True)  # Time 3
    temperature_4 = models.FloatField(null=True, blank=True)  # Time 4
    temperature_5 = models.FloatField(null=True, blank=True)  # Time 5
    temperature_6 = models.FloatField(null=True, blank=True)  # Time 6
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-date']
        
    def __str__(self):
        return f"Daily katheer Record - {self.date}"


class FeedStock(models.Model):
    date = models.DateField(default=timezone.now)
    kg = models.FloatField()  # Weight in KG
    bundles = models.FloatField()  # Calculated from kg (1 bundle = 60 kg)
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-date']
    
    def save(self, *args, **kwargs):
        # Automatically calculate bundles from kg (1 bundle = 60 kg)
        self.bundles = round(self.kg / 60, 2)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"Feed Stock - {self.date}: {self.kg} kg ({self.bundles} bundles)"


class MaleBirdsStock(models.Model):
    """Track male birds batch information with status tracking"""
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('ended', 'Ended'),
    ]
    
    initial_birds = models.IntegerField(default=0)
    batch_start_date = models.DateField(null=True, blank=True)
    batch_end_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')
    final_mortality = models.IntegerField(default=0)  # Total mortality at batch end
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-batch_start_date']
    
    def get_current_mortality(self):
        """Calculate current mortality for this batch"""
        if not self.batch_start_date:
            return 0
        # Use batch-specific mortality records when available
        mortality = self.mortality_records.aggregate(models.Sum('mortality_count'))['mortality_count__sum'] or 0
        return mortality
    
    def get_current_birds(self):
        """Get current alive birds in this batch"""
        mortality = self.get_current_mortality()
        return max(0, self.initial_birds - mortality)
    
    def __str__(self):
        return f"Male Birds Batch - {self.batch_start_date}: {self.initial_birds} birds ({self.status})"


class MaleBirdsMortality(models.Model):
    """Track male birds mortality records"""
    batch = models.ForeignKey(MaleBirdsStock, on_delete=models.CASCADE, null=True, blank=True, related_name='mortality_records')
    date = models.DateField(default=timezone.now)
    mortality_count = models.IntegerField(default=0)
    mortality_reason = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-date']
    
    def __str__(self):
        return f"Male Birds Mortality - {self.date}: {self.mortality_count} birds"
    
class FemaleBirdsStock(models.Model):
    """Track female birds batch information with status tracking"""
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('ended', 'Ended'),
    ]
    
    initial_birds = models.IntegerField(default=0)
    batch_start_date = models.DateField(null=True, blank=True)
    batch_end_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')
    final_mortality = models.IntegerField(default=0)  # Total mortality at batch end
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-batch_start_date']
    
    def get_current_mortality(self):
        """Calculate current mortality for this batch"""
        if not self.batch_start_date:
            return 0
        # Use batch-specific mortality records when available
        mortality = self.mortality_records.aggregate(models.Sum('mortality_count'))['mortality_count__sum'] or 0
        return mortality
    
    def get_current_birds(self):
        """Get current alive birds in this batch"""
        mortality = self.get_current_mortality()
        return max(0, self.initial_birds - mortality)
    
    def __str__(self):
        return f"Female Birds Batch - {self.batch_start_date}: {self.initial_birds} birds ({self.status})"


class FemaleBirdsMortality(models.Model):
    """Track female birds mortality records"""
    batch = models.ForeignKey(FemaleBirdsStock, on_delete=models.CASCADE, null=True, blank=True, related_name='mortality_records')
    date = models.DateField(default=timezone.now)
    mortality_count = models.IntegerField(default=0)
    mortality_reason = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-date']
    
    def __str__(self):
        return f"Female Birds Mortality - {self.date}: {self.mortality_count} birds"


class EggOut(models.Model):
    """Track egg out records"""
    date = models.DateField(default=timezone.now)
    egg_out_count = models.IntegerField(default=0)
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-date']
        unique_together = ('date',)
    
    def __str__(self):
        return f"Egg Out - {self.date}: {self.egg_out_count} eggs"
