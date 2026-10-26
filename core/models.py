from django.db import models

# 1. Base User Model
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    is_employer = models.BooleanField(default=False)
    is_candidate = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# 2. Employer Profile (OneToOne with User)
class Employer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=150)
    company_website = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.company_name} ({self.user.name})"

# 3. Candidate Profile (OneToOne with User)
class Candidate(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)
    skills = models.TextField(help_text="Comma-separated skills")

    def __str__(self):
        return self.user.name

# 4. Job Model (OneToMany with Employer)
class Job(models.Model):
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    posted_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# 5. Application Model (Connects Candidate and Job)
class Application(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    applied_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, default='Pending')

    def __str__(self):
        return f"{self.candidate.user.name} applied for {self.job.title}"