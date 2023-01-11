from django.contrib.auth.models import AbstractUser
from django.db import models
from django.forms import ModelForm, Textarea, NumberInput, Select, TextInput


class User(AbstractUser):
    pass

class Comment(models.Model):
    comment = models.CharField(max_length=64)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_comment")

class Listing(models.Model):
    
    CATEGORIES = [
    ('Toys', 'Toys'),
    ('Electronics', 'Electronics'),
    ('Lifestyle', 'Lifestyle'),
    ('Home', 'Home'),
    ('Fashion', 'Fashion'),
    ('Other', 'Other')
    ]   

    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="creator")
    title = models.CharField(max_length=64, blank=False, null=False)
    minimum_bid = models.IntegerField(blank=False, null=True) 
    description = models.CharField(blank=True, max_length=1064, null=True)
    starting_bid = models.IntegerField(blank=True, null=True)
    category = models.CharField(max_length=64, blank=True, choices=CATEGORIES)
    image = models.ImageField(default='https://user-images.githubusercontent.com/52632898/161646398-6d49eca9-267f-4eab-a5a7-6ba6069d21df.png')
    bid_counter = models.IntegerField(default=0)
    active = models.BooleanField(default=True)
    winner = models.CharField(max_length=64, blank=True, null=True)

    def _str__(self):
        return f"{self.title} by {self.creator}"

# Creating a listing form out of the Listings model
class ListingForm(ModelForm):
    class Meta:
        model = Listing
        exclude = ['creator', 'bid_counter', 'active', 'winner']
        widgets = {
            'title': TextInput(
                attrs={'class': 'form-control', "style": "margin-bottom: 10px", 'placeholder': 'Title'}),
            'description': Textarea(
                attrs={'rows': 10, 'columns':4, 'class': 'form-control', "style": "margin-bottom: 10px", 'placeholder': 'Description'}),
            'minimum_bid' : NumberInput(
                attrs={"class": "form-control", "style": "margin-bottom: 10px", "placeholder": "Minimum Bid ($)"}),
            'starting_bid': NumberInput(attrs={'class': 'form-control', "placeholder": "Starting Bid ($)"}),
            'category' : Select(attrs={'choices': Listing.CATEGORIES, "class": "form-control"})
        }

class Bid(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_bid")
    bid = models.IntegerField()
    date_created = models.DateTimeField(auto_now=True)
    auction = models.ForeignKey(Listing, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.bid} made by {self.user}"
