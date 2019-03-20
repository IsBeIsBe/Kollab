from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


class Tag(models.Model):
    """ Tag model: Stores information regarding the tags, which are associated with an individual UserProfile and are
        searchable. """

    name = models.CharField(max_length=128)
    
    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        return super(Tag, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name


class UserProfile(models.Model):
    """ UserProfile model, which extends the inbuilt Django User model. A number of fields are added that aren't used withing
        the Django UserModel"""
    user = models.OneToOneField(User)

    # Users chosen location stored as latitude and longditude
    # floatfield is just a decimal number like 50.938892 or -14.324333
    lat = models.FloatField(blank=True, null=True)
    lon = models.FloatField(blank=True, null=True)

    firstname = models.CharField(max_length=128,blank=True, null=True)
    lastname = models.CharField(max_length=128,blank=True, null=True)

    picture = models.ImageField(upload_to='profile_images', blank=True)
    
    selfinfo = models.TextField(blank=True, null=True) #
        
    slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super(UserProfile, self).save(*args, **kwargs)

    # User has a many-to-many relationship with Tags becuase
    # tags are shared between users, (eg, musician tag can belong to two
    # users) and users can have several tags
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.user.username

class Collabs(models.Model):
    """d of Warning
       It is easy to duplicate the Collab relationships because two 'creator' profiles can add each other,
       and it will provide two unique instances of a Collabs object. unfortunately we only want one
       
       Its not beautiful, but in functions you can avoid doing this by checking that the recipient has
       not already sent one to you by using the below condition:
       
       if not adder_userprof.collabs_recieved.filter(creator=recip_userprof).exists(): 
       
       in English: "if its not true that the creator has recieved a Collabs where the creator 
       of THAT Collabs is the same user profile as the one we are sending to" """   SENT = 'SENT'
    CONFIRMED = 'CONF'
    DENIED = 'DEN'
    STATUS_CHOICES = (
        ('SENT', 'SENT'),
        ('CONF', 'CONFIRMED'),
        ('DEN', 'DENIED'),
    )
    created = models.DateTimeField(auto_now_add=True, editable=False)
    creator = models.ForeignKey(UserProfile, related_name="collabs_initiated")
    friend = models.ForeignKey(UserProfile, related_name="collabs_recieved")
    status = models.CharField(max_length=4, choices=STATUS_CHOICES)
    

class Project(models.Model):
    """ Currently not implemented due to being somewhat redundant. This may be added on future iterations
        if it's a functionality which is required. The idea was for users to be able to create project
        pages, which contain tags and members, and users could search or join these.
    """

    name = models.CharField(max_length=128)
    short = models.CharField(max_length=128, blank=True, null=True)
    long = models.TextField(blank=True, null=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    """ to be added:
        privacy setting - could be simple private/public or one to one link to a 
            project settings class
        projectAdmin --> one to many -->Admin
    """
    
    # many to many as many tags can belong to many projects
    tags = models.ManyToManyField(Tag)
    
    # members is a list of Users
    members = models.ManyToManyField(UserProfile, through='Membership')
    
    slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Project, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name


class Membership(models.Model):
    """ this sets a user as a member and ensures that if the user is deleted from the project
        that they are not deleted from the database!
        Blank = true ensures that when creating a new membership that having a user/project
        is not a mandatory field
    """
    userProfile = models.ForeignKey(UserProfile, models.SET_NULL, blank=True, null=True)
    project = models.ForeignKey(Project,models.SET_NULL, blank=True, null=True)

    # to be added:
    # date started membership / ended membership

    def __str__(self):
        return self.userProfile.user.username + ' ' + self.project.name